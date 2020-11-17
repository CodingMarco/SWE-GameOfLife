import logging


class Board:
    def __init__(self, width, height, preset=None):
        self.width = width
        self.height = height
        self._cell_data = [[0 for y in range(height)] for x in range(width)]
        if preset is not None:
            self._place_preset_in_middle_of_board(preset)

    def toggle_living(self, x, y):
        if x < self.width and y < self.height:
            self._cell_data[x][y] = 0 if self._cell_data[x][y] else 1
        else:
            logging.error("Board: toggle_living(): x = {} or y = {} out of range!".format(x, y))

    def get_number_of_living_neighbours(self, x, y):
        living_neighbours = 0

        if self.get_living((x + 1) % self.width, y % self.height):            # 1    # 4 3 2
            living_neighbours += 1                                                   # 5 o 1
                                                                                     # 6 7 8
        if self.get_living((x + 1) % self.width, (y + 1) % self.height):      # 2
            living_neighbours += 1

        if self.get_living(x % self.width, (y + 1) % self.height):            # 3
            living_neighbours += 1

        if self.get_living((x - 1) % self.width, (y + 1) % self.height):      # 4
            living_neighbours += 1

        if self.get_living((x - 1) % self.width, y % self.height):            # 5
            living_neighbours += 1

        if self.get_living((x - 1) % self.width, (y - 1) % self.height):      # 6
            living_neighbours += 1

        if self.get_living(x % self.width, (y - 1) % self.height):            # 7
            living_neighbours += 1

        if self.get_living((x + 1) % self.width, (y - 1) % self.height):      # 8
            living_neighbours += 1

        return living_neighbours

    def get_living(self, x, y):
        if x < self.width and y < self.height:
            return self._cell_data[x][y]
        else:
            logging.error("Board: get_living(): x = {} or y = {} out of range!".format(x, y))

    def _place_preset_in_middle_of_board(self, preset):
        preset_width = len(preset[0])
        preset_height = len(preset)
        preset_offset_x = self.width // 2 - preset_width // 2
        preset_offset_y = self.height // 2 - preset_height // 2

        if preset_width > self.width or preset_height > self.height:
            logging.error("Board: The board size is too small for the chosen preset!")
            return

        preset_x = 0
        preset_y = 0
        for x in range(preset_offset_x, preset_offset_x + preset_width):
            for y in range(preset_offset_y, preset_offset_y + preset_height):
                self._cell_data[x][y] = preset[preset_y][preset_x]
                preset_y += 1
            preset_x += 1
            preset_y = 0