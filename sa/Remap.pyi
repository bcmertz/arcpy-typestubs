from . import CompoundParameter
from _typeshed import Incomplete

__all__ = ['RemapRange', 'RemapValue']

class Remap(CompoundParameter._CompoundParameter):
    table: Incomplete
    def __init__(self, minNrValuesPerRecord, maxNrValuesPerRecord, table) -> None: ...

class RemapRange(Remap):
    __esri_toolinfo__: Incomplete
    def __init__(self, table) -> None: ...

class RemapValue(Remap):
    __esri_toolinfo__: Incomplete
    def __init__(self, table) -> None: ...
