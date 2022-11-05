from abc import abstractmethod
from itertools import cycle
from typing import TYPE_CHECKING, Any

import pygame
from pygame.event import Event

if TYPE_CHECKING:
    from game.core.base_objects import BaseObject


class BaseSprite(pygame.sprite.Sprite):
    buffer_delta_time: float
    animation_pause_delay: float
    animation_delay: int
    images: tuple[pygame.surface.Surface, ...]
    index: cycle
    rect: pygame.Rect
    main_img: pygame.surface.Surface
    size: float
    frame_size: tuple[int, int]

    def __init__(self, object: 'BaseObject', *args: list[Any], **kwargs: dict[str, Any]) -> None:
        super().__init__(*args)  # type: ignore
        self.object = object
        self.buffer_delta_time = 0.0
        self.size = self.object.size
        self.frame_size = (0, 0)

        self.load_sprite_images()
        self._prepare_images()
        self._load_sprite_buffer()

    @abstractmethod
    def load_sprite_images(self) -> None:
        raise NotImplementedError

    def _prepare_images(self) -> None:
        self.rect = pygame.Rect(0, 0, *self.frame_size[::-1])
        self.images = tuple(
            pygame.transform.scale(image, (self.frame_size[0] * self.size, self.frame_size[1] * self.size))
            for image in self.images
        )

    def _load_sprite_buffer(self) -> None:
        self.index = cycle(range(len(self.images)))
        self.image = self.images[next(self.index)]
        self.animation_pause_delay = self.animation_delay / len(self.images)

    def update(self, delta_time: float, events: list[Event], *args: list[Any], **kwargs: dict[str, Any]) -> None:
        super().update(*args, **kwargs)
        self.rect.x = self.object.coords[0]
        self.rect.y = self.object.coords[1]
        self.buffer_delta_time += delta_time
        if self.buffer_delta_time >= self.animation_pause_delay:
            self.image = self.images[next(self.index)]
            self.buffer_delta_time = 0
