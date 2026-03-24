from . import CompoundParameter
from _typeshed import Incomplete

__all__ = ['HfBinary', 'HfForward', 'HfLinear', 'HfInverseLinear', 'HfTable']

class HorizontalFactor(CompoundParameter._CompoundParameter):
    def __init__(self, keyword) -> None: ...

class HfBinary(HorizontalFactor):
    __esri_toolinfo__: Incomplete
    zeroFactor: Incomplete
    cutAngle: Incomplete
    def __init__(self, zeroFactor=None, cutAngle=None) -> None: ...

class HfForward(HorizontalFactor):
    __esri_toolinfo__: Incomplete
    zeroFactor: Incomplete
    sideValue: Incomplete
    def __init__(self, zeroFactor=None, sideValue=None) -> None: ...

class HfLinear(HorizontalFactor):
    __esri_toolinfo__: Incomplete
    zeroFactor: Incomplete
    cutAngle: Incomplete
    slope: Incomplete
    def __init__(self, zeroFactor=None, cutAngle=None, slope=None) -> None: ...

class HfInverseLinear(HorizontalFactor):
    __esri_toolinfo__: Incomplete
    zeroFactor: Incomplete
    cutAngle: Incomplete
    slope: Incomplete
    def __init__(self, zeroFactor=None, cutAngle=None, slope=None) -> None: ...

class HfTable(HorizontalFactor):
    __esri_toolinfo__: Incomplete
    inTable: Incomplete
    def __init__(self, inTable) -> None: ...
