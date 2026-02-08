"""Sample unit tests to verify test infrastructure."""

import pytest


def test_basic_assertion():
    """Verify basic test execution works."""
    assert 1 + 1 == 2


def test_sample_fixture(sample_fixture):
    """Verify pytest fixtures work."""
    assert sample_fixture["status"] == "ok"
