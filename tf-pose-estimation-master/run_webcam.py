from flask import Flask, render_template, Response
app = Flask(__name__)

app.run(host='0.0.0.0',port=9000,debug=True)


#http://127.0.0.1:5000/video_feed

def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        frame = pose_image  # read the camera frame
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

import tensorflow as tf
print(tf.__version__)

import argparse
import logging
import time
import _thread

import cv2
import numpy as np

from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh

from tensorflow import keras
from numpy import array
model = keras.models.load_model('f1_b16_42.h5') #(f1_b16_42 / f2_b16_42)

import matplotlib.pyplot as plt
import gc
from datetime import datetime

import self_API.db as dbAPI
import self_API.processData as processDataAPI 

logger = logging.getLogger('TfPoseEstimator-WebCam')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

fps_time = 0    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tf-pose-estimation realtime webcam')
    parser.add_argument('--camera', type=int, default=0)

    parser.add_argument('--resize', type=str, default='656x368',
                        help='if provided, resize images before they are processed. default=0x0, Recommends : 432x368 or 656x368 or 1312x736 ')
    parser.add_argument('--resize-out-ratio', type=float, default=4.0,
                        help='if provided, resize heatmaps before they are post-processed. default=1.0')

    parser.add_argument('--model', type=str, default='mobilenet_thin', help='mobilenet_thin / cmu')

    parser.add_argument('--output_json', type=str, default='C:/Users/sam/Desktop/tf-pose-estimation-master/tmp/', help='writing output json dir')
    
    parser.add_argument('--output_img', type=str, default='C:/Users/sam/Desktop/tf-pose-estimation-master/tmp_img/', help='writing output json dir')

    parser.add_argument('--show-process', type=bool, default=False,
                        help='for debug purpose, if enabled, speed for inference is dropped.')
    args = parser.parse_args()

    logger.debug('initialization %s : %s' % (args.model, get_graph_path(args.model)))
    w, h = model_wh(args.resize)

    if w > 0 and h > 0:
        e = TfPoseEstimator(get_graph_path(args.model), target_size=(w, h))
    else:
        e = TfPoseEstimator(get_graph_path(args.model), target_size=(432, 368))
    logger.debug('cam read+')
    cam = cv2.VideoCapture(args.camera)
    ret_val, image = cam.read()
    logger.info('cam image=%dx%d' % (image.shape[1], image.shape[0]))

    frame = 0
    keypoints = []
    resetFallCount = 0
    stateFall = False
    tmpFallRate = 0
    processDataFrameCheckpoint = 0
    gifImage = []
    processDataState = "Detecting..."
    processDataNum = 0
    gifName = ""
    fallCount = 0
    webcamID = 1
    
    #plt.ion()
    x = [0]
    y = [0]
    x2 = []
    y2 = [70] * 50
    xMin = 0
    xMax = 50
    plt.ylim((-10,110))
    plt.xlim((xMin,xMax))
    for i in range(xMin , xMax):
        x2.append(i)
    fig = plt.gcf()
    plt.title('The real time fall detection system')
    plt.ylabel('probality of  fall (%)')
    plt.xlabel('number of frames')
    line1 = plt.plot(x,y, label = "real time value", color='blue')
    plt.plot(x2, y2, label = "falling value", color='red')
    plt.legend()
    #fig.show()
    fig.canvas.draw()
    
    while True:
        ret_val, image = cam.read()

        #logger.debug('image process+')
        humans = e.inference(image, resize_to_default=(w > 0 and h > 0), upsample_size=args.resize_out_ratio)
        #print('humans' + str(humans))

        #logger.debug('postprocess+')

        image, points = TfPoseEstimator.draw_humans(image, humans, imgcopy=False, frame=frame, )#output_json_dir=args.output_json 
        
        pose_keypoints_2d = []
        #pose_keypoints_2d = points
        pose_keypoints_2d = points[:42]
        keypoints.append(pose_keypoints_2d)

        if len(keypoints) > 20:
            keypoints.remove(keypoints[0])
        
        image_h, image_w = image.shape[:2]      
        
        test = []

        # normalize data
        for record in keypoints:
            #for i in range(0, 54, 3):
            for i in range(0, 42, 3):
              record[i] = float(record[i])/ float(image_w)
              record[i + 1] = float(record[i + 1]) / float(image_h)
              #print('X: ' + str(image_w))
              #print('Y: ' + str(image_h))
            test.append(record)


        test = array(test)
        test = test.reshape((len(test), 1, len(test[0])))
        probality = model.predict_proba(test)
        
        probalityPrint = '%.2f' % (float(probality[-1][0]) * 100)

        #print(str(frame) + ": " + str(float(probality[-1][0])))
               
        if float(probality[-1][0]) > 0.7 and stateFall == False:
            stateFall = True
            tmpFallRate = probalityPrint
            resetFallCount = 20
            fallCount += 1
            if processDataNum == 0:
                processDataNum = 1
                processDataFrameCheckpoint = frame
                saveGIFState = True
                now = datetime.now()
                gif_time = now.strftime("%b-%d-%Y")
                gifName = gif_time + "_" + str(fallCount) + ".gif"
                processDataState = "Saveing GIF..."
        elif resetFallCount <= 0 and stateFall == True:
            stateFall = False            
        elif float(probality[-1][0]) < 0.1 and stateFall == True:
            resetFallCount -= 1
            probalityPrint = tmpFallRate
        elif resetFallCount > 0 and stateFall == True:
            probalityPrint = tmpFallRate

        if (processDataFrameCheckpoint + 20) == frame and processDataFrameCheckpoint != 0:
            _thread.start_new_thread( processDataAPI.img2gif, (gifImage, gifName, ) )
            
        if len(gifImage) >= 40:
            gifImage.remove(gifImage[0])            
                  
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        
        if (processDataFrameCheckpoint + 250) == frame and processDataFrameCheckpoint != 0:
            processDataState = "Sending Email..."
            _thread.start_new_thread( processDataAPI.send_email_message, ('1', ) )
            
        if (processDataFrameCheckpoint + 550) == frame and processDataFrameCheckpoint != 0:
            processDataState = "Sending Whatsapp..."
            _thread.start_new_thread( dbAPI.dbAddFallRecord, (gifName, webcamID, date_time, fallCount, ) )
            _thread.start_new_thread( processDataAPI.send_whatsapp, ( ) )
            
        if (processDataFrameCheckpoint + 600) == frame and processDataFrameCheckpoint != 0:
            processDataNum = 0
            
        if (processDataNum == 0):
            processDataState = "Detecting..."
        
        cv2.rectangle(image, (0, 0), (image_w, 30), (0,0,0), -1)
                    
        if stateFall == True:
            cv2.putText(image,
                    "State: Fall",
                    (200, 20),  cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (55, 0, 255), 2)
        else:
            cv2.putText(image,
                    "State: Not Fall",
                    (200, 20),  cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (55, 0, 255), 2)
                    
        cv2.putText(image,
                    date_time,
                    (400, 20),  cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                    (0, 255, 255), 2)
           
        #cv2.putText(image, str(probalityPrint + '%'),(250, 50),  cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0, 255, 0), 2)

        #plt.cla()
        #plt.clf()
        #plt.ylim((-10,110))
        #plt.xlim((xMin,xMax))
        x.append(frame)
        y.append(float(probalityPrint))
        #plt.title('The real time fall detection system')
        #plt.ylabel('probality of  fall (%)')
        #plt.xlabel('number of frames')
        line = line1.pop(0)
        line.remove()
        line1 = plt.plot(x,y, color='blue')
        #plt.plot(x2, y2, color='red')
        #plt.legend()
        fig.canvas.draw()
        #plt.show(block=False)
        #plt.pause(0.5)
                    
                    
        if (frame % 50 == 0 ) and (frame != 0):
            plt.cla()
            x = []
            y = []
            x2 = []
            gc.collect()
            xMin = frame
            xMax = xMax + 50
            for i in range(xMin , xMax):
                x2.append(i)
            plt.title('The real time fall detection system')
            plt.ylabel('probality of  fall (%)')
            plt.xlabel('number of frames')
            line1 = plt.plot(x,y, label = "real time value", color='blue')
            plt.plot(x2, y2, label = "falling value", color='red')
            plt.legend()
            plt.xlim((xMin,xMax))
            plt.ylim((-10,110))
            fig.canvas.draw()
                               
        
        #plt.savefig('fig.png')
        #fig_line = cv2.imread('fig.png')
        img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
        img  = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))

        # img is rgb, convert to opencv's default bgr
        fig_line = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        
        #cv2.imwrite((args.output_img + '{0}.jpg'.format(str(frame).zfill(12))), image)        
        frame += 1

        #logger.debug('show+')
        cv2.putText(image,
                    "Process: " + processDataState,
                    (10, 50),  cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                    (0, 255, 0), 2)       
        
        cv2.putText(image,
                    "FPS: %f" % (1.0 / (time.time() - fps_time)),
                    (10, 20),  cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                    (0, 255, 0), 2)
        cp_image = np.concatenate((image, fig_line), axis=1) 
        cv2.imshow('tf-pose-estimation result', cp_image)
        pose_image = np.concatenate((image, fig_line), axis=0)
        
        image= cv2.cvtColor(image,cv2.COLOR_BGR2RGB)        
        gifImage.append(image)
            
        fps_time = time.time()        
        if cv2.waitKey(1) == 27:           
            break
        #logger.debug('finished+')
        #print(keypoints)

    cv2.destroyAllWindows()