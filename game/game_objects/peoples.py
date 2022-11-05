import pygame.image

from game.core.base_objects import BaseObject
from game.core.base_sprite import BaseSprite
from game.settings import ASSETS_DIR

PEOPLES_ASSETS_DIR = ASSETS_DIR / 'peoples'


class Human1(BaseObject):
    class IdleSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            main_img = pygame.image.load(PEOPLES_ASSETS_DIR / '1' / 'idle.png')
            self.animation_delay = 1000
            self.frame_size = (24, 40)
            self.images = (
                main_img.subsurface((5, 8), self.frame_size),
                main_img.subsurface((53, 8), self.frame_size),
                main_img.subsurface((101, 8), self.frame_size),
                main_img.subsurface((149, 8), self.frame_size),
                main_img.subsurface((196, 8), self.frame_size),
                main_img.subsurface((244, 8), self.frame_size),
            )

    class WalkSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            main_img = pygame.image.load(PEOPLES_ASSETS_DIR / '1' / 'walk.png')
            self.animation_delay = 1000
            self.frame_size = (25, 41)
            self.images = (
                main_img.subsurface((5, 7), self.frame_size),
                main_img.subsurface((53, 7), self.frame_size),
                main_img.subsurface((101, 7), self.frame_size),
                main_img.subsurface((149, 7), self.frame_size),
                main_img.subsurface((196, 7), self.frame_size),
                main_img.subsurface((246, 7), self.frame_size),
            )

    class SpecialSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            main_img = pygame.image.load(PEOPLES_ASSETS_DIR / '1' / 'special.png')
            self.animation_delay = 1000
            self.frame_size = (33, 40)
            self.images = (
                main_img.subsurface((5, 8), self.frame_size),
                main_img.subsurface((53, 8), self.frame_size),
                main_img.subsurface((101, 8), self.frame_size),
                main_img.subsurface((147, 8), self.frame_size),
                main_img.subsurface((196, 8), self.frame_size),
                main_img.subsurface((244, 8), self.frame_size),
            )

    def load_animations(self) -> None:
        self.animations = {
            'idle': self.IdleSprite(object=self),
            'walk': self.WalkSprite(object=self),
            'special': self.SpecialSprite(object=self),
        }
        self.current_sprite_group.add(self.animations['idle'])


class Human2(BaseObject):
    class IdleSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            main_img = pygame.image.load(PEOPLES_ASSETS_DIR / '2' / 'idle.png')
            self.animation_delay = 1000
            self.frame_size = (22, 39)
            self.images = (
                main_img.subsurface((4, 9), self.frame_size),
                main_img.subsurface((52, 9), self.frame_size),
                main_img.subsurface((100, 9), self.frame_size),
                main_img.subsurface((148, 9), self.frame_size),
            )

    class WalkSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            main_img = pygame.image.load(PEOPLES_ASSETS_DIR / '2' / 'walk.png')
            self.animation_delay = 1000
            self.frame_size = (26, 39)
            self.images = (
                main_img.subsurface((2, 9), self.frame_size),
                main_img.subsurface((50, 9), self.frame_size),
                main_img.subsurface((98, 9), self.frame_size),
                main_img.subsurface((146, 9), self.frame_size),
                main_img.subsurface((194, 9), self.frame_size),
                main_img.subsurface((243, 9), self.frame_size),
            )

    class SpecialSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            main_img = pygame.image.load(PEOPLES_ASSETS_DIR / '2' / 'special.png')
            self.animation_delay = 1000
            self.frame_size = (24, 39)
            self.images = (
                main_img.subsurface((3, 9), self.frame_size),
                main_img.subsurface((51, 9), self.frame_size),
                main_img.subsurface((100, 9), self.frame_size),
                main_img.subsurface((148, 9), self.frame_size),
            )

    def load_animations(self) -> None:
        self.animations = {
            'idle': self.IdleSprite(object=self),
            'walk': self.WalkSprite(object=self),
            'special': self.SpecialSprite(object=self),
        }
        self.current_sprite_group.add(self.animations['idle'])


class Human3(BaseObject):
    class IdleSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            main_img = pygame.image.load(PEOPLES_ASSETS_DIR / '3' / 'idle.png')
            self.animation_delay = 1000
            self.frame_size = (22, 39)
            self.images = (
                main_img.subsurface((4, 9), self.frame_size),
                main_img.subsurface((52, 9), self.frame_size),
                main_img.subsurface((100, 9), self.frame_size),
                main_img.subsurface((148, 9), self.frame_size),
            )

    class WalkSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            main_img = pygame.image.load(PEOPLES_ASSETS_DIR / '3' / 'walk.png')
            self.animation_delay = 1000
            self.frame_size = (26, 39)
            self.images = (
                main_img.subsurface((2, 9), self.frame_size),
                main_img.subsurface((50, 9), self.frame_size),
                main_img.subsurface((98, 9), self.frame_size),
                main_img.subsurface((146, 9), self.frame_size),
                main_img.subsurface((194, 9), self.frame_size),
                main_img.subsurface((243, 9), self.frame_size),
            )

    class SpecialSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            main_img = pygame.image.load(PEOPLES_ASSETS_DIR / '3' / 'special.png')
            self.animation_delay = 1000
            self.frame_size = (24, 39)
            self.images = (
                main_img.subsurface((3, 9), self.frame_size),
                main_img.subsurface((51, 9), self.frame_size),
                main_img.subsurface((100, 9), self.frame_size),
                main_img.subsurface((148, 9), self.frame_size),
            )

    def load_animations(self) -> None:
        self.animations = {
            'idle': self.IdleSprite(object=self),
            'walk': self.WalkSprite(object=self),
            'special': self.SpecialSprite(object=self),
        }
        self.current_sprite_group.add(self.animations['idle'])


