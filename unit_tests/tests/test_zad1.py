from zad1 import is_palindrome


def test_is_palindrome():
    assert is_palindrome("kajak") is True
    assert is_palindrome("Kobyła ma mały bok") is True
    assert is_palindrome("python") is False
    assert is_palindrome("") is True
    assert is_palindrome("A") is True
