from unittest import TestCase
from unittest import main
from cutting_stock import *
from knapsack.knapsack import knapsack


class TestSimplex(TestCase):
    def test_initial(self):
        capacity = 20
        w = [9, 8, 7, 6]
        n = [511, 301, 263, 383]
        exception = [[2, 0, 0, 0],
                     [0, 2, 0, 0],
                     [0, 0, 2, 0],
                     [0, 0, 0, 3]]
        self.assertEqual(get_initial_solution(w, capacity), exception)

    def test_new_column(self):
        capacity = 20
        w = [9, 8, 7, 6]
        n = [511, 301, 263, 383]
        a = [[2, 0, 0, 0],
             [0, 2, 0, 0],
             [0, 0, 2, 0],
             [0, 0, 0, 3]]
        aa = copy_two_dimension_list(a)
        nn = n.copy()
        c = [-1, -1, -1, -1]
        result = simplex(-1, 4, 4, aa, nn, c)
        dual = solve_dual(result, 4, 4, aa, nn, c)
        value, decision = knapsack(w, dual, capacity)
        self.assertEqual(decision, [0, 0, 2, 1])

    def test_cutting_stock(self):
        capacity = 20
        w = [9, 8, 7, 6]
        n = [511, 301, 263, 383]
        result = cutting_stock(w, n, capacity)
        exception = [Fraction(511, 2), Fraction(701, 8), 0, 0, Fraction(263, 2), Fraction(503, 4)]
        self.assertEqual(result, exception)


if __name__ == '__main__':
    main()
