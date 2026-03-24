from arcgisscripting import na as cna
from enum import IntEnum

__all__ = ['RouteInputDataType', 'RouteOutputDataType', 'Route']

class RouteInputDataType(IntEnum):
    Stops = 0
    PointBarriers = 1
    LineBarriers = 2
    PolygonBarriers = 3

class RouteOutputDataType(IntEnum):
    Stops = 0
    Routes = 1
    RouteEdges = 2
    DirectionPoints = 3
    DirectionLines = 4
    Directions = 5
    RouteJunctions = 6
    RouteTurns = 7

class Route(cna.Route):
    def __init__(self, in_network) -> None: ...
