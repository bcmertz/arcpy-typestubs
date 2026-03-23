from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from .CIMLayer import CIMBaseLayer as CIMBaseLayer
from .CIMVectorLayers import CIMDataConnection as CIMDataConnection
from _typeshed import Incomplete

class CIMSchematicDataConnection(CIMDataConnection):
    workspaceConnectionString: Incomplete
    workspaceFactory: Incomplete
    customWorkspaceFactoryCLSID: Incomplete
    dataset: Incomplete
    datasetType: Incomplete
    schematicDataset: Incomplete
    diagramTemplate: Incomplete
    diagram: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSchematicLayer(CIMBaseLayer):
    layers: Incomplete
    schematicDiagram: str
    symbolLayerDrawing: str
    referenceScale: float
    isTemplate: bool
    def __init__(self, *args, **Kwargs) -> None: ...
