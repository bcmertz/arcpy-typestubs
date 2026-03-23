from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from _typeshed import Incomplete

class CIMDefinition:
    name: Incomplete
    uRI: Incomplete
    sourceURI: Incomplete
    sourceModifiedTime: Incomplete
    metadataURI: Incomplete
    useSourceMetadata: bool
    sourcePortalUrl: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPortalItem:
    portalURL: Incomplete
    itemID: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...
