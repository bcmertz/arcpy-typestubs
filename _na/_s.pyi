from _typeshed import Incomplete
from enum import IntEnum

__all__ = ['TraversedElementType', 'DirectionsFieldMapping', 'CurbApproach', 'DrivingSide', 'LandmarkSide', 'ReferenceLandmarkType', 'DirectionPointType', 'DirectionPoint', 'DirectionsName', 'DirectionsCustomizer', 'TraversedJunction', 'TraversedEdge', 'TraversedElement', 'TraversedTurn', 'DirectionsQuery', 'AdjacentEdge', 'SpatialLandmark', 'ReferenceLandmark', 'NameClass']

class TraversedElementType(IntEnum):
    Unknown: Incomplete
    Junction: Incomplete
    Edge: Incomplete
    Turn: Incomplete
    Road: Incomplete
    HighwayRoad: Incomplete
    Ramp: Incomplete
    Ferry: Incomplete
    RoundaboutRoad: Incomplete
    MajorRoad: Incomplete
    Walkway: Incomplete
    TurningArc: Incomplete
    Stairs: Incomplete
    Escalator: Incomplete
    Elevator: Incomplete
    PedestrianRamp: Incomplete
    MovingWalkway: Incomplete
    Hallway: Incomplete
    Indoor: Incomplete
    Transit: Incomplete
    SailingLine: Incomplete
    Stop: Incomplete
    Waypoint: Incomplete
    RestBreak: Incomplete
    RoadIntersection: Incomplete

class CurbApproach(IntEnum):
    Unknown: Incomplete
    EitherSide: Incomplete
    RightSide: Incomplete
    LeftSide: Incomplete
    NoUTurn: int

class DrivingSide(IntEnum):
    Unknown: Incomplete
    RightSide: Incomplete
    LeftSide: int

class LandmarkSide(IntEnum):
    Unknown: int
    Both: Incomplete
    Left: Incomplete
    Right: int

class ReferenceLandmarkType(IntEnum):
    Turn: Incomplete
    Confirmation: Incomplete
    StopSign: Incomplete
    TrafficLight: Incomplete
    RailwayCrossing: int

class NameClass(IntEnum):
    Unknown: int
    StreetName: Incomplete
    RouteNumber: int

class DirectionPointType(IntEnum):
    Unknown: Incomplete
    Header: Incomplete
    ManeuverArrive: Incomplete
    ManeuverDepart: Incomplete
    ManeuverStraight: Incomplete
    ManeuverFerryOn: Incomplete
    ManeuverFerryOff: Incomplete
    ManeuverForkCentral: Incomplete
    ManeuverRoundabout: Incomplete
    ManeuverUTurn: Incomplete
    ManeuverDoor: Incomplete
    ManeuverStairs: Incomplete
    ManeuverElevator: Incomplete
    ManeuverEscalator: Incomplete
    ManeuverPedestrianRamp: Incomplete
    ManeuverForkLeft: Incomplete
    ManeuverRampLeft: Incomplete
    ManeuverRoundaboutLeft: Incomplete
    ManeuverUTurnLeft: Incomplete
    ManeuverBearLeft: Incomplete
    ManeuverTurnLeft: Incomplete
    ManeuverSharpLeft: Incomplete
    ManeuverTurnLeftLeft: Incomplete
    ManeuverTurnLeftRight: Incomplete
    ManeuverForkRight: Incomplete
    ManeuverRampRight: Incomplete
    ManeuverRoundaboutRight: Incomplete
    ManeuverUTurnRight: Incomplete
    ManeuverBearRight: Incomplete
    ManeuverTurnRight: Incomplete
    ManeuverSharpRight: Incomplete
    ManeuverTurnRightLeft: Incomplete
    ManeuverTurnRightRight: Incomplete
    ManeuverElevatorUp: Incomplete
    ManeuverEscalatorUp: Incomplete
    ManeuverStairsUp: Incomplete
    ManeuverElevatorDown: Incomplete
    ManeuverEscalatorDown: Incomplete
    ManeuverStairsDown: Incomplete
    Event: Incomplete
    EventLandmark: Incomplete
    EventTimeZone: Incomplete
    EventTraffic: Incomplete
    EventBarrier: Incomplete
    EventBoundary: Incomplete
    EventRestrictionViolation: int

class DirectionsFieldMapping(IntEnum):
    FullName: int
    BaseName: int
    PrefixType: int
    SuffixType: int
    HighwayDirection: int
    PrefixDirection: int
    SuffixDirection: int
    Phrase: int
    Language: int
    NameClass: int

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
