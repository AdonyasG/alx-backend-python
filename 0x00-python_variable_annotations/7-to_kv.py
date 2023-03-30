#!/usr/bin/env python3
"""
Module - 7-to_kv
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes a string and an int or float and returns as tuple"""
    return (k, float(v**2))
