import importlib.util
import pathlib
import unittest


SCRIPT = pathlib.Path(__file__).parents[1] / "scripts" / "douyin_download.py"
SPEC = importlib.util.spec_from_file_location("douyin_download", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ClassifyMediaProbeTests(unittest.TestCase):
    def test_video_detail_wins_before_dom_is_ready(self):
        probe = {
            "detailReady": True,
            "awemeType": 0,
            "hasImages": False,
            "hasVideo": True,
        }
        self.assertEqual(MODULE.classify_media_probe(probe), "video")

    def test_image_collection_is_a_note(self):
        probe = {
            "detailReady": True,
            "awemeType": 68,
            "hasImages": True,
            "hasVideo": False,
        }
        self.assertEqual(MODULE.classify_media_probe(probe), "note")

    def test_images_take_priority_when_both_media_shapes_exist(self):
        probe = {
            "detailReady": True,
            "awemeType": 68,
            "hasImages": True,
            "hasVideo": True,
        }
        self.assertEqual(MODULE.classify_media_probe(probe), "note")

    def test_incomplete_detail_is_inconclusive(self):
        self.assertIsNone(MODULE.classify_media_probe({"detailReady": False}))


class PickAudioSourceTests(unittest.TestCase):
    def test_note_audio_prefers_video_play_address(self):
        detail = {
            "video_play_urls": ["https://example.com/note-audio.m4a"],
            "music_play_urls": [],
            "music_original_urls": ["https://example.com/original.m4a"],
        }
        self.assertEqual(MODULE.pick_audio_source(detail), "https://example.com/note-audio.m4a")

    def test_music_original_is_the_last_fallback(self):
        detail = {
            "video_play_urls": [],
            "music_play_urls": [],
            "music_original_urls": ["https://example.com/original.m4a"],
        }
        self.assertEqual(MODULE.pick_audio_source(detail), "https://example.com/original.m4a")

    def test_missing_audio_is_explicit(self):
        self.assertIsNone(MODULE.pick_audio_source({"video_play_urls": [], "music_play_urls": []}))


if __name__ == "__main__":
    unittest.main()
