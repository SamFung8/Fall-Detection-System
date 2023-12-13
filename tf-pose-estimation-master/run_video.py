import argparse
import logging
import time

import cv2
import numpy as np

from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh

from tensorflow import keras
from numpy import array
model = keras.models.load_model('new5.h5')

logger = logging.getLogger('TfPoseEstimator-Video')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

fps_time = 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tf-pose-estimation Video')
    parser.add_argument('--video', type=str, default='')
    parser.add_argument('--resolution', type=str, default='432x368', help='network input resolution. default=432x368')
    parser.add_argument('--model', type=str, default='cmu', help='mobilenet_thin / mobilenet_thin / mobilenet_v2_large / mobilenet_v2_small')
    parser.add_argument('--show-process', type=bool, default=False,
                        help='for debug purpose, if enabled, speed for inference is dropped.')
    parser.add_argument('--showBG', type=bool, default=True, help='False to show skeleton only.')
    parser.add_argument('--output_json', type=str, default='C:/Users/sam/Desktop/tf-pose-estimation-master/tmp/', help='writing output json dir')
    parser.add_argument('--output_img', type=str, default='C:/Users/sam/Desktop/tf-pose-estimation-master/tmp_img/', help='writing output json dir')
    parser.add_argument('--resize-out-ratio', type=float, default=4.0, help='if provided, resize heatmaps before they are post-processed. default=1.0')
    args = parser.parse_args()

    logger.debug('initialization %s : %s' % (args.model, get_graph_path(args.model)))
    w, h = model_wh(args.resolution)
    e = TfPoseEstimator(get_graph_path(args.model), target_size=(w, h))
    cap = cv2.VideoCapture(args.video)

    frame = 0
    keypoints = []
    if cap.isOpened() is False:
        print("Error opening video stream or file")
    while cap.isOpened():
        ret_val, image = cap.read()

        humans = e.inference(image, resize_to_default=(w > 0 and h > 0), upsample_size=args.resize_out_ratio)
        if not args.showBG:
            image = np.zeros(image.shape)
            
        image, points = TfPoseEstimator.draw_humans(image, humans, imgcopy=False, frame=frame, output_json_dir=args.output_json)
        
        pose_keypoints_2d = []
        #pose_keypoints_2d = points
        pose_keypoints_2d = points[:42]
        keypoints.append(pose_keypoints_2d)
        

        
        image_h, image_w = image.shape[:2]    
        
        test = []

        # normalize data
        for record in keypoints:
            #for i in range(0, 54, 3):
            for i in range(0, 42, 3):
              record[i] = float(record[i])/ float(image_w)
              record[i + 1] = float(record[i + 1]) / float(image_h)
            test.append(record)


        test = array(test)
        test = test.reshape((len(test), 1, len(test[0])))
        probality = model.predict_proba(test)

        print(str(frame) + ": " + str(float(probality[-1][0])))
        
        
        if float(probality[-1][0]) > 0.9:
            cv2.putText(image,
                    "Fall",
                    (250, 10),  cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0, 255, 0), 2)
        else:
            cv2.putText(image,
                    "Not Fall",
                    (250, 10),  cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0, 255, 0), 2)
           
        cv2.putText(image,
                    str(float(probality[-1][0])),
                    (250, 50),  cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0, 255, 0), 2)
        
        cv2.imwrite((args.output_img + '{0}.jpg'.format(str(frame).zfill(12))), image)
        frame += 1

        cv2.putText(image, "FPS: %f" % (1.0 / (time.time() - fps_time)), (10, 10),  cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.imshow('tf-pose-estimation result', image)
        fps_time = time.time()
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
logger.debug('finished+')
