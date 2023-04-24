#!/usr/bin/env python3
"""
test_utils
"""
import unittest
import utils
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """test class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """tests access nested map"""
        result = utils.access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """key check and raise error"""
        with self.assertRaises(KeyError) as C:
            utils.access_nested_map(nested_map, path)

        self.assertEqual((C.exception), "KeyError: '{}'".format(path[0]))


if __name__ == '__main__':
    unittest.main()
