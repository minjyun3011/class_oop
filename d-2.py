import math

height = int(input("長方形の幅は？: "))
width = int(input("長方形の高さは？: "))

class Rectangle():
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        # 長方形の面積を計算して返す
        return round(self.height * self.width, 2)

    def diagonal(self):
        # 長方形の対角線の長さを計算して返す
        return round(math.sqrt(self.height**2 + self.width**2), 2)


# 高さ5、幅6の長方形を作成
rectangle = Rectangle(height, width)
print(f"rectangle = Rectangle(height={height}, width={width})")
print(f"{rectangle.area()}")
print(f"{rectangle.diagonal()}")

