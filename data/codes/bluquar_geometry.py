# geometry.py# Chris Barker# CMU S13 15-112 Term Project
from math import pi, tan, acos, atan
class Vector(object): """An n-dimensional vector has a list of n components.    <a,b,c> + <d,e,f> == <a+d, b+e, c+f>    <a,b,c> ** <d,e,f> == ad+be+cf    A*B = A x B    <a,b,c> * n = <an,bn,cn>    A ^ m returns a vector in the direction of A with magnitude m    A // B returns True if A and B are parallel and False otherwise    ~A returns and arbitrary vector perpendicular to A    A > B returns the projection of A onto B """     epsilon = 1e-6
 @staticmethod def cross(x1, y1, z1, x2, y2, z2): """Returns the cross product of two 3-dimensional vectors.""" return Vector(y1 * z2 - z1 * y2,                      z1 * x2 - x1 * z2,                      x1 * y2 - y1 * x2)
 @staticmethod def almostEqual(a, b): """Compares two floating point values for near-equality.""" return abs(a - b) < Vector.epsilon
 def __init__(self, *components): if type(components[0]) == Vector: # Instantiate a vector with another vector. self.components = components[0].components elif hasattr(components[0], '__iter__'): # Passed in an iterable self = Vector(components[0]) else: self.components = [ float(q) for q in components ]
 def __str__(self): """a.__str__ <==> str(a)""" return '<%s>' % (','.join([str(c) for c in self.components]))  def __repr__(self): """a.__repr__ <==> repr(a)""" return 'Vector(%r)' % (self.components)
 def __hash__(self): """a.__hash__ <==> hash(a)""" return hash(tuple(self.components))
 # Component properties @property def x(self): if len(self.components) < 1: return 0 return self.components[0] @x.setter def x(self, value): if len(self.components) > 0: self.components[0] = value @x.deleter def x(self): if len(self.components) > 0: self.components[0] = 0
 @property def y(self): if len(self.components) < 2: return 0 return self.components[1] @y.setter def y(self, value): if len(self.components) > 1: self.components[1] = value @y.deleter def y(self): if len(self.components) > 1: self.components[1] = 0
 @property def z(self): if len(self.components) < 3: return 0 return self.components[2] @z.setter def z(self, value): if len(self.components > 2): self.components[2] = value @z.deleter def z(self): if len(self.components) > 2: self.components[2] = 0
 @property def mag(self): return (self.x**2 + self.y**2 + self.z**2)**0.5
 @mag.setter def mag(self, value): self = self.unit() * value
 @mag.deleter def mag(self): pass
 def mag2(self): """Returns the square of the magnitude of a.""" return self.x**2 + self.y**2 + self.z**2
 def __mul__(self, other): if type(other) == int or type(other) == float or type(other) == long: return Vector(*[comp * other for comp in self.components]) elif type(other) == Vector: # Cross product return Vector.cross(*(self.components[:3] + other.components[:3]))
 def __rmul__(self, other): return self * other  def __pow__(self, other): if type(other) == int or type(other) == float or type(other) == long: return Vector(*[comp ** other for comp in self.components]) elif type(other) == Vector: # Dot product return sum([a*b for a, b in zip(self.components, other.components)])
 def __imul__(self, other): return self * other
 def __eq__(self, other): """a.__eq__(b) <==> a==b""" if not isinstance(other, Vector): if other == 0: return self.isZero() else: if len(self.components) != len(other.components): return False return [Vector.almostEqual(a,b) for (a,b) in zip(self.components,other.components)]
 def __neq__(self, other): return not (self == other)

 def __add__(self, other):        addends = [ self.components, other.components ]        total = [ 0 ] * max([len(addend) for addend in addends]) for compList in addends: for i in xrange(len(compList)):                total[i] += compList[i] return Vector(*total)
 def __iadd__(self, other): return self + other
 def __sub__(self, other): return self + (-1 * other)
 def __neg__(self): return self * -1
 def __pos__(self): return self * +1
 def __isub__(self, other): return self - other
 def __xor__(self, other): if isinstance(other, (int, long, float)): return self.unit() * other
 def __ixor__(self, other): return self ^ other
 def __invert__(self): return self.perp()
 def __floordiv__(self, other): if isinstance(other, (int, long, float)): return self / other elif isinstance(other, Vector): return self.isParallel(other)
 def __div__(self, other): if isinstance(other, (int, long, float)): return self * (1./other)
 def __rdiv__(self, other): return self / other
 def __gt__(self, other): return self.project(other)
 def dot(self, other): return self.x*other.x + self.y*other.y + self.z*other.z
 def isZero(self): for comp in self.components: if not comp == 0: return False return True
 def dist(self, other): return (self - other).mag
 def dist0(self, other): return self.mag()
 def unit(self): if self.isZero(): return self return self * (1./self.mag)
 def project(self, other): return other * ((self ** other) / other.mag2())
 def isEqual(self, other): return self.x == other.x and self.y == other.y and self.z == other.z
 def isNegation(self, other): return self.scalar(-1).isEqual(other)
 def isParallel(self, other): return (self * other).mag < Vector.epsilon
 def isPerpendicular(self, other): return self.dot(other) == 0
 def angleBetween(self, other): return acos(self.dot(other) / (self.mag * other.mag))
 def perp(self): """Returns an arbitrary perpendicular vector"""        vect = Vector(1,0,0) - (Vector(1,0,0) > self) if not vect.isZero(): return vect else: return Vector(0,1,0) - (Vector(1,0,0) > self)
 def flatten(self, camera): """Returns 2D 'film' coordinates given a 3D position vector and a camera"""        view = camera.view        up = camera.up        right = camera.right        field = camera.field        cameraPos = camera.pos        width = camera.width        height = camera.height
        displacement = self - cameraPos        horiz = displacement - (displacement > up)        vertic = displacement - (displacement > right)        forward = horiz > view        edge = forward + (right ^ (forward.mag * field))        rightComp = edge - forward        horizComp = horiz - forward        ratio = horizComp.mag / rightComp.mag if rightComp ** horizComp < 0:            ratio *= -1        length = min(width, height)        x = (width/2) + (ratio*length)
        forward = vertic > view        edge = forward + (up ^ (vertic.mag * field))        topComp = edge - forward        verticComp = vertic - forward        ratio = verticComp.mag / topComp.mag if topComp ** verticComp < 0:            ratio *= -1        y = (height/2) + (ratio*length)
 return (x,y)

I_HAT = Vector(+1, 0, 0)J_HAT = Vector( 0,+1, 0)K_HAT = Vector( 0, 0,+1)

class Camera(object): def __init__(self, pos, origin, angle, dim, sensitivity=0.2): self.pos = pos self.origin = origin self.field = tan(angle) self.angle = angle self.view = (origin - pos) ^ 1 self.right = (~self.view) ^ 1 self.up = (self.right * self.view) ^ 1 self.width = dim['width'] self.height = dim['height'] self.sensitivity = sensitivity
 def rotate(self, direction):        (x, y) = direction        zoom = self.pos.mag        right = self.view * self.up self.pos = self.pos + (self.up * y) self.view = self.origin - self.pos self.pos = self.pos ^ zoom self.up = (right * self.view) ^ self.up.mag self.pos = self.pos + (right * x) self.pos = self.pos ^ zoom self.view = (self.origin - self.pos) ^ 1 self.up = (right * self.view) ^ 1 self.right = (self.view * self.up) ^ 1
 def fisheye(self, inc):        factor = inc self.angle *= factor self.field = tan(self.angle) self.pos.mag = self.pos.mag / factor self.view = (self.origin - self.pos) ^ 1