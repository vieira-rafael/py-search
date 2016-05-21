# solutions.py# Chris Barker# CMU S13 15-112 Term Project
# Some code in this module is adapted from color_histogram.py,# which is provided in the OpenCV-2.4.4 release# Go here for OpenCV downloads: http://opencv.org/downloads.html# The code that I did not write is clearly marked as follows:
 # I did not write this code: ############################## # " Code I didn't write" ##############################
# I also did not write any of the numpy, cv, cv2, video, # sys, Tkinter, or getopt modules.
import numpy as npimport cv, cv2import videoimport sysimport getoptfrom coloranalytics import colorByHSV, colorByRGBfrom Tkinter import Labelfrom geometry import *
fnt = cv2.FONT_HERSHEY_PLAIN
# Quick mapping from string to hex for cube sticker colorscolorCodes = { 'red': '#ff0000', 'green': '#00ff00', 'blue': '#0000ff', 'orange': '#ff8800', 'yellow': '#ffff00', 'white': '#ffffff', 'gray': '#888888'}
# Object attribute containerclass Struct(): pass
def colorTuple(s): # Converts a color string to a color tuple.
 if type(s) == tuple: return s elif type(s) != str: # fallback value        s = '#888888'
    s = s.lower() if s[0] != '#': if s in colorCodes:            s = colorCodes[s] else: # fallback value            s = '#888888'
    base = 0x10    red = int(s[1:3], base)    green = int(s[3:5], base)    blue = int(s[5:7], base) return (blue, green, red) # OpenCV uses BGR
def selectionColor(x, y, data): # Takes a click (x,y) and returns the color of the palette at that point if (data.colorSelectionStartY <= y <=         data.colorSelectionStartY + data.colorSelectionHeight):        xNow = data.colorSelectionStartX for color in data.colorSelections: if xNow <= x <= xNow + data.colorSelectionWidth: return color            xNow += data.colorSelectionWidth
def suff(i): return 'st' if i==1 else 'nd' if i==2 else 'rd' if i==3 else 'th'
def onMouse(e, x, y, flags, param, data): if e == 0: # Movement pass elif e == 1: # Click down pass elif e == 4: # Release mouse button        index = data.cube.faceClicked(x, y) print 'index', index if index is not None:            data.showingSelector = True print 'now showing selector!'            data.selectionIndex= index else: if data.showingSelector:                newColor = selectionColor(x, y, data) if newColor is not None:                    data.cube.setColor(data.selectionIndex, newColor)
class Streamer(object): def __init__(self, stream): self.index = 0 self.stream = stream def __iter__(self): return self def next(self): while self.index != len(self.stream.events): if self.stream.events[self.index][0] == 'face': break self.index += 1 else: raise StopIteration         prevTurnIndex = self.index        prevTurn = None while prevTurnIndex >= 0: if self.stream.events[prevTurnIndex][0] == 'turn':                prevTurn = self.stream.events[prevTurnIndex][1] break            prevTurnIndex -= 1
        prevFaceIndex = self.index - 1        prevFace = None while prevFaceIndex >= 0: if self.stream.events[prevFaceIndex][0] == 'face':                prevFace = self.stream.events[prevFaceIndex][1] break            prevFaceIndex -= 1
        nextTurnIndex = self.index        nextTurn = None while nextTurnIndex < len(self.stream.events): if self.stream.events[nextTurnIndex][0] == 'turn':                nextTurn = self.stream.events[nextTurnIndex][1] break            nextTurnIndex += 1
        nextFaceIndex = self.index + 1        nextFace = None while nextFaceIndex < len(self.stream.events): if self.stream.events[nextFaceIndex][0] == 'face':                nextFace = self.stream.events[nextFaceIndex][1] break            nextFaceIndex += 1
        currentFace = self.stream.events[self.index][1]
        data = Struct()        data.currentFace = currentFace        data.prevFace = prevFace        data.nextFace = nextFace        data.prevTurn = prevTurn        data.nextTurn = nextTurn
 self.index += 1
 return data
