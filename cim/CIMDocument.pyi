from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from _typeshed import Incomplete

class CIMBinaryReference:
    uRI: Incomplete
    data: Incomplete
    object: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMColorReplacementRule:
    inputColor: str
    outputColor: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGISProject:
    views: Incomplete
    moduleSettings: Incomplete
    projectItems: Incomplete
    databaseConnections: Incomplete
    serverConnections: Incomplete
    folderConnections: Incomplete
    viewLayoutXML: Incomplete
    defaultGeoDatabase: Incomplete
    defaultToolbox: Incomplete
    defaultSpatialReference: Incomplete
    defaultFolder: Incomplete
    projectMetadata: Incomplete
    sourceURI: Incomplete
    sourceModifiedTime: Incomplete
    readOnly: bool
    forceUpdate: bool
    thumbnailOptions: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMModuleSettings:
    moduleName: Incomplete
    settingsXML: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMProjectItem:
    alias: Incomplete
    iD: Incomplete
    catalogPath: Incomplete
    pathHint: Incomplete
    itemType: Incomplete
    name: Incomplete
    propertiesXML: Incomplete
    sourceURI: Incomplete
    sourceModifiedTime: Incomplete
    consolidatePath: bool
    consolidationResources: Incomplete
    pathSaveRelative: bool
    metadataURI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMProjectThumbnailOptions:
    generationMethod: Incomplete
    automaticGenerationSource: Incomplete
    mapURI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStatisticalDataCollection:
    name: Incomplete
    shortDescription: Incomplete
    longDescription: Incomplete
    keywords: Incomplete
    countries: Incomplete
    categories: Incomplete
    author: Incomplete
    creationDate: Incomplete
    lastRevisionDate: Incomplete
    calculators: Incomplete
    dataVintage: Incomplete
    dataVintageDescription: Incomplete
    icon: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStatisticalDataCollectionCalculator:
    name: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStatisticalDataCollectionField:
    name: Incomplete
    alias: Incomplete
    category: Incomplete
    apportionmentMethod: Incomplete
    summaryType: Incomplete
    weightFieldName: Incomplete
    precision: int
    fieldFormat: str
    vintage: Incomplete
    script: Incomplete
    scriptLanguage: Incomplete
    usedFields: Incomplete
    showInDataBrowser: bool
    outputFieldType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStatisticalDataCollectionInputAreaProperty:
    units: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStatisticalDataCollectionInputProperty:
    name: Incomplete
    alias: Incomplete
    propertyType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStatisticalDataCollectionStandardVariable:
    name: Incomplete
    showInDataBrowser: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVersion:
    version: Incomplete
    build: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMView:
    viewableObjectPath: Incomplete
    viewType: Incomplete
    instanceID: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBookmarkDocument(CIMVersion):
    spatialReference: Incomplete
    bookmarks: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMColorReplacementDocument(CIMVersion):
    replacementRules: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDocumentInfo(CIMVersion):
    documentTitle: Incomplete
    subject: Incomplete
    author: Incomplete
    category: Incomplete
    comments: Incomplete
    keywords: Incomplete
    credits: Incomplete
    hyperlinkBase: Incomplete
    savePreview: bool
    activeMapRepositoryPath: Incomplete
    useRelativePath: bool
    antialiasing: Incomplete
    textAntialiasing: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGenericView(CIMView):
    viewProperties: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLayerDocument(CIMVersion):
    layers: Incomplete
    tables: Incomplete
    layerDefinitions: Incomplete
    binaryReferences: Incomplete
    tableDefinitions: Incomplete
    rGBColorProfile: Incomplete
    cMYKColorProfile: Incomplete
    elevationSurfaceLayerDefinitions: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLayoutDocument(CIMVersion):
    binaryReferences: Incomplete
    layerDefinitions: Incomplete
    mapDefinitions: Incomplete
    tableDefinitions: Incomplete
    layoutDefinition: str
    linkChartDefinitions: Incomplete
    timelineDefinitions: Incomplete
    videoDefinitions: Incomplete
    elevationSurfaceLayerDefinitions: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMapDocument(CIMVersion):
    mapDefinition: str
    layerDefinitions: Incomplete
    binaryReferences: Incomplete
    tableDefinitions: Incomplete
    linkChartDefinitions: Incomplete
    timelineDefinitions: Incomplete
    videoDefinitions: Incomplete
    elevationSurfaceLayerDefinitions: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMapView(CIMView):
    viewingMode: Incomplete
    camera: str
    verticalExaggerationScaleFactor: float
    timeDisplay: str
    layerRanges: Incomplete
    rangeSliderSettings: str
    timeSliderSettings: str
    floorFilterSettings: str
    sceneDrawingMode: Incomplete
    fieldOfView: float
    pauseDrawing: bool
    pauseAnimatedSymbols: bool
    exploratoryAnalysis: Incomplete
    visualEffect: str
    cameraEffect: str
    postprocessingEffects: Incomplete
    colorVisionDeficiencyMode: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStatisticalDataCollectionDocument(CIMVersion):
    statisticalDataCollection: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStatisticalDataCollectionFeatureLayerCalculator(CIMStatisticalDataCollectionCalculator):
    datasetID: Incomplete
    dataConnection: str
    fields: Incomplete
    apportionmentDatasetConnection: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStatisticalDataCollectionInputPropertiesCalculator(CIMStatisticalDataCollectionCalculator):
    area: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStatisticalDataCollectionScriptCalculator(CIMStatisticalDataCollectionCalculator):
    scripts: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStatisticalDataCollectionStandardDataCalculator(CIMStatisticalDataCollectionCalculator):
    datasetID: Incomplete
    variables: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTableView(CIMView):
    fieldOrder: Incomplete
    sortInformation: Incomplete
    selectionMode: bool
    honorTime: bool
    frozenFields: int
    zoomLevel: int
    fieldWidth: Incomplete
    displaySubtypeDomainDescriptions: bool
    qualifyJoinFieldNames: bool
    time: Incomplete
    honorRange: bool
    ranges: Incomplete
    extent: Incomplete
    timeRelation: Incomplete
    showOnlyContingentValueFields: bool
    highlightInvalidContingentValueFields: bool
    autoPopulateContingentValueFields: bool
    columnHeaderRowHeight: Incomplete
    rowHeight: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMExternalTableView(CIMTableView):
    dataConnection: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMapTableView(CIMTableView):
    mapURI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...
