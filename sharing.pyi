from _typeshed import Incomplete
from arcpy._sharingproperties import _ParameterChecker
from arcpy.arcobjects._base import _ObjectWithoutInitCall

class _SharingDraftBase(_ParameterChecker):
    overwriteExistingService: bool
    serviceName: str
    portalFolder: str
    summary: str
    tags: str
    description: str
    credits: str
    useLimitations: bool
    offline: bool
    sharing: Incomplete
    def __init__(self) -> None: ...
    def exportToSDDraft(self, out_sddraft): ...

class _FeatureSharingDraft(_SharingDraftBase):
    maxRecordCount: Incomplete
    checkUniqueIDAssignment: bool
    useCIMSymbols: bool
    approvePublicDataCollection: bool
    preserveEditUsersAndTimestamps: bool
    allowUpdateWithoutMValues: bool
    featureCapabilities: str
    zDefault: Incomplete
    timezone: Incomplete
    def __init__(self) -> None: ...

class _TileSharingDraft(_SharingDraftBase):
    cache: Incomplete
    def __init__(self) -> None: ...

class _MapImageSharingDraft(_SharingDraftBase):
    maxRecordCount: Incomplete
    federatedServerUrl: str
    serverFolder: str
    copyDataToServer: bool
    checkUniqueIDAssignment: bool
    useCIMSymbols: bool
    enableDynamicWorkspaces: bool
    mapOperations: str
    enableCache: bool
    extension: Incomplete
    cache: Incomplete
    timezone: Incomplete
    pooling: Incomplete
    def __init__(self) -> None: ...

class _MapServiceSharingDraft(_SharingDraftBase):
    maxRecordCount: Incomplete
    federatedServerUrl: str
    targetServer: str
    serverType: str
    serviceType: str
    serverFolder: str
    copyDataToServer: bool
    checkUniqueIDAssignment: bool
    enableDynamicWorkspaces: bool
    mapOperations: str
    enableCache: bool
    extension: Incomplete
    cache: Incomplete
    timezone: Incomplete
    pooling: Incomplete
    def __init__(self) -> None: ...
    def exportToSDDraft(self, out_sddraft) -> None: ...

class GeoprocessingSharingDraft(_ObjectWithoutInitCall):
    serverType: str
    serviceType: str
    serviceName: str
    draftValue: Incomplete
    description: str
    summary: str
    tags: str
    offline: bool
    targetServer: str
    overwriteExistingService: bool
    copyDataToServer: bool
    executionType: str
    serverFolder: str
    portalFolder: str
    maximumRecords: int
    maxInstances: int
    minInstances: int
    resultMapService: bool
    messageLevel: str
    maxUsageTime: int
    maxWaitTime: int
    maxIdleTime: int
    capabilities: Incomplete
    constantValues: Incomplete
    choiceLists: Incomplete
    offlineTarget: str
    enableOutputFeatureService: Incomplete
    convertFeatureLayerURL: bool
    removeDefaultValues: Incomplete
    GPStringValues: Incomplete
    enableOutputImageService: bool
    def __init__(self, **kwargs) -> None: ...
    def exportToSDDraft(self, out_sddraft): ...
    def analyzeSDDraft(self, out_sddraft: Incomplete | None = None): ...

def CreateSharingDraft(server_type, service_type, service_name, draft_value): ...

class _SceneLayerSharingDraft(_ParameterChecker):
    serviceType: Incomplete
    serviceName: Incomplete
    compressedTextures: bool
    export: bool
    def __init__(self, serviceType, serviceName, draftValue, sharingDraft, isLocalScene) -> None: ...
    def analyzeForSharing(self): ...

def Publish(object, item_id: Incomplete | None = None): ...
