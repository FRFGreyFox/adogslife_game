from typing import TYPE_CHECKING, Union

from more_itertools import chunked
from pygame.event import Event
from pygame.surface import Surface

from game.game_objects.animals import Cat1, Cat2, Dog1, Dog2, Rat1

if TYPE_CHECKING:
    from game.game import Game


class TestFrame:
    def __init__(self, game: 'Game') -> None:
        self.game = game
        self.objects = [
            Dog1(), Dog1(), Dog1(), Dog1(), Dog1(),
            Dog2(), Dog2(), Dog2(), Dog2(), Dog2(),
            Cat1(), Cat1(), Cat1(), Cat1(), Cat1(),
            Cat2(), Cat2(), Cat2(), Cat2(), Cat2(),
            Rat1(), Rat1(), Rat1(), Rat1(), Rat1(),
        ]

        start_x = 50
        buf_y = 50
        for objects in chunked(self.objects, 5):
            buf_x = start_x
            buf_y += 50
            for object_, animation in zip(objects, ('idle', 'walk', 'attack', 'death_progress', 'death_idle')):
                object_.change_animation(animation)
                object_.coords = [buf_x, buf_y]
                buf_x += 50

    def unload_frame(self) -> None:
        del self.objects

    def update(self, delta_time: float, events: list[Event]) -> None:
        for obj in self.objects:
            obj.update(delta_time, events)

    def draw(self, surface: Union[Surface, None] = None, offset: tuple[int, int] = (0, 0)) -> None:
        if surface is None:
            surface = self.game.screen
        for obj in self.objects:
            obj.draw(surface)  # type: ignore
