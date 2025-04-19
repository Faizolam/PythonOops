class Rectangle:
    def __init__(self, length, width) -> None:
        self.l = length
        self.w = width

    def __mul__(self, other):
        area = 