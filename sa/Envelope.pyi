import arcpy
from _typeshed import Incomplete

__all__ = ['Envelope', 'Extent', 'Rectangle']

class Extent(arcpy.Extent):
    __esri_toolinfo__: Incomplete
    def __init__(self, XMin, YMin, XMax, YMax) -> None: ...
Rectangle = Extent
Envelope = Extent
