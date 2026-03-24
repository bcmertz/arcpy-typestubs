from arcgisscripting import na as cna
from enum import IntEnum

__all__ = ['TimeOfDayUsage', 'ClosestFacilityInputDataType', 'ClosestFacilityOutputDataType', 'ClosestFacility']

class TimeOfDayUsage(IntEnum):
    DepartureTime = 0
    ArrivalTime = 1

class ClosestFacilityInputDataType(IntEnum):
    Incidents = 0
    Facilities = 1
    PointBarriers = 2
    LineBarriers = 3
    PolygonBarriers = 4

class ClosestFacilityOutputDataType(IntEnum):
    Incidents = 0
    Facilities = 1
    Routes = 2
    ClosestFacilities = 3
    DirectionPoints = 4
    DirectionLines = 5
    Directions = 6

class ClosestFacility(cna.ClosestFacility):
    def __init__(self, in_network) -> None: ...
