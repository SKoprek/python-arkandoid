class Coordinates:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def get_center(self):
        return Coordinates(self.x / 2, self.y / 2)
