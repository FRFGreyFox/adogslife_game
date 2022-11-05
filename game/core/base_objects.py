from abc import abstractmethod
from typing import TYPE_CHECKING

from pygame.event import Event
from pygame.sprite import Group
from pygame.surface import Surface

from game.constants import BASE_SIZE

if TYPE_CHECKING:
    from game.core.base_sprite import BaseSprite


class BaseObject:
    def __init__(self, *, size: float = BASE_SIZE) -> None:
        self.animations: dict[str, 'BaseSprite'] = {}
        self.coords = [0, 0]
        self.size = size
        self.is_moving = False
        self.in_air = False
        self.current_sprite_group = Group()
        self.load_animations()

    @abstractmethod
    def load_animations(self) -> None:
        raise NotImplementedError

    def set_coords(self, x: int, y: int) -> None:
        self.coords = [x, y]

    def change_animation(self, animation_name: str) -> None:
        self.current_sprite_group.empty()
        new_animation = self.animations.get(animation_name, self.animations['idle'])
        self.current_sprite_group.add(new_animation)

    def update(self, delta_time: float, events: list[Event]) -> None:
        self.current_sprite_group.update(delta_time, events)

    def draw(self, surface: Surface, offset: tuple[int, int] = (0, 0)) -> None:
        self.current_sprite_group.draw(surface)

    def resize_inst(self, new_size: float) -> None:
        self.size = new_size
