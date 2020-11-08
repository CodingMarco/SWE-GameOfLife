import pygame
from ui import Ui
from board import Board


class Controller:
    def __init__(self, board_width, board_height, cell_size):
        self.board = Board(board_width, board_height)
        self.ui = Ui(cell_size, self.board)
        self.quit = False


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

    def process_mouse_event(self):
        x, y = self.ui.mouse_coordinates_to_cell()
        self.board.toggle_living(x, y)

    def update_ui(self):
        self.ui.draw_game_goard(self.board)
        pygame.display.update()



