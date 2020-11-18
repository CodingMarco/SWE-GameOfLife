import pygame
from ui import Ui
from board import Board
import gamerules


class Controller:
    GENERATIONUPDATE = pygame.USEREVENT+1

    def __init__(self, board: Board, cell_size):
        self._board = board
        self._ui = Ui(cell_size, self._board)
        self._new_generation_delay = 100
        self._quit = False
        self._generation_update_enabled = False

        # Mouse motions would trigger unnecessary redraw events very frequently
        pygame.event.set_blocked(pygame.MOUSEMOTION)

    def run(self):
        pygame.init()

        while not self._quit:
            self._update_ui()
            event = pygame.event.wait()
            self._handle_event(event)

        pygame.quit()

    def _update_ui(self):
        self._ui.draw_game(self._board)
        pygame.display.update()

    def _handle_event(self, event):
        if event.type == pygame.QUIT:
            self._quit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self._handle_mouse_event()
        elif event.type == pygame.KEYDOWN:
            self._handle_keydown_event(event)
        elif event.type == Controller.GENERATIONUPDATE:
            self._board = gamerules.apply_new_generation(self._board)

    def _handle_mouse_event(self):
        x, y = self._ui.mouse_coordinates_to_cell()
        self._board.toggle_living(x, y)

    def _handle_keydown_event(self, event):
        if event.key == pygame.K_r:
            self._set_generationupdate_enabled(True)
        elif event.key == pygame.K_SPACE:
            self._on_space_pressed()
        elif event.key == pygame.K_MINUS:
            self._new_generation_delay = round(self._new_generation_delay * 1.2)
            self._update_generationupdate_timer_delay()
        elif event.key == pygame.K_PLUS:
            self._new_generation_delay = round(self._new_generation_delay * 0.8)
            self._update_generationupdate_timer_delay()
        elif event.key == pygame.K_ESCAPE:
            self._quit = True

    def _set_generationupdate_enabled(self, enable):
        if enable == self._generation_update_enabled:
            return

        if enable:
            self._update_generationupdate_timer_delay()

        else:
            pygame.time.set_timer(Controller.GENERATIONUPDATE, 0)

        self._generation_update_enabled = enable

    def _on_space_pressed(self):
        if self._generation_update_enabled:
            self._set_generationupdate_enabled(False)
        else:
            self._post_single_generationupdate_event()

    @staticmethod
    def _post_single_generationupdate_event():
        pygame.event.post(pygame.event.Event(Controller.GENERATIONUPDATE))

    def _update_generationupdate_timer_delay(self):
        pygame.time.set_timer(Controller.GENERATIONUPDATE, self._new_generation_delay)