class Human4(BaseObject):
    class IdleSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            main_img = pygame.image.load(PEOPLES_ASSETS_DIR / '4' / 'idle.png')
            self.animation_delay = 1000
            self.frame_size = (22, 39)
            self.images = (
                main_img.subsurface((4, 9), self.frame_size),
                main_img.subsurface((52, 9), self.frame_size),
                main_img.subsurface((100, 9), self.frame_size),
                main_img.subsurface((148, 9), self.frame_size),
            )

    class WalkSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            main_img = pygame.image.load(PEOPLES_ASSETS_DIR / '4' / 'walk.png')
            self.animation_delay = 1000
            self.frame_size = (26, 39)
            self.images = (
                main_img.subsurface((2, 9), self.frame_size),
                main_img.subsurface((50, 9), self.frame_size),
                main_img.subsurface((98, 9), self.frame_size),
                main_img.subsurface((146, 9), self.frame_size),
                main_img.subsurface((194, 9), self.frame_size),
                main_img.subsurface((243, 9), self.frame_size),
            )

    class SpecialSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            main_img = pygame.image.load(PEOPLES_ASSETS_DIR / '4' / 'special.png')
            self.animation_delay = 1000
            self.frame_size = (24, 39)
            self.images = (
                main_img.subsurface((3, 9), self.frame_size),
                main_img.subsurface((51, 9), self.frame_size),
                main_img.subsurface((100, 9), self.frame_size),
                main_img.subsurface((148, 9), self.frame_size),
            )

    def load_animations(self) -> None:
        self.animations = {
            'idle': self.IdleSprite(object=self),
            'walk': self.WalkSprite(object=self),
            'special': self.SpecialSprite(object=self),
        }
        self.current_sprite_group.add(self.animations['idle'])


class Human5(BaseObject):
    class IdleSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            main_img = pygame.image.load(PEOPLES_ASSETS_DIR / '5' / 'idle.png')
            self.animation_delay = 1000
            self.frame_size = (22, 39)
            self.images = (
                main_img.subsurface((4, 9), self.frame_size),
                main_img.subsurface((52, 9), self.frame_size),
                main_img.subsurface((100, 9), self.frame_size),
                main_img.subsurface((148, 9), self.frame_size),
            )

    class WalkSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            main_img = pygame.image.load(PEOPLES_ASSETS_DIR / '5' / 'walk.png')
            self.animation_delay = 1000
            self.frame_size = (26, 39)
            self.images = (
                main_img.subsurface((2, 9), self.frame_size),
                main_img.subsurface((50, 9), self.frame_size),
                main_img.subsurface((98, 9), self.frame_size),
                main_img.subsurface((146, 9), self.frame_size),
                main_img.subsurface((194, 9), self.frame_size),
                main_img.subsurface((243, 9), self.frame_size),
            )

    def load_animations(self) -> None:
        self.animations = {
            'idle': self.IdleSprite(object=self),
            'walk': self.WalkSprite(object=self),
        }
        self.current_sprite_group.add(self.animations['idle'])


class Human6(BaseObject):
    class IdleSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            main_img = pygame.image.load(PEOPLES_ASSETS_DIR / '6' / 'idle.png')
            self.animation_delay = 1000
            self.frame_size = (22, 39)
            self.images = (
                main_img.subsurface((4, 9), self.frame_size),
                main_img.subsurface((52, 9), self.frame_size),
                main_img.subsurface((100, 9), self.frame_size),
                main_img.subsurface((148, 9), self.frame_size),
            )

    class WalkSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            main_img = pygame.image.load(PEOPLES_ASSETS_DIR / '6' / 'walk.png')
            self.animation_delay = 1000
            self.frame_size = (26, 39)
            self.images = (
                main_img.subsurface((2, 9), self.frame_size),
                main_img.subsurface((50, 9), self.frame_size),
                main_img.subsurface((98, 9), self.frame_size),
                main_img.subsurface((146, 9), self.frame_size),
                main_img.subsurface((194, 9), self.frame_size),
                main_img.subsurface((243, 9), self.frame_size),
            )

    class SpecialSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            main_img = pygame.image.load(PEOPLES_ASSETS_DIR / '6' / 'special.png')
            self.animation_delay = 1000
            self.frame_size = (24, 39)
            self.images = (
                main_img.subsurface((3, 9), self.frame_size),
                main_img.subsurface((51, 9), self.frame_size),
                main_img.subsurface((100, 9), self.frame_size),
                main_img.subsurface((148, 9), self.frame_size),
            )

    def load_animations(self) -> None:
        self.animations = {
            'idle': self.IdleSprite(object=self),
            'walk': self.WalkSprite(object=self),
            'special': self.SpecialSprite(object=self),
        }
        self.current_sprite_group.add(self.animations['idle'])
