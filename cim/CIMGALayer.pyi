from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from .CIMLayer import CIMBaseLayer as CIMBaseLayer
from .CIMSymbolizers import CIMClassBreaksRendererBase as CIMClassBreaksRendererBase
from .CIMVectorLayers import CIMDataConnection as CIMDataConnection
from _typeshed import Incomplete

class CIMGAMethod:
    model: Incomplete
    dataConnection: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGADataConnection(CIMDataConnection):
    dataConnections: Incomplete
    spatialReference: Incomplete
    metaData: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGAIsoRenderer(CIMClassBreaksRendererBase):
    isoQuality: int
    isoType: Incomplete
    noResultSymbol: str
    refineOnZoom: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGALayer(CIMBaseLayer):
    aOI: Incomplete
    method: str
    renderers: Incomplete
    rangeDefinitions: Incomplete
    activeRangeName: Incomplete
    isFlattened: bool
    def __init__(self, *args, **Kwargs) -> None: ...
