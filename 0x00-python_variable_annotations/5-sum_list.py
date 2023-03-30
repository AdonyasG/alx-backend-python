#!/usr/bin/env python3
"""
Module 5-sum_list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns sum of list"""
    n: float = 0.0
    for sum in input_list:
        n += sum
    return n
