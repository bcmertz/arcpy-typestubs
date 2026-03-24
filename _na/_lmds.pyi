from arcgisscripting import na as cna
from enum import IntEnum

__all__ = ['LastMileDeliveryInputDataType', 'LastMileDeliveryOutputDataType', 'LastMileDelivery']

class LastMileDeliveryInputDataType(IntEnum):
    Orders = 200
    Depots = 201
    Routes = 202
    OrderSpecialties = 203
    RouteSpecialties = 204
    Zones = 205
    PointBarriers = 206
    LineBarriers = 207
    PolygonBarriers = 208

class LastMileDeliveryOutputDataType(IntEnum):
    Orders = 250
    Depots = 251
    DepotVisits = 252
    Routes = 253
    DirectionPoints = 254
    DirectionLines = 255

class LastMileDelivery(cna.LastMileDelivery):
    def __init__(self, in_network) -> None: ...
