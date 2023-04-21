from itertools import count

0
def test_count():
    assert count("hello, um, world") == 1
    assert count("yummy") == 0
    assert count("Um, um, um") == 3
    assert count("") == 0
    assert count("Umbrella") == 0
    assert count("Umberto") == 0
    assert count("This is a test of the um function.") == 1
