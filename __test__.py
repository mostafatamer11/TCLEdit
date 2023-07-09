"""This file is for testing"""
import ctypes
__doc__ == """This file is for testing"""

lib = ctypes.WinDLL("shared.dll")
lib.macro(1)

"""PS D:\code\py\CTAEdit> & D:/bash/pyPy/python.exe d:/code/py/CTAEdit/__test__.py
Traceback (most recent call last):
  File "d:\code\py\CTAEdit\__test__.py", line 5, in <module>
    ctypes.CDLL(r"D:\code\py\CTAEditor\ansi.so")
  File "D:\bash\pyPy\Lib\ctypes\__init__.py", line 376, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
uctor syntax.
PS D:\code\py\CTAEdit> & D:/bash/python/python311/python.exe d:/code/py/CTAEdit/__test__.py
Traceback (most recent call last):
  File "d:\code\py\CTAEdit\__test__.py", line 5, in <module>
    ctypes.CDLL(r"D:\code\py\CTAEditor\ansi.so")
  File "D:\bash\python\python311\Lib\ctypes\__init__.py", line 376, in __init__
    self._handle = _dlopen(self._name, mode)
uctor syntax.
PS D:\code\py\CTAEdit> & D:/bash/python/python311/python.exe d:/code/py/CTAEdit/__test__.py
Traceback (most recent call last):
  File "d:\code\py\CTAEdit\__test__.py", line 5, in <module>
    ctypes.CDLL(r"D:\code\py\CTAEdit\ansi.so")
  File "D:\bash\python\python311\Lib\ctypes\__init__.py", line 376, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: [WinError 193] %1 is not a valid Win32 application
PS D:\code\py\CTAEdit> & D:/bash/python/python311/python.exe d:/code/py/CTAEdit/__test__.py
PS D:\code\py\CTAEdit> & D:/bash/python/python311/python.exe d:/code/py/CTAEdit/__test__.py
  File "d:\code\py\CTAEdit\__test__.py", line 7, in <module>
    print(lib.RESET)
          ^^^^^^^^^
  File "D:\bash\python\python311\Lib\ctypes\__init__.py", line 389, in __getattr__
    func = self.__getitem__(name)
           ^^^^^^^^^^^^^^^^^^^^^^
  File "D:\bash\python\python311\Lib\ctypes\__init__.py", line 394, in __getitem__
    func = self._FuncPtr((name_or_ordinal, self))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: the _handle attribute of the second argument must be an integer
PS D:\code\py\CTAEdit> & D:/bash/python/python311/python.exe d:/code/py/CTAEdit/__test__.py
  File "d:\code\py\CTAEdit\__test__.py", line 7, in <module>
    print(lib.RESET)
          ^^^^^^^^^
  File "D:\bash\python\python311\Lib\ctypes\__init__.py", line 389, in __getattr__
    func = self.__getitem__(name)
           ^^^^^^^^^^^^^^^^^^^^^^
  File "D:\bash\python\python311\Lib\ctypes\__init__.py", line 394, in __getitem__
    func = self._FuncPtr((name_or_ordinal, self))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: function 'RESET' not found
PS D:\code\py\CTAEdit> & D:/bash/python/python311/python.exe d:/code/py/CTAEdit/__test__.py
  File "d:\code\py\CTAEdit\__test__.py", line 7, in <module>
    print(lib.RESET)
          ^^^^^^^^^
  File "D:\bash\python\python311\Lib\ctypes\__init__.py", line 389, in __getattr__
    func = self.__getitem__(name)
           ^^^^^^^^^^^^^^^^^^^^^^
  File "D:\bash\python\python311\Lib\ctypes\__init__.py", line 394, in __getitem__
    func = self._FuncPtr((name_or_ordinal, self))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: function 'RESET' not found
PS D:\code\py\CTAEdit> & D:/bash/python/python311/python.exe d:/code/py/CTAEdit/__test__.py
  File "d:\code\py\CTAEdit\__test__.py", line 7, in <module>
    print(lib.macro(1))
          ^^^^^^^^^
  File "D:\bash\python\python311\Lib\ctypes\__init__.py", line 389, in __getattr__
    func = self.__getitem__(name)
           ^^^^^^^^^^^^^^^^^^^^^^
  File "D:\bash\python\python311\Lib\ctypes\__init__.py", line 394, in __getitem__
    func = self._FuncPtr((name_or_ordinal, self))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: function 'macro' not found
PS D:\code\py\CTAEdit> & D:/bash/python/python311/python.exe d:/code/py/CTAEdit/__test__.py
  File "d:\code\py\CTAEdit\__test__.py", line 7, in <module>
    lib.macro(1)
    ^^^^^^^^^
  File "D:\bash\python\python311\Lib\ctypes\__init__.py", line 389, in __getattr__
    func = self.__getitem__(name)
           ^^^^^^^^^^^^^^^^^^^^^^
  File "D:\bash\python\python311\Lib\ctypes\__init__.py", line 394, in __getitem__
    func = self._FuncPtr((name_or_ordinal, self))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
PS D:\code\py\CTAEdit> & D:/bash/python/python311/python.exe d:/code/py/CTAEdit/__test__.py
Traceback (most recent call last):
  File "d:\code\py\CTAEdit\__test__.py", line 5, in <module>
    lib = ctypes.CDLL(r"D:\code\py\CTAEdit\shared.dll")
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\bash\python\python311\Lib\ctypes\__init__.py", line 376, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: Could not find module 'D:\code\py\CTAEdit\shared.dll' (or one of its dependencies). Try using the full path with constPS D:\code\py\CTAEdit> & D:/bash/python/python311/python.exe d:/code/py/CTAEdit/__test__.py
Traceback (most recent call last):
  File "d:\code\py\CTAEdit\__test__.py", line 5, in <module>
    lib = ctypes.CDLL(r"D:\code\py\CTAEdit\shared.dll")
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\bash\python\python311\Lib\ctypes\__init__.py", line 376, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: Could not find module 'D:\code\py\CTAEdit\shared.dll' (or one of its dependencies). Try using the full path with constPS D:\code\py\CTAEdit> & D:/bash/python/python311/python.exe d:/code/py/CTAEdit/__test__.py
Traceback (most recent call last):
  File "d:\code\py\CTAEdit\__test__.py", line 5, in <module>
    lib = ctypes.CDLL(r"D:\code\py\CTAEdit\shared.dll")
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\bash\python\python311\Lib\ctypes\__init__.py", line 376, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: Could not find module 'D:\code\py\CTAEdit\shared.dll' (or one of its dependencies). Try using the full path with constPS D:\code\py\CTAEdit> & D:/bash/python/python311/python.exe d:/code/py/CTAEdit/__test__.py
Traceback (most recent call last):
  File "d:\code\py\CTAEdit\__test__.py", line 5, in <module>
    lib = ctypes.CDLL(r"D:\code\py\CTAEdit\shared.dll")
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\bash\python\python311\Lib\ctypes\__init__.py", line 376, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: Could not find module 'D:\code\py\CTAEdit\shared.dll' (or one of its dependencies). Try using the full path with constPS D:\code\py\CTAEdit> & D:/bash/python/python311/python.exe d:/code/py/CTAEdit/__test__.py
Traceback (most recent call last):
  File "d:\code\py\CTAEdit\__test__.py", line 5, in <module>
    lib = ctypes.CDLL(r"D:\code\py\CTAEdit\shared.dll")
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\bash\python\python311\Lib\ctypes\__init__.py", line 376, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
ructor syntax.
PS D:\code\py\CTAEdit> & D:/bash/python/python311/python.exe d:/code/py/CTAEdit/__test__.py
Traceback (most recent call last):
  File "d:\code\py\CTAEdit\__test__.py", line 7, in <module>
    lib.macro(1)
  File "D:\bash\python\python311\Lib\ctypes\__init__.py", line 446, in __getattr__
    dll = self._dlltype(name)
          ^^^^^^^^^^^^^^^^^^^
TypeError: 'str' object is not callable
PS D:\code\py\CTAEdit> & D:/bash/python/python311/python.exe d:/code/py/CTAEdit/__test__.py
  File "d:\code\py\CTAEdit\__test__.py", line 5, in <module>
    lib = ctypes.LibraryLoader.LoadLibrary(r"D:\code\py\CTAEdit\shared.dll")
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: LibraryLoader.LoadLibrary() missing 1 required positional argument: 'name'
PS D:\code\py\CTAEdit> & D:/bash/python/python311/python.exe d:/code/py/CTAEdit/__test__.py
Traceback (most recent call last):
  File "d:\code\py\CTAEdit\__test__.py", line 5, in <module>
    lib = ctypes.LibraryLoader()
          ^^^^^^^^^^^^^^^^^^^^^^
TypeError: LibraryLoader.__init__() missing 1 required positional argument: 'dlltype'
PS D:\code\py\CTAEdit> & D:/bash/python/python311/python.exe d:/code/py/CTAEdit/__test__.py
  File "d:\code\py\CTAEdit\__test__.py", line 6, in <module>
    lib.LoadLibrary(r"D:\code\py\CTAEdit\shared.dll")
  File "D:\bash\python\python311\Lib\ctypes\__init__.py", line 454, in LoadLibrary
    return self._dlltype(name)
           ^^^^^^^^^^^^^^^^^^^
  File "D:\bash\python\python311\Lib\ctypes\__init__.py", line 376, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: Could not find module 'D:\code\py\CTAEdit\shared.dll' (or one of its dependencies). Try using the full path with constructor syntax.
PS D:\code\py\CTAEdit> & D:/bash/python/python311/python.exe d:/code/py/CTAEdit/__test__.py
Traceback (most recent call last):
  File "d:\code\py\CTAEdit\__test__.py", line 6, in <module>
    lib.LoadLibrary(r"D:\\code\\py\\CTAEdit\\shared.dll")
  File "D:\bash\python\python311\Lib\ctypes\__init__.py", line 454, in LoadLibrary
    return self._dlltype(name)
           ^^^^^^^^^^^^^^^^^^^
  File "D:\bash\python\python311\Lib\ctypes\__init__.py", line 376, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: Could not find module 'D:\code\py\CTAEdit\shared.dll' (or one of its dependencies). Try using the full path with constructor syntax.
PS D:\code\py\CTAEdit> """