# https://code.google.com/codejam/contest/2434486/dashboard#s=p1
from collections import OrderedDict
from math import factorial, pow

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
                return prev, h
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
        # Fill the left-hand column first
        num_free = _fill_column(left_col, num_free)
        _fill_column(right_col, num_free)
        return left_col, right_col

    def is_certain(self, right, index):
        return right[index]

    def calculate_probability(self, index, num):
        # Index is effectively how many heads we want - 1
        # num is effectively the number of coin tosses
        # Number of permutations giving by binomial
        index += 1
        total = 0
        while index <= num:
            perms = factorial(num)/(factorial(index)*factorial(num - index))
            total += perms / pow(2, num)
            index += 1
        return total

    def get_number_free(self):
        p, __ = self.calculate_height(self.num)
        return self.num - TRIANGLES[p]

    def get_probability(self, x, y):
        # Due to symmetry can ignore sign
        x = abs(x)

        # Look for some early outs
        p, h = self.calculate_height(self.num)

        if y >= h:
            return 0.0

        if x == 0 and y == 0 and self.num > 0:
            return 1.0

        h = self.get_max_edge_height(self.num)
        left_col = [False] * h
        right_col = [False] * h
        free = self.get_number_free()
        left_col, right_col = self.populate_columns(left_col, right_col, free)
        hits = []

        # Check to see if with left full the selected index is occupied
        # This means 1.0
        if self.is_certain(right_col, y):
            return 1.0

        # Calculate probability
        return self.calculate_probability(y, free)
