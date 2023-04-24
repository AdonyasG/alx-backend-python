#!/usr/bin/env python3
"""
test_utils
"""
import unittest
from unittest.mock import Mock, patch
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
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """key check and raise error"""
        with self.assertRaises(expected):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """test class"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """mock http"""
       # val = {'json.return_value': test_payload}
        with patch('requests.get') as mock_get:
            mock_get.return_value = Mock()
            mock_get.return_value.json.return_value = test_payload

            result = utils.get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
