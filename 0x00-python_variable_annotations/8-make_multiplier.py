#!/usr/bin/env python3
"""
Module 8-make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float multiplier as argument and
    eturns a function that multiplies a float by multiplier"""
    def multiplier_func(num: float) -> float:
        """multiplier function"""
        return num * multiplier
    return multiplier_func
