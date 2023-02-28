import game_constants as c
class Skier:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.width, self.height = c.SKIER_WIDTH, c.SKIER_HEIGHT

    def print_skier(self):
        return f'Skier is at {self.x},{self.y}'
    

