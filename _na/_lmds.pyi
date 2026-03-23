from arcgisscripting import na as cna
from enum import IntEnum

__all__ = ['LastMileDeliveryInputDataType', 'LastMileDeliveryOutputDataType', 'LastMileDelivery']

class LastMileDeliveryInputDataType(IntEnum):
    Orders: int
    Depots: int
    Routes: int
    OrderSpecialties: int
    RouteSpecialties: int
    Zones: int
    PointBarriers: int
    LineBarriers: int
    PolygonBarriers: int

class LastMileDeliveryOutputDataType(IntEnum):
    Orders: int
    Depots: int
    DepotVisits: int
    Routes: int
    DirectionPoints: int
    DirectionLines: int

class LastMileDelivery(cna.LastMileDelivery):
    def __init__(self, in_network) -> None: ...
