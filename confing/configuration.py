import pygame

from data.classes import Coordinates


class Config:
    """
    Class containing app configuration.
    """

    def __init__(self):
        """Object initiation"""
        self.version: str = "v.0.1"
        self.created_by = "Szymon Koprek"

        self.resolution: Coordinates = Coordinates(640, 480)

        # Player Config
        self.player_lives = 3
        self.ball_speed = 4

        print("APP INFORMATION".center(50, "-"))
        print(f"{'App version: '.ljust(20)}: {self.version}")
        print(f"{'Pygame version: '.ljust(20)}: v.{pygame.ver}")
        print("*".center(50, "-"))
