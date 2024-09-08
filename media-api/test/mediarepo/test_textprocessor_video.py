import unittest

from sympy.core.exprtools import Term

from mediarepo.textprocessor import TextExtractor

class MyTestCase(unittest.TestCase):

    def test_TextExtractor_video(self):
        te = TextExtractor()

        path = '/home/thachln/projects/aic-2024/videos/video/'

        nCount = te.extract_text_folder(path, source_type=1)
        self.assertEqual(29, nCount)
if __name__ == '__main__':
    unittest.main()
