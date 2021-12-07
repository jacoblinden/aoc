import unittest

import aoc


class TestAoc(unittest.TestCase):

    def test_get_solution_1_should_return_sum_of_input_entries(self):
        self.assertEqual(150, aoc.getSolutionPart1([16, 1, 2, 0, 4, 2, 7, 1, 2, 14]))

    def test_get_solution_2_should_return_product_of_input_entries(self):
        self.assertEqual(900, aoc.getSolutionPart2(["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]))


if __name__ == '__main__':
    unittest.main()