class Stream(object): def __init__(self): self.events = [ ] def logFace(self, a): L = [ a[:3], a[3:6], a[6:] ] self.events.append(('face', L)) def logTurn(self, turn): self.events.append(('turn', turn)) def __iter__(self): return Streamer(self)
def averageRGB(img):    red = 0    green = 0    blue = 0    num = 0 for y in xrange(len(img)): if y%10 == 0:            a = img[y] for x in xrange(len(a)): if x%10 == 0:                    b = img[y][x]                    num += 1                    red += b[0]                    green += b[1]                    blue += b[2]    red /= num    green /= num    blue /= num return (red, green, blue)
def histMode(hist, maxAmt):    bin_count = int(hist.shape[0])    maxAmount = int(hist[0])    maxIndex = 0    numZero = 0    numTotal = 0 for i in xrange(bin_count):        h = int(hist[i]) if h == 0: numZero += 1        numTotal += 1 if h > maxAmount:            maxIndex = i            maxAmount = h    val = int(maxAmt * maxIndex / bin_count) return val
class DemoCube(object):    directions = (K_HAT, J_HAT, I_HAT, -J_HAT, -I_HAT, -K_HAT)    ups = (-J_HAT, K_HAT, K_HAT, K_HAT, K_HAT, -I_HAT)    rights = (I_HAT, I_HAT, -J_HAT, -I_HAT, J_HAT, J_HAT)
 def __init__(self): self.colors = ['gray'] * 54        (self.width, self.height) = (400, 500) self.dim = {'width': self.width, 'height': self.height} self.faceIndex = 0 self.transitionSpeed = 1 self.camera = Camera(Vector(2, -4, 10), Vector(0,0,0), pi/5, self.dim)
 @staticmethod def faceInfo(i):        faceIndex = i / 9        norm = DemoCube.directions[faceIndex]        up = DemoCube.ups[faceIndex]        right = DemoCube.rights[faceIndex]        faceCenter = norm * 1.5        faceCenter = faceCenter - ((i / 3)%3 - 1) * up        faceCenter = faceCenter - (i%3 - 1) * right return (faceCenter, norm, up, right)
 def adjustCamera(self):        destination = (DemoCube.directions[self.faceIndex]) ^ 1        current = (self.camera.view) ^ 1 if destination ** current < 0.6:            currentPos = self.camera.pos            destinationPos = self.camera.origin + destination * (currentPos.mag)            deltaY = destinationPos ** self.camera.up            deltaX = destinationPos ** self.camera.right            deltaX *= 0.1            deltaY *= 0.1 self.camera.rotate((deltaX, deltaY))
 def faceClicked(self, x, y): for i in xrange(len(self.colors)):            (center, norm, up, right) = self.faceInfo(i) if norm ** (center - self.camera.pos) < 0:                corners = (center + up * 0.5 + right * 0.5,                           center + up * 0.5 - right * 0.5,                           center - up * 0.5 - right * 0.5,                           center - up * 0.5 + right * 0.5)                corners = [corner.flatten(self.camera) for corner in corners]                corners = [(int(corner[0]), int(corner[1])) for corner in corners] for corner in xrange(len(corners) - 1):                    prev = (corner - 1) % len(corners)                    cursor = Vector(x - corners[corner][0], y - corners[corner][1], 0)                    prevVect = Vector(corners[prev][0] - corners[corner][0],                                      corners[prev][1] - corners[corner][1], 0)                    nextVect = Vector(corners[corner+1][0] - corners[corner][0],                                      corners[corner+1][1] - corners[corner][1], 0) if ((prevVect * cursor) ** (cursor * nextVect) < 0): break else: return i
 def draw(self, vis): self.adjustCamera() for i in xrange(len(self.colors)):            (center, norm, up, right) = self.faceInfo(i) if norm ** (center - self.camera.pos) < 0:                corners = (center + up * 0.5 + right * 0.5,                           center + up * 0.5 - right * 0.5,                           center - up * 0.5 - right * 0.5,                           center - up * 0.5 + right * 0.5)                corners = [corner.flatten(self.camera) for corner in corners]                corners = [(int(corner[0]), int(corner[1])) for corner in corners]                cv.FillConvexPoly(cv.fromarray(vis),                     corners, colorTuple(self.colors[i]), lineType=4, shift=0)
 for i in xrange(len(self.colors)):            (center, norm, up, right) = self.faceInfo(i) if norm ** (center - self.camera.pos) < 0:                corners = (center + up * 0.5 + right * 0.5,                           center + up * 0.5 - right * 0.5,                           center - up * 0.5 - right * 0.5,                           center - up * 0.5 + right * 0.5)                corners = [corner.flatten(self.camera) for corner in corners]                corners = [(int(corner[0]), int(corner[1]))  for corner in corners]
 for j in xrange(len(corners)):                    k = (j + 1) % (len(corners))                    cv.Line(cv.fromarray(vis), corners[j], corners[k], (0,0,0))
 def setColors(self, colors, faceIndex): if faceIndex > 5: return        i = faceIndex * 9 for c in colors: self.colors[i] = c            i += 1
 def setColor(self, index, color): self.colors[index] = color
 def toStream(self):        stream = Stream()        stream.logFace(self.colors[:9])        stream.logTurn('up')        stream.logFace(self.colors[9:18])        stream.logTurn('right')        stream.logFace(self.colors[18:27])        stream.logTurn('right')        stream.logFace(self.colors[27:36])        stream.logTurn('right')        stream.logFace(self.colors[36:45])        stream.logTurn('up')        stream.logFace(self.colors[45:]) return stream


