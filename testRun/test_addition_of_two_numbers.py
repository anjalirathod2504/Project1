import pytest
from testCases import addition_of_two_numbers


def test_add_two_numbers():
    a = 10
    b = 20
    output = addition_of_two_numbers.add(a, b)
    assert output != 27
    print("assert ok")



