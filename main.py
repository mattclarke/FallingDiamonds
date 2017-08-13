# https://code.google.com/codejam/contest/2434486/dashboard#s=p1
from collections import OrderedDict

SMALL_N = 20
BIG_N = 1000000


def calculate_triangles_up_to_n(n):
    triangles = OrderedDict()
    # Height in diamonds at x = 0 goes up in twos starting from zero
    h = 0
    while True:
        if h == 0:
            triangles[0] = 1
        else:
            # Number of whole diamonds = (h + 1) + (h) + (h - 1) ... + (1)
            w = h + 1
            # Both these calculations work but which is quicker?
            # ans = sum(x for x in range(w + 1))
            ans = ((w * w) - w)/2 + w
            triangles[h] = ans
            if ans >= n:
                break
        h += 2
    return triangles

TRIANGLES = calculate_triangles_up_to_n(SMALL_N)


class Solver:
    def __init__(self, num):
        self.num = num

    def calculate_height(self, num):
        prev = 0

        for h, n in TRIANGLES.items():
            if n > num:
                return prev
            prev = h

    def get_max_edge_height(self, num):
        # Edge height is the same as the central height
        # for the next biggest triangle
        # because we don't include the tip diamond as part of the edge
        for h, n in TRIANGLES.items():
            if n > num:
                return h

    def create_columns(self):
        h = self.get_max_edge_height(self.num)
        left_col = [False] * h
        right_col = [False] * h
        return left_col, right_col

    def populate_columns(self, left_col, right_col, num_free):
        def _fill_column(col, num_free):
            while True:
                if num_free == 0:
                    return 0
                if col[-1]:
                    # All of the column is full
                    return num_free
                # Fill the first unfilled space
                col[col.index(False)] = True
                num_free -= 1
        # Fill the right-hand column first
        num_free = _fill_column(right_col, num_free)
        _fill_column(left_col, num_free)
        return left_col, right_col

    def shift_diamond_left(self, left_col, right_col):
        # Should throw if cannot shift further left?
        pass

    def calculate_probability(self):
        h = self.get_max_edge_height(self.num)
        left_col = [False] * h
        right_col = [False] * h
        free = self.get_number_free()

    def get_number_free(self):
        h = self.calculate_height(self.num)
        return self.num - TRIANGLES[h]

    def get_probability(self, x, y):
        # Due to symmetry can ignore sign
        x = abs(x)
        if self.calculate_height(self.num) < y:
            return 0.0
        return 1.0
