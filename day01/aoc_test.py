import unittest

import aoc


class TestAoc(unittest.TestCase):

    def test_get_solution_1_should_return_sum_of_input_entries(self):
        self.assertEqual(2421, aoc.getSolutionPart1([0, 3, 4, 42, 106, 107, 267, 269]))

    def test_get_solution_2_should_return_product_of_input_entries(self):
        self.assertEqual(335, aoc.getSolutionPart2([0, 3, 4, 42, 106, 107, 267, 269]))


if __name__ == '__main__':
    unittest.main()
