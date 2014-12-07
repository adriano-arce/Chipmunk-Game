from sprite_sheet import SpriteSheet


class GraphicsComponent(object):
    def __init__(self, filename, patch_size, final_size, patch_pos):
        self.sheet = SpriteSheet(filename, patch_size, final_size)
        self.patch_pos = patch_pos

    def get_image(self):
        return self.sheet.get_patch(self.patch_pos)

    def update(self, sprite):
        sprite.image = self.get_image()