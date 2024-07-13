from typing import List

from pygame.sprite import Sprite, collide_rect

from data.classes import Coordinates, Ball


class Player(Sprite):

    def __init__(self, boundaries: Coordinates, textures_assets, player_speed: float, ball_speed):
        Sprite.__init__(self)
        from data.service.change_the_name import create_game_object
        self.size = Coordinates(boundaries.x / 5, boundaries.y / 25)
        self.position = Coordinates(boundaries.get_center().x - (self.size.x / 2), boundaries.y - self.size.y * 2)
        self.boundaries = boundaries
        self.lives = 3
        self.score = 0
        self.speed = player_speed
        self.surf = create_game_object(textures_assets.PLATFORM_TEXTURE, self.size)
        self.rect = self.surf.get_rect()
        self.rect.x = self.position.x
        self.rect.y = self.position.y
        self.ball: Ball = Ball(
            position=Coordinates(self.boundaries.get_center().x - self.size.y/2, self.position.y - self.size.y),
            ball_radius=self.size.y, speed=ball_speed)

    def update(self, direction: List, boundaries: Coordinates) -> None:
        if "LEFT" in direction:
            self.rect.move_ip(-self.speed, 0)
            if self.rect.left < 0:
                self.rect.left = 0
        if "RIGHT" in direction:
            self.rect.move_ip(self.speed, 0)
            if self.rect.right > boundaries.x:
                self.rect.right = boundaries.x

        # self.ball.update(boundaries, self, direction)
        if not self.ball.move:
            print(f"Platform center: {(self.rect.x + self.surf.get_width() / 2)}")
            print(f"Ball center: {self.ball.rect.x}")
            self.ball.rect.x = self.rect.x + (self.surf.get_width() / 2) - self.size.y
            self.ball.rect.y = self.position.y - self.size.y
            if "UP" in direction:
                if "LEFT" in direction:
                    self.ball.direction.x = -self.ball.speed
                    self.ball.direction.y = -self.ball.speed
                elif "RIGHT" in direction:
                    self.ball.direction.x = self.ball.speed
                    self.ball.direction.y = -self.ball.speed
                else:
                    self.ball.direction.x = 0
                    self.ball.direction.y = -self.ball.speed
                self.ball.move = True
        else:
            self.ball.rect.move_ip(self.ball.direction.x, self.ball.direction.y)
            if self.ball.rect.top <= 0:
                self.ball.direction.y *= -1
            if self.ball.rect.left <= 0:
                self.ball.direction.x *= -1 if self.ball.direction.x <= 0 else 1
            if self.ball.rect.right >= boundaries.x - self.ball.surf.get_width():
                self.ball.direction.x *= -1 if self.ball.direction.x >= 0 else 1
            if self.ball.rect.top > boundaries.y + self.ball.surf.get_height():
                self.lives -= 1
                self.ball.move = False
            if collide_rect(self.ball, self):
                if self.rect.colliderect(self.ball.rect):
                    self.ball.direction.y *= -1
                    print(((self.rect.x + self.surf.get_width() / 2) - self.ball.rect.x))
                    offset = abs(
                        ((self.rect.x + self.surf.get_width() / 2) - self.ball.rect.x) / (self.surf.get_width() / 2))
                    print('Offset: ', offset)
                    if self.ball.rect.x < (self.rect.x + self.surf.get_width() / 2 + self.ball.rect.x):
                        self.ball.direction.x = -1 * self.ball.speed - offset
                        self.ball.direction.y = -1 * self.ball.speed + offset
                        print("lewo")  # TODO KEEP THE SPEED
                    elif self.ball.rect.x > (self.rect.x + self.surf.get_width() / 2 + self.ball.rect.x):
                        self.ball.direction.x = 1 * self.ball.speed + offset
                        self.ball.direction.y = -1 * self.ball.speed - offset
                        print("prawo")  # TODO KEEP THE SPEED
                    else:
                        print("CENTEr")
                print(self.ball.direction)
                print(f"sum = {self.ball.direction.x + self.ball.direction.y}")
