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
    def __init__(self, zeroFactor=None, lowCutAngle=None, highCutAngle=None) -> None: ...

class VfLinear(VerticalFactor):
    __esri_toolinfo__: Incomplete
    zeroFactor: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    slope: Incomplete
    def __init__(self, zeroFactor=None, lowCutAngle=None, highCutAngle=None, slope=None) -> None: ...

class VfInverseLinear(VerticalFactor):
    __esri_toolinfo__: Incomplete
    zeroFactor: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    slope: Incomplete
    def __init__(self, zeroFactor=None, lowCutAngle=None, highCutAngle=None, slope=None) -> None: ...

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
    def __init__(self, zeroFactor=None, lowCutAngle=None, highCutAngle=None, slope=None) -> None: ...

class VfCos(VerticalFactor):
    __esri_toolinfo__: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    cosPower: Incomplete
    def __init__(self, lowCutAngle=None, highCutAngle=None, cosPower=None) -> None: ...

class VfSec(VerticalFactor):
    __esri_toolinfo__: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    secPower: Incomplete
    def __init__(self, lowCutAngle=None, highCutAngle=None, secPower=None) -> None: ...

class VfCosSec(VerticalFactor):
    __esri_toolinfo__: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    cosPower: Incomplete
    secPower: Incomplete
    def __init__(self, lowCutAngle=None, highCutAngle=None, cosPower=None, secPower=None) -> None: ...

class VfSecCos(VerticalFactor):
    __esri_toolinfo__: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    secPower: Incomplete
    cosPower: Incomplete
    def __init__(self, lowCutAngle=None, highCutAngle=None, secPower=None, cosPower=None) -> None: ...

class VfTable(VerticalFactor):
    __esri_toolinfo__: Incomplete
    inTable: Incomplete
    def __init__(self, inTable) -> None: ...

class VfHikingTime(VerticalFactor):
    __esri_toolinfo__: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    def __init__(self, lowCutAngle=None, highCutAngle=None) -> None: ...

class VfBidirHikingTime(VerticalFactor):
    __esri_toolinfo__: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    def __init__(self, lowCutAngle=None, highCutAngle=None) -> None: ...
