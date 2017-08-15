import unittest
from main import Solver, calculate_triangles_up_to_n


class FallingDiamondsTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_calculate_triangles_matches_hand_calculated_values(self):
        ans = calculate_triangles_up_to_n(66)
        self.assertEqual(1, ans[0])
        self.assertEqual(6, ans[2])
        self.assertEqual(15, ans[4])
        self.assertEqual(28, ans[6])
        self.assertEqual(45, ans[8])
        self.assertEqual(66, ans[10])

    def test_one_diamond_hits_zero_zero(self):
        s = Solver(1)
        self.assertEqual(1.0, s.get_probability(0, 0))

    def test_calculate_height_for_one_diamond_is_zero(self):
        s = Solver(1)
        self.assertEqual(0, s.calculate_height()[0])

    def test_calculate_height_for_five_diamonds_is_zero(self):
        s = Solver(5)
        self.assertEqual(0, s.calculate_height()[0])

    def test_calculate_height_for_six_diamonds_is_two(self):
        s = Solver(6)
        self.assertEqual(2, s.calculate_height()[0])

    def test_calculate_height_for_fourteen_diamonds_is_two(self):
        s = Solver(14)
        self.assertEqual(2, s.calculate_height()[0])

    def test_calculate_height_for_fifteen_diamonds_is_four(self):
        s = Solver(15)
        self.assertEqual(4, s.calculate_height()[0])

    def test_one_diamond_misses_zero_two(self):
        s = Solver(1)
        self.assertEqual(0.0, s.get_probability(0, 2))

    def test_three_diamonds_hits_zero_zero(self):
        s = Solver(3)
        self.assertEqual(1.0, s.get_probability(0, 0))

    def test_edge_height_for_seven_to_fourteen_is_four(self):
        s = Solver(7)
        self.assertEqual(4, s.get_max_edge_height())
        s = Solver(14)
        self.assertEqual(4, s.get_max_edge_height())

    def test_edge_height_for_sixteen_to_twentyseven_is_six(self):
        s = Solver(16)
        self.assertEqual(6, s.get_max_edge_height())
        s = Solver(27)
        self.assertEqual(6, s.get_max_edge_height())

    def test_number_of_free_diamonds_is_correct(self):
        s = Solver(3)
        self.assertEqual(2, s.get_number_free())
        s = Solver(5)
        self.assertEqual(4, s.get_number_free())
        s = Solver(7)
        self.assertEqual(1, s.get_number_free())
        s = Solver(14)
        self.assertEqual(8, s.get_number_free())
        s = Solver(16)
        self.assertEqual(1, s.get_number_free())
        s = Solver(27)
        self.assertEqual(12, s.get_number_free())

    def test_populate_columns_for_height_four_and_eight_diamonds_fills_right(self):
        s = Solver(14)
        r = s.populate_right_column(s.calculate_height()[1], 8)
        self.assertEqual([True, True, True, True], r)

    def test_populate_columns_for_height_four_and_six_diamonds_fills_half_right(self):
        s = Solver(12)
        r = s.populate_right_column(s.calculate_height()[1], 6)
        self.assertEqual([True, True, False, False], r)

    def test_is_certain_when_right_column_contains_two_and_index_is_one(self):
        s = Solver(5)
        r = s.populate_right_column(s.calculate_height()[1], 4)
        self.assertEqual(True, s.is_certain(r, 1))

    def test_when_one_diamond_index_zeros_probability_is_50(self):
        s = Solver(14)
        self.assertEqual(0.5, s.calculate_probability(0, 1))

    def test_when_two_diamonds_index_zeros_probability_is_75(self):
        s = Solver(14)
        self.assertEqual(0.75, s.calculate_probability(0, 2))

    def test_when_three_diamonds_index_zeros_probability_is_875(self):
        s = Solver(14)
        self.assertEqual(0.875, s.calculate_probability(0, 3))

    def test_when_one_diamond_index_ones_probability_is_0(self):
        s = Solver(14)
        self.assertEqual(0.0, s.calculate_probability(1, 1))

    def test_when_two_diamonds_index_ones_probability_is_25(self):
        s = Solver(14)
        self.assertEqual(0.25, s.calculate_probability(1, 2))

    def test_three_diamonds_hits_two_zero_often(self):
        s = Solver(3)
        self.assertEqual(0.75, s.get_probability(2, 0))

    def test_three_diamonds_hits_one_one_occasionally(self):
        s = Solver(3)
        self.assertEqual(0.25, s.get_probability(1, 1))

    def test_four_diamonds_hits_one_one_half_the_time(self):
        s = Solver(4)
        self.assertEqual(0.5, s.get_probability(1, 1))

    def test_four_diamonds_hits_one_two_never(self):
        s = Solver(4)
        self.assertEqual(0, s.get_probability(0, 2))

    def test_if_in_previous_triangle_then_true(self):
        s = Solver(7)
        self.assertEqual(True, s.inside_triangle(4, 0, 2))
        self.assertEqual(True, s.inside_triangle(4, 0, 4))
        self.assertEqual(True, s.inside_triangle(4, 1, 3))
        self.assertEqual(True, s.inside_triangle(4, 2, 2))
        self.assertEqual(True, s.inside_triangle(4, 3, 1))

    def test_if_not_in_previous_triangle_then_false(self):
        s = Solver(7)
        self.assertEqual(False, s.inside_triangle(4, 0, 6))
        self.assertEqual(False, s.inside_triangle(4, 1, 5))
        self.assertEqual(False, s.inside_triangle(4, 2, 4))
        self.assertEqual(False, s.inside_triangle(4, 3, 3))

    def test_six_diamonds_hits_zero_two_always(self):
        s = Solver(6)
        self.assertEqual(1.0, s.get_probability(0, 2))
