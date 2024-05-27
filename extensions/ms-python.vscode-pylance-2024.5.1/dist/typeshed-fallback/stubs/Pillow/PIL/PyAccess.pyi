from _typeshed import Incomplete
from typing import Protocol

ffi: Incomplete

# Copy of PIL._imaging.PixelAccess.
# See https://github.com/python/typeshed/issues/11688.
class _PixelAccessor(Protocol):
    def __setitem__(self, xy: tuple[int, int], color, /) -> None: ...
    def __getitem__(self, xy: tuple[int, int], /): ...
    def putpixel(self, xy: tuple[int, int], color, /) -> None: ...
    def getpixel(self, xy: tuple[int, int], /): ...

class PyAccess(_PixelAccessor):
    readonly: Incomplete
    image8: Incomplete
    image32: Incomplete
    image: Incomplete
    def __init__(self, img, readonly: bool = False) -> None: ...
    def __setitem__(self, xy: tuple[int, int], color) -> None: ...
    def __getitem__(self, xy: tuple[int, int]): ...
    def putpixel(self, xy: tuple[int, int], color) -> None: ...
    def getpixel(self, xy: tuple[int, int]): ...
    def check_xy(self, xy: tuple[int, int]): ...

class _PyAccess32_2(PyAccess):
    def get_pixel(self, x, y): ...
    def set_pixel(self, x, y, color) -> None: ...

class _PyAccess32_3(PyAccess):
    def get_pixel(self, x, y): ...
    def set_pixel(self, x, y, color) -> None: ...

class _PyAccess32_4(PyAccess):
    def get_pixel(self, x, y): ...
    def set_pixel(self, x, y, color) -> None: ...

class _PyAccess8(PyAccess):
    def get_pixel(self, x, y): ...
    def set_pixel(self, x, y, color) -> None: ...

class _PyAccessI16_N(PyAccess):
    def get_pixel(self, x, y): ...
    def set_pixel(self, x, y, color) -> None: ...

class _PyAccessI16_L(PyAccess):
    def get_pixel(self, x, y): ...
    def set_pixel(self, x, y, color) -> None: ...

class _PyAccessI16_B(PyAccess):
    def get_pixel(self, x, y): ...
    def set_pixel(self, x, y, color) -> None: ...

class _PyAccessI32_N(PyAccess):
    def get_pixel(self, x, y): ...
    def set_pixel(self, x, y, color) -> None: ...

class _PyAccessI32_Swap(PyAccess):
    def reverse(self, i): ...
    def get_pixel(self, x, y): ...
    def set_pixel(self, x, y, color) -> None: ...

class _PyAccessF(PyAccess):
    def get_pixel(self, x, y): ...
    def set_pixel(self, x, y, color) -> None: ...

mode_map: Incomplete

def new(img, readonly: bool = False): ...
