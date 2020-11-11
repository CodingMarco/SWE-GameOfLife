import unittest

from src.board import Board


def draw_board(b: Board):
    print("---------------------------------")
    for y in range(0, b.get_height()):
        for x in range(0, b.get_width()):
            print(b.get_living(x, y), end=" ")
        print()


class BoardTest(unittest.TestCase):
    def test_set_and_get_living(self):
        b = Board(5, 5)
        b.toggle_living(2, 3)
        self.assertTrue(b.get_living(2, 3))


class GetNumberOfLivingNeighboursTest(unittest.TestCase):
    def test_3_horizontal(self):
        b = Board(5, 3)
        b.toggle_living(1, 1)
        b.toggle_living(2, 1)
        b.toggle_living(3, 1)
        self.assertEqual(b.get_number_of_living_neighbours(1, 1), 1)
        self.assertEqual(b.get_number_of_living_neighbours(2, 1), 2)
        self.assertEqual(b.get_number_of_living_neighbours(3, 1), 1)

    def test_3_vertical(self):
        b = Board(3, 5)
        b.toggle_living(1, 1)
        b.toggle_living(1, 2)
        b.toggle_living(1, 3)
        draw_board(b)
        self.assertEqual(b.get_number_of_living_neighbours(1, 1), 1)
        self.assertEqual(b.get_number_of_living_neighbours(1, 2), 2)
        self.assertEqual(b.get_number_of_living_neighbours(1, 3), 1)



    def test_in_middle(self):
        b = Board(5, 5)
        b.toggle_living(2, 3)
        b.toggle_living(2, 1)
        self.assertEqual(b.get_number_of_living_neighbours(2, 2), 2)

    def test_at_top(self):
        b = Board(5, 5)
        b.toggle_living(0, 3)
        b.toggle_living(1, 2)
        self.assertEqual(b.get_number_of_living_neighbours(0, 2), 2)

    def test_index_not_out_of_range_at_bottom(self):
        b = Board(5, 5)
        b.toggle_living(4, 1)
        b.toggle_living(4, 3)
        self.assertEqual(b.get_number_of_living_neighbours(4, 2), 2)

    def test_at_bottom_over_edge(self):
        b = Board(5, 5)
        b.toggle_living(4, 1)
        b.toggle_living(4, 3)
        b.toggle_living(0, 2)
        self.assertEqual(b.get_number_of_living_neighbours(4, 2), 3)




if __name__ == '__main__':
    unittest.main()