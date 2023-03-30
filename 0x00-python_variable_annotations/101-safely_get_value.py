#!/usr/bin/env python3
"""
Module - 101-safely_get_value
"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[Any, T] = None) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
