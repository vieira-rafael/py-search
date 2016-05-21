### This module is provided as a sample with OpenCV# I did not write any of it### This is provided in the OpenCV-2.4.4 release# Go here for OpenCV downloads: http://opencv.org/downloads.html##

#/usr/bin/env python
'''This sample demonstrates Canny edge detection.Usage:  edge.py [<video source>]  Trackbars control edge thresholds.'''
import cv2import sys

if __name__ == '__main__': print __doc__
 try: fn = sys.argv[1] except: fn = 0
 def nothing(*arg): pass
    cv2.namedWindow('edge')    cv2.createTrackbar('thrs1', 'edge', 2000, 5000, nothing)    cv2.createTrackbar('thrs2', 'edge', 4000, 5000, nothing)
def create_capture(source = 0): '''source: <int> or '<int>|<filename>|synth [:<param_name>=<value> [:...]]' '''    source = str(source).strip()    chunks = source.split(':') # hanlde drive letter ('c:', ...) if len(chunks) > 1 and len(chunks[0]) == 1 and chunks[0].isalpha():        chunks[1] = chunks[0] + ':' + chunks[1] del chunks[0]
    source = chunks[0]  # Source is 0  try: source = int(source) except ValueError: pass    params = dict( s.split('=') for s in chunks[1:] )
    cap = None if source == 'synth':        Class = classes.get(params.get('class', None), VideoSynthBase) try: cap = Class(**params) except: pass else: # Here is where the actual Video Capture is created        cap = cv2.VideoCapture(source) if 'size' in params:            w, h = map(int, params['size'].split('x'))            cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, w)            cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, h) if cap is None or not cap.isOpened(): print 'Warning: unable to open video source: ', source if fallback is not None: return create_capture(fallback, None) return cap
    cap = create_capture(fn) while True:        flag, img = cap.read()        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        thrs1 = cv2.getTrackbarPos('thrs1', 'edge')        thrs2 = cv2.getTrackbarPos('thrs2', 'edge')        edge = cv2.Canny(gray, thrs1, thrs2, apertureSize=5)        vis = img.copy()        vis /= 2        vis[edge != 0] = (0, 255, 0)        cv2.imshow('edge', vis)        ch = cv2.waitKey(5) if ch == 27: break    cv2.destroyAllWindows()
