import pickle
from typing import List

import pygame

from pygame.time import Clock

from confing import Config
from data.classes import Player, Level, UI
from data.classes.assets import ImageAssets
from pygame import Surface, KEYDOWN, K_ESCAPE, K_SPACE


class Game:
    def __init__(self, config: Config):
        self.confing: Config = config
        self.textures_assets: ImageAssets = ImageAssets()  # INIT ASSETS

        self.instance = pygame
        self.instance.init()  # INIT PYGAME
        self.instance.display.set_caption(f"Arca clone by f{self.confing.created_by}")  # SET DISPLAY TITLE
        self.instance.display.set_mode([self.confing.resolution.x, self.confing.resolution.y])  # INIT SCREEN

        self.screen_instance: Surface = self.instance.display.get_surface()
        self.clock: Clock = self.instance.time.Clock()

        self.running = True
        self.pause = False
        self.ball_speed: float = 4
        self.player_speed: float = 5

        self.ui: UI = UI(screen_instance=self.screen_instance)
        self.level: Level = Level(screen_width=self.confing.resolution.x, screen_height=self.confing.resolution.y)

        self.player: Player = Player(self.confing.resolution, self.textures_assets, self.player_speed, self.ball_speed)

    def run(self):
        while self.running:
            for event in self.instance.event.get():
                # Windows window buttons
                if event.type == self.instance.QUIT:
                    self.running = False
                # Key input
                if event.type == KEYDOWN:
                    # Quit the game
                    if event.key == K_ESCAPE:
                        self.running = False
                    # Confirm or change level(pause screen)
                    if event.key == K_SPACE:
                        if self.level.level == 0:
                            from data.service import start_game
                            start_game(self)
                        elif self.level.level < 0:
                            from data.service import menu_screen
                            menu_screen(self)
                            # here go to menu!!!
                            self.level.level = 0
                        elif self.level.level > 0:
                            if self.pause:
                                self.pause = not self.pause
                                print(f"Pauza {self.pause}")
                            else:
                                self.pause = not self.pause
                                print(f"Pauza {self.pause}")
            event = self.instance.key.get_pressed()
            if self.level.level > 0 and self.pause is False:
                direction: List = []
                if event[self.instance.K_w]:
                    direction.append("UP")
                if event[self.instance.K_s]:
                    print("s")
                if event[self.instance.K_a]:
                    direction.append("LEFT")
                if event[self.instance.K_d]:
                    direction.append("RIGHT")
                self.player.update(direction, self.confing.resolution)

            self.screen_instance.fill((0, 0, 0))  # < reset te screen per frame

            for klocek in self.level.klocki:
                self.screen_instance.blit(klocek.surf, klocek.rect)
            self.screen_instance.blit(self.player.surf, self.player.rect)
            self.screen_instance.blit(self.player.ball.surf, self.player.ball.rect)

            if pygame.sprite.spritecollideany(self.player.ball, self.level.klocki):
                delete_klocek = pygame.sprite.spritecollideany(self.player.ball, self.level.klocki)
                delete_klocek.kill()
                if not self.level.klocki:
                    self.level.level += 1
                    self.player.ball.move = False
                    self.level.generate_level(self.textures_assets)
                self.player.ball.direction.y *= -1
                self.player.score += 10
                # usuniecie klocka
            if self.level.level == 0:
                self.ui.menu_display()
            if self.level.level > 0:
                self.ui.display(self.player.score, self.player.lives)
                if self.pause:
                    self.ui.pause_display()
            if self.level.level == -1:
                self.ui.display_gameOver(self.player.score)
                self.ui.lastScore = self.player.score
                if self.player.score > self.ui.bestScore:
                    self.ui.bestScore = self.player.score
                self.ui.scoresList[0] = self.ui.lastScore
                self.ui.scoresList[1] = self.ui.bestScore
                pickle.dump(self.ui.scoresList, open("scores", "wb"))
            if self.level.level == -2:
                self.ui.display_u_win(self.player.score)
                self.ui.lastScore = self.player.score
                if self.player.score > self.ui.bestScore:
                    self.ui.bestScore = self.player.score
                self.ui.scoresList[0] = self.ui.lastScore
                self.ui.scoresList[1] = self.ui.bestScore
                pickle.dump(self.ui.scoresList, open("scores", "wb"))

            if self.player.lives <= 0:
                print("GAME OVER")
                from data.service import game_over
                game_over(self)
            self.clock.tick(60)
            self.instance.display.flip()
        self.instance.quit()
