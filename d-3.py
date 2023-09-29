import math

length = int(input("正方形の幅は？: "))

class Square():
    def __init__(self, length):
        self.length = length

    def area(self):
        return round(self.length**2)
    
    def diagonal(self):
        return round(math.sqrt(2)*self.length, 2)
    
square = Square(length=5)
print(f"square = (length={length})")
print(f"{square.area()}")
print(f"{square.diagonal()}")
