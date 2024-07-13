from pygame.sprite import Sprite
from pygame import Surface, image


class Block(Sprite):
    """
    Block class
    """

    def __init__(self, width: float, height: float, textures_assets):
        """
        Object initial
        :param width:
        :param height:
        """
        from data.service.change_the_name import create_game_object
        from data.classes import Coordinates
        Sprite.__init__(self)
        self.surf = create_game_object(textures_assets.BLOCK_TEXTURE, Coordinates(40, 20))
        self.rect = self.surf.get_rect(center=(width, height))

    def set_color(self, color):
        """
        Update the color of a block
        :param color:
        :return:
        """
        self.surf.fill(color)
