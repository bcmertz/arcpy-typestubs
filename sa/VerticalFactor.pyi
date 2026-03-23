from . import CompoundParameter
from _typeshed import Incomplete

__all__ = ['VfBinary', 'VfLinear', 'VfInverseLinear', 'VfSymLinear', 'VfSymInverseLinear', 'VfCos', 'VfSec', 'VfCosSec', 'VfSecCos', 'VfTable', 'VfHikingTime', 'VfBidirHikingTime']

class VerticalFactor(CompoundParameter._CompoundParameter):
    def __init__(self, keyword) -> None: ...

class VfBinary(VerticalFactor):
    __esri_toolinfo__: Incomplete
    zeroFactor: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    def __init__(self, zeroFactor: Incomplete | None = None, lowCutAngle: Incomplete | None = None, highCutAngle: Incomplete | None = None) -> None: ...

class VfLinear(VerticalFactor):
    __esri_toolinfo__: Incomplete
    zeroFactor: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    slope: Incomplete
    def __init__(self, zeroFactor: Incomplete | None = None, lowCutAngle: Incomplete | None = None, highCutAngle: Incomplete | None = None, slope: Incomplete | None = None) -> None: ...

class VfInverseLinear(VerticalFactor):
    __esri_toolinfo__: Incomplete
    zeroFactor: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    slope: Incomplete
    def __init__(self, zeroFactor: Incomplete | None = None, lowCutAngle: Incomplete | None = None, highCutAngle: Incomplete | None = None, slope: Incomplete | None = None) -> None: ...

class VfSymLinear(VerticalFactor):
    __esri_toolinfo__: Incomplete
    zeroFactor: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    slope: Incomplete
    def __init__(self, zeroFactor: float = 1.0, lowCutAngle: float = -90.0, highCutAngle: float = 90.0, slope: float = 0.011111) -> None: ...

class VfSymInverseLinear(VerticalFactor):
    __esri_toolinfo__: Incomplete
    zeroFactor: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    slope: Incomplete
    def __init__(self, zeroFactor: Incomplete | None = None, lowCutAngle: Incomplete | None = None, highCutAngle: Incomplete | None = None, slope: Incomplete | None = None) -> None: ...

class VfCos(VerticalFactor):
    __esri_toolinfo__: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    cosPower: Incomplete
    def __init__(self, lowCutAngle: Incomplete | None = None, highCutAngle: Incomplete | None = None, cosPower: Incomplete | None = None) -> None: ...

class VfSec(VerticalFactor):
    __esri_toolinfo__: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    secPower: Incomplete
    def __init__(self, lowCutAngle: Incomplete | None = None, highCutAngle: Incomplete | None = None, secPower: Incomplete | None = None) -> None: ...

class VfCosSec(VerticalFactor):
    __esri_toolinfo__: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    cosPower: Incomplete
    secPower: Incomplete
    def __init__(self, lowCutAngle: Incomplete | None = None, highCutAngle: Incomplete | None = None, cosPower: Incomplete | None = None, secPower: Incomplete | None = None) -> None: ...

class VfSecCos(VerticalFactor):
    __esri_toolinfo__: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    secPower: Incomplete
    cosPower: Incomplete
    def __init__(self, lowCutAngle: Incomplete | None = None, highCutAngle: Incomplete | None = None, secPower: Incomplete | None = None, cosPower: Incomplete | None = None) -> None: ...

class VfTable(VerticalFactor):
    __esri_toolinfo__: Incomplete
    inTable: Incomplete
    def __init__(self, inTable) -> None: ...

class VfHikingTime(VerticalFactor):
    __esri_toolinfo__: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    def __init__(self, lowCutAngle: Incomplete | None = None, highCutAngle: Incomplete | None = None) -> None: ...

class VfBidirHikingTime(VerticalFactor):
    __esri_toolinfo__: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    def __init__(self, lowCutAngle: Incomplete | None = None, highCutAngle: Incomplete | None = None) -> None: ...
