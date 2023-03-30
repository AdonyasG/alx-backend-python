#!/usr/bin/env python3
"""
Module - 9-element_length
"""
from typing import Sequence, List, Iterable, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """default"""
    return [(i, len(i)) for i in lst]
