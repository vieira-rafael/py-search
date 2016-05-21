# unittests.py# Chris Barker# CMU S13 15-112 Term Project
from geometry import Vector
def testGeometry(): print 'testing geometry...',    vec1 = Vector(1, 2, 3)    vec2 = Vector(-2, 4, 5) assert vec1 + vec2 == Vector(-1, 6, 8) assert vec1 ** vec2 == -2 + 8 + 15 assert vec1 * vec2 == -1 * (vec2 * vec1) assert vec1 * -1 == Vector(-1, -2, -3) print 'passed!'

if __name__ == '__main__':    testGeometry()