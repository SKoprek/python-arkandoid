import pygame
import pickle
from pygame.locals import KEYDOWN, K_ESCAPE, K_UP, K_DOWN, K_LEFT, K_RIGHT, QUIT, K_SPACE

print(pygame.ver)

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

uruchomiona = True
pauza = False
ball_speed = 4
player_speed = 5
# UI #
text = pygame.font.SysFont('bold-arial', 18)
text_sub = pygame.font.SysFont('bold-arial', 24)
text_title = pygame.font.SysFont('bold-arial', 30)


class UI:
    def __init__(self):
        try:
            self.scoresList = pickle.load(open("scores", "rb"))
        except:
            self.scoresList = [0, 0]
        print(self.scoresList)
        self.lastScore = self.scoresList[0]
        self.bestScore = self.scoresList[1]

    def menu_dispay(self):

        self.text_MENU = text_title.render('MENU', True, (255, 255, 255))
        self.text_Controls = text_sub.render('CONTROLS', True, (255, 255, 255))
        self.text_C_start = text.render("Start: Space", True, (255, 255, 255))
        self.text_C_moves = text.render("Move: left and right arrow", True, (255, 255, 255))
        self.text_C_lunch = text.render("Ball launch: up arrow", True, (255, 255, 255))
        self.text_C_pause = text.render("Pause: SPACE", True, (255, 255, 255))
        self.text_C_quit = text.render("Quit: ESC", True, (255, 255, 255))
        screen.blit(self.text_MENU, dest=(((SCREEN_WIDTH / 2) - 4), SCREEN_HEIGHT / 8))
        screen.blit(self.text_Controls, dest=(((SCREEN_WIDTH / 4) - 4), SCREEN_HEIGHT / 4))
        screen.blit(self.text_C_start, dest=(((SCREEN_WIDTH / 4) - 8), SCREEN_HEIGHT / 4 + 20))
        screen.blit(self.text_C_moves, dest=(((SCREEN_WIDTH / 4) - 8), SCREEN_HEIGHT / 4 + 40))
        screen.blit(self.text_C_lunch, dest=(((SCREEN_WIDTH / 4) - 8), SCREEN_HEIGHT / 4 + 60))
        screen.blit(self.text_C_pause, dest=(((SCREEN_WIDTH / 4) - 8), SCREEN_HEIGHT / 4 + 80))
        screen.blit(self.text_C_quit, dest=(((SCREEN_WIDTH / 4) - 8), SCREEN_HEIGHT / 4 + 100))
        self.text_Score = text_sub.render("SCORE:", True, (255, 255, 255))
        screen.blit(self.text_Score, dest=(((SCREEN_WIDTH / 4) * 3 - 4), SCREEN_HEIGHT / 4))
        self.text_S_best = text.render("Best score: {} POINTS".format(self.bestScore), True, (255, 255, 255))
        screen.blit(self.text_S_best, dest=(((SCREEN_WIDTH / 4) * 3 - 4), SCREEN_HEIGHT / 4 + 40))
        self.text_S_last = text.render("Last score: {} POINTS".format(self.lastScore), True, (255, 255, 255))
        screen.blit(self.text_S_last, dest=(((SCREEN_WIDTH / 4) * 3 - 4), SCREEN_HEIGHT / 4 + 60))

    def display(self, score, lives):
        self.text_INFO = text.render('Lives [♥]: {} --|-- SCORE: {} '.format(lives, score), True, (255, 255, 255))
        screen.blit(self.text_INFO, dest=(0, SCREEN_HEIGHT - 18))
        pass

    def pause_display(self):
        if pauza:
            self.text_pause = text_sub.render("|| PAUSE ||", True, (255, 255, 255))
            screen.blit(self.text_pause, dest=(((SCREEN_WIDTH / 2) - 4), SCREEN_HEIGHT / 2))
            self.text_pause_c = text.render("press space", True, (255, 255, 255))
            screen.blit(self.text_pause_c, dest=(SCREEN_WIDTH / 2, ((SCREEN_HEIGHT / 2) + 20)))
        else:
            pass

    def display_gameOver(self, score):
        self.text_gameOver = text_sub.render("|| Game Over ||", True, (255, 255, 255))
        screen.blit(self.text_gameOver, dest=(((SCREEN_WIDTH / 2) - 4), SCREEN_HEIGHT / 2))
        self.text_Y_Score = text_sub.render("Your score: {}".format(score), True, (255, 255, 255))
        screen.blit(self.text_Y_Score, dest=(((SCREEN_WIDTH / 4) * 3 - 4), SCREEN_HEIGHT / 4))
        self.text_end = text_sub.render("|| Press space ||", True, (255, 255, 255))
        screen.blit(self.text_end, dest=(((SCREEN_WIDTH / 2) - 4), SCREEN_HEIGHT / 2))

    def display_u_win(self, score):
        self.text_u_win = text_sub.render("|| YOU WIN ||", True, (255, 255, 255))
        screen.blit(self.text_u_win, dest=(((SCREEN_WIDTH / 2) - 4), SCREEN_HEIGHT / 4))
        self.text_Y_Score = text_sub.render("Your score: {}".format(score), True, (255, 255, 255))
        screen.blit(self.text_Y_Score, dest=(((SCREEN_WIDTH / 4) * 3 - 4), SCREEN_HEIGHT / 4))
        self.text_end = text_sub.render("|| Press space ||", True, (255, 255, 255))
        screen.blit(self.text_end, dest=(((SCREEN_WIDTH / 2) - 4), SCREEN_HEIGHT / 2))


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        self.lives = 3
        self.score = 0
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((30, 10))
        self.surf.fill((255, 0, 0))
        self.surf = pygame.image.load("images/belka.png").convert()
        self.rect = self.surf.get_rect(center=(x, y))
        print(self.surf.get_rect(center=(x, y)))

    def update(self, pressed_keys):
        if pauza:
            return
        if pressed_keys[K_LEFT] and level.level > 0:
            self.rect.move_ip(-player_speed, 0)
        if pressed_keys[K_RIGHT] and level.level > 0:
            self.rect.move_ip(player_speed, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH


class Klocek(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((20, 10))
        self.surf = pygame.image.load("images/klocek.png").convert()
        self.rect = self.surf.get_rect(center=(x, y))


    def set_kolor(self, color):
        self.surf.fill(color)


class Ball(pygame.sprite.Sprite):

    def __init__(self, x, y):
        self.surf = pygame.Surface((5, 5))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=(x, y))
        self.move = False
        self.direction = pygame.Vector2()
        print(self.surf.get_rect(center=(x, y)))

    def update(self):
        if pauza:
            return
        elif not self.move:
            self.rect.x = player.rect.x + ((player.surf.get_width() / 2) - 1)
            self.rect.y = player.rect.y - self.surf.get_height() - 1
            if level.level > 0:
                if pressed_keys[K_UP] and pressed_keys[K_LEFT]:
                    self.direction.x = -ball_speed
                    self.direction.y = -ball_speed
                if pressed_keys[K_UP] and pressed_keys[K_RIGHT]:
                    self.direction.x = ball_speed
                    self.direction.y = -ball_speed
                if pressed_keys[K_UP]:
                    self.direction.y = -ball_speed
                    self.move = True
            else:
                pass
        elif self.move:
            # print("Payer: ",player.rect.x," | BALL: ",ball.rect.x)
            self.rect.move_ip(self.direction.x, self.direction.y)
            if self.rect.bottom < 0:
                print("HIT TOP")
                self.direction.y *= -1
            if self.rect.left < 0:
                print("HIT LEFT")
                self.direction.x *= -1
            if self.rect.right > SCREEN_WIDTH - self.surf.get_width():
                self.direction.x *= -1
                print("HIT RIGHT")
            if self.rect.top > SCREEN_HEIGHT - self.surf.get_height():
                print("HIT bottom")
                player.lives -= 1
                if (player.lives <= 0):
                    print("GAME OVER")
                    level.game_over()
                self.move = False
            if pygame.sprite.collide_rect(self, player):
                if self.rect.x < (player.rect.x + player.surf.get_width() / 2):
                    self.direction.x = 0
                    self.direction.x = -ball_speed
                    self.direction.y *= -1
                    print("lewo")
                elif self.rect.x > (player.rect.x + player.surf.get_width() / 2):
                    self.direction.x = 0
                    self.direction.x = ball_speed
                    self.direction.y *= -1
                    print("prawo")
                else:
                    print("CENTEr")
                    self.direction.y *= -1

            pass
        else:
            print("Error???")


class Level:
    def __init__(self):
        self.level = 0
        ui.menu_dispay()
        self.klocki = pygame.sprite.Group()

    def generate_level(self):
        if level.level == 6:
            level.level = -2
        print("generate level: ", self.level)
        player.rect = player.surf.get_rect(center=(305, 450))
        self.klocki = pygame.sprite.Group()
        if self.level == 1:
            klocek = Klocek(SCREEN_WIDTH / 2 - 20, 20)
            self.klocki.add(klocek)
        else:
            for x in range(self.level * 10):
                if (x % 4 == 0):
                    klocek = Klocek(SCREEN_WIDTH / 2 - (20 * (x / 4) + 5 * (x / 4)), SCREEN_HEIGHT / 4)
                elif (x % 4 == 1):
                    klocek = Klocek(SCREEN_WIDTH / 2 - (20 * (x / 4) + 5 * (x / 4)), SCREEN_HEIGHT / 4 - 60)
                elif (x % 4 == 2):
                    klocek = Klocek(SCREEN_WIDTH / 2 + (20 * (x / 4) + 5 * (x / 4)), SCREEN_HEIGHT / 4 - 90)
                else:
                    klocek = Klocek(SCREEN_WIDTH / 2 + (20 * (x / 4) + 5 * (x / 4)), SCREEN_HEIGHT / 4 - 30)
                self.klocki.add(klocek)
        pass

    def start_game(self):
        self.level = 1
        player.lives = 3
        player.score = 0
        self.generate_level()
        print("Game Start")

    def game_over(self):
        self.level = -1
        self.klocki.empty()
        print("Game Over")


pygame.display.set_caption("Szymon Koprek")

ui = UI()
level = Level()

player = Player(305, 450)
ball = Ball(315, 440)

# def update_ball_position():
#     pass



while uruchomiona:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            uruchomiona = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                uruchomiona = False
            if event.key == K_SPACE:
                if level.level == 0:
                    level.start_game()
                elif level.level < 0:
                    level.level = 0
                elif level.level > 0:
                    if pauza:
                        pauza = not pauza
                        print("Pauza F")
                    else:
                        pauza = not pauza
                        print("Pauza T")

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    ball.update()

    screen.fill((0, 0, 0))

    for klocek in level.klocki:
        screen.blit(klocek.surf, klocek.rect)
    screen.blit(player.surf, player.rect)
    screen.blit(ball.surf, ball.rect)

    if pygame.sprite.spritecollideany(ball, level.klocki):
        delete_klocek = pygame.sprite.spritecollideany(ball, level.klocki)
        delete_klocek.kill()
        if not level.klocki:
            level.level += 1
            ball.move = False
            level.generate_level()
        ball.direction.y *= -1
        player.score += 10
        # usuniecie klocka
    if level.level == 0:
        ui.menu_dispay()
    if level.level > 0:
        ui.display(player.score, player.lives)
        ui.pause_display()
    if level.level == -1:
        ui.display_gameOver(player.score)
        ui.lastScore = player.score
        if player.score > ui.bestScore:
            ui.bestScore = player.score
        ui.scoresList[0] = ui.lastScore
        ui.scoresList[1] = ui.bestScore
        pickle.dump(ui.scoresList, open("scores", "wb"))
    if level.level == -2:
        ui.display_u_win(player.score)
        ui.lastScore = player.score
        if player.score > ui.bestScore:
            ui.bestScore = player.score
        ui.scoresList[0] = ui.lastScore
        ui.scoresList[1] = ui.bestScore
        pickle.dump(ui.scoresList, open("scores", "wb"))
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
