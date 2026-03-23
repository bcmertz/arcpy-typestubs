from arcgisscripting import na as cna
from enum import IntEnum

__all__ = ['LocationAllocationInputDataType', 'LocationAllocationOutputDataType', 'LocationAllocationProblemType', 'DecayFunctionType', 'LocationAllocation']

class LocationAllocationInputDataType(IntEnum):
    Facilities: int
    DemandPoints: int
    PointBarriers: int
    LineBarriers: int
    PolygonBarriers: int

class LocationAllocationOutputDataType(IntEnum):
    Facilities: int
    DemandPoints: int
    Lines: int

class LocationAllocationProblemType(IntEnum):
    MaximizeAttendance: int
    MaximizeCapacitatedCoverage: int
    MaximizeCoverage: int
    MaximizeMarketShare: int
    MinimizeFacilities: int
    MinimizeImpedance: int
    TargetMarketShare: int

class DecayFunctionType(IntEnum):
    Linear: int
    Power: int
    Exponential: int

class LocationAllocation(cna.LocationAllocation):
    def __init__(self, in_network) -> None: ...
