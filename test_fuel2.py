import pytest
import fuel


def test_convert():
    assert fuel.convert("0/100") == 0
    assert fuel.convert("1/100") == 1
    assert fuel.convert("50/100") == 50
    assert fuel.convert("99/100") == 99
    assert fuel.convert("100/100") == 100

    with pytest.raises(ValueError):
        fuel.convert("50.5/100")
    with pytest.raises(ValueError):
        fuel.convert("100/50")
    with pytest.raises(ValueError):
        fuel.convert("50/1000")
    with pytest.raises(ZeroDivisionError):
        fuel.convert("50/0")


def test_gauge():
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(98) == "98%"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(100) == "F"
