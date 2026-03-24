from arcgisscripting import na as cna
from enum import IntEnum

__all__ = ['WasteCollectionInputDataType', 'WasteCollectionOutputDataType', 'StopCollectionMode', 'WasteCollection']

class WasteCollectionInputDataType(IntEnum):
    Stops = 400
    Depots = 401
    Routes = 402
    Renewals = 403
    RouteRenewals = 404
    RenewalVisits = 405
    PointBarriers = 406
    LineBarriers = 407
    PolygonBarriers = 408

class WasteCollectionOutputDataType(IntEnum):
    Stops = 450
    Depots = 451
    RenewalVisits = 452
    RouteLines = 453
    Routes = 454
    Renewals = 455
    DirectionPoints = 456
    DirectionLines = 457

class StopCollectionMode(IntEnum):
    OneSide = 1
    BothSides = 2

class WasteCollection(cna.WasteCollection):
    def __init__(self, in_network) -> None: ...
