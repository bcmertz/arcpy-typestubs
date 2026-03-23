from _typeshed import Incomplete
from arcgisscripting import na as cna
from enum import IntEnum

__all__ = ['SnapToRoads', 'SnapToRoadsResult', 'SnapToRoadsInputDataType', 'SnapToRoadsOutputDataType']

class SnapToRoadsInputDataType(IntEnum):
    Points: int

class SnapToRoadsOutputDataType(IntEnum):
    SnappedPoints: int
    Lines: int

SnapToRoadsResult: Incomplete

class SnapToRoads(cna.SnapToRoads):
    def __init__(self, in_network) -> None: ...
