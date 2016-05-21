# solutions.py# Chris Barker# CMU S13 15-112 Term Project
# solutions.beginner3Layer(state) takes a CubeState (see cube.py)# and returns a list of moves.
from geometry import *import timeimport datetime
SOLVED_STATE = [[[ ( 1, 210), ( 2, 210), ( 3, 210) ],                [ ( 4, 210), ( 5, 210), ( 6, 210) ],                [ ( 7, 210), ( 8, 210), ( 9, 210) ]],
               [[ (10, 210), (11, 210), (12, 210) ],                [ (13, 210), (14, 210), (15, 210) ],                [ (16, 210), (17, 210), (18, 210) ]],
               [[ (19, 210), (20, 210), (21, 210) ],                [ (22, 210), (23, 210), (24, 210) ],                [ (25, 210), (26, 210), (27, 210) ]]]CUBE_DIMENSION = 3MOVE_CODES = { K_HAT: 'U', -K_HAT: 'D', -I_HAT: 'L', I_HAT: 'R', J_HAT: 'F', -J_HAT: 'B'}
COLOR_CODES =    { I_HAT : 'green', -I_HAT : 'blue', J_HAT : 'red', -J_HAT : 'orange', K_HAT : 'yellow', -K_HAT : 'white'}
def valueAtPos(vec, state):    (x, y, z) = vec.components    (x, y, z) = (int(x+1), int(y+1), int(z+1)) return state.state[z][y][x]def solutionAtPos(vec):    (x, y, z) = vec.components    (x, y, z) = (int(x+1), int(y+1), int(z+1)) return SOLVED_STATE[z][y][x]def posOfVal(val, state): for z in xrange(CUBE_DIMENSION): for y in xrange(CUBE_DIMENSION): for x in xrange(CUBE_DIMENSION): if hasattr(state, 'state'): if state.state[z][y][x][0] == val: return Vector(x-1, y-1, z-1) else: if state[z][y][x][0] == val: return Vector(x-1, y-1, z-1)def makeMoves(axes, state, moves, status='Solving'): for axis in axes:        move = MOVE_CODES[axis[0]] if axis[1]: move += "'"        state.rotate(state.rotationInfo(move))        move = (move, status)        moves.append(move)
class Struct(): pass
def getPerpendicular(vec): if vec // K_HAT:        val = +J_HAT else: val = +K_HAT return val
def refine(L): while True: for i in xrange(len(L) - 1): if i+2 != len(L) and L[i][0] == L[i+1][0] == L[i+2][0]: if "'" in L[i][0]: L[i:i+3] = [(L[i][0][0], L[i][1])] else: L[i:i+3] = [(L[i][0] + "'", L[i][1])] break if L[i][0] == L[i+1][0] + "'" or L[i+1][0] == L[i][0] + "'": L[i:i+2] = [] break else: break
def determineFixTXB(info):    pos = info.pos    desiredValue = info.desiredValue    desiredOrientation = info.desiredOrientation    currentValue = info.currentValue    currentOrientation = info.currentOrientation    topLayer = info.topLayer    state = info.state    orientation = info.orientation    posOfValue = info.posOfValue
 if desiredValue == currentValue: # Correct location if desiredOrientation == currentOrientation: return retain else: return flipTopCrossBeginner else: # Incorrect location if posOfValue ** topLayer > 0: # Elsewhere on the top layer if orientation / 100 == desiredOrientation / 100: # Same color facing upward return relocateTopLayerTXB else: # Top-layer color not facing up return reorientTopLayerTXB
 elif posOfValue ** topLayer == 0: return secondLayerTXB
 else: if orientation / 100 == desiredOrientation / 100: return relocateBottomLayerTXB else: return reorientBottomLayerTXB
def determineFixTCB(info):    pos = info.pos    desiredValue = info.desiredValue    desiredOrientation = info.desiredOrientation    currentValue = info.currentValue    currentOrientation = info.currentOrientation    topLayer = info.topLayer    state = info.state    moves = info.moves    orientation = info.orientation    posOfValue = info.posOfValue
 if desiredValue == currentValue: if desiredOrientation == currentOrientation: # Already where we want it return retain else: return flipTopTCB else: if posOfValue ** topLayer > 0: # Elsewhere on the top layer return moveCornerDown
 else: # On the bottom layer return moveCornerUp
