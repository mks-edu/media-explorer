import unittest
from mediarepo import MyClip

class MyClipTestCase(unittest.TestCase):
    myclip = MyClip()
    json_folder = '../data/aic-2024/media-info'
    out_pkl_filepath = '../out/aic2024_metajson.pkl'
    def test_build_repo(self):



        self.myclip.build_video_embeddings_metajson(self.json_folder, self.out_pkl_filepath)

    def test_search_video(self):
        query = "Tin tuc thoi su Viet nam ngày 07/10/2023"
        self.myclip.load(self.out_pkl_filepath)
        self.myclip.search(query)

if __name__ == '__main__':
    unittest.main()
