import pytest
from mediaflow_proxy.utils.http_utils import Streamer


class TestFormatBytes:
    """Tests for Streamer.format_bytes method."""

    @pytest.mark.parametrize(
        "size, expected",
        [
            (0, "0.00 B"),
            (1, "1.00 B"),
            (500, "500.00 B"),
            (1024, "1024.00 B"),
            (1025, "1.00 KB"),
            (1500, "1.46 KB"),
            (1024 * 1024, "1024.00 KB"),
            (1024 * 1024 + 1, "1.00 MB"),
            (5 * 1024 * 1024, "5.00 MB"),
            (1024**3 + 1, "1.00 GB"),
            (int(2.5 * 1024**3), "2.50 GB"),
            (1024**4 + 1, "1.00 TB"),
            (10 * 1024**4, "10.00 TB"),
            (10.5, "10.50 B"),
            (1500.5, "1.47 KB"),
        ],
    )
    def test_format_bytes_various_sizes(self, size, expected):
        assert Streamer.format_bytes(size) == expected
