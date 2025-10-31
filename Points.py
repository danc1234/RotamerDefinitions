import math

class Points:
    def __init__(self, x, y, z): # x, y, and z are coordinates of a point, they are floats
        self.x = x
        self.y = y
        self.z = z

    # Accessor Methods
    def getX(self):
        return self.x
    def getY(self):
        return self.y 
    def getZ(self):
        return self.z

    # self is the instance (the thing you attach .distance() to) and point is the other point.
    # This method returns a float.
    def distance(self, point):
        a = (self.x-point.getX())**2
        b = (self.y-point.getY())**2
        c = (self.z-point.getZ())**2
        return math.sqrt(a+b+c)

    # Parameters are same as distance, except this time, vector returns a list
    def vector(self, point):
        return [self.x-point.getX(), self.y-point.getY(), self.z-point.getZ()]

# a, b are vectors. Returns a scalar
def dot(a, b): 
    return(a[0]*b[0]+a[1]*b[1]+a[2]*b[2])

# a, b are vectors. Returns a vector
def cross(a, b):
    x_value = a[1]*b[2]-a[2]*b[1]
    y_value = -1*(a[0]*b[2]-b[0]*a[2])
    z_value = a[0]*b[1]-b[0]*a[1]
    return [x_value, y_value, z_value]

# Finds the magnitude of a vector
def magnitude(a):
    return math.sqrt(a[0]**2+a[1]**2+a[2]**2)

# a,b,c,d are part of the class Points. This function returns a float. The code made here
# were derived from this website by Mr. Lei Mao, which explains how to calculate dihedral angles. 
# https://leimao.github.io/blog/Dihedral-Angles/ 
def dihedralCalculator(a,b,c,d):
    v1 = b.vector(a)
    v2 = c.vector(b)
    v3 = d.vector(c)
    reference = Points(0,0,0)
    # The code below calculates cos(theta).
    numer1 = dot(cross(v1, v2), cross(v2, v3))
    denom1 = magnitude(cross(v1, v2))
    cosine = numer1 / denom1
    print(cosine)
    # The code below calculates sin(theta).
    numer2 = dot(cross(cross(v1,v2), cross(v2,v3)),v2)
    denom2 = magnitude(cross(v1,v2)) * magnitude(cross(v2,v3)) * magnitude(v2)
    sine = numer2 / denom2
    print(sine)
    return math.degrees(math.atan2(sine, cosine)) # returns in radians so use math.degrees to convert to degrees

if __name__ == "__main__":
    atom1 = Points(71.542, 14.389, 91.604)
    atom2 = Points(70.052, 14.573, 91.280)
    atom3 = Points(69.227, 13.419, 91.854)
    atom4 = Points(67.722, 13.607, 91.686)
    print(dihedralCalculator(atom1, atom2, atom3, atom4))    