def determineFixSLB(info):    pos = info.pos    desiredValue = info.desiredValue    desiredOrientation = info.desiredOrientation    currentValue = info.currentValue    currentOrientation = info.currentOrientation    topLayer = info.topLayer    state = info.state    moves = info.moves    orientation = info.orientation    posOfValue = info.posOfValue
 if desiredValue == currentValue:        desO = list(str(desiredOrientation))        curO = list(str(currentOrientation))        desO.remove('2')        curO.remove('2') if desO == curO: return retain else: return moveSecondLayerDown else: if posOfValue ** topLayer < 0: return moveSecondLayerUp else: return moveSecondLayerDown
def retain(info): return
def named(pieceId):    pos = posOfVal(pieceId, SOLVED_STATE)    colors = [COLOR_CODES[k] for k in COLOR_CODES if k**pos > 0]
 if len(colors) == 2: return 'the %s and %s edge piece' % (colors[0], colors[1]) elif len(colors) == 3:        msg = 'the %s, %s, and %s corner piece' return msg % (colors[0], colors[1], colors[2]) else: return str(colors)
def flipTopCrossBeginner(info):    axesToRotate = [ # Put the piece on the second layer                    (info.pos - (info.pos > info.topLayer), False),                    (info.topLayer, True), # Rotate the top layer # Put the piece back on the top layer                    (info.pos * info.topLayer, False),                     (info.topLayer, False) # Put the top layer back                ]    msg = "Flipping %s on the first layer." % (named(info.desiredValue))    makeMoves(axesToRotate, info.state, info.moves, msg)
def relocateTopLayerTXB(info):    desiredAxis = info.pos - (info.pos > info.topLayer)    currentAxis = info.posOfValue - (info.posOfValue > info.topLayer) if desiredAxis // currentAxis: # Opposite side        numRotations = 2 elif (desiredAxis * currentAxis) ** info.topLayer < 0:        numRotations = -1 else:        numRotations = 1    axesToRotate = [ ]    axesToRotate.append((currentAxis, False)) for i in xrange(abs(numRotations)):        axesToRotate.append((info.topLayer, numRotations < 0))    axesToRotate.append((currentAxis, True)) for i in xrange(abs(numRotations)):        axesToRotate.append((info.topLayer, numRotations > 0))    msg = 'Moving %s into place.' % named(info.desiredValue)    makeMoves(axesToRotate, info.state, info.moves, msg)
def reorientTopLayerTXB(info):    desiredAxis = info.pos - (info.pos > info.topLayer)    currentAxis = info.posOfValue - (info.posOfValue > info.topLayer) if desiredAxis // currentAxis: # Opposite side        numRotations = 1 elif (desiredAxis * currentAxis) ** info.topLayer < 0:        numRotations = 2 else:        numRotations = 0    axesToRotate = [ ]    axesToRotate.append((currentAxis, False)) for i in xrange(abs(numRotations)):        axesToRotate.append((info.topLayer, numRotations < 0))    axesToRotate.append((currentAxis * info.topLayer, False)) for i in xrange(abs(numRotations)):        axesToRotate.append((info.topLayer, numRotations > 0))
    msg = "Relocating %s on the first layer." % (named(info.desiredValue))
    makeMoves(axesToRotate, info.state, info.moves, msg)
def secondLayerTXB(info):    pos = info.pos    desiredValue = info.desiredValue    desiredOrientation = info.desiredOrientation    currentValue = info.currentValue    currentOrientation = info.currentOrientation    topLayer = info.topLayer    state = info.state    moves = info.moves    orientation = info.orientation    posOfValue = info.posOfValue
    orientation = str(orientation)    orientation = list(orientation)    orientation.remove('2') if len(orientation) == 2: # The top-facing is on the y-face        rotating = +I_HAT else: rotating = +J_HAT if rotating ** posOfValue < 0:        rotating = rotating * -1    cclock = False if (rotating * topLayer) ** posOfValue > 0:        cclock = True
    desiredAxis = pos - (pos > topLayer)    currentAxis = rotating if desiredAxis // currentAxis: if desiredAxis ** currentAxis > 0:            numRotations = 0 else:            numRotations = 2 elif (desiredAxis * currentAxis) ** topLayer < 0:        numRotations = 1 else:        numRotations = -1    axesToRotate = [ ] for i in xrange(abs(numRotations)):        axesToRotate.append((topLayer, numRotations > 0))    axesToRotate.append((currentAxis, cclock)) for i in xrange(abs(numRotations)):        axesToRotate.append((topLayer, numRotations < 0))
    task = 'Moving %s from the second layer to the first layer.'     msg = task % (named(info.desiredValue))
    makeMoves(axesToRotate, state, moves, msg)
def relocateBottomLayerTXB(info):    pos = info.pos    desiredValue = info.desiredValue    desiredOrientation = info.desiredOrientation    currentValue = info.currentValue    currentOrientation = info.currentOrientation    topLayer = info.topLayer    state = info.state    moves = info.moves    orientation = info.orientation    posOfValue = info.posOfValue
    desiredAxis = pos - (pos > topLayer)    currentAxis = posOfValue - (posOfValue > topLayer) if desiredAxis // currentAxis: if desiredAxis ** currentAxis > 0:            numRotations = 0 else:            numRotations = 2 elif (desiredAxis * currentAxis) ** topLayer < 0:        numRotations = 1 else:        numRotations = -1
    axesToRotate = [ ] for i in xrange(abs(numRotations)):        axesToRotate.append(( -1 * topLayer, numRotations > 0))    axesToRotate.append((desiredAxis, True))    axesToRotate.append((desiredAxis, True))    task = 'Moving %s from the third layer to the first layer.'    msg = task % (named(info.desiredValue))    makeMoves(axesToRotate, state, moves, msg)
def reorientBottomLayerTXB(info):    pos = info.pos    desiredValue = info.desiredValue    desiredOrientation = info.desiredOrientation    currentValue = info.currentValue    currentOrientation = info.currentOrientation    topLayer = info.topLayer    state = info.state    moves = info.moves    orientation = info.orientation    posOfValue = info.posOfValue
    desiredAxis = pos - (pos > topLayer)    currentAxis = posOfValue - (posOfValue > topLayer) if desiredAxis // currentAxis: if desiredAxis ** currentAxis > 0:            numRotations = 0 else:            numRotations = 2 elif (desiredAxis * currentAxis) ** topLayer < 0:        numRotations = 1 else:        numRotations = -1
    axesToRotate = [ ] for i in xrange(abs(numRotations)): # Rotate top to correct position        axesToRotate.append(( topLayer, numRotations > 0))
 # Move piece up to second layer    axesToRotate.append((currentAxis, False)) 
 # Move open space on top layer accordingly    axesToRotate.append((topLayer, False))    axesToRotate.append((topLayer * currentAxis, True))    axesToRotate.append((topLayer, True)) for i in xrange(abs(numRotations)):        axesToRotate.append(( topLayer, numRotations < 0))    task = 'Moving %s from the third layer to the first layer.'    msg =  task % (named(info.desiredValue))    makeMoves(axesToRotate, state, moves, msg)
def flipTopTCB(info):    pos = info.pos    desiredValue = info.desiredValue    desiredOrientation = info.desiredOrientation    currentValue = info.currentValue    currentOrientation = info.currentOrientation    topLayer = info.topLayer    state = info.state    moves = info.moves    orientation = info.orientation    posOfValue = info.posOfValue
    orientation = str(orientation)    orientation = list(orientation) if len(orientation) == 2:        orientation = ['0'] + orientation if orientation[0] == '0': # The top-facing is on the x-face        (rotating, other) = (+I_HAT, +J_HAT) else: (rotating, other) = (+J_HAT, +I_HAT) if rotating ** posOfValue < 0:        rotating = rotating * -1 if other ** posOfValue < 0:        other = other * -1
    cclock = (rotating * other) ** topLayer > 0
    axesToRotate = [ ]
    axesToRotate.append((rotating, cclock))    axesToRotate.append((topLayer * -1, cclock))    axesToRotate.append((rotating, not cclock))    axesToRotate.append((topLayer * -1, not cclock))    axesToRotate.append((rotating, cclock))    axesToRotate.append((topLayer * -1, cclock))    axesToRotate.append((rotating, not cclock))
    msg = 'Rotating %s on the first layer.' % named(info.desiredValue)
    makeMoves(axesToRotate, state, moves, msg)
def moveCornerDown(info):    pos = info.pos    desiredValue = info.desiredValue    desiredOrientation = info.desiredOrientation    currentValue = info.currentValue    currentOrientation = info.currentOrientation    topLayer = info.topLayer    state = info.state    moves = info.moves    orientation = info.orientation    posOfValue = info.posOfValue
    (axis0, axis1) = (+I_HAT, +J_HAT) if axis0 ** posOfValue < 0:        axis0 = axis0 * -1 if axis1 ** posOfValue < 0:        axis1 = axis1 * -1
 if (axis1 * axis0) ** topLayer < 0:        (axis1, axis0) = (axis0, axis1)
    axesToRotate = [ ]    axesToRotate.append((axis1, True))    axesToRotate.append((topLayer * -1, False))    axesToRotate.append((axis1, False))
    task = 'Moving %s from the first layer to the third layer.'    msg = task % named(info.desiredValue)
    makeMoves(axesToRotate, state, moves, msg)
def moveCornerUp(info):    pos = info.pos    desiredValue = info.desiredValue    desiredOrientation = info.desiredOrientation    currentValue = info.currentValue    currentOrientation = info.currentOrientation    topLayer = info.topLayer    state = info.state    moves = info.moves    orientation = info.orientation    posOfValue = info.posOfValue
    (axis0, axis1) = (+I_HAT, +J_HAT) if axis0 ** pos < 0:        axis0 = axis0 * -1 if axis1 ** pos < 0:        axis1 = axis1 * -1 if (axis1 * axis0) ** topLayer < 0:        (axis1, axis0) = (axis0, axis1)
    pos = pos - (pos > topLayer)    posOfValue = posOfValue - (posOfValue > topLayer) if (pos * posOfValue) ** topLayer > 0:        numRotations = 1 elif (pos * posOfValue) ** topLayer < 0:        numRotations = -1 else: if pos ** posOfValue > 0:            numRotations = 0 else:            numRotations = 2
    axesToRotate = [ ] for i in xrange(abs(numRotations)):        axesToRotate.append((topLayer * -1, numRotations < 0))    axesToRotate.append((axis1, True))    axesToRotate.append((topLayer * -1, True))    axesToRotate.append((axis1, False))
    task = 'Moving %s from the third layer to the first layer.'    msg = task % named(info.desiredValue)
    makeMoves(axesToRotate, state, moves, msg)
def moveSecondLayerDown(info):    pos = info.pos    desiredValue = info.desiredValue    desiredOrientation = info.desiredOrientation    currentValue = info.currentValue    currentOrientation = info.currentOrientation    topLayer = info.topLayer    state = info.state    moves = info.moves    orientation = info.orientation    posOfValue = info.posOfValue
    (axis0, axis1) = (+I_HAT, +J_HAT) if axis0 ** posOfValue < 0:        axis0 = axis0 * -1 if axis1 ** posOfValue < 0:        axis1 = axis1 * -1 if (axis1 * axis0) ** topLayer < 0:        (axis1, axis0) = (axis0, axis1)
    axesToRotate = [ ]    axesToRotate.append((axis1, True))    axesToRotate.append((topLayer * -1, False))    axesToRotate.append((axis1, False))    axesToRotate.append((topLayer * -1, False))    axesToRotate.append((axis0, False))    axesToRotate.append((topLayer * -1, True))    axesToRotate.append((axis0, True))
    task = 'Moving %s from the second layer to the third layer temporarily.'    msg = task % named(info.desiredValue)
    makeMoves(axesToRotate, state, moves, msg)
def moveSecondLayerUp(info):    pos = info.pos    desiredValue = info.desiredValue    desiredOrientation = info.desiredOrientation    currentValue = info.currentValue    currentOrientation = info.currentOrientation    topLayer = info.topLayer    state = info.state    moves = info.moves    orientation = info.orientation    posOfValue = info.posOfValue
    currentAxis = posOfValue - (posOfValue > topLayer)
    (axis0, axis1) = (+I_HAT, +J_HAT) if axis0 ** pos < 0:        axis0 = axis0 * -1 if axis1 ** pos < 0:        axis1 = axis1 * -1 if (axis1 * axis0) ** topLayer < 0:        (axis1, axis0) = (axis0, axis1)
    orientation = list(str(orientation)) # what matters is whether z comes first or not if len(orientation) == 2:        orientation = ['0'] + orientation if posOfValue ** I_HAT == 0:        orientation.remove('0') if posOfValue ** J_HAT == 0:        orientation.remove('1')
 if orientation[0] == '2': # The Y value is displayed on the Z axis # So the X value is displayed above        setupAxis = pos > I_HAT else:        setupAxis = pos > J_HAT 
 if setupAxis // currentAxis: if setupAxis ** currentAxis > 0:            numRotations = 0 else:            numRotations = 2 elif (setupAxis * currentAxis) ** topLayer < 0:        numRotations = 1 else:        numRotations = -1
    axesToRotate = [ ]
 for i in xrange(abs(numRotations)):        axesToRotate.append((-1 * topLayer, numRotations > 0))
 if (setupAxis * pos) ** topLayer > 0: # Right side        axesToRotate.append((topLayer * -1, False))        axesToRotate.append((axis0, False))        axesToRotate.append((topLayer * -1, True))        axesToRotate.append((axis0, True))        axesToRotate.append((topLayer * -1, True))        axesToRotate.append((axis1, True))        axesToRotate.append((topLayer * -1, False))        axesToRotate.append((axis1, False)) else: # Left side        axesToRotate.append((topLayer * -1, True))        axesToRotate.append((axis1, True))        axesToRotate.append((topLayer * -1, False))        axesToRotate.append((axis1, False))        axesToRotate.append((topLayer * -1, False))        axesToRotate.append((axis0, False))        axesToRotate.append((topLayer * -1, True))        axesToRotate.append((axis0, True))
    msg = 'Moving %s from the third layer to the second layer.' % (        named(info.desiredValue))
    makeMoves(axesToRotate, state, moves, msg)
def topCrossBeginner(state, topLayer, log):    moves = [ ]
    axis0 = getPerpendicular(topLayer)    axis1 = topLayer * axis0    topCross = [ topLayer + axis0 ,                 topLayer - axis0 ,                 topLayer + axis1 ,                 topLayer - axis1]
 for pos in topCross:
        (desiredValue, desiredOrientation) = solutionAtPos(pos)        (currentValue, currentOrientation) = valueAtPos(pos, state)        posOfValue = posOfVal(desiredValue, state)        orientation = valueAtPos(posOfValue, state)[1]
        info = Struct()        info.desiredValue = desiredValue        info.desiredOrientation = desiredOrientation        info.pos = pos        info.moves = moves        info.currentValue = currentValue        info.currentOrientation = currentOrientation        info.state = state        info.orientation = orientation        info.topLayer = topLayer        info.posOfValue = posOfValue
        fix = determineFixTXB(info)        fix(info)
    log.append('TXB:%d' % (len(moves))) return moves
def topCornersBeginner(state, topLayer, log):    moves = [ ]
    axis0 = getPerpendicular(topLayer)    axis1 = topLayer * axis0
    topCorners = [ topLayer + axis0 + axis1,                   topLayer + axis0 - axis1,                   topLayer - axis0 + axis1,                   topLayer - axis0 - axis1 ]
    doneUp = done = False
 while not done:
        changedThisRound = False
 for pos in topCorners:
            fix = None            count = 0
            (desiredValue, desiredOrientation) = solutionAtPos(pos)            (currentValue, currentOrientation) = valueAtPos(pos, state)            posOfValue = posOfVal(desiredValue, state)            orientation = valueAtPos(posOfValue, state)[1]
            info = Struct()            info.desiredValue = desiredValue            info.desiredOrientation = desiredOrientation            info.pos = pos            info.moves = moves            info.currentValue = currentValue            info.currentOrientation = currentOrientation            info.state = state            info.orientation = orientation            info.topLayer = topLayer            info.posOfValue = posOfValue
            fix = determineFixTCB(info)
 if (((fix == flipTopTCB) or (fix == moveCornerDown)) and (not doneUp)): continue else:                fix(info)                changedThisRound = changedThisRound or fix != retain
        done = (not changedThisRound) and doneUp        doneUp = not changedThisRound
    log.append('TCB:%d' % (len(moves))) return moves
def secondLayerBeginner(state, topLayer, log):    moves = [ ]
    axis0 = getPerpendicular(topLayer)    axis1 = topLayer * axis0    secondLayer = [axis0 + axis1,                   axis0 - axis1,                   (-1 * axis0) + axis1,                   (-1 * axis0) - axis1]

    doneUp = False    done = False
 while not done:
        changedThisRound = False for pos in secondLayer:
            fix = None            count = 0
            (desiredValue, desiredOrientation) = solutionAtPos(pos)            (currentValue, currentOrientation) = valueAtPos(pos, state)            posOfValue = posOfVal(desiredValue, state)            orientation = valueAtPos(posOfValue, state)[1]
            info = Struct()            info.desiredValue = desiredValue            info.desiredOrientation = desiredOrientation            info.pos = pos            info.moves = moves            info.currentValue = currentValue            info.currentOrientation = currentOrientation            info.state = state            info.orientation = orientation            info.topLayer = topLayer            info.posOfValue = posOfValue
            fix = determineFixSLB(info) if fix == moveSecondLayerDown and not doneUp: continue else:                fix(info)                changedThisRound = changedThisRound or fix != retain
        done = (not changedThisRound) and doneUp        doneUp = not changedThisRound
    log.append('SLB:%d' % (len(moves))) return moves
def thirdLayerCornerOrientation(state, topLayer, log):    moves = [ ]
    axis0 = getPerpendicular(topLayer)    axis1 = topLayer * axis0
    bottomLayer = topLayer * -1    bottomCorners = [ bottomLayer + axis0 + axis1,                   bottomLayer + axis0 - axis1,                   bottomLayer - axis0 + axis1,                   bottomLayer - axis0 - axis1 ]
 # Bottom, right, top, left    axes = [ axis0, axis1, -1 * axis0, -1 * axis1]
    count = 50 while count > 0:        orientations = [valueAtPos(corner,state)[1] for                         corner in bottomCorners]        facingDowns = [i for i in bottomCorners if valueAtPos(i,state)[1] > 200]        facingXs = [i for i in bottomCorners if valueAtPos(i,state)[1] < 100]        facingYs = [i for i in bottomCorners if 100 < valueAtPos(i,state)[1] < 200]        numFacingDown = len(facingDowns) if numFacingDown == 4: break elif numFacingDown == 3: raise ValueError('Impossible cube!') elif numFacingDown == 2:            pos0 = facingDowns[0]            pos1 = facingDowns[1] if pos0 // pos1:                pos = facingDowns[0]                pos = pos - (pos > bottomLayer)                operator = ((bottomLayer * pos) + pos) / 2 else: if len(facingXs) == 2: if ((I_HAT ** facingXs[0]) *                         (I_HAT ** facingXs[1]) > 0):                        operator = (facingXs[0] > -I_HAT) ^ 1 else:                        pos = facingXs[0] + facingXs[1]                        operator = (bottomLayer * pos) ^ 1 elif len(facingYs) == 2: if ((J_HAT ** facingYs[0]) *                        (J_HAT ** facingYs[1]) > 0):                        operator = (facingYs[0] > -J_HAT) ^ 1 else:                        pos = facingYs[0] + facingYs[1]                        operator = (bottomLayer * pos) ^ 1 else:                    operator = +I_HAT
  elif numFacingDown == 1:            pos = facingDowns[0]            pos = pos - (pos > bottomLayer)             operator = ((bottomLayer * pos) - pos) / 2 elif numFacingDown == 0: if len(facingXs) == 4:                operator = +I_HAT elif len(facingXs) == 0:                operator = +J_HAT else: if ((I_HAT ** facingXs[0]) *                     (I_HAT ** facingXs[1]) > 0): # The Xs are facing the same direction                    unequals = (facingXs[0] > I_HAT) ^ 1 else:                    unequals = (facingYs[0] > J_HAT) ^ 1                pos = unequals - (unequals > bottomLayer)                operator = ((pos * bottomLayer) ^ 1)
 try:            s = MOVE_CODES[operator] except: print 'UNTREATED CASE.', print 'numFacingDown = %d.' % (numFacingDown), print 'facingXs=%s, facingYs%s, facingDowns%s' % (                facingXs, facingYs, facingDowns) break
        axesToRotate = [ (operator, True), (bottomLayer, True),                         (operator, False), (bottomLayer, True),                          (operator, True), (bottomLayer, True),                         (bottomLayer, True), (operator, False) ]
        msg = 'Orienting the third layer corners by rotating %s and %s.' % ( COLOR_CODES[operator], COLOR_CODES[bottomLayer])
        makeMoves(axesToRotate, state, moves, msg)
        count -= 1 else: raise ValueError('Could not generate solution.')
    log.append('BCO:%d' % (len(moves)))
 return moves
def thirdLayerEdgeOrientation(state, topLayer, log):    moves = [ ]
    axis0 = getPerpendicular(topLayer)    axis1 = topLayer * axis0
    bottomLayer = topLayer * -1    bottomEdges = [ bottomLayer + axis0,                    bottomLayer - axis0,                    bottomLayer + axis1,                    bottomLayer - axis1]
    count = 50 while count > 0:        orientations = [valueAtPos(edge,state)[1] for edge in bottomEdges]        facingDowns = [ ]        facingXs = [ ]        facingYs = [ ] for edge in bottomEdges:            (pos, orient) = valueAtPos(edge, state)            orient = list(str(orient)) if len(orient) == 2:                orient = ['0'] + orient if edge ** I_HAT == 0:                orient.remove('0') if edge ** J_HAT == 0:                orient.remove('1') if edge ** K_HAT == 0:                orient.remove('2')
 if orient[0] == '2':                facingDowns.append(edge) elif orient[0] == '1':                facingYs.append(edge) elif orient[0] == '0':                facingXs.append(edge)
        numFacingDown = len(facingDowns)
 if numFacingDown == 4: break elif numFacingDown == 3: return raise ValueError('Impossible cube! 3 down') elif numFacingDown == 2: if len(facingXs) == 1: # Diagonal case if (facingXs[0] * facingYs[0]) ** bottomLayer < 0:                    operator = facingXs[0] > (-I_HAT) else:                    operator = facingYs[0] > (-J_HAT) else: if len(facingXs) == 2:                    operator = +J_HAT else:                    operator = +I_HAT elif numFacingDown == 1: return raise ValueError('Impossible cube! Only 1 down') elif numFacingDown == 0:            operator = +I_HAT
        axesToRotate = [ ]         front = operator        right = front * bottomLayer
        axesToRotate.append((right, True))        axesToRotate.append((bottomLayer, True))        axesToRotate.append((front, True))        axesToRotate.append((bottomLayer, False))        axesToRotate.append((front, False))        axesToRotate.append((right, False))
        msg = 'Orienting third layer edges.'
        makeMoves(axesToRotate, state, moves, msg)
        count -= 1 else: raise ValueError('Could not generate solution.')
    log.append('BEO:%d' % (len(moves))) return moves
def thirdLayerCornerPermutation(state, topLayer, log):    moves = [ ]
    axis0 = getPerpendicular(topLayer)    axis1 = topLayer * axis0
    bottomLayer = topLayer * -1    bottomCorners = [ bottomLayer + axis0 + axis1,                   bottomLayer + axis0 - axis1,                   bottomLayer - axis0 - axis1,                   bottomLayer - axis0 + axis1 ]
    count = 50 while count > 0:        adjacentPairs = [ ]
 for i in xrange(len(bottomCorners)):            corner1 = bottomCorners[i]            corner2 = bottomCorners[(i+1) % (len(bottomCorners))]
 # what we have at corner 1 right now            (currentValue1, currentOrientation1) = valueAtPos(corner1, state) # where that piece should be            desired1 = posOfVal(currentValue1, SOLVED_STATE)
 # what we have at corner 2 right now            (currentValue2, currentOrientation2) = valueAtPos(corner2, state) # where that piece should be            desired2 = posOfVal(currentValue2, SOLVED_STATE)
 if not ((desired1 - bottomLayer) // (desired2 - bottomLayer)): # they are adjacent corners if (((desired1 - bottomLayer) * (desired2 - bottomLayer)) **                     ((corner1 - bottomLayer) * (corner2 - bottomLayer))) > 0: # correct orientation                    adjacentPairs.append((corner1, corner2))
 if len(adjacentPairs) == 4: break elif len(adjacentPairs) == 0:            operator = +I_HAT elif len(adjacentPairs) == 1:            (corner1, corner2) = adjacentPairs[0]            nonOp = (corner1 - bottomLayer) + (corner2 - bottomLayer)            operator = (-1 * nonOp) / 2 else: print adjacentPairs print state raise ValueError('bad corners')
        top = bottomLayer        front = operator        back = operator * -1        right = operator * bottomLayer
        axesToRotate = [ (right,  True), (front, False), (right,  True),                         ( back,  True), ( back,  True), (right, False),                         (front,  True), (right,  True), ( back,  True),                         ( back,  True), (right,  True), (right,  True) ]
        task = 'Permuting third layer corners.'        msg='%s. So far, %d %s permuted correctly.' % (            task, len(adjacentPairs), 'pair is' if  len(adjacentPairs) == 1 else 'pairs are')
        makeMoves(axesToRotate, state, moves, msg)        count -= 1 else: raise ValueError('Could not generate solution.')
    posOfValue = bottomCorners[0]    val = valueAtPos(posOfValue, state)    solvedPos = posOfVal(val[0], SOLVED_STATE)
 if (solvedPos * posOfValue) ** topLayer > 0:        numRotations = 1 elif (solvedPos * posOfValue) ** topLayer < 0:        numRotations = -1 else: if solvedPos ** posOfValue > 0:            numRotations = 0 else:            numRotations = 2
    axesToRotate = [ ] for i in xrange(abs(numRotations)):        axesToRotate.append((bottomLayer, numRotations < 0))
    msg = 'Rotating third layer to align corners.'
    makeMoves(axesToRotate, state, moves, msg)

    log.append('BCP:%d' % (len(moves))) return moves
def thirdLayerEdgePermutation(state, topLayer, log):    moves = [ ]
    axis0 = getPerpendicular(topLayer)    axis1 = topLayer * axis0
    bottomLayer = topLayer * -1    bottomEdges = [ bottomLayer + axis0,                bottomLayer - axis0,                bottomLayer + axis1,                bottomLayer - axis1]
    count = 10 while count != 0:        corrects = [ ] for pos in bottomEdges: if valueAtPos(pos, state)[0] == solutionAtPos(pos)[0]:                corrects.append(pos)
 if len(corrects) == 4: break elif len(corrects) == 0:            operator = +I_HAT elif len(corrects) == 1:            operator = (corrects[0] - bottomLayer) * (-1)
        front = operator        top = bottomLayer        right = operator * bottomLayer
        axesToRotate = [            (right, False), (  top, False), (right,  True),            (  top, False), (right, False), (  top, False),            (  top, False), (right,  True), (front,  True),            (  top,  True), (front, False), (  top,  True),            (front,  True), (  top,  True), (  top,  True),            (front, False),        ]
        msg='Rotating third layer edges. So far, %d %s permuted correctly.'%( len(corrects), 'edge is' if len(corrects) == 1 else 'edges are')
        makeMoves(axesToRotate, state, moves, msg)
        count -= 1 else: raise ValueError("Could not generate solution.")
    log.append('BEP:%d' % (len(moves))) return moves
def beginner3Layer(state, topLayer=+K_HAT): """A simple human-based algorithm that combines intuition for the    first layer with short algorithms for the next layers. Here the    intuition has been made into an algorithm."""    start = time.time()
    moves = [ ]    log = [ ]
 # The log records information about solution # generations and saves it in solutionLogs.txt    log.extend([str(datetime.datetime.now()), 'Beginner', state.condense()])
    steps = [topCrossBeginner,             topCornersBeginner,             secondLayerBeginner,             thirdLayerEdgeOrientation,             thirdLayerCornerOrientation,             thirdLayerCornerPermutation,             thirdLayerEdgePermutation]
 for step in steps:        moves.extend(step(state, topLayer, log))
    refine(moves)
    strMoves = [move[0] for move in moves]    log.append(''.join(strMoves))    log.append('Time: ' + str(time.time() - start) + " sec")    log.append('Moves:' + str(len(moves)))    log = [str(e) for e in log]    log = ';'.join(log)
 with open('solutionLogs.txt', 'r+') as file:        logs = eval(file.read())        logs.append(log) file.seek(0) file.truncate() file.write("# Datetime, method_name, initial_state, move_data,\move_string, time_elapsed, total_moves\n") file.write(repr(logs))
 return moves