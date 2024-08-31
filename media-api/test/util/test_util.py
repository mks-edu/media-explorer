import unittest
from util import find_file_csv_fieno

class MyTestCase(unittest.TestCase):
    def test_find_file_csv_fieno(self):
        folder_path = r'\Data_2024\Map Keyframe\map-keyframes-b1\map-keyframes'
        file_path = r'\Data_2024\Keyframe\Keyframes_L01\keyframes\L01_V001\001.jpg'

        filecsv, n = find_file_csv_fieno(folder_path, file_path)
        self.assertEqual(filecsv, 'L01_V001.csv')
        self.assertEqual(n, 1)


if __name__ == '__main__':
    unittest.main()
