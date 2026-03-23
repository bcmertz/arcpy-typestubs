from . import CompoundParameter
from _typeshed import Incomplete

__all__ = ['NbrAnnulus', 'NbrCircle', 'NbrIrregular', 'NbrRectangle', 'NbrWedge', 'NbrWeight']

class Neighborhood(CompoundParameter._CompoundParameter):
    def __init__(self, keyword) -> None: ...

class NbrAnnulus(Neighborhood):
    __esri_toolinfo__: Incomplete
    innerRadius: Incomplete
    outerRadius: Incomplete
    units: Incomplete
    def __init__(self, innerRadius: Incomplete | None = None, outerRadius: Incomplete | None = None, units: Incomplete | None = None) -> None: ...

class NbrCircle(Neighborhood):
    __esri_toolinfo__: Incomplete
    radius: Incomplete
    units: Incomplete
    def __init__(self, radius: Incomplete | None = None, units: Incomplete | None = None) -> None: ...

class NbrIrregular(Neighborhood):
    __esri_toolinfo__: Incomplete
    inKernelFile: Incomplete
    def __init__(self, inKernelFile) -> None: ...

class NbrRectangle(Neighborhood):
    __esri_toolinfo__: Incomplete
    width: Incomplete
    height: Incomplete
    units: Incomplete
    def __init__(self, width: Incomplete | None = None, height: Incomplete | None = None, units: Incomplete | None = None) -> None: ...

class NbrWedge(Neighborhood):
    __esri_toolinfo__: Incomplete
    radius: Incomplete
    startAngle: Incomplete
    endAngle: Incomplete
    units: Incomplete
    def __init__(self, radius: Incomplete | None = None, startAngle: Incomplete | None = None, endAngle: Incomplete | None = None, units: Incomplete | None = None) -> None: ...

class NbrWeight(Neighborhood):
    __esri_toolinfo__: Incomplete
    inKernelFile: Incomplete
    def __init__(self, inKernelFile) -> None: ...
