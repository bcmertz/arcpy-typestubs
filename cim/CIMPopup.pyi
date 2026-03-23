from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from _typeshed import Incomplete

class CIMMediaInfo:
    row: int
    column: int
    refreshRate: float
    refreshRateUnit: Incomplete
    rowSpan: int
    columnSpan: int
    isCarousel: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPopupFieldDescription:
    alias: Incomplete
    fieldName: Incomplete
    numberFormat: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPopupInfo:
    title: Incomplete
    expressionInfos: Incomplete
    mediaInfos: Incomplete
    relatedRecordSortOrder: Incomplete
    gridLayout: str
    fieldDescriptions: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPopupLayout:
    columnWidths: Incomplete
    borderWidth: int
    borderColor: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMAttachmentsMediaInfo(CIMMediaInfo):
    caption: Incomplete
    title: Incomplete
    contentType: Incomplete
    displayType: Incomplete
    sortField: Incomplete
    sortOrder: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMCarouselMediaInfo(CIMMediaInfo):
    caption: Incomplete
    title: Incomplete
    mediaInfos: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartMediaInfo(CIMMediaInfo):
    fields: Incomplete
    normalizeField: Incomplete
    caption: Incomplete
    title: Incomplete
    maximumAxisValue: float
    colorRamp: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMColumnChartMediaInfo(CIMChartMediaInfo):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMExpressionMediaInfo(CIMMediaInfo):
    expression: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMImageMediaInfo(CIMMediaInfo):
    sourceURL: Incomplete
    linkURL: Incomplete
    caption: Incomplete
    title: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLineChartMediaInfo(CIMChartMediaInfo):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPieChartMediaInfo(CIMChartMediaInfo):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRelationshipMediaInfo(CIMMediaInfo):
    caption: Incomplete
    title: Incomplete
    displayCount: int
    relationshipName: Incomplete
    relatedRecordSortOrder: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTableMediaInfo(CIMMediaInfo):
    fields: Incomplete
    useLayerFields: bool
    caption: Incomplete
    title: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTextMediaInfo(CIMMediaInfo):
    text: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBarChartMediaInfo(CIMChartMediaInfo):
    def __init__(self, *args, **Kwargs) -> None: ...
