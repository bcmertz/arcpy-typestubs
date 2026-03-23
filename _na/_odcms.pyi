from arcgisscripting import na as cna
from enum import IntEnum

__all__ = ['OriginDestinationCostMatrixInputDataType', 'OriginDestinationCostMatrixOutputDataType', 'OriginDestinationCostMatrix']

class OriginDestinationCostMatrixInputDataType(IntEnum):
    Origins: int
    Destinations: int
    PointBarriers: int
    LineBarriers: int
    PolygonBarriers: int

class OriginDestinationCostMatrixOutputDataType(IntEnum):
    Origins: int
    Destinations: int
    Lines: int

class OriginDestinationCostMatrix(cna.OriginDestinationCostMatrix):
    def __init__(self, in_network) -> None: ...
