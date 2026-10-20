
from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello there") == 0


def test_starts_with_h():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("Howdy") == 20
    assert value("Hey there") == 20


def test_other_greetings():
    assert value("good morning") == 100
    assert value("What's up?") == 100
    assert value("Goodbye") == 100


def test_hello_inside_not_at_start():
    assert value("say hello") == 100


def test_empty_string():
    assert value("") == 100
