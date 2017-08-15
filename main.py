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

TRIANGLES = calculate_triangles_up_to_n(BIG_N)


class Solver:
    def __init__(self, num):
        self.num = num

    def calculate_height(self):
        prev = 0
        for h, n in TRIANGLES.items():
            if n > self.num:
                return prev, h
            prev = h

    def get_max_edge_height(self):
        # Edge height is the same as the central height
        # for the next biggest triangle
        # because we don't include the tip diamond as part of the edge
        for h, n in TRIANGLES.items():
            if n > self.num:
                return h

    def populate_right_column(self, height, num_free):
        num_right = int(num_free - height)
        right_col = [False] * height
        if num_right <= 0:
            return right_col
        for i in range(num_right):
            right_col[i] = True
        return right_col

    def is_certain(self, right, index):
        return right[index]

    def calculate_probability(self, index, num):
        # Index is effectively how many heads we want - 1
        # num is effectively the number of coin tosses
        # Number of permutations giving by binomial
        index += 1
        total = 0
        # Scipy's binom would make this simpler
        while index <= num:
            perms = factorial(num)/(factorial(index)*factorial(num - index))
            total += perms / pow(2, num)
            index += 1
        return total

    def get_number_free(self):
        p, __ = self.calculate_height()
        return self.num - TRIANGLES[p]

    def inside_triangle(self, h, x, y):
        # Can treat triangle as right-angle by ignoring left side
        if x + y <= h:
            return True
        return False

    def get_probability(self, x, y):
        # Due to symmetry can ignore sign
        x = abs(x)

        # Look for some early outs
        if x == 0 and y == 0 and self.num > 0:
            return 1.0

        p, h = self.calculate_height()
        if y >= h:
            return 0.0

        # If position inside previous triangle then it is a hit
        if self.inside_triangle(p, x, y):
            return 1.0

        # If cannot be in next triangle then it is a miss
        if not self.inside_triangle(h, x, y):
            return 0.0

        h = self.get_max_edge_height()
        free = self.get_number_free()
        right_col = self.populate_right_column(h, free)

        # Check to see if with left full the selected index is occupied
        # This means 1.0
        if self.is_certain(right_col, y):
            return 1.0

        # Calculate probability
        return self.calculate_probability(y, free)


if __name__ == "__main__":
    f = open("B-large-practice.in", "r")
    input_data = f.read().strip()
    f.close()

    lines = input_data.split('\n')

    for i, line in enumerate(lines):
        s = line.split(' ')
        solver = Solver(int(s[0]))
        ans = solver.get_probability(int(s[1]), int(s[2]))
        print("Case #{0}: {1}".format(i + 1, ans))
