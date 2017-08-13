# https://code.google.com/codejam/contest/2434486/dashboard#s=p1

SMALL_N = 20
BIG_N = 1000000


def calculate_triangles_up_to_n(n):
    triangles = []
    # Height in diamonds at x = 0 goes up in twos starting from zero
    h = 0
    while True:
        if h == 0:
            triangles.append((0, 1))
        else:
            # Number of whole diamonds wide = height + 1
            w = h + 1
            ans = ((w * w) - w)/2 + w
            triangles.append((h, ans))
            if ans >= n:
                break
        h += 2
    return triangles

TRIANGLES = calculate_triangles_up_to_n(SMALL_N)


class Solver:
    def __init__(self, num):
        self.num = num

    def calculate_height(self, num):
        for h, n in TRIANGLES:
            print(h, n)
            if n >= num:
                return h

    def get_probability(self, x, y):
        if self.calculate_height(self.num) < y:
            return 0.0
        return 1.0
