import unittest
from main import Solver, calculate_triangles_up_to_n


class FallingDiamondsTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_calculate_triangles_matches_hand_calculated_values(self):
        ans = calculate_triangles_up_to_n(66)
        self.assertEqual(1, ans[0][1])
        self.assertEqual(6, ans[1][1])
        self.assertEqual(15, ans[2][1])
        self.assertEqual(28, ans[3][1])
        self.assertEqual(45, ans[4][1])
        self.assertEqual(66, ans[5][1])

    def test_one_diamond_hits_zero_zero(self):
        s = Solver(1)
        self.assertEqual(1.0, s.get_probability(0, 0))

    def test_calculate_height_for_one_diamond_is_zero(self):
        s = Solver(1)
        self.assertEqual(0, s.calculate_height(1))

    def test_one_diamond_misses_zero_two(self):
            s = Solver(1)
            self.assertEqual(0.0, s.get_probability(0, 2))


# 7
# 1 0 0
# 1 0 2
# 3 0 0
# 3 2 0
# 3 1 1
# 4 1 1
# 4 0 2
# 	Case #1: 1.0
# Case #2: 0.0
# Case #3: 1.0
# Case #4: 0.75
# Case #5: 0.25
# Case #6: 0.5
# Case #7: 0.0