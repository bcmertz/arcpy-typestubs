from _typeshed import Incomplete
from arcgisscripting import na as cna
from enum import IntEnum

__all__ = ['VehicleRoutingProblemInputDataType', 'VehicleRoutingProblemOutputDataType', 'VehicleRoutingProblemInputDataType2', 'VehicleRoutingProblemOutputDataType2', 'VehicleRoutingProblemSchemaVersion', 'VehicleRoutingProblem']

class VehicleRoutingProblemInputDataType(IntEnum):
    Orders: int
    Depots: int
    Routes: int
    Breaks: int
    RouteZones: int
    RouteRenewals: int
    OrderPairs: int
    PointBarriers: int
    LineBarriers: int
    PolygonBarriers: int

class VehicleRoutingProblemInputDataType2(IntEnum):
    Orders: int
    Depots: int
    Routes: int
    Breaks: int
    RouteZones: int
    RouteRenewals: int
    OrderPairs: int
    PointBarriers: int
    LineBarriers: int
    PolygonBarriers: int
    OrderSpecialties: int
    RouteSpecialties: int

class VehicleRoutingProblemOutputDataType(IntEnum):
    UnassignedStops: int
    Stops: int
    Routes: int
    Directions: int

class VehicleRoutingProblemOutputDataType2(IntEnum):
    Orders: int
    Depots: int
    DepotVisits: int
    Breaks: int
    Routes: int
    DirectionPoints: int
    DirectionLines: int

class VehicleRoutingProblemSchemaVersion(IntEnum):
    One: int
    Two: int

class VehicleRoutingProblem(cna.VehicleRoutingProblem):
    def __init__(self, in_network, version: Incomplete | None = None) -> None: ...
