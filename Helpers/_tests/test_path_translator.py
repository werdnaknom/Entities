from unittest import mock
from dataclasses import asdict

from pathlib import Path
import platform

from ..path_translator import PathTranslator


from basicTestCase.basic_test_case import BasicTestCase

class PathTranslatorTestCase(BasicTestCase):

    def _setUp(self):
        self.p ="//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/Tests/Load Profile/1/CH5.bin"

    def _linux_PathTranslator(self):
        with mock.patch("pathlib.Path.exists") as mock_exists:
            mock_exists.return_value = True
            pt = PathTranslator(path_str=self.p, system="Linux", path_name="Test")
        return pt

    def _windows_PathTranslator(self):
        with mock.patch("pathlib.Path.exists") as mock_exists:
            mock_exists.return_value = True
            pt = PathTranslator(path_str=self.p, system="Windows", path_name="Test")
        return pt

    def test_windows_init_PathTranslator(self):
        p = "//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/Tests/Load Profile/1/CH5.bin"
        pt = PathTranslator(path_str=p, path_name="Test")

        self.assertEqual(p, pt.path_str)
        self.assertIsInstance(pt.path, Path)
        self.assertEqual("Windows", pt.system)


    @mock.patch('pathlib.Path.exists')
    def test_Linux_init_PathTranslator(self, mock_exists):
        mock_exists.return_value = True
        p = "//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/Tests/Load Profile/1/CH5.bin"

        with mock.patch('platform.system') as mock_system:
            mock_system.return_value = "Linux"
            pt = PathTranslator(path_str=p, system=platform.system(), path_name="Test")

        self.logger.debug(f"{pt}")

        self.assertEqual(p, pt.path_str)
        self.assertIsInstance(pt.path, Path)
        self.assertEqual(p[1:], str(pt.path.resolve()))
        self.assertEqual("Linux", pt.system)

    def test_pt_to_windows(self):
        windows_pt = self._windows_PathTranslator()
        linux_pt = self._linux_PathTranslator()

        self.assertEqual(self.p, windows_pt.to_windows())

        self.assertEqual(self.p, linux_pt.to_windows())
        self.assertNotEqual(self.p, linux_pt.path_str)

    def test_pt_path(self):
        windows_pt = self._windows_PathTranslator()
        linux_pt = self._linux_PathTranslator()

        self.assertIsInstance(windows_pt.path, Path)
        self.assertIsInstance(linux_pt.path, Path)

    def test_to_dict(self):
        pt = PathTranslator(path_name="capture_image", path_str=r"F:\ATS DATABASE\Island Rapids\K87758-002\00\894DA0\1014\Tests\Aux To Main\10\capture.png")
        self.assertDictEqual({"capture_image":r"F:\ATS DATABASE\Island Rapids\K87758-002\00\894DA0\1014\Tests\Aux To Main\10\capture.png" },
                             pt.to_dict())
        self.assertDictEqual(asdict(pt), pt.to_dict())
