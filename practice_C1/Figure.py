class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area_rectangle(self):
        return self.width * self.height


class Square:
    def __init__(self, side):
        self.side = side

    def get_area_square(self):
        return self.side ** 2
