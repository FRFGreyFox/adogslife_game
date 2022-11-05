import pygame

from game.core.base_objects import BaseObject
from game.core.base_sprite import BaseSprite
from game.settings import ASSETS_DIR

ANIMALS_ASSETS_DIR = ASSETS_DIR / 'animals'
DOGS_ASSETS_DIR = ANIMALS_ASSETS_DIR / 'dogs'
CATS_ASSETS_DIR = ANIMALS_ASSETS_DIR / 'cats'
RATS_ASSETS_DIR = ANIMALS_ASSETS_DIR / 'rats'


class Dog1(BaseObject):
    class IdleSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            self.main_img = pygame.image.load(DOGS_ASSETS_DIR / '1' / 'idle.png')
            self.animation_delay = 750
            self.frame_size = (36, 26)
            self.rect = pygame.Rect(0, 0, *self.frame_size[::-1])
            self.images = (
                self.main_img.subsurface((2, 22), self.frame_size),
                self.main_img.subsurface((50, 22), self.frame_size),
                self.main_img.subsurface((97, 22), self.frame_size),
                self.main_img.subsurface((146, 22), self.frame_size),
            )

    class WalkSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            self.main_img = pygame.image.load(DOGS_ASSETS_DIR / '1' / 'walk.png')
            self.animation_delay = 500
            self.frame_size = (41, 26)
            self.rect = pygame.Rect(0, 0, *self.frame_size[::-1])

            self.images = (
                self.main_img.subsurface((1, 22), self.frame_size),
                self.main_img.subsurface((50, 22), self.frame_size),
                self.main_img.subsurface((98, 22), self.frame_size),
                self.main_img.subsurface((146, 22), self.frame_size),
                self.main_img.subsurface((191, 22), self.frame_size),
                self.main_img.subsurface((239, 22), self.frame_size),
            )

    class AttackSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            self.main_img = pygame.image.load(DOGS_ASSETS_DIR / '1' / 'attack.png')
            self.animation_delay = 500
            self.frame_size = (42, 26)
            self.rect = pygame.Rect(0, 0, *self.frame_size[::-1])
            self.images = (
                self.main_img.subsurface((4, 22), self.frame_size),
                self.main_img.subsurface((51, 22), self.frame_size),
                self.main_img.subsurface((100, 22), self.frame_size),
                self.main_img.subsurface((148, 22), self.frame_size),
            )

    class DeathProgressSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            self.main_img = pygame.image.load(DOGS_ASSETS_DIR / '1' / 'death.png')
            self.animation_delay = 500
            self.frame_size = (41, 26)
            self.rect = pygame.Rect(0, 0, *self.frame_size[::-1])

            self.images = (
                self.main_img.subsurface((2, 22), self.frame_size),
                self.main_img.subsurface((53, 22), self.frame_size),
                self.main_img.subsurface((101, 22), self.frame_size),
                self.main_img.subsurface((149, 22), self.frame_size),
            )

    class DeathIdleSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            self.main_img = pygame.image.load(DOGS_ASSETS_DIR / '1' / 'death.png')
            self.animation_delay = 500
            self.frame_size = (42, 26)
            self.rect = pygame.Rect(0, 0, *self.frame_size[::-1])

            self.images = (
                self.main_img.subsurface((149, 22), self.frame_size),
            )

    def load_animations(self) -> None:
        self.animations = {
            'idle': self.IdleSprite(object=self),
            'walk': self.WalkSprite(object=self),
            'attack': self.AttackSprite(object=self),
            'death_progress': self.DeathProgressSprite(object=self),
            'death_idle': self.DeathIdleSprite(object=self),
        }
        self.current_sprite_group.add(self.animations['idle'])


