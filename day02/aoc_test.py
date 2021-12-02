import unittest

import aoc


class TestAoc(unittest.TestCase):

    def test_get_solution_1_should_return_sum_of_input_entries(self):
        self.assertEqual(150, aoc.getSolutionPart1(["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]))

    def test_get_solution_2_should_return_product_of_input_entries(self):
        self.assertEqual(5, aoc.getSolutionPart2([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]))


if __name__ == '__main__':
    unittest.main()
