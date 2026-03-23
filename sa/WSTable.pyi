from . import CompoundParameter
from _typeshed import Incomplete

__all__ = ['WSTable']

class WSTable(CompoundParameter._CompoundParameter):
    __esri_toolinfo__: Incomplete
    table: Incomplete
    def __init__(self, table) -> None: ...
