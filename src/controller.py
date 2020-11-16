import pygame
from ui import Ui
from board import Board
import gamerules


class Controller:
    GENERATIONUPDATE = pygame.USEREVENT+1

    def __init__(self, board: Board, cell_size):
        print("Constr")
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
            event = pygame.event.wait()
            self.process_event(event)
        pygame.event.clear()
        self.set_update_paused(True)

    def process_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.process_mouse_event()
        elif event.type == pygame.KEYDOWN:
            self.process_keydown_event(event)
        elif event.type == Controller.GENERATIONUPDATE:
            self.board = gamerules.apply_new_generation(self.board)

    def process_keydown_event(self, event):
        if event.key == pygame.K_r:
            self.set_update_paused(False)
        elif event.key == pygame.K_SPACE:
            self.space_pressed()
        elif event.key == pygame.K_MINUS:
            self.new_generation_delay = round(self.new_generation_delay * 1.1)
            self.update_generationupdate_timer_delay()
        elif event.key == pygame.K_PLUS:
            self.new_generation_delay = round(self.new_generation_delay * 0.9)
            self.update_generationupdate_timer_delay()
        elif event.key == pygame.K_ESCAPE:
            self.quit = True

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
            self.update_generationupdate_timer_delay()

        self.paused = do_pause

    def update_generationupdate_timer_delay(self):
        pygame.time.set_timer(Controller.GENERATIONUPDATE, self.new_generation_delay)

    def update_ui(self):
        self.ui.draw_game_board(self.board)
        pygame.display.update()



