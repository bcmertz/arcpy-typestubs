from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from .CIMCore import CIMDefinition as CIMDefinition
from _typeshed import Incomplete

class CIMTimelineLayer:
    iD: Incomplete
    alias: Incomplete
    layerURI: Incomplete
    displayField: Incomplete
    categoryField: Incomplete
    visibility: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTimelineSwimlane:
    iD: Incomplete
    alias: Incomplete
    visibility: bool
    expanded: bool
    swimlaneExpanded: bool
    layers: Incomplete
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
    def __init__(self, *args, **Kwargs) -> None: ...
