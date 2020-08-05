class Point2D():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '{}, {}'.format(self.x, self.y)

    def __repr__(self):
        return '{}, {}'.format(self.x, self.y)

print(str(Point2D(5, 4)))

print(repr(Point2D(5, 4)))

        
