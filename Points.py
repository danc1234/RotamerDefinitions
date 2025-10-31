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

if __name__ == "__main__":
    borb = Points(0,0,0)
    barb = Points(2,4,-1)
    test1 = Points(0,0,0)
    test2 = Points(10,25,20)
    print(cross(borb.vector(barb), test1.vector(test2)))    