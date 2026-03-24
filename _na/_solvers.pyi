from _typeshed import Incomplete
from enum import IntEnum

__all__ = ['MessageSeverity', 'TimeZoneUsage', 'TravelDirection', 'TimeUnits', 'DistanceUnits', 'DirectionsStyle', 'RouteShapeType', 'LimitError', 'LineShapeType', 'Importance', 'DirectionsError', 'VrpResultError', 'InputDataError']

LimitError: Incomplete
DirectionsError: Incomplete
VrpResultError: Incomplete
InputDataError: Incomplete

class MessageSeverity(IntEnum):
    All = 0
    Warning = 1
    Error = 2
    Info = 3

class TimeZoneUsage(IntEnum):
    LocalTimeAtLocations = 0
    UTC = 1

class TravelDirection(IntEnum):
    FromFacility = 0
    ToFacility = 1

class TimeUnits(IntEnum):
    Seconds = 20
    Minutes = 21
    Hours = 22
    Days = 23

class DistanceUnits(IntEnum):
    Feet = 3
    Yards = 4
    Miles = 5
    NauticalMiles = 6
    Meters = 9
    Kilometers = 10
    Inches = 11
    Centimeters = 12
    Millimeters = 13
    Decimeters = 14

class DirectionsStyle(IntEnum):
    Navigation = 0
    Campus = 1
    Desktop = 2

class RouteShapeType(IntEnum):
    NoLine = 0
    StraightLine = 1
    TrueShape = 2
    TrueShapeWithMeasures = 3

class LineShapeType(IntEnum):
    NoLine = 0
    StraightLine = 1

class Importance(IntEnum):
    Low = 0
    Medium = 1
    High = 2
