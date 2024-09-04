import unittest
from util import find_file_csv_fileno
from util import find_file_csv_fileno_frame_idx

class MyTestCase(unittest.TestCase):
    def test_find_file_csv_fileno(self):
        folder_path = r'data/aic-2024/map-keyframes'
        file_path = r'data/aic-2024/keyframes/L01_V001/001.jpg'

        filecsv, n = find_file_csv_fileno(folder_path, file_path)
        self.assertEqual(filecsv, 'L01_V001.csv')
        self.assertEqual(n, 1)

    def test_find_file_csv_fileno_frame_idx(self):
        folder_path = r'../data/aic-2024/map-keyframes'
        file_path = r'data/aic-2024/keyframes/L01_V001/001.jpg'

        filecsv, n, frame_idx = find_file_csv_fileno_frame_idx(folder_path, file_path)
        self.assertEqual(filecsv, 'L01_V001.csv')
        self.assertEqual(n, 1)
        self.assertEqual(frame_idx, 0)

if __name__ == '__main__':
    unittest.main()
