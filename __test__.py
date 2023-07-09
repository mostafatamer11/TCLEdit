"""This file is for testing"""
import ctypes
__doc__ == """This file is for testing"""

lib = ctypes.WinDLL("D:\\code\\py\\CTAEdit\\shared.dll")


func = lib.macro

func.argtypes = [ctypes.c_char_p, ctypes.c_int]
func.restype = ctypes.c_char_p

print(func(1))