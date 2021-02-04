import unittest
import cube_volume

class TestCase(unittest.TestCase):
    def test1(self):
        result = cube_volume.vol(5)
        self.assertEqual(result, 125)

    def test2(self):
        result = cube_volume.vol(-5)
        self.assertEqual(result, 125)

    def test3(self):
        result = cube_volume.vol(5.0)
        self.assertEqual(result, 125)

    def test4(self):
        result = cube_volume.vol(-5.0)
        self.assertEqual(result, 125)

if __name__ == "__main__":
    unittest.main()   