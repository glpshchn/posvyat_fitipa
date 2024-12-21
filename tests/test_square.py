import unittest
from square import area, perimeter


class TestSquare(unittest.TestCase):

    def test1(self):
        a = -13
        with self.assertRaises(ValueError):
            perimeter(a)

    def test2(self):
        a = -13
        with self.assertRaises(ValueError):
            area(a)

    def test3(self):
        a = 0
        correct = 0
        self.assertEqual(area(a), correct)

    def test4(self):
        a = 0
        correct = 0
        self.assertEqual(perimeter(a), correct)

    def test5(self):
        a = 13
        correct = a * a
        self.assertEqual(area(a), correct)

    def test6(self):
        a = 13
        correct = 4 * a
        self.assertEqual(perimeter(a), correct)


if __name__ == '__main__':
    unittest.main()
