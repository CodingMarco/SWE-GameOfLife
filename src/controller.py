import pygame
from ui import Ui
from board import Board
from gamerules import GameRules


class Controller:
    GENERATIONUPDATE = pygame.USEREVENT+1

    def __init__(self, board, cell_size):
        self.board = board
        self.ui = Ui(cell_size, self.board)
        self.new_generation_delay = 100
        # Mouse motions would trigger unnecessary redraw events
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        self.quit = False
        self.paused = True

    def run(self):
        while not self.quit:
            self.update_ui()
            events = self.wait_for_at_least_one_event()
            self.process_events(events)

    @staticmethod
    def wait_for_at_least_one_event():
        return [pygame.event.wait()] + pygame.event.get()

    def process_events(self, events):
        for event in events:
            self.process_event(event)

    def process_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            self.quit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.process_mouse_event()
        elif event.type == pygame.KEYDOWN:
            self.process_keydown_event(event)
        elif event.type == Controller.GENERATIONUPDATE:
            self.board = GameRules.apply_new_generation(self.board)

    def process_keydown_event(self, event):
        if event.key == pygame.K_r:
            self.set_update_paused(False)
        elif event.key == pygame.K_SPACE:
            self.space_pressed()

    def process_mouse_event(self):
        x, y = self.ui.mouse_coordinates_to_cell()
        self.board.toggle_living(x, y)

    def space_pressed(self):
        if self.paused:
            self.single_generationupdate_event()
        else:
            self.set_update_paused(True)

    @staticmethod
    def single_generationupdate_event():
        pygame.event.post(pygame.event.Event(Controller.GENERATIONUPDATE))

    def set_update_paused(self, do_pause):
        if do_pause == self.paused:
            return

        if do_pause:
            pygame.time.set_timer(Controller.GENERATIONUPDATE, 0)
        else:
            pygame.time.set_timer(Controller.GENERATIONUPDATE, self.new_generation_delay)

        self.paused = do_pause

    def update_ui(self):
        self.ui.draw_game_board(self.board)
        pygame.display.update()



