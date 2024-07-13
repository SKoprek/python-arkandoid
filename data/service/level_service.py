from data.game_class import Game


def menu_screen(game_instance: Game):
    game_instance.ui.menu_display()


def start_game(game_instance: Game):
    game_instance.level.level = 1
    game_instance.level.generate_level(textures_assets=game_instance.textures_assets)

    game_instance.player.lives = 3
    game_instance.player.score = 0
    # game_instance.player.rect = game_instance.player.surf.get_rect(center=(305, 450))
    print(f"Game Start level: {game_instance.level.level}")


def next_level(game_instance: Game):
    game_instance.level.level += 1
    game_instance.level.generate_level(textures_assets=game_instance.textures_assets)

    # game_instance.player.rect = game_instance.player.surf.get_rect(center=(305, 450))
    print(f"Game Start level: {game_instance.level.level}")


def game_over(game_instance: Game):
    game_instance.level.level = -1
    game_instance.level.klocki.empty()
    print("Game Over")
