from io import BytesIO

import cairosvg
import io

from pygame.transform import scale
from pygame.image import load
from pygame import Surface

from data.classes import Coordinates


def load_svg_as_asset(file_path: str) -> Surface:
    """
    This method is used to load svg images int pygame :class:`Surface`

    :param file_path:
    :return:
    """
    new_bites = cairosvg.svg2png(url=file_path)
    return load(io.BytesIO(new_bites))


def create_game_object(surface: Surface, size: Coordinates) -> Surface:
    return scale(surface, (size.x, size.y))
