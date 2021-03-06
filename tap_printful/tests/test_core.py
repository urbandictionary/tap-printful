"""Tests standard tap features using the built-in SDK tests library."""

from singer_sdk.testing import get_standard_tap_tests
from tap_printful.tap import TapPrintful

SAMPLE_CONFIG = {}


def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(TapPrintful, config=SAMPLE_CONFIG)
    for test in tests:
        test()
