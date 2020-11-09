import logging


class Board:
    def __init__(self, width, height, preset):
        self.width = width
        self.height = height
        self.cell_data = [[0 for x in range(width)] for y in range(height)]
        self.place_preset_in_middle_of_board(preset)

    def place_preset_in_middle_of_board(self, preset):
        preset_width = len(preset[0])
        preset_height = len(preset)
        preset_offset_x = self.width // 2 - preset_width // 2
        preset_offset_y = self.height // 2 - preset_height // 2

        preset_x = 0
        preset_y = 0
        for x in range(preset_offset_x, preset_offset_x + preset_width):
            for y in range(preset_offset_y, preset_offset_y + preset_height):
                self.cell_data[x][y] = preset[preset_x][preset_y]
                preset_y += 1
            preset_x += 1
            preset_y = 0

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def toggle_living(self, x, y):
        if x < self.width and y < self.height:
            self.cell_data[x][y] = 0 if self.cell_data[x][y] else 1
        else:
            logging.error("Board: set_living(): x = {} or y = {} out of range!".format(x, y))

    def get_number_of_living_neighbours(self, x, y):
        nr_of_liv_neig = 0

        if self.cell_data[(x + 1) % self.width][y % self.height]:            # 1     # 4 3 2
            nr_of_liv_neig += 1                                                      # 5 o 1
                                                                                     # 6 7 8
        if self.cell_data[(x + 1) % self.width][(y + 1) % self.height]:      # 2
            nr_of_liv_neig += 1

        if self.cell_data[x % self.width][(y + 1) % self.height]:            # 3
            nr_of_liv_neig += 1

        if self.cell_data[(x - 1) % self.width][(y + 1) % self.height]:      # 4
            nr_of_liv_neig += 1

        if self.cell_data[(x - 1) % self.width][y % self.height]:            # 5
            nr_of_liv_neig += 1

        if self.cell_data[(x - 1) % self.width][(y - 1) % self.height]:      # 6
            nr_of_liv_neig += 1

        if self.cell_data[x % self.width][(y - 1) % self.height]:            # 7
            nr_of_liv_neig += 1

        if self.cell_data[(x + 1) % self.width][(y - 1) % self.height]:      # 8
            nr_of_liv_neig += 1

        return nr_of_liv_neig

    def get_living(self, x, y):
        if x < self.width and y < self.height:
            return self.cell_data[x][y]
        else:
            logging.error("Board: get_living(): x = {} or y = {} out of range!".format(x, y))
