from ._base import _NamedAttrObject
from _typeshed import Incomplete
from arcpy.arcobjects import Result

__all__ = ['SearchNeighborhoodStandard', 'SearchNeighborhoodSmooth', 'SearchNeighborhoodStandardCircular', 'SearchNeighborhoodSmoothCircular', 'SearchNeighborhoodStandard3D', 'CrossValidationResult', 'GeostatisticalDatasets']

class SearchNeighborhoodStandard(_NamedAttrObject):
    __esri_toolinfo__: Incomplete
    majorSemiaxis: Incomplete
    minorSemiaxis: Incomplete
    angle: Incomplete
    nbrMax: Incomplete
    nbrMin: Incomplete
    sectorType: Incomplete
    def __init__(self, majorSemiaxis=None, minorSemiaxis=None, angle: float = 0.0, nbrMax: int = 15, nbrMin: int = 10, sectorType: str = 'ONE_SECTOR') -> None: ...

class SearchNeighborhoodSmooth(_NamedAttrObject):
    __esri_toolinfo__: Incomplete
    majorSemiaxis: Incomplete
    minorSemiaxis: Incomplete
    angle: Incomplete
    smoothFactor: Incomplete
    def __init__(self, majorSemiaxis=None, minorSemiaxis=None, angle: float = 0.0, smoothFactor: float = 0.2) -> None: ...

class SearchNeighborhoodStandardCircular(_NamedAttrObject):
    __esri_toolinfo__: Incomplete
    radius: Incomplete
    angle: Incomplete
    nbrMax: Incomplete
    nbrMin: Incomplete
    sectorType: Incomplete
    def __init__(self, radius=None, angle: float = 0.0, nbrMax: int = 15, nbrMin: int = 10, sectorType: str = 'ONE_SECTOR') -> None: ...

class SearchNeighborhoodSmoothCircular(_NamedAttrObject):
    __esri_toolinfo__: Incomplete
    radius: Incomplete
    smoothFactor: Incomplete
    def __init__(self, radius=None, smoothFactor: float = 0.2) -> None: ...

class SearchNeighborhoodStandard3D(_NamedAttrObject):
    __esri_toolinfo__: Incomplete
    radius: Incomplete
    nbrMax: Incomplete
    nbrMin: Incomplete
    sectorType: Incomplete
    def __init__(self, radius=None, nbrMax: int = 2, nbrMin: int = 1, sectorType: str = 'TWELVE_SECTORS') -> None: ...

class CrossValidationResult(Result):
    @property
    def count(self): ...
    @property
    def meanError(self): ...
    @property
    def rootMeanSquare(self): ...
    @property
    def averageStandard(self): ...
    @property
    def meanStandardized(self): ...
    @property
    def rootMeanSquareStandardized(self): ...
    @property
    def percentIn90Interval(self): ...
    @property
    def percentIn95Interval(self): ...
    @property
    def averageCRPS(self): ...

class GADatasets:
    def __init__(self, info) -> None: ...

def GeostatisticalDatasets(ga_model_source): ...
