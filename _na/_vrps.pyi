from arcgisscripting import na as cna
from enum import IntEnum

__all__ = ['VehicleRoutingProblemInputDataType', 'VehicleRoutingProblemOutputDataType', 'VehicleRoutingProblemInputDataType2', 'VehicleRoutingProblemOutputDataType2', 'VehicleRoutingProblemSchemaVersion', 'VehicleRoutingProblem']

class VehicleRoutingProblemInputDataType(IntEnum):
    Orders = 0
    Depots = 1
    Routes = 2
    Breaks = 3
    RouteZones = 4
    RouteRenewals = 5
    OrderPairs = 6
    PointBarriers = 7
    LineBarriers = 8
    PolygonBarriers = 9

class VehicleRoutingProblemInputDataType2(IntEnum):
    Orders = 100
    Depots = 101
    Routes = 102
    Breaks = 103
    RouteZones = 104
    RouteRenewals = 105
    OrderPairs = 106
    PointBarriers = 107
    LineBarriers = 108
    PolygonBarriers = 109
    OrderSpecialties = 110
    RouteSpecialties = 111

class VehicleRoutingProblemOutputDataType(IntEnum):
    UnassignedStops = 0
    Stops = 1
    Routes = 2
    Directions = 3

class VehicleRoutingProblemOutputDataType2(IntEnum):
    Orders = 100
    Depots = 101
    DepotVisits = 102
    Breaks = 103
    Routes = 104
    DirectionPoints = 105
    DirectionLines = 106

class VehicleRoutingProblemSchemaVersion(IntEnum):
    One = 1
    Two = 2

class VehicleRoutingProblem(cna.VehicleRoutingProblem):
    def __init__(self, in_network, version=None) -> None: ...
