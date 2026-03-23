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
    def __init__(self, semivariogramType: Incomplete | None = None, lagSize: Incomplete | None = None, majorRange: Incomplete | None = None, partialSill: Incomplete | None = None, nugget: Incomplete | None = None) -> None: ...

class KrigingModelUniversal(KrigingModel):
    __esri_toolinfo__: Incomplete
    semivariogramType: Incomplete
    lagSize: Incomplete
    majorRange: Incomplete
    partialSill: Incomplete
    nugget: Incomplete
    def __init__(self, semivariogramType: Incomplete | None = None, lagSize: Incomplete | None = None, majorRange: Incomplete | None = None, partialSill: Incomplete | None = None, nugget: Incomplete | None = None) -> None: ...
