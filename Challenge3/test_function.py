import unittest
from get_value import get_value

class TestGetValue(unittest.TestCase):

    def test_nested_key_ex1(self):
        obj = {"a": {"b": {"c": "d"}}}
        key = "a/b/c"
        self.assertEqual(get_value(obj, key), "d")

    def test_nested_key_ex2(self):
        obj = {"x": {"y": {"z": "a"}}}
        key = "x/y/z" 
        self.assertEqual(get_value(obj, key), "a")

    def test_non_existent_key(self):
        obj = {"x": {"y": {"z": "a"}}}
        key = "x/y/q"
        self.assertEqual(get_value(obj, key), None)

    def test_empty_key(self):
        obj = {"x": "a"}
        key = ""
        self.assertEqual(get_value(obj, key), obj)

    def test_invalid_key(self):
        obj = {"x": "a"}
        key = "x/y/z"
        self.assertEqual(get_value(obj, key), None)

if __name__ == '__main__':
    unittest.main()
