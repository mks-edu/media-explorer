import unittest
from mediarepo import MyClip

class MyClipTestCase(unittest.TestCase):
    def test_build_repo(self):
        json_folder = '../data/aic-2024/media-info'
        out_pkl_filepath = '../out/aic2024_metajson.pkl'

        myclip = MyClip()
        myclip.build_video_embeddings_metajson(json_folder, out_pkl_filepath)


if __name__ == '__main__':
    unittest.main()
