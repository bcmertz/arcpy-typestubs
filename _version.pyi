from _typeshed import Incomplete
from functools import cached_property

__all__ = ['version', '__version__']

class Version:
    data: Incomplete
    def __init__(self) -> None: ...
    @cached_property
    def build(self): ...
    @cached_property
    def install_dir(self): ...
    @cached_property
    def arcobjects(self): ...
    @cached_property
    def arcgisscripting(self): ...

version: Incomplete
__version__: Incomplete
