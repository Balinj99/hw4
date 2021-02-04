import unittest
import full_name

class TestCase(unittest.TestCase):
    def test1(self):
        result = full_name.full("Jacob", "Balin")
        self.assertEqual(result, "Jacob Balin")

    def test2(self):
        result = full_name.full("Jacob123", "Balin456")
        self.assertEqual(result, "Jacob123 Balin456")

    def test3(self):
        result = full_name.full(5, 6)
        self.assertEqual(result, "5 6")

    def test4(self):
        result = full_name.full(5, "Balin")
        self.assertEqual(result, "5 Balin")

if __name__ == "__main__":
    unittest.main()   