
from plates import is_valid


def test_valid_plates():
    assert is_valid("CS50")
    assert is_valid("AAA222")
    assert is_valid("AB")
    assert is_valid("CS05")


def test_length():
    assert not is_valid("A")
    assert not is_valid("ABCDEFG")
    assert is_valid("AB")


def test_first_two_characters():
    assert not is_valid("1ABC")
    assert not is_valid("A1")
    assert not is_valid("ABC123")


def test_numbers_at_end():
    assert not is_valid("CS50P")
    assert not is_valid("PI3.14")
    assert not is_valid("AB12CD")


def test_first_number_not_zero():
    assert not is_valid("CS05")
    assert not is_valid("AB012")
    assert is_valid("CS50")
    assert is_valid("AA20")


def test_punctuation_and_spaces():
    assert not is_valid("PI 3")
    assert not is_valid("AB-12")
    assert not is_valid("AB.12")
    assert not is_valid("AB,12")
