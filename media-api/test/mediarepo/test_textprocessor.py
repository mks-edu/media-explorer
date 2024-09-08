import unittest

from sympy.core.exprtools import Term

from mediarepo.textprocessor import TextExtractor

class MyTestCase(unittest.TestCase):
    def test_TextExtractor_sameFolder(self):
        te = TextExtractor()

        folder_path = '../data/aic-2024/keyframes'
        nCount = te.extract_text_folder(folder_path)
        self.assertEqual(3, nCount)

    def test_TextExtractor_outFolder(self):
        te = TextExtractor()

        folder_path = '../data/aic-2024/keyframes'
        out_folder_path = '../out/extracted_text/keyframes'
        nCount = te.extract_text_folder(folder_path, out_folder_path)
        self.assertEqual(3, nCount)

if __name__ == '__main__':
    unittest.main()