def cubeFromCam(app=None, callback=None):
 # I did not write this code: ############################## try:        video_src = sys.argv[1] except:        video_src = 0 ##############################
    data = Struct()
    data.app = app    data.after = None    data.waiting = False    data.callback = callback
 # I did not write this code: ##############################    data.cam = video.create_capture(video_src)    cv2.namedWindow('Cube Input') ##############################
    data.stream = Stream()    data.delay = 20    data.colorSelections = ['red', 'orange', 'yellow',  'green', 'blue', 'white']    data.colorSelectionStartX = 20    data.colorSelectionStartY = 400    data.colorSelectionWidth = 40    data.colorSelectionHeight = 40    data.cube = DemoCube()    data.numLogged = 0    data.showingSelector = False    data.selectionIndex= 0    mouse = lambda e,x,y,f,p: onMouse(e,x,y,f,p, data)    cv2.setMouseCallback('Cube Input', mouse)
    (x, y, dx, dy, margin, rows, cols) = (400, 100, 150, 150, 10, 3, 3)    data.regions = [ ] for row in xrange(rows): for col in xrange(cols):            data.regions.append((x + col * dx + margin,                                 y + row * dy + margin,                                 x + (col + 1) * dx - margin,                                 y + (row + 1) * dy - margin))
 while timer(data): pass
