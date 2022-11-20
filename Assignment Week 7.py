"""
a) Implement a method called get_json_str(p) that receives a point p
and returns a json string that describes the object as output. As an
example, the following code:

p=Point(1,2)
z=(get_json_str(p))
print(z)
should produce the following output:

{
    "__class__": "Point",
    "x": 1,
    "y": 2
}
"""

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def setX(self, x):
        self.__x = x
    
    def getX(self):
        return self.__x

    def setY(self, y):
        self.__y = y

    def getY(self):
        return self.__y
        
p = Point(1,2)
def get_json_str(p):
    return {"__class__": "Point", "x": p.getX(), "y": p.getY()}

z = (get_json_str(p))
print(z)

"""
# b) Now implement a function called read_json_str(s) that receives a string s
as input and returns a Point object as output.
"""

def read_json_str(s):
    p = Point(int(s), 0)
    return get_json_str(p)

a = read_json_str("7")
print(a)