class Dog2(BaseObject):
    class IdleSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            self.main_img = pygame.image.load(DOGS_ASSETS_DIR / '2' / 'idle.png')
            self.animation_delay = 750
            self.frame_size = (32, 32)
            self.rect = pygame.Rect(0, 0, *self.frame_size[::-1])
            self.images = (
                self.main_img.subsurface((3, 16), self.frame_size),
                self.main_img.subsurface((51, 16), self.frame_size),
                self.main_img.subsurface((99, 16), self.frame_size),
                self.main_img.subsurface((147, 16), self.frame_size),
            )

    class WalkSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            self.main_img = pygame.image.load(DOGS_ASSETS_DIR / '2' / 'walk.png')
            self.animation_delay = 500
            self.frame_size = (45, 30)
            self.rect = pygame.Rect(0, 0, *self.frame_size[::-1])
            self.images = (
                self.main_img.subsurface((0, 18), self.frame_size),
                self.main_img.subsurface((49, 18), self.frame_size),
                self.main_img.subsurface((99, 18), self.frame_size),
                self.main_img.subsurface((147, 18), self.frame_size),
                self.main_img.subsurface((191, 18), self.frame_size),
                self.main_img.subsurface((240, 18), self.frame_size),
            )

    class AttackSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            self.main_img = pygame.image.load(DOGS_ASSETS_DIR / '2' / 'attack.png')
            self.animation_delay = 500
            self.frame_size = (42, 32)
            self.rect = pygame.Rect(0, 0, *self.frame_size[::-1])
            self.images = (
                self.main_img.subsurface((3, 16), self.frame_size),
                self.main_img.subsurface((52, 16), self.frame_size),
                self.main_img.subsurface((100, 16), self.frame_size),
                self.main_img.subsurface((147, 16), self.frame_size),
            )

    class DeathProgressSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            self.main_img = pygame.image.load(DOGS_ASSETS_DIR / '2' / 'death.png')
            self.animation_delay = 500
            self.frame_size = (44, 32)
            self.rect = pygame.Rect(0, 0, *self.frame_size[::-1])

            self.images = (
                self.main_img.subsurface((3, 16), self.frame_size),
                self.main_img.subsurface((52, 16), self.frame_size),
                self.main_img.subsurface((100, 16), self.frame_size),
                self.main_img.subsurface((148, 16), self.frame_size),
            )

    class DeathIdleSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            self.main_img = pygame.image.load(DOGS_ASSETS_DIR / '2' / 'death.png')
            self.animation_delay = 500
            self.frame_size = (44, 32)
            self.rect = pygame.Rect(0, 0, *self.frame_size[::-1])
            self.images = (
                self.main_img.subsurface((148, 16), self.frame_size),
            )

    def load_animations(self) -> None:
        self.animations = {
            'idle': self.IdleSprite(object=self),
            'walk': self.WalkSprite(object=self),
            'attack': self.AttackSprite(object=self),
            'death_progress': self.DeathProgressSprite(object=self),
            'death_idle': self.DeathIdleSprite(object=self),
        }
        self.current_sprite_group.add(self.animations['idle'])


class Cat1(BaseObject):
    class IdleSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            self.main_img = pygame.image.load(CATS_ASSETS_DIR / '1' / 'idle.png')
            self.animation_delay = 750
            self.frame_size = (32, 32)
            self.rect = pygame.Rect(0, 0, *self.frame_size[::-1])
            self.images = (
                self.main_img.subsurface((3, 16), self.frame_size),
                self.main_img.subsurface((51, 16), self.frame_size),
                self.main_img.subsurface((99, 16), self.frame_size),
                self.main_img.subsurface((147, 16), self.frame_size),
            )

    class WalkSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            self.main_img = pygame.image.load(CATS_ASSETS_DIR / '1' / 'walk.png')
            self.animation_delay = 500
            self.frame_size = (45, 30)
            self.rect = pygame.Rect(0, 0, *self.frame_size[::-1])
            self.images = (
                self.main_img.subsurface((0, 18), self.frame_size),
                self.main_img.subsurface((49, 18), self.frame_size),
                self.main_img.subsurface((99, 18), self.frame_size),
                self.main_img.subsurface((147, 18), self.frame_size),
                self.main_img.subsurface((191, 18), self.frame_size),
                self.main_img.subsurface((240, 18), self.frame_size),
            )

    class AttackSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            self.main_img = pygame.image.load(CATS_ASSETS_DIR / '1' / 'attack.png')
            self.animation_delay = 500
            self.frame_size = (42, 32)
            self.rect = pygame.Rect(0, 0, *self.frame_size[::-1])
            self.images = (
                self.main_img.subsurface((3, 16), self.frame_size),
                self.main_img.subsurface((52, 16), self.frame_size),
                self.main_img.subsurface((100, 16), self.frame_size),
                self.main_img.subsurface((147, 16), self.frame_size),
            )

    class DeathProgressSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            self.main_img = pygame.image.load(CATS_ASSETS_DIR / '1' / 'death.png')
            self.animation_delay = 500
            self.frame_size = (44, 32)
            self.rect = pygame.Rect(0, 0, *self.frame_size[::-1])

            self.images = (
                self.main_img.subsurface((3, 16), self.frame_size),
                self.main_img.subsurface((52, 16), self.frame_size),
                self.main_img.subsurface((100, 16), self.frame_size),
                self.main_img.subsurface((148, 16), self.frame_size),
            )

    class DeathIdleSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            self.main_img = pygame.image.load(CATS_ASSETS_DIR / '1' / 'death.png')
            self.animation_delay = 500
            self.frame_size = (44, 32)
            self.rect = pygame.Rect(0, 0, *self.frame_size[::-1])
            self.images = (
                self.main_img.subsurface((148, 16), self.frame_size),
            )

    def load_animations(self) -> None:
        self.animations = {
            'idle': self.IdleSprite(object=self),
            'walk': self.WalkSprite(object=self),
            'attack': self.AttackSprite(object=self),
            'death_progress': self.DeathProgressSprite(object=self),
            'death_idle': self.DeathIdleSprite(object=self),
        }
        self.current_sprite_group.add(self.animations['idle'])