def timer(data): # I did not write this code: ##############################    ret, frame = data.cam.read()    vis = frame.copy()    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, np.array((0., 60., 50.)),                            np.array((180., 255., 255.))) ##############################
    mask2 = cv2.inRange(hsv, np.array((0., 0., 0.)),                              np.array((180., 255., 255.)))
    texts = [ ]    colors = [ ]
 for (x0, y0, x1, y1) in data.regions:        (w, h) = (x1 - x0, y1 - y0)        (x0m, y0m, x1m, y1m) = (x0 + w/5, y0 + h/5, x1 - w/5, y1 - h/5)
 # I did not write this code: ##############################        hsv_roi = hsv[y0m:y1m, x0m:x1m]        mask_roi = mask[y0m:y1m, x0m:x1m] ##############################
        mask_roi2 = mask2[y0m:y1m, x0m:x1m]
 # I did not write this code: ##############################        histHue = cv2.calcHist( [hsv_roi], [0], mask_roi, [50], [0, 180] ) ##############################
        histSat = cv2.calcHist( [hsv_roi], [1], mask_roi2, [50], [0, 180] )        histVal = cv2.calcHist( [hsv_roi], [2], mask_roi2, [50], [0, 180] )
 # I did not write this code: ##############################        cv2.normalize(histHue, histHue, 0, 255, cv2.NORM_MINMAX);        histHue = histHue.reshape(-1) ##############################
        histSat = histSat.reshape(-1)        histVal = histVal.reshape(-1)
        hue = histMode(histHue, 180.)        sat = histMode(histSat, 255.)        val = histMode(histVal, 255.)
        rgb_inRegion = vis[y0m:y1m, x0m:x1m]
        avghsv = (hue, sat, val)        avgrgb = averageRGB(rgb_inRegion)
        color = colorByRGB(avgrgb, avghsv)        colors.append(color)
        cv2.rectangle(vis, (x0, y0), (x1, y1), (255, 255, 255))        texts.append((vis.shape[1] - (x0+x1) / 2, (y0 + y1) / 2, str(color)))
    vis = vis[::,::-1].copy()
 for (x, y, color) in texts:        fill = (255,255,255) if color in ('blue', 'green', 'red') else (0,0,0)        cv2.putText(vis, color, (x, y), cv2.FONT_HERSHEY_PLAIN, 1, fill)
    cv2.rectangle(vis, (0, 0), (400, 1200), (0,0,0), -1)    wid = vis.shape[1]    cv2.rectangle(vis, (wid-400, 0), (wid, 1200), (0,0,0), -1)
    data.cube.setColors(colors, data.numLogged)    data.cube.draw(vis)
 if data.waiting: help = ["Press spacebar to advance",  "to the next face.",  "or click on a square",  "to change its color."] else:        i = data.numLogged+1 help = ["Press spacebar to",  "lock this face.", "You may manually adjust",  "the cube once it is locked.", "You are currently logging the %d%s face." % (i, suff(i))]
    startY = 25    startX = 25
 for h in help:        white = (255,255,255)        cv2.putText(vis, h,(startX, startY), fnt, 1, white)        startY += 20
    tips = [ "Red looks like orange?", "Move somewhere with more light.", "Non-white looks like white?", "Tilt your cube up, down, left, or right.", "Still not working", "Press spacebar and then click on the", "incorrect color to manually select the", "color it should be.", "", "Press ESC to close this window."    ]
    startY = 25    startX = wid - 375
 for tip in tips:        white = (255,255,255)        cv2.putText(vis, tip, (startX, startY), fnt, 1, white)        startY += 20
 if data.showingSelector:        xNow = data.colorSelectionStartX        yNow = data.colorSelectionStartY        (wNow, hNow) = (data.colorSelectionWidth, data.colorSelectionHeight) for colorSelect in data.colorSelections:            p1 = (xNow, yNow)            p2 = (xNow + wNow, yNow + hNow)            cv2.rectangle(vis, p1, p2, colorTuple(colorSelect), -1)            xNow += wNow
 # I did not write this code: ##############################    cv2.imshow('Cube Input', vis)
    ch = 0xff & cv2.waitKey(20) # Gets keyboard input ##############################
 if ch == 32: # Spacebar        data.showingSelector = False if data.waiting:            data.cube.faceIndex += 1 else:            data.stream.logFace(colors)            data.numLogged += 1        data.waiting = not data.waiting
 if data.numLogged in (1, 5):            data.stream.logTurn('up') else:            data.stream.logTurn('right')
 if ch == 27 or data.cube.faceIndex == 6: # Escape key        data.callback(data.cube.toStream()) # I did not write this code: ##############################        cv2.destroyAllWindows() ############################## return False
 return True