from . import CompoundParameter
from _typeshed import Incomplete

__all__ = ['HfBinary', 'HfForward', 'HfLinear', 'HfInverseLinear', 'HfTable']

class HorizontalFactor(CompoundParameter._CompoundParameter):
    def __init__(self, keyword) -> None: ...

class HfBinary(HorizontalFactor):
    __esri_toolinfo__: Incomplete
    zeroFactor: Incomplete
    cutAngle: Incomplete
    def __init__(self, zeroFactor: Incomplete | None = None, cutAngle: Incomplete | None = None) -> None: ...

class HfForward(HorizontalFactor):
    __esri_toolinfo__: Incomplete
    zeroFactor: Incomplete
    sideValue: Incomplete
    def __init__(self, zeroFactor: Incomplete | None = None, sideValue: Incomplete | None = None) -> None: ...

class HfLinear(HorizontalFactor):
    __esri_toolinfo__: Incomplete
    zeroFactor: Incomplete
    cutAngle: Incomplete
    slope: Incomplete
    def __init__(self, zeroFactor: Incomplete | None = None, cutAngle: Incomplete | None = None, slope: Incomplete | None = None) -> None: ...

class HfInverseLinear(HorizontalFactor):
    __esri_toolinfo__: Incomplete
    zeroFactor: Incomplete
    cutAngle: Incomplete
    slope: Incomplete
    def __init__(self, zeroFactor: Incomplete | None = None, cutAngle: Incomplete | None = None, slope: Incomplete | None = None) -> None: ...

class HfTable(HorizontalFactor):
    __esri_toolinfo__: Incomplete
    inTable: Incomplete
    def __init__(self, inTable) -> None: ...
