from pygame import Surface
from pygame.sprite import Sprite


class GameObject(Sprite):
    def __init__(self, asset: Surface):
        Sprite.__init__(self)
        self.surf = asset
