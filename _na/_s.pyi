from _typeshed import Incomplete
from enum import IntEnum

__all__ = ['TraversedElementType', 'DirectionsFieldMapping', 'CurbApproach', 'DrivingSide', 'LandmarkSide', 'ReferenceLandmarkType', 'DirectionPointType', 'DirectionPoint', 'DirectionsName', 'DirectionsCustomizer', 'TraversedJunction', 'TraversedEdge', 'TraversedElement', 'TraversedTurn', 'DirectionsQuery', 'AdjacentEdge', 'SpatialLandmark', 'ReferenceLandmark', 'NameClass']

class TraversedElementType(IntEnum):
    Unknown = (0,)
    Junction = ...
    Edge = ...
    Turn = ...
    Road = ...
    HighwayRoad = ...
    Ramp = ...
    Ferry = ...
    RoundaboutRoad = ...
    MajorRoad = ...
    Walkway = ...
    TurningArc = ...
    Stairs = ...
    Escalator = ...
    Elevator = ...
    PedestrianRamp = ...
    MovingWalkway = ...
    Hallway = ...
    Indoor = ...
    Transit = ...
    SailingLine = ...
    Stop = ...
    Waypoint = ...
    RestBreak = ...
    RoadIntersection = ...

class CurbApproach(IntEnum):
    Unknown = (-1,)
    EitherSide = (0,)
    RightSide = (1,)
    LeftSide = (2,)
    NoUTurn = 3

class DrivingSide(IntEnum):
    Unknown = (0,)
    RightSide = (1,)
    LeftSide = 2

class LandmarkSide(IntEnum):
    Unknown = -1
    Both = (0,)
    Left = (1,)
    Right = 2

class ReferenceLandmarkType(IntEnum):
    Turn = (0,)
    Confirmation = (1,)
    StopSign = (2,)
    TrafficLight = (3,)
    RailwayCrossing = 4

class NameClass(IntEnum):
    Unknown = -1
    StreetName = (0,)
    RouteNumber = 1

class DirectionPointType(IntEnum):
    Unknown = (0,)
    Header = (1,)
    ManeuverArrive = (50,)
    ManeuverDepart = (51,)
    ManeuverStraight = (52,)
    ManeuverCollectLeft = (53,)
    ManeuverCollectRight = (54,)
    ManeuverCollectBoth = (55,)
    ManeuverFerryOn = (100,)
    ManeuverFerryOff = (101,)
    ManeuverForkCentral = (102,)
    ManeuverRoundabout = (103,)
    ManeuverUTurn = (104,)
    ManeuverDoor = (150,)
    ManeuverStairs = (151,)
    ManeuverElevator = (152,)
    ManeuverEscalator = (153,)
    ManeuverPedestrianRamp = (154,)
    ManeuverForkLeft = (200,)
    ManeuverRampLeft = (201,)
    ManeuverRoundaboutLeft = (202,)
    ManeuverUTurnLeft = (203,)
    ManeuverBearLeft = (204,)
    ManeuverTurnLeft = (205,)
    ManeuverSharpLeft = (206,)
    ManeuverTurnLeftLeft = (207,)
    ManeuverTurnLeftRight = (208,)
    ManeuverForkRight = (300,)
    ManeuverRampRight = (301,)
    ManeuverRoundaboutRight = (302,)
    ManeuverUTurnRight = (303,)
    ManeuverBearRight = (304,)
    ManeuverTurnRight = (305,)
    ManeuverSharpRight = (306,)
    ManeuverTurnRightLeft = (307,)
    ManeuverTurnRightRight = (308,)
    ManeuverElevatorUp = (400,)
    ManeuverEscalatorUp = (401,)
    ManeuverStairsUp = (402,)
    ManeuverElevatorDown = (500,)
    ManeuverEscalatorDown = (501,)
    ManeuverStairsDown = (502,)
    Event = (1000,)
    EventLandmark = (1001,)
    EventTimeZone = (1002,)
    EventTraffic = (1003,)
    EventBarrier = (1004,)
    EventBoundary = (1005,)
    EventRestrictionViolation = 1006

class DirectionsFieldMapping(IntEnum):
    FullName = 0
    BaseName = 1
    PrefixType = 2
    SuffixType = 3
    HighwayDirection = 4
    PrefixDirection = 5
    SuffixDirection = 6
    Phrase = 7
    Language = 8
    NameClass = 9

DirectionPoint: Incomplete
DirectionsName: Incomplete
DirectionsCustomizer: Incomplete
TraversedElement: Incomplete
TraversedJunction: Incomplete
TraversedEdge: Incomplete
TraversedTurn: Incomplete
AdjacentEdge: Incomplete
SpatialLandmark: Incomplete
ReferenceLandmark: Incomplete
DirectionsQuery: Incomplete
