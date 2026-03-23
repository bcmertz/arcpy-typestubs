from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from .CIMCore import CIMDefinition as CIMDefinition
from _typeshed import Incomplete

class CIMLinkChartEntity:
    iD: Incomplete
    name: Incomplete
    layerURI: Incomplete
    labelFieldName: Incomplete
    nonSpatial: bool
    drawingInfo: str
    labelingInfo: str
    expanded: bool
    keyFieldNames: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLinkChartFieldFilter:
    field: Incomplete
    fieldType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLinkChartFilter:
    iD: Incomplete
    name: Incomplete
    description: Incomplete
    enabled: bool
    isExclusion: bool
    filterStage: Incomplete
    filterType: Incomplete
    filterScope: Incomplete
    targetIds: Incomplete
    valueSetURI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLinkChartFilterGroup:
    iD: Incomplete
    name: Incomplete
    description: Incomplete
    enabled: bool
    filters: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLinkChartLabelingInfo:
    showLabels: bool
    labelFontFamilyName: Incomplete
    labelFontStyleName: Incomplete
    labelFontType: Incomplete
    labelFontSize: int
    labelFontColor: str
    labelBackgroundColor: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLinkChartLinkDrawingInfo:
    linkColor: str
    linkWidth: int
    linkDashStyle: Incomplete
    showDirection: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLinkChartNodeDrawingInfo:
    collapseDuplicates: bool
    nodeSymbology: Incomplete
    overrideSymbol: str
    overrideOverviewSymbolColor: bool
    overviewSymbolColor: str
    showNodeFrames: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLinkChartPropertyFilter:
    dataType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLinkChartRelationship:
    iD: Incomplete
    name: Incomplete
    sourceEntityId: Incomplete
    sourceEntityBackingField: Incomplete
    targetEntityId: Incomplete
    targetEntityBackingField: Incomplete
    drawingInfo: str
    labelingInfo: str
    expanded: bool
    keyType: Incomplete
    mapMemberURI: Incomplete
    sourceEntityKeyField: Incomplete
    targetEntityKeyField: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLinkChartViewport:
    centerX: float
    centerY: float
    zoomLevel: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLinkChartBase(CIMDefinition):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLinkChart(CIMLinkChartBase):
    entities: Incomplete
    relationships: Incomplete
    layout: Incomplete
    graphMLURI: Incomplete
    expanded: bool
    locked: bool
    interactiveLayoutMode: bool
    viewport: str
    filterByMinLinks: bool
    minLinks: int
    filterGroups: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLinkChartLinkLabelingInfo(CIMLinkChartLabelingInfo):
    labelPlacement: Incomplete
    defaultLabel: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLinkChartNodeLabelingInfo(CIMLinkChartLabelingInfo):
    def __init__(self, *args, **Kwargs) -> None: ...