class Cat2(BaseObject):
    class IdleSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            self.main_img = pygame.image.load(CATS_ASSETS_DIR / '2' / 'idle.png')
            self.animation_delay = 750
            self.frame_size = (32, 32)
            self.rect = pygame.Rect(0, 0, *self.frame_size[::-1])
            self.images = (
                self.main_img.subsurface((3, 16), self.frame_size),
                self.main_img.subsurface((51, 16), self.frame_size),
                self.main_img.subsurface((99, 16), self.frame_size),
                self.main_img.subsurface((147, 16), self.frame_size),
            )

    class WalkSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            self.main_img = pygame.image.load(CATS_ASSETS_DIR / '2' / 'walk.png')
            self.animation_delay = 500
            self.frame_size = (45, 30)
            self.rect = pygame.Rect(0, 0, *self.frame_size[::-1])
            self.images = (
                self.main_img.subsurface((0, 18), self.frame_size),
                self.main_img.subsurface((49, 18), self.frame_size),
                self.main_img.subsurface((99, 18), self.frame_size),
                self.main_img.subsurface((147, 18), self.frame_size),
                self.main_img.subsurface((191, 18), self.frame_size),
                self.main_img.subsurface((240, 18), self.frame_size),
            )

    class AttackSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            self.main_img = pygame.image.load(CATS_ASSETS_DIR / '2' / 'attack.png')
            self.animation_delay = 500
            self.frame_size = (42, 32)
            self.rect = pygame.Rect(0, 0, *self.frame_size[::-1])
            self.images = (
                self.main_img.subsurface((3, 16), self.frame_size),
                self.main_img.subsurface((52, 16), self.frame_size),
                self.main_img.subsurface((100, 16), self.frame_size),
                self.main_img.subsurface((147, 16), self.frame_size),
            )

    class DeathProgressSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            self.main_img = pygame.image.load(CATS_ASSETS_DIR / '2' / 'death.png')
            self.animation_delay = 500
            self.frame_size = (44, 32)
            self.rect = pygame.Rect(0, 0, *self.frame_size[::-1])

            self.images = (
                self.main_img.subsurface((3, 16), self.frame_size),
                self.main_img.subsurface((52, 16), self.frame_size),
                self.main_img.subsurface((100, 16), self.frame_size),
                self.main_img.subsurface((148, 16), self.frame_size),
            )

    class DeathIdleSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            self.main_img = pygame.image.load(CATS_ASSETS_DIR / '2' / 'death.png')
            self.animation_delay = 500
            self.frame_size = (44, 32)
            self.rect = pygame.Rect(0, 0, *self.frame_size[::-1])
            self.images = (
                self.main_img.subsurface((148, 16), self.frame_size),
            )

    def load_animations(self) -> None:
        self.animations = {
            'idle': self.IdleSprite(object=self),
            'walk': self.WalkSprite(object=self),
            'attack': self.AttackSprite(object=self),
            'death_progress': self.DeathProgressSprite(object=self),
            'death_idle': self.DeathIdleSprite(object=self),
        }
        self.current_sprite_group.add(self.animations['idle'])


class Rat1(BaseObject):
    class IdleSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            self.main_img = pygame.image.load(RATS_ASSETS_DIR / '1' / 'idle.png')
            self.animation_delay = 750
            self.frame_size = (20, 8)
            self.rect = pygame.Rect(0, 0, *self.frame_size[::-1])
            self.images = (
                self.main_img.subsurface((3, 24), self.frame_size),
                self.main_img.subsurface((35, 24), self.frame_size),
                self.main_img.subsurface((67, 24), self.frame_size),
                self.main_img.subsurface((99, 24), self.frame_size),
            )

    class WalkSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            self.main_img = pygame.image.load(RATS_ASSETS_DIR / '1' / 'walk.png')
            self.animation_delay = 500
            self.frame_size = (20, 8)
            self.rect = pygame.Rect(0, 0, *self.frame_size[::-1])
            self.images = (
                self.main_img.subsurface((3, 24), self.frame_size),
                self.main_img.subsurface((35, 24), self.frame_size),
                self.main_img.subsurface((67, 24), self.frame_size),
                self.main_img.subsurface((99, 24), self.frame_size),
            )

    class DeathProgressSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            self.main_img = pygame.image.load(RATS_ASSETS_DIR / '1' / 'death.png')
            self.animation_delay = 500
            self.frame_size = (20, 7)
            self.rect = pygame.Rect(0, 0, *self.frame_size[::-1])

            self.images = (
                self.main_img.subsurface((3, 25), self.frame_size),
                self.main_img.subsurface((35, 25), self.frame_size),
            )

    class DeathIdleSprite(BaseSprite):
        def load_sprite_images(self) -> None:
            self.main_img = pygame.image.load(RATS_ASSETS_DIR / '1' / 'death.png')
            self.animation_delay = 500
            self.frame_size = (20, 7)
            self.rect = pygame.Rect(0, 0, *self.frame_size[::-1])
            self.images = (
                self.main_img.subsurface((35, 25), self.frame_size),
            )

    def load_animations(self) -> None:
        self.animations = {
            'idle': self.IdleSprite(object=self),
            'walk': self.WalkSprite(object=self),
            'death_progress': self.DeathProgressSprite(object=self),
            'death_idle': self.DeathIdleSprite(object=self),
        }
        self.current_sprite_group.add(self.animations['idle'])
