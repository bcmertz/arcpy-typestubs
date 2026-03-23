from arcgisscripting import na as cna
from enum import IntEnum

__all__ = ['ServiceAreaInputDataType', 'ServiceAreaOutputDataType', 'ServiceAreaPolygonCutoffGeometry', 'ServiceAreaOverlapGeometry', 'ServiceAreaPolygonDetail', 'ServiceAreaOutputType', 'ServiceArea']

class ServiceAreaInputDataType(IntEnum):
    Facilities: int
    PointBarriers: int
    LineBarriers: int
    PolygonBarriers: int

class ServiceAreaOutputDataType(IntEnum):
    Facilities: int
    Lines: int
    Polygons: int

class ServiceAreaPolygonCutoffGeometry(IntEnum):
    Disks: int
    Rings: int

class ServiceAreaOverlapGeometry(IntEnum):
    Split: int
    Overlap: int
    Dissolve: int

class ServiceAreaPolygonDetail(IntEnum):
    Generalized: int
    Standard: int
    High: int

class ServiceAreaOutputType(IntEnum):
    Polygons: int
    Lines: int
    PolygonsAndLines: int

class ServiceArea(cna.ServiceArea):
    def __init__(self, in_network) -> None: ...
