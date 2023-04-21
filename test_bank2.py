import bank


def test_value_hello():
    assert bank.value("Hello, world!") == 0
    assert bank.value("HELLO") == 0
    assert bank.value("hELLO, world!") == 0
    assert bank.value("hello") == 0
    assert bank.value("   hello") == 0


def test_value_h():
    assert bank.value("Hi there") == 20
    assert bank.value("Hi") == 20
    assert bank.value("hi") == 20
    assert bank.value("hI tHeRe") == 20


def test_value_other():
    assert bank.value("Goodbye") == 100
    assert bank.value("Howdy, partner!") == 100
    assert bank.value("12345") == 100
    assert bank.value("h") == 20
    assert bank.value("H") == 20
    assert bank.value("  H") == 20
