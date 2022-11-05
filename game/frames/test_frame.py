from typing import TYPE_CHECKING, Union

from more_itertools import chunked
from pygame.event import Event
from pygame.surface import Surface

from game.game_objects import animals

if TYPE_CHECKING:
    from game.game import Game


class TestFrame:
    def __init__(self, game: 'Game') -> None:
        self.game = game
        self.objects = [
            animals.Dog1(), animals.Dog1(), animals.Dog1(), animals.Dog1(), animals.Dog1(),
            animals.Dog2(), animals.Dog2(), animals.Dog2(), animals.Dog2(), animals.Dog2(),
            animals.Cat1(), animals.Cat1(), animals.Cat1(), animals.Cat1(), animals.Cat1(),
            animals.Cat2(), animals.Cat2(), animals.Cat2(), animals.Cat2(), animals.Cat2(),
            animals.Rat1(), animals.Rat1(), animals.Rat1(), animals.Rat1(), animals.Rat1(),
            animals.Rat2(), animals.Rat2(), animals.Rat2(), animals.Rat2(), animals.Rat2(),
            animals.Bird1(), animals.Bird1(), animals.Bird1(), animals.Bird1(), animals.Bird1(),
            animals.Bird2(), animals.Bird2(), animals.Bird2(), animals.Bird2(), animals.Bird2(),
        ]

        start_x = 50
        buf_y = 0
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
