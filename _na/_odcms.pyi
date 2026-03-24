from arcgisscripting import na as cna
from enum import IntEnum

__all__ = ['OriginDestinationCostMatrixInputDataType', 'OriginDestinationCostMatrixOutputDataType', 'OriginDestinationCostMatrix']

class OriginDestinationCostMatrixInputDataType(IntEnum):
    Origins = 0
    Destinations = 1
    PointBarriers = 2
    LineBarriers = 3
    PolygonBarriers = 4

class OriginDestinationCostMatrixOutputDataType(IntEnum):
    Origins = 0
    Destinations = 1
    Lines = 2

class OriginDestinationCostMatrix(cna.OriginDestinationCostMatrix):
    def __init__(self, in_network) -> None: ...
