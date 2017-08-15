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
        self.assertEqual(0, s.calculate_height(1)[0])

    def test_calculate_height_for_five_diamonds_is_zero(self):
        s = Solver(1)
        self.assertEqual(0, s.calculate_height(5)[0])

    def test_calculate_height_for_six_diamonds_is_two(self):
        s = Solver(1)
        self.assertEqual(2, s.calculate_height(6)[0])

    def test_calculate_height_for_fourteen_diamonds_is_two(self):
        s = Solver(1)
        self.assertEqual(2, s.calculate_height(14)[0])

    def test_calculate_height_for_fifteen_diamonds_is_four(self):
        s = Solver(1)
        self.assertEqual(4, s.calculate_height(15)[0])

    def test_one_diamond_misses_zero_two(self):
        s = Solver(1)
        self.assertEqual(0.0, s.get_probability(0, 2))

    def test_three_diamonds_hits_zero_zero(self):
        s = Solver(3)
        self.assertEqual(1.0, s.get_probability(0, 0))

    def test_edge_height_for_seven_to_fourteen_is_four(self):
        s = Solver(7)
        self.assertEqual(4, s.get_max_edge_height(7))
        s = Solver(14)
        self.assertEqual(4, s.get_max_edge_height(14))

    def test_edge_height_for_sixteen_to_twentyseven_is_six(self):
        s = Solver(16)
        self.assertEqual(6, s.get_max_edge_height(16))
        s = Solver(27)
        self.assertEqual(6, s.get_max_edge_height(27))

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

    def test_create_columns_for_various_n_gives_correct_length(self):
        s = Solver(3)
        ans = s.create_columns()
        self.assertEqual(2, len(ans[0]))
        self.assertEqual(2, len(ans[1]))
        s = Solver(14)
        ans = s.create_columns()
        self.assertEqual(4, len(ans[0]))
        self.assertEqual(4, len(ans[1]))
        s = Solver(27)
        ans = s.create_columns()
        self.assertEqual(6, len(ans[0]))
        self.assertEqual(6, len(ans[1]))

    def test_populate_columns_for_height_four_and_eight_diamonds_fills_both(self):
        s = Solver(14)
        l, r = s.create_columns()
        l, r = s.populate_columns(l, r, 8)
        self.assertEqual([True, True, True, True], l)
        self.assertEqual([True, True, True, True], r)

    def test_populate_columns_for_height_four_and_six_diamonds_fills_left_and_half_right(self):
        s = Solver(14)
        l, r = s.create_columns()
        l, r = s.populate_columns(l, r, 6)
        self.assertEqual([True, True, True, True], l)
        self.assertEqual([True, True, False, False], r)

    def test_is_certain_when_right_column_contains_two_and_index_is_one(self):
        s = Solver(14)
        l, r = s.create_columns()
        l, r = s.populate_columns(l, r, 6)
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

    def test_four_diamonds_hits_one_two_half_never(self):
        s = Solver(4)
        self.assertEqual(0, s.get_probability(0, 2))
