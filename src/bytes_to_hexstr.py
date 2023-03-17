#!/usr/bin/env python3

from typing import Literal

def bytes_to_hexstr8(src: bytes) -> str:
    """ バイト列を8ビット幅16進数の文字列表現に変換する
    """
    return ''.join(r'\x{:02X}'.format(b) for b in src)

def bytes_to_hexstr16(src: bytes, byteorder: Literal['big', 'little']) -> str:
    """ バイト列を16ビット幅16進数の文字列表現に変換する
    """
    it = iter(src)
    return ''.join(r'\x{:04X}'.format(int.from_bytes([b0, b1], byteorder=byteorder)) for b0, b1 in zip(it, it))

def bytes_to_hexstr32(src: bytes, byteorder: Literal['big', 'little']) -> str:
    """ バイト列を32ビット幅16進数の文字列表現に変換する
    """
    it = iter(src)
    return ''.join(r'\x{:08X}'.format(int.from_bytes([b0, b1, b2, b3], byteorder=byteorder)) for b0, b1, b2, b3 in zip(it, it, it, it))

if __name__ == '__main__':
    pass
