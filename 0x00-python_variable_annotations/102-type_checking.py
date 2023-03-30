#!/usr/bin/env python3
"""
Module - 102-type_checking
"""
from typing import Tuple, List, Sequence


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Default"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

tuple_array = tuple(array)

zoom_2x = zoom_array(tuple_array)

zoom_3x = zoom_array(tuple_array, 3)
