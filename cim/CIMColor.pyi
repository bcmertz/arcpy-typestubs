from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from _typeshed import Incomplete

class CIMColor:
    colorSpace: str
    values: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMColorRamp:
    colorSpace: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMColorSpace:
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMCMYKColor(CIMColor):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMContinuousColorRamp(CIMColorRamp):
    fromColor: str
    toColor: str
    primitiveName: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFixedColorRamp(CIMColorRamp):
    colors: Incomplete
    arrangement: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGrayColor(CIMColor):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMHSLColor(CIMColor):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMHSVColor(CIMColor):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMICCColorSpace(CIMColorSpace):
    url: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLABColor(CIMColor):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLinearContinuousColorRamp(CIMContinuousColorRamp):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMultipartColorRamp(CIMColorRamp):
    colorRamps: Incomplete
    weights: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPolarContinuousColorRamp(CIMContinuousColorRamp):
    interpolationSpace: Incomplete
    polarDirection: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRGBColor(CIMColor):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRandomHSVColorRamp(CIMColorRamp):
    minH: int
    maxH: int
    minS: int
    maxS: int
    minV: int
    maxV: int
    minAlpha: int
    maxAlpha: int
    seed: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSpotColor(CIMColor):
    name: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSpotColorSpace(CIMColorSpace):
    description: Incomplete
    name: Incomplete
    alternativeColor: str
    bookColor: str
    bookID: Incomplete
    isReferencedColor: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMXYZColor(CIMColor):
    def __init__(self, *args, **Kwargs) -> None: ...
