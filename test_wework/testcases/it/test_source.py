import pytest

from test_wework.api.source import Source


class TestSource:
    source = Source()
    # @pytest.mark.parametrize("type", ["image", "voice", "video", "file"])
    def test_upload_tmp_source(self):
        self.source.upload_tmp_source("file")

    def test_upload_long_source(self):
        self.source.upload_long_source()

