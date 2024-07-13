from pygame.sprite import Group

from data.classes import Block


class Level:

    def __init__(self, screen_width: float, screen_height: float):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.level = 0
        self.klocki = Group()

    def generate_level(self, textures_assets):
        if self.level == 6:
            self.level = -2
        self.klocki = Group()
        if self.level == 1:
            klocek = Block(int(self.screen_width / 2 - 20), 20, textures_assets=textures_assets)
            self.klocki.add(klocek)
        else:
            for x in range(self.level * 10):
                if x % 4 == 0:
                    klocek = Block(int(self.screen_width / 2 - (20 * (x / 4) + 5 * (x / 4))), self.screen_height / 4, textures_assets)
                elif x % 4 == 1:
                    klocek = Block(int(self.screen_width / 2 - (20 * (x / 4) + 5 * (x / 4))), int(self.screen_height / 4 - 60), textures_assets)
                elif x % 4 == 2:
                    klocek = Block(int(self.screen_width / 2 + (20 * (x / 4) + 5 * (x / 4))), int(self.screen_height / 4 - 90), textures_assets)
                else:
                    klocek = Block(int(self.screen_width / 2 + (20 * (x / 4) + 5 * (x / 4))), int(self.screen_height / 4 - 30), textures_assets)
                self.klocki.add(klocek)
        pass

