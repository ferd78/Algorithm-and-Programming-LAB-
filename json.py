class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def setY(self,x):
        self.__x = x
    def setY(self,x):
        self.__y = x
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
        
        

def get_json_str(x):
    return {"__class__": "Point", "x": x.getX(), "y": x.getY()}
def read_json_str(x):
    int(x)
    read = Point(x,1)
    return get_json_str(read)

output = read_json_str(5)
print(output)
