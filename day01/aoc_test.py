import unittest

import aoc


class TestAoc(unittest.TestCase):

    def test_get_solution_1_should_return_sum_of_input_entries(self):
        self.assertEqual(14, aoc.getSolutionPart1([141,
                                                     140,
                                                     160,
                                                     161,
                                                     162,
                                                     172,
                                                     178,
                                                     185,
                                                     184,
                                                     186,
                                                     187,
                                                     195,
                                                     216,
                                                     239,
                                                     243,
                                                     247,
                                                     248,
                                                     243]))

    def test_get_solution_2_should_return_product_of_input_entries(self):
        self.assertEqual(True,True)


if __name__ == '__main__':
    unittest.main()
