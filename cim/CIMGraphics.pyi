from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from _typeshed import Incomplete

class CIMGraphic:
    symbol: str
    transparency: float
    blendingMode: Incomplete
    masks: Incomplete
    referenceScale: float
    attributes: Incomplete
    placement: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGraphicFrame:
    backgroundSymbol: str
    borderSymbol: str
    shadowSymbol: str
    backgroundGapX: int
    backgroundGapY: int
    backgroundCornerRounding: int
    borderGapX: int
    borderGapY: int
    borderCornerRounding: int
    shadowOffsetX: int
    shadowOffsetY: int
    shadowCornerRounding: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLeader:
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMInkGraphic(CIMGraphic):
    bounds: Incomplete
    inkData: Incomplete
    roughSketch: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLeaderLine(CIMLeader):
    line: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLeaderPoint(CIMLeader):
    point: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPictureGraphic(CIMGraphic):
    pictureURL: Incomplete
    box: Incomplete
    frame: str
    sourceURL: Incomplete
    referenceURI: Incomplete
    shape: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMShapeGraphic(CIMGraphic):
    name: Incomplete
    popupHtmlText: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTextGraphicBase(CIMGraphic):
    text: Incomplete
    shape: Incomplete
    leaders: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLineGraphic(CIMShapeGraphic):
    line: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMultiPatchGraphic(CIMShapeGraphic):
    multiPatch: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMultipointGraphic(CIMShapeGraphic):
    multipoint: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMParagraphTextGraphic(CIMTextGraphicBase):
    frame: str
    columnCount: int
    columnGap: float
    margin: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPointGraphic(CIMShapeGraphic):
    location: Incomplete
    leaders: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPolygonGraphic(CIMShapeGraphic):
    polygon: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTextGraphic(CIMTextGraphicBase):
    def __init__(self, *args, **Kwargs) -> None: ...
