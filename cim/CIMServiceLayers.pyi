from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from .CIMLayer import CIMBaseLayer as CIMBaseLayer, CIMSubLayerBase as CIMSubLayerBase
from .CIMVectorLayers import CIMDataConnection as CIMDataConnection
from _typeshed import Incomplete

class CIMIsosurface:
    iD: Incomplete
    color: str
    isCustomColor: bool
    value: int
    name: Incomplete
    visible: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMObject3DRenderingFilter:
    iD: Incomplete
    name: Incomplete
    description: Incomplete
    filterBlocks: Incomplete
    authoringInfo: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMObject3DRenderingFilterAuthoringInfo:
    isVisible: bool
    filterBlocks: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMObject3DRenderingFilterBlock:
    title: Incomplete
    mode: Incomplete
    expression: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMObject3DRenderingFilterBlockAuthoringInfo:
    filterStates: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMObject3DRenderingFilterState:
    filterType: Incomplete
    selectedValues: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMServerConnection:
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMServiceSubTable:
    name: Incomplete
    subTableID: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVoxelColorUniqueValue:
    value: int
    label: Incomplete
    color: str
    visible: bool
    description: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVoxelFilter:
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVoxelFormat:
    scale: float
    offset: float
    useNoDataValue: bool
    noDataValue: float
    scalarFormat: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVoxelLighting:
    isDiffuseEnabled: bool
    diffuse: float
    isSpecularEnabled: bool
    specular: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVoxelPlane:
    iD: Incomplete
    name: Incomplete
    visible: bool
    position: Incomplete
    normal: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVoxelRenderer:
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVoxelStaticSection:
    iD: int
    name: Incomplete
    visible: bool
    expanded: bool
    variable: Incomplete
    slices: Incomplete
    plane: str
    rasterURI: Incomplete
    format: str
    height: int
    width: int
    timeIndex: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVoxelVariableProfile:
    variable: Incomplete
    description: Incomplete
    dataType: Incomplete
    filters: Incomplete
    renderer: str
    precision: Incomplete
    signature: Incomplete
    signatureVersion: int
    isosurfaces: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVoxelVolume:
    iD: int
    sections: Incomplete
    slices: Incomplete
    variableProfiles: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBuildingDisciplineSceneLayer(CIMBaseLayer):
    subLayers: Incomplete
    subLayerID: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBuildingSceneLayer(CIMBaseLayer):
    subLayers: Incomplete
    dataConnection: str
    filters: Incomplete
    activeFilterID: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMIndexedSceneLayer(CIMBaseLayer):
    snappable: bool
    renderer: str
    featureElevationExpression: Incomplete
    labelClasses: Incomplete
    labelVisibility: bool
    dataConnection: str
    useRealWorldSymbolSizes: bool
    exclusionSet: Incomplete
    definitionExpression: Incomplete
    definitionExpressionName: Incomplete
    definitionFilterChoices: Incomplete
    associatedFeatureLayerURI: Incomplete
    indexedSceneLayerType: Incomplete
    selectable: bool
    selectionSetURI: Incomplete
    modificationLayerURI: Incomplete
    modificationLayerEnabled: bool
    usePredefinedMaxScreenThreshold: bool
    floorAwareTableProperties: str
    timeFields: str
    timeDefinition: str
    timeDisplayDefinition: str
    rangeDefinitions: Incomplete
    activeRangeName: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMServiceCompositeSubLayer(CIMSubLayerBase):
    subLayers: Incomplete
    definitionExpression: Incomplete
    uRI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMServiceConnection(CIMDataConnection):
    description: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMServiceLayer(CIMBaseLayer):
    serviceConnection: str
    subLayers: Incomplete
    transparentColor: str
    backgroundColor: str
    subTables: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMServiceSubLayer(CIMSubLayerBase):
    showLabels: bool
    scaleSymbols: bool
    definitionExpression: Incomplete
    sourceID: Incomplete
    useTime: bool
    drawTimeCumulative: bool
    timeOffset: float
    timeOffsetUnits: Incomplete
    layerDefinition: Incomplete
    popupInfo: str
    showPopups: bool
    floorAwareTableProperties: str
    uRI: Incomplete
    definitionExpressionName: Incomplete
    definitionFilterChoices: Incomplete
    selectionSetURI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTiles3DDataConnection(CIMDataConnection):
    customParameters: Incomplete
    uRI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTiles3DLayer(CIMBaseLayer):
    dataConnection: str
    snappable: bool
    tiles3DLayerType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVoxelDataConnection(CIMDataConnection):
    uRI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVoxelLayer(CIMBaseLayer):
    dataConnection: str
    lighting: str
    isosurfaceContainerExpanded: bool
    isosurfaceContainerVisible: bool
    optimization: Incomplete
    sectionContainerExpanded: bool
    sectionContainerVisible: bool
    selectedVariable: Incomplete
    sliceContainerExpanded: bool
    sliceContainerVisible: bool
    snappable: bool
    staticSections: Incomplete
    staticSectionContainerExpanded: bool
    staticSectionContainerVisible: bool
    surfaceContainerExpanded: bool
    visualization: Incomplete
    alignment: Incomplete
    volumes: Incomplete
    timeDefinition: str
    timeDisplayDefinition: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMWMSSubLayer(CIMSubLayerBase):
    styleName: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMAGSServiceConnection(CIMServiceConnection):
    customParameters: Incomplete
    objectName: Incomplete
    objectType: Incomplete
    url: Incomplete
    capabilities: Incomplete
    serverConnection: str
    gdbVersion: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDCOMServerConnection(CIMServerConnection):
    domain: Incomplete
    hideUserProperty: bool
    machine: Incomplete
    managerURL: Incomplete
    password: Incomplete
    user: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDynamicServiceLayer(CIMServiceLayer):
    imageFormat: Incomplete
    useTime: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMInternetServerConnectionBase(CIMServerConnection):
    anonymous: bool
    hideUserProperty: bool
    password: Incomplete
    url: Incomplete
    user: Incomplete
    authenticationInfo: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLANServerConnection(CIMServerConnection):
    machine: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMapImageLayer(CIMDynamicServiceLayer):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMOGCAPIMapTilesServiceConnection(CIMServiceConnection):
    layerName: Incomplete
    version: Incomplete
    serverConnection: str
    style: Incomplete
    imageFormat: Incomplete
    tileMatrixSet: Incomplete
    capabilitiesParameters: Incomplete
    templateUrl: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMOGCAPIServiceConnection(CIMServiceConnection):
    serviceName: Incomplete
    version: Incomplete
    serverConnection: str
    capabilitiesParameters: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMProjectServerConnection(CIMInternetServerConnectionBase):
    connectionMode: Incomplete
    name: Incomplete
    serverType: Incomplete
    stagingFolder: Incomplete
    useDefaultStagingFolder: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStandardServiceConnection(CIMServiceConnection):
    serviceProvider: Incomplete
    serviceType: Incomplete
    url: Incomplete
    culture: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTiledServiceLayer(CIMServiceLayer):
    associatedFeatureLayerURI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVoxelRangeValueFilter(CIMVoxelFilter):
    min: int
    max: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVoxelStretchRenderer(CIMVoxelRenderer):
    colorRamp: str
    minLabel: Incomplete
    maxLabel: Incomplete
    isDataFilterEnabled: bool
    dataFilterMin: int
    dataFilterMax: int
    colorRangeMin: int
    colorRangeMax: int
    useTransparencyStops: bool
    transparencyStopPositions: Incomplete
    transparencyStopValues: Incomplete
    heading: Incomplete
    interpolation: Incomplete
    showFullDataRange: bool
    numberFormat: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVoxelUniqueValueRenderer(CIMVoxelRenderer):
    classes: Incomplete
    colorRamp: str
    heading: Incomplete
    useDefaultColor: bool
    defaultColor: str
    defaultLabel: Incomplete
    defaultDescription: Incomplete
    unlistedValues: Incomplete
    showClassVisibility: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVoxelValueFilter(CIMVoxelFilter):
    values: Incomplete
    mode: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMWCSServiceConnection(CIMServiceConnection):
    coverageName: Incomplete
    version: Incomplete
    serverConnection: str
    capabilitiesParameters: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMWFSServiceConnection(CIMServiceConnection):
    layerName: Incomplete
    version: Incomplete
    serverConnection: str
    capabilitiesParameters: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMWMSLayer(CIMDynamicServiceLayer):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMWMSServiceConnection(CIMServiceConnection):
    layerName: Incomplete
    version: Incomplete
    serverConnection: str
    capabilitiesParameters: Incomplete
    mapParameters: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMWMTSServiceConnection(CIMServiceConnection):
    layerName: Incomplete
    version: Incomplete
    serverConnection: str
    style: Incomplete
    dimensions: Incomplete
    imageFormat: Incomplete
    tileMatrixSet: Incomplete
    capabilitiesParameters: Incomplete
    mapParameters: Incomplete
    templateUrl: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMInternetServerConnection(CIMInternetServerConnectionBase):
    def __init__(self, *args, **Kwargs) -> None: ...
