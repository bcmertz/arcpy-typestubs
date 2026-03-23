from . import CompoundParameter
from _typeshed import Incomplete

__all__ = ['WOTable']

class WOTable(CompoundParameter._CompoundParameter):
    __esri_toolinfo__: Incomplete
    table: Incomplete
    list: Incomplete
    def __init__(self, table, sequence) -> None: ...
