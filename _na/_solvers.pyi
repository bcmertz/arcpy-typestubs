from _typeshed import Incomplete
from enum import IntEnum

__all__ = ['MessageSeverity', 'TimeZoneUsage', 'TravelDirection', 'TimeUnits', 'DistanceUnits', 'DirectionsStyle', 'RouteShapeType', 'LimitError', 'LineShapeType', 'Importance', 'DirectionsError', 'VrpResultError', 'InputDataError']

LimitError: Incomplete
DirectionsError: Incomplete
VrpResultError: Incomplete
InputDataError: Incomplete

class MessageSeverity(IntEnum):
    All: int
    Warning: int
    Error: int
    Info: int

class TimeZoneUsage(IntEnum):
    LocalTimeAtLocations: int
    UTC: int

class TravelDirection(IntEnum):
    FromFacility: int
    ToFacility: int

class TimeUnits(IntEnum):
    Seconds: int
    Minutes: int
    Hours: int
    Days: int

class DistanceUnits(IntEnum):
    Feet: int
    Yards: int
    Miles: int
    NauticalMiles: int
    Meters: int
    Kilometers: int

class DirectionsStyle(IntEnum):
    Navigation: int
    Campus: int
    Desktop: int

class RouteShapeType(IntEnum):
    NoLine: int
    StraightLine: int
    TrueShape: int
    TrueShapeWithMeasures: int

class LineShapeType(IntEnum):
    NoLine: int
    StraightLine: int

class Importance(IntEnum):
    Low: int
    Medium: int
    High: int
