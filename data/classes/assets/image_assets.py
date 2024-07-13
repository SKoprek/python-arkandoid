from pygame import Surface




class ImageAssets:
    """
    Images class
    TODO is faster because init??
    """

    def __init__(self):
        assets_path = "assets/textures/"
        from data.service import load_svg_as_asset
        self.PLATFORM_TEXTURE: Surface = load_svg_as_asset(f"{assets_path}platform.svg")
        self.BLOCK_TEXTURE: Surface = load_svg_as_asset(f"{assets_path}block.svg")
