from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from .CIMLayer import CIMGroupLayer as CIMGroupLayer
from .CIMVectorLayers import CIMDataConnection as CIMDataConnection
from _typeshed import Incomplete

class CIMDiagramLayer(CIMGroupLayer):
    referenceScale: float
    dataConnection: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDiagramRelQueryDataConnection(CIMDataConnection):
    workspaceConnectionString: Incomplete
    workspaceFactory: Incomplete
    customWorkspaceFactoryCLSID: Incomplete
    dataset: Incomplete
    datasetType: Incomplete
    featureDataset: Incomplete
    diagramDatasetFeatureClass: Incomplete
    networkSourceID: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMNetworkDiagramDataConnection(CIMDataConnection):
    workspaceConnectionString: Incomplete
    workspaceFactory: Incomplete
    customWorkspaceFactoryCLSID: Incomplete
    dataset: Incomplete
    datasetType: Incomplete
    featureDataset: Incomplete
    diagram: Incomplete
    isStored: bool
    table: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...
