from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from .CIMDocument import CIMView as CIMView
from _typeshed import Incomplete

class CIMDataEngineeringFieldStatistics:
    fieldName: Incomplete
    treatFieldAs: Incomplete
    values: Incomplete
    previewChart: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDataEngineeringPreviewChart:
    minimum: Incomplete
    maximum: Incomplete
    values: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDataEngineeringStatisticColumn:
    name: Incomplete
    isFrozen: bool
    isSorted: bool
    isVisible: bool
    sortDirection: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDataEngineeringStatisticValue:
    statisticType: Incomplete
    value: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDataEngineeringView(CIMView):
    mapURI: Incomplete
    sourceFilter: Incomplete
    useFieldAliases: bool
    rowHeight: int
    zoomPercent: int
    layoutType: Incomplete
    columns: Incomplete
    fieldTypeFilter: Incomplete
    fieldTypeFilters: Incomplete
    fieldStatistics: Incomplete
    displayNumericStatistics: bool
    displayDateTimeStatistics: bool
    displayTextStatistics: bool
    def __init__(self, *args, **Kwargs) -> None: ...
