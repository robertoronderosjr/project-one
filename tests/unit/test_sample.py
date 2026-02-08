"""Sample unit tests to verify test infrastructure."""


def test_basic_assertion():
    """Verify basic test execution works."""
    assert 1 + 1 == 2


def test_example_fixture(example_fixture):
    """Verify pytest fixtures work."""
    assert example_fixture["status"] == "ok"
