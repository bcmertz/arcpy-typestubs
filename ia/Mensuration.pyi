import arcgisscripting
from typing import NamedTuple

class Mensuration(arcgisscripting.Mensuration):
    base_to_top: int
    base_to_shadow: int
    top_to_shadow: int
    class PointMeasurement(NamedTuple):
        lon: float
        lat: float
        elev: float
        sensor_name: str
    class LinearMeasurement(NamedTuple):
        distance: float
        azimuth: float
        sensor_name: str
    class AreaMeasurement(NamedTuple):
        area: float
        perimeter: float
        sensor_name: str
    class HeightMeasurement(NamedTuple):
        height: float
        sensor_name: str
    def __init__(self, in_raster) -> None: ...
    def __new__(cls, in_raster): ...
    def point(self, point): ...
    def distance(self, from_point, to_point): ...
    def area(self, polygon): ...
    def height(self, base_point, top_point, height_type): ...
