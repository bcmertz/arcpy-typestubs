from arcgisscripting import na as cna
from enum import IntEnum

__all__ = ['TimeOfDayUsage', 'ClosestFacilityInputDataType', 'ClosestFacilityOutputDataType', 'ClosestFacility']

class TimeOfDayUsage(IntEnum):
    DepartureTime: int
    ArrivalTime: int

class ClosestFacilityInputDataType(IntEnum):
    Incidents: int
    Facilities: int
    PointBarriers: int
    LineBarriers: int
    PolygonBarriers: int

class ClosestFacilityOutputDataType(IntEnum):
    Incidents: int
    Facilities: int
    Routes: int
    ClosestFacilities: int
    DirectionPoints: int
    DirectionLines: int
    Directions: int

class ClosestFacility(cna.ClosestFacility):
    def __init__(self, in_network) -> None: ...
