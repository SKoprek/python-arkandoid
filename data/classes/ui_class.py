import pygame
import pickle

from pygame import Surface


class UI:
    def __init__(self, screen_instance: Surface):
        self.screen_instance = screen_instance
        try:
            self.scoresList = pickle.load(open("scores", "rb"))
        except Exception as e:
            print(f"Exception UI: {e}")
            self.scoresList = [0, 0]
        print(self.scoresList)
        self.lastScore = self.scoresList[0]
        self.bestScore = self.scoresList[1]

        self.text = pygame.font.SysFont('bold-arial', 18)
        self.text_sub = pygame.font.SysFont('bold-arial', 24)
        self.text_title = pygame.font.SysFont('bold-arial', 30)

    # TODO to separate service!!
    def menu_display(self):

        text_MENU = self.text_title.render('MENU', True, (255, 255, 255))
        self.screen_instance.blit(text_MENU, dest=(
            ((self.screen_instance.get_width() / 2) - 4), self.screen_instance.get_height() / 8))
        self.screen_instance.blit(self.text_sub.render('CONTROLS', True, (255, 255, 255)),
                                  dest=(
                                      ((self.screen_instance.get_width() / 4) - 4),
                                      self.screen_instance.get_height() / 4))
        self.screen_instance.blit(self.text.render("Start: Space", True, (255, 255, 255)),
                                  dest=(((self.screen_instance.get_width() / 4) - 8),
                                        self.screen_instance.get_height() / 4 + 20))
        self.screen_instance.blit(self.text.render("Move: left and right arrow", True, (255, 255, 255)),
                                  dest=(((self.screen_instance.get_width() / 4) - 8),
                                        self.screen_instance.get_height() / 4 + 40))
        self.screen_instance.blit(self.text.render("Ball launch: up arrow", True, (255, 255, 255)),
                                  dest=(((self.screen_instance.get_width() / 4) - 8),
                                        self.screen_instance.get_height() / 4 + 60))
        self.screen_instance.blit(self.text.render("Pause: SPACE", True, (255, 255, 255)),
                                  dest=(((self.screen_instance.get_width() / 4) - 8),
                                        self.screen_instance.get_height() / 4 + 80))
        self.screen_instance.blit(self.text.render("Quit: ESC", True, (255, 255, 255)),
                                  dest=(((self.screen_instance.get_width() / 4) - 8),
                                        self.screen_instance.get_height() / 4 + 100))
        text_Score = self.text_sub.render("SCORE:", True, (255, 255, 255))
        self.screen_instance.blit(text_Score, dest=(
            ((self.screen_instance.get_width() / 4) * 3 - 4), self.screen_instance.get_height() / 4))
        text_S_best = self.text.render("Best score: {} POINTS".format(self.bestScore), True, (255, 255, 255))
        self.screen_instance.blit(text_S_best, dest=(
            ((self.screen_instance.get_width() / 4) * 3 - 4), self.screen_instance.get_height() / 4 + 40))
        text_S_last = self.text.render("Last score: {} POINTS".format(self.lastScore), True, (255, 255, 255))
        self.screen_instance.blit(text_S_last, dest=(
            ((self.screen_instance.get_width() / 4) * 3 - 4), self.screen_instance.get_height() / 4 + 60))

    def display(self, score, lives):
        text_INFO = self.text.render('Lives [♥]: {} --|-- SCORE: {} '.format(lives, score), True, (255, 255, 255))
        self.screen_instance.blit(text_INFO, dest=(0, self.screen_instance.get_height() - 18))
        pass

    def pause_display(self):
        text_pause = self.text_sub.render("|| PAUSE ||", True, (255, 255, 255))
        self.screen_instance.blit(text_pause, dest=(
            ((self.screen_instance.get_width() / 2) - 4), self.screen_instance.get_height() / 2))
        text_pause_c = self.text.render("press space", True, (255, 255, 255))
        self.screen_instance.blit(text_pause_c, dest=(
            self.screen_instance.get_width() / 2, ((self.screen_instance.get_height() / 2) + 20)))

    def display_gameOver(self, score):
        text_gameOver = self.text_sub.render("|| Game Over ||", True, (255, 255, 255))
        self.screen_instance.blit(text_gameOver, dest=(
            ((self.screen_instance.get_width() / 2) - 4), self.screen_instance.get_height() / 2))
        text_Y_Score = self.text_sub.render("Your score: {}".format(score), True, (255, 255, 255))
        self.screen_instance.blit(text_Y_Score, dest=(
            ((self.screen_instance.get_width() / 4) * 3 - 4), self.screen_instance.get_height() / 4))
        text_end = self.text_sub.render("|| Press space ||", True, (255, 255, 255))
        self.screen_instance.blit(text_end, dest=(
            ((self.screen_instance.get_width() / 2) - 4), self.screen_instance.get_height() / 2))

    def display_u_win(self, score):
        text_u_win = self.text_sub.render("|| YOU WIN ||", True, (255, 255, 255))
        self.screen_instance.blit(text_u_win, dest=(
            ((self.screen_instance.get_width() / 2) - 4), self.screen_instance.get_height() / 4))
        text_Y_Score = self.text_sub.render("Your score: {}".format(score), True, (255, 255, 255))
        self.screen_instance.blit(text_Y_Score, dest=(
            ((self.screen_instance.get_width() / 4) * 3 - 4), self.screen_instance.get_height() / 4))
        text_end = self.text_sub.render("|| Press space ||", True, (255, 255, 255))
        self.screen_instance.blit(text_end, dest=(
            ((self.screen_instance.get_width() / 2) - 4), self.screen_instance.get_height() / 2))
