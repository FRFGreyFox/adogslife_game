import sys

import pygame
from pygame.event import Event

from game.constants import TICK_RATE
from game.frames.test_frame import TestFrame


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption('A dog`s life')
        self.clock = pygame.time.Clock()
        self.main()

    def get_events(self) -> tuple[float, list[Event]]:
        delta_time = self.clock.tick(TICK_RATE)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4:
                    pygame.display.toggle_fullscreen()
        return delta_time, events

    def main(self) -> None:
        current_frame = TestFrame(self)

        while True:
            delta_time, events = self.get_events()
            current_frame.update(delta_time, events)

            self.screen.fill(pygame.Color('white'))
            current_frame.draw()
            pygame.display.flip()
