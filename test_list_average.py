import unittest
import list_average

class TestCase(unittest.TestCase):
    def test1(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = list_average.ave(arr)
        self.assertEqual(result, 5.5)

    def test2(self):
        arr = [-1, -2, -3, -4, -5]
        result = list_average.ave(arr)
        self.assertEqual(result, -3)

    def test3(self):
        arr = [1, -2, 3, -4, 5]
        result = list_average.ave(arr)
        self.assertEqual(result, 0.6)

    def test4(self):
        arr = [1.0, 2.1, 3.2, 4.3, 5.4]
        result = list_average.ave(arr)
        self.assertEqual(result, 3.2)

    def test5(self):
        arr = [1, 2.1, 3, 4.4, 5]
        result = list_average.ave(arr)
        self.assertEqual(result, 3.1)

    def test6(self):
        arr = []
        result = list_average.ave(arr)
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()   