import pygame
from pygame import Surface, Vector2
from pygame.sprite import Sprite

from data.classes import Coordinates


class Ball(Sprite):

    def __init__(self, position: Coordinates, ball_radius: float, speed: float):
        Sprite.__init__(self)
        self.speed = speed
        self.position = position
        self.ball_radius = ball_radius / 2
        self.surf = Surface((self.ball_radius * 2, self.ball_radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(surface=self.surf, color=(255, 255, 255), center=(self.ball_radius, self.ball_radius),
                           radius=self.ball_radius)
        self.rect = self.surf.get_rect()
        self.rect.x = position.x
        self.rect.y = position.y
        self.move = False
        self.last_collide_pint = Coordinates(self.surf.get_width(), self.surf.get_height())
        self.direction = Vector2()
        print("position", self.rect.x)
