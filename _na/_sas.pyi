from arcgisscripting import na as cna
from enum import IntEnum

__all__ = ['ServiceAreaInputDataType', 'ServiceAreaOutputDataType', 'ServiceAreaPolygonCutoffGeometry', 'ServiceAreaOverlapGeometry', 'ServiceAreaPolygonDetail', 'ServiceAreaOutputType', 'ServiceArea']

class ServiceAreaInputDataType(IntEnum):
    Facilities = 0
    PointBarriers = 1
    LineBarriers = 2
    PolygonBarriers = 3

class ServiceAreaOutputDataType(IntEnum):
    Facilities = 0
    Lines = 1
    Polygons = 2

class ServiceAreaPolygonCutoffGeometry(IntEnum):
    Disks = 0
    Rings = 1

class ServiceAreaOverlapGeometry(IntEnum):
    Split = 0
    Overlap = 1
    Dissolve = 2

class ServiceAreaPolygonDetail(IntEnum):
    Generalized = 0
    Standard = 1
    High = 2

class ServiceAreaOutputType(IntEnum):
    Polygons = 0
    Lines = 1
    PolygonsAndLines = 2

class ServiceArea(cna.ServiceArea):
    def __init__(self, in_network) -> None: ...
