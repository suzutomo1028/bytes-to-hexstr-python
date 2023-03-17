#!/usr/bin/env python3

import sys, os
import unittest

sys.path.append(os.pardir)
import src.bytes_to_hexstr as test_module

class Test_bytes_to_hexstr(unittest.TestCase):

    def test_bytes_to_hexstr8(self) -> None:

        result = test_module.bytes_to_hexstr8(b'')
        self.assertEqual(result, '')

        result = test_module.bytes_to_hexstr8(b'0123')
        self.assertEqual(result, '\\x30\\x31\\x32\\x33')
        
        result = test_module.bytes_to_hexstr8(b'01234')
        self.assertEqual(result, '\\x30\\x31\\x32\\x33\\x34')

    def test_bytes_to_hexstr16(self) -> None:

        result = test_module.bytes_to_hexstr16(b'', byteorder='big')
        self.assertEqual(result, '')
        
        result = test_module.bytes_to_hexstr16(b'0123', byteorder='big')
        self.assertEqual(result, '\\x3031\\x3233')

        result = test_module.bytes_to_hexstr16(b'01234', byteorder='big')
        self.assertEqual(result, '\\x3031\\x3233')

        result = test_module.bytes_to_hexstr16(b'01234', byteorder='little')
        self.assertEqual(result, '\\x3130\\x3332')

        with self.assertRaises(ValueError):
            result = test_module.bytes_to_hexstr16(b'01234', byteorder='hoge')

    def test_bytes_to_hexstr32(self) -> None:

        result = test_module.bytes_to_hexstr32(b'', byteorder='big')
        self.assertEqual(result, '')

        result = test_module.bytes_to_hexstr32(b'01234567', byteorder='big')
        self.assertEqual(result, '\\x30313233\\x34353637')

        result = test_module.bytes_to_hexstr32(b'012345678', byteorder='big')
        self.assertEqual(result, '\\x30313233\\x34353637')

        result = test_module.bytes_to_hexstr32(b'012345678', byteorder='little')
        self.assertEqual(result, '\\x33323130\\x37363534')

        with self.assertRaises(ValueError):
            result = test_module.bytes_to_hexstr32(b'012345678', byteorder='hoge')

if __name__ == '__main__':
    unittest.main(verbosity=2)
