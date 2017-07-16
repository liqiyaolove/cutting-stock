from unittest import TestCase
from unittest import main
from Simplex import Simplex


class TestSimplex(TestCase):
    def test_tableau(self):
        with open('text', 'r', encoding='utf-8') as f:
            m = int(f.readline().split()[0])
            n = int(f.readline().split()[0])
            a = [[0 for x in range(n)] for y in range(m)]
            for i in range(m):
                tmp = f.readline().split()
                for j in range(n):
                    a[i][j] = int(tmp[j])
            b = []
            for i in range(m):
                b.append(int(f.readline().split()[0]))
            c = []
            for j in range(n):
                c.append(int(f.readline().split()[0]))
        s = Simplex(m, n, a, b, c)
        result = [[2, 3, 1, 0, 0, 0, 6], [-3, 2, 0, 1, 0, 0, 3], [0, 2, 0, 0, 1, 0, 5],
                  [2, 1, 0, 0, 0, 1, 4], [-4, -3, 0, 0, 0, 0, 0]]
        self.assertEqual(s.create_tableau(), result)

if __name__ == '__main__':
    main()