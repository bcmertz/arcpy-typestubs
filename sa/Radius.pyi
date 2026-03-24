from . import CompoundParameter
from _typeshed import Incomplete

__all__ = ['RadiusVariable', 'RadiusFixed']

class Radius(CompoundParameter._CompoundParameter):
    def __init__(self, keyword) -> None: ...

class RadiusVariable(Radius):
    __esri_toolinfo__: Incomplete
    numberOfPoints: Incomplete
    maxDistance: Incomplete
    def __init__(self, numberOfPoints=None, maxDistance=None) -> None: ...

class RadiusFixed(Radius):
    __esri_toolinfo__: Incomplete
    distance: Incomplete
    minNumberOfPoints: Incomplete
    def __init__(self, distance=None, minNumberOfPoints=None) -> None: ...
