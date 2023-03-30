#!/usr/bin/env python3
"""
Module - 6-sum_mixed_list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns sum of mixed list"""
    n: float = 0
    for i in mxd_lst:
        n += i
    return n
