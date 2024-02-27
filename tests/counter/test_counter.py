""" import pytest """
from src.pre_built.counter import count_ocurrences


def test_counter():
    path = "data/jobs.csv"
    word = "engineer"

    result = count_ocurrences(path, word)

    assert result >= 0

    result_case_insensitive = count_ocurrences(path, word.upper())
    assert result == result_case_insensitive
