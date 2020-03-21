from pprint import pprint


class Canvas():
    def __init__(self):
        self.shapes = []
        self.row = []
        self.canvas = []

        # create a list of rows within canvas list [[],[],[]]
        for num in enumerate(range(10)):
            self.canvas.append([])
        # add columns to rows within canvas -> [['','',''],['','',''],['','','']]
        for row in self.canvas:
            for num in enumerate(range(10)):
                row.append('.')

    def add_shape(self, shape):
        self.shapes.append(shape)

    def print_canvas(self):
        self.clear_canvas()
        print('------------------------')
        for shape in self.shapes:
            shape.check_bounds()
            for y, value in enumerate(range(shape.length), shape.start_y):
                for x, value in enumerate(range(shape.width), shape.start_x):
                    self.canvas[y][x] = shape.fill_char

        for row in self.canvas:
            print(' '.join(row))

    def clear_canvas(self):
        for row in self.canvas:
            for i, v in enumerate(range(10)):
                row[i] = '.'


class Rectangle():
    def __init__(self, start_y, start_x, end_y, end_x, fill_char):
        self.fill_char = fill_char
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.length = abs(self.end_y - self.start_y)+1
        self.width = abs(self.end_x - self.start_x)+1

    def translate(self, axis, num):
        if axis == 'x' or axis == 'X':
            self.start_x += num
            self.end_x += num
        elif axis == 'y' or axis == 'Y':
            self.start_y += num
            self.end_y += num

    def check_bounds(self):
        '''modifies instance's coordinates to fit within canvas '''
        if self.start_x < 0:
            self.start_x = 0
        if self.start_y < 0:
            self.start_y = 0
        if self.end_x > 9:
            self.end_x = 9
        if self.end_y > 9:
            self.end_y = 9
        self.length = abs(self.end_y - self.start_y)+1
        self.width = abs(self.end_x - self.start_x)+1

# cv = Canvas()
# sq = Rectangle(1, 1, 4, 4, '+')
# rec = Rectangle(2, 3, 7, 7, 'x')
# rec2 = Rectangle(7, 1, 18, 7, 'o')

# cv.add_shape(sq)
# cv.add_shape(rec)
# cv.add_shape(rec2)
# cv.print_canvas()
# rec2.translate('y', -2)
# cv.print_canvas()
# rec2.translate('x', 4)
# cv.print_canvas()
# rec.fill_char = 'x'
# cv.print_canvas()

# rec.translate('x', 2)
# cv.print_canvas()
# rec.translate('x', -2)
# cv.print_canvas()
