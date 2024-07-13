from confing import Config
from data.game_class import Game

config: Config = Config()
game_instance: Game = Game(config=config)


if __name__ == "__main__":
    game_instance.run()
