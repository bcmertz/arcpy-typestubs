from arcgisscripting import na as cna
from enum import IntEnum

__all__ = ['LocationAllocationInputDataType', 'LocationAllocationOutputDataType', 'LocationAllocationProblemType', 'DecayFunctionType', 'LocationAllocation']

class LocationAllocationInputDataType(IntEnum):
    Facilities = 0
    DemandPoints = 1
    PointBarriers = 2
    LineBarriers = 3
    PolygonBarriers = 4

class LocationAllocationOutputDataType(IntEnum):
    Facilities = 0
    DemandPoints = 1
    Lines = 2

class LocationAllocationProblemType(IntEnum):
    MaximizeAttendance = 0
    MaximizeCapacitatedCoverage = 1
    MaximizeCoverage = 2
    MaximizeMarketShare = 3
    MinimizeFacilities = 4
    MinimizeImpedance = 5
    TargetMarketShare = 6

class DecayFunctionType(IntEnum):
    Linear = 0
    Power = 1
    Exponential = 2

class LocationAllocation(cna.LocationAllocation):
    def __init__(self, in_network) -> None: ...
