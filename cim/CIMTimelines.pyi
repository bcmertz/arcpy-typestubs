from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from .CIMCore import CIMDefinition as CIMDefinition
from _typeshed import Incomplete

class CIMTimelineLaneDataSource:
    iD: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTimelineLaneDrawingInfo:
    viewType: Incomplete
    maxNumberOfCascadeRows: int
    timeSpanSymbolBoundary: Incomplete
    colorRamp: str
    timeSpanSymbol: str
    symbolStyleType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTimelineLayer:
    iD: Incomplete
    alias: Incomplete
    layerURI: Incomplete
    displayField: Incomplete
    categoryField: Incomplete
    visibility: bool
    drawingInfo: str
    dataSources: Incomplete
    layerType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTimelineSwimlane:
    iD: Incomplete
    alias: Incomplete
    visibility: bool
    expanded: bool
    swimlaneExpanded: bool
    layers: Incomplete
    drawingInfo: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTimeline(CIMDefinition):
    units: Incomplete
    startTime: Incomplete
    endTime: Incomplete
    showSwimlanes: bool
    showSwimlaneLabels: bool
    honorTimeSlider: bool
    expanded: bool
    swimlanes: Incomplete
    honorSelection: bool
    honorExtent: bool
    honorRange: bool
    viewType: Incomplete
    binningTimespan: Incomplete
    selectionSetURI: Incomplete
    timelineTextSymbol: str
    theme: Incomplete
    timeIndicator: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTimelineLaneMapMemberDataSource(CIMTimelineLaneDataSource):
    mapMemberURI: Incomplete
    displayField: Incomplete
    categoryField: Incomplete
    categoryValue: Incomplete
    categoryValueType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...
