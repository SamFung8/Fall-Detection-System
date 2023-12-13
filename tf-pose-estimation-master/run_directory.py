import argparse
import logging
import time
import glob
import ast
import os
import dill

from tf_pose import common
import cv2
import numpy as np
from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh

#from lifting.prob_model import Prob3dPose
#from lifting.draw import plot_pose

logger = logging.getLogger('TfPoseEstimator')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tf-pose-estimation run by folder')
    parser.add_argument('--folder', type=str, default='./images/')
    parser.add_argument('--resolution', type=str, default='432x368', help='network input resolution. default=432x368')
    parser.add_argument('--output_json', type=str, default='C:/Users/sam/Desktop/data/json/', help='writing output json dir')
    parser.add_argument('--model', type=str, default='mobilenet_thin', help='mobilenet_thin / mobilenet_thin / mobilenet_v2_large / mobilenet_v2_small')
    parser.add_argument('--resize-out-ratio', type=float, default=4.0,
                        help='if provided, resize heatmaps before they are post-processed. default=4.0')
    parser.add_argument('--scales', type=str, default='1.0', help='for multiple scales, eg. [1.0, (1.1, 0.05)]')
    args = parser.parse_args()
    scales = ast.literal_eval(args.scales)

    w, h = model_wh(args.resolution)
    e = TfPoseEstimator(get_graph_path(args.model), target_size=(w, h))

    files_grabbed = glob.glob(os.path.join(args.folder, '*.jpg'))
    all_humans = dict()
    frame = 0
    for i, file in enumerate(files_grabbed):
        # estimate human poses from a single image !
        image = common.read_imgfile(file, None, None)
        t = time.time()
        humans = e.inference(image, resize_to_default=(w > 0 and h > 0), upsample_size=args.resize_out_ratio)
        elapsed = time.time() - t

        logger.info('inference image #%d: %s in %.4f seconds.' % (i, file, elapsed))

        image, points = TfPoseEstimator.draw_humans(image, humans, imgcopy=False, frame=frame, output_json_dir=args.output_json)
        cv2.imshow('tf-pose-estimation result', image)
        image_h, image_w = image.shape[:2]    
        print('image_h' + str(image_h))
        print('image_w' + str(image_w))
        cv2.imwrite(r'C:\Users\sam\Desktop\final_v1\test.jpg', image)     
        cv2.waitKey(5)

        all_humans[file.replace(args.folder, '')] = humans
        frame+=1

    #with open(os.path.join(args.folder, 'pose.dil'), 'wb') as f:
     #   dill.dump(all_humans, f, protocol=dill.HIGHEST_PROTOCOL)
