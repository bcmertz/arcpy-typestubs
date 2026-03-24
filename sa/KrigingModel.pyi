from . import CompoundParameter
from _typeshed import Incomplete

__all__ = ['KrigingModelOrdinary', 'KrigingModelUniversal']

class KrigingModel(CompoundParameter._CompoundParameter):
    def __init__(self) -> None: ...

class KrigingModelOrdinary(KrigingModel):
    __esri_toolinfo__: Incomplete
    semivariogramType: Incomplete
    lagSize: Incomplete
    majorRange: Incomplete
    partialSill: Incomplete
    nugget: Incomplete
    def __init__(self, semivariogramType=None, lagSize=None, majorRange=None, partialSill=None, nugget=None) -> None: ...

class KrigingModelUniversal(KrigingModel):
    __esri_toolinfo__: Incomplete
    semivariogramType: Incomplete
    lagSize: Incomplete
    majorRange: Incomplete
    partialSill: Incomplete
    nugget: Incomplete
    def __init__(self, semivariogramType=None, lagSize=None, majorRange=None, partialSill=None, nugget=None) -> None: ...
