#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
face detection using haar cascades

USAGE:
    facedetect.py [--cascade <cascade_fn>] [--nested-cascade <cascade_fn>] [<video_source>]


Keys:
    ESC    - exit
    SPACE  - save current frame to <shot path> directory
'''

# Python 2/3 compatibility
from __future__ import print_function
import rospy
from std_msgs.msg import String
import os
import numpy as np
import cv2

# local modules
from video import create_capture
from common import clock, draw_str


def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),
                                     flags=cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

if __name__ == '__main__':
    import sys, getopt
    print(__doc__)
    saveflag = 0    
    #talker()
    args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
    try:
        video_src = video_src[0]
    except:
        video_src = 0
    args = dict(args)
    cascade_fn = args.get('--cascade', "src/face_system/haarcascade_frontalface_alt.xml")
    nested_fn  = args.get('--nested-cascade', "src/face_system/haarcascade_eye.xml")

    cascade = cv2.CascadeClassifier(cascade_fn)
    nested = cv2.CascadeClassifier(nested_fn)

    cam = create_capture(video_src, fallback='synth:bg=../data/lena.jpg:noise=0.05')

    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        t = clock()
        rects = detect(gray, cascade)
        vis = img.copy()
        draw_rects(vis, rects, (0, 255, 0))
	imgs = []	
	imgs.append(img)
        if not nested.empty() :
            for x1, y1, x2, y2 in rects:
                roi = gray[y1:y2, x1:x2]
                vis_roi = vis[y1:y2, x1:x2]
                subrects = detect(roi.copy(), nested)
                draw_rects(vis_roi, subrects, (255, 0, 0))
	        if saveflag == 0:
			fn = 'src/face_system/image/new.jpg'
		        cv2.imwrite(fn, img)			
			print ("save image")
			saveflag = 1
	        else : 
			  print ("image exist")
			  break
        dt = clock() - t

        draw_str(vis, (20, 20), 'time: %.1f ms' % (dt*1000))
        cv2.imshow('facedetect', vis)
	
	ch = cv2.waitKey(5)
        if ch == 27:
            break
	if ch == ord(' '):
            for i, img in enumerate(imgs):
                fn = 'src/face_system/image/new.jpg'
                print(fn, 'saved')
                saveflag = 0
		if saveflag == 0:
		        cv2.imwrite(fn, img)
			saveflag = 1
		else : 
			
			break

    cv2.destroyAllWindows()
