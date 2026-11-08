import pytest
from zad4 import calculate_discount


def test_calculate_discount():
    assert calculate_discount(100.0, 0.2) == 80.0
    assert calculate_discount(50.0, 0.0) == 50.0
    assert calculate_discount(200.0, 1.0) == 0.0

    with pytest.raises(ValueError):
        calculate_discount(100.0, -0.1)

    with pytest.raises(ValueError):
        calculate_discount(100.0, 1.5)
