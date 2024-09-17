from ims_envista.version import Version
import unittest
import pytest


class TestVersion(unittest.TestCase):
    def test_set_version(self):
        ver = Version("1.0.0")
        self.assertEqual(ver.number, "1.0.0")

    def test_version_immutable(self):
        ver = Version("1.0.0")
        with pytest.raises(TypeError):
            ver.number = "1.1.0"
