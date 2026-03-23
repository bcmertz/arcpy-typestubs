from arcgisscripting import na as cna
from enum import IntEnum

__all__ = ['RouteInputDataType', 'RouteOutputDataType', 'Route']

class RouteInputDataType(IntEnum):
    Stops: int
    PointBarriers: int
    LineBarriers: int
    PolygonBarriers: int

class RouteOutputDataType(IntEnum):
    Stops: int
    Routes: int
    RouteEdges: int
    DirectionPoints: int
    DirectionLines: int
    Directions: int
    RouteJunctions: int
    RouteTurns: int

class Route(cna.Route):
    def __init__(self, in_network) -> None: ...
