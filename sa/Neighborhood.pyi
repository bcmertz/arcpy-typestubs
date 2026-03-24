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
    def __init__(self, innerRadius=None, outerRadius=None, units=None) -> None: ...

class NbrCircle(Neighborhood):
    __esri_toolinfo__: Incomplete
    radius: Incomplete
    units: Incomplete
    def __init__(self, radius=None, units=None) -> None: ...

class NbrIrregular(Neighborhood):
    __esri_toolinfo__: Incomplete
    inKernelFile: Incomplete
    def __init__(self, inKernelFile) -> None: ...

class NbrRectangle(Neighborhood):
    __esri_toolinfo__: Incomplete
    width: Incomplete
    height: Incomplete
    units: Incomplete
    def __init__(self, width=None, height=None, units=None) -> None: ...

class NbrWedge(Neighborhood):
    __esri_toolinfo__: Incomplete
    radius: Incomplete
    startAngle: Incomplete
    endAngle: Incomplete
    units: Incomplete
    def __init__(self, radius=None, startAngle=None, endAngle=None, units=None) -> None: ...

class NbrWeight(Neighborhood):
    __esri_toolinfo__: Incomplete
    inKernelFile: Incomplete
    def __init__(self, inKernelFile) -> None: ...
