from _typeshed import Incomplete
from arcpy.arcobjects._base import _ObjectWithoutInitCall

class FeatureSharingDraft(_ObjectWithoutInitCall):
    overwriteExistingService: bool
    serverType: str
    serviceType: str
    serviceName: str
    portalFolder: str
    summary: str
    tags: str
    description: str
    credits: str
    useLimitations: bool
    offline: bool
    checkUniqueIDAssignment: bool
    useCIMSymbols: bool
    def __init__(self) -> None: ...
    def exportToSDDraft(self, out_sddraft): ...

class TileSharingDraft(_ObjectWithoutInitCall):
    overwriteExistingService: bool
    serverType: str
    serviceType: str
    serviceName: str
    portalFolder: str
    summary: str
    tags: str
    description: str
    credits: str
    useLimitations: bool
    offline: bool
    def __init__(self) -> None: ...
    def exportToSDDraft(self, out_sddraft): ...

class MapImageSharingDraft(_ObjectWithoutInitCall):
    federatedServerUrl: str
    overwriteExistingService: bool
    serverType: str
    serviceType: str
    serviceName: str
    portalFolder: str
    serverFolder: str
    summary: str
    tags: str
    description: str
    credits: str
    useLimitations: bool
    offline: bool
    copyDataToServer: bool
    checkUniqueIDAssignment: bool
    useCIMSymbols: bool
    def __init__(self) -> None: ...
    def exportToSDDraft(self, out_sddraft): ...

class MapServiceSharingDraft(_ObjectWithoutInitCall):
    federatedServerUrl: str
    targetServer: str
    overwriteExistingService: bool
    serverType: str
    serviceType: str
    serviceName: str
    portalFolder: str
    serverFolder: str
    summary: str
    tags: str
    description: str
    credits: str
    useLimitations: bool
    offline: bool
    copyDataToServer: bool
    checkUniqueIDAssignment: bool
    def __init__(self) -> None: ...
    def exportToSDDraft(self, out_sddraft): ...

class GeoprocessingSharingDraft(_ObjectWithoutInitCall):
    serverType: str
    serviceType: str
    serviceName: str
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
    draftValue: Incomplete
    offlineTarget: str
    enableOutputFeatureService: Incomplete
    convertFeatureLayerURL: bool
    removeDefaultValues: Incomplete
    def __init__(self) -> None: ...
    def exportToSDDraft(self, out_sddraft): ...

def CreateSharingDraft(server_type, service_type, service_name, draft_value): ...
