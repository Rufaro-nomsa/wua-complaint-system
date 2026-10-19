import pytest
from calculate_tax import calculate_tax


def test_normal_amount():
    assert calculate_tax(100) == 15.0


def test_zero_amount():
    assert calculate_tax(0) == 0.0


def test_large_amount():
    assert calculate_tax(1000000) == 150000.0


def test_negative_amount():
    with pytest.raises(ValueError):
        calculate_tax(-50)