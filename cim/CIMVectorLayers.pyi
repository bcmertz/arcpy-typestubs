from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from .CIMCore import CIMDefinition as CIMDefinition
from .CIMLayer import CIMBaseLayer as CIMBaseLayer, CIMSubLayerBase as CIMSubLayerBase
from _typeshed import Incomplete

class CIMActivity:
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMAggregateVisualization:
    renderer: str
    labelClass: str
    showLabels: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBindVariable:
    variableName: Incomplete
    alias: Incomplete
    dataType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBinningVisualization:
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMCondition:
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDataConnection:
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDatabaseRelateInfo:
    relationshipClassName: Incomplete
    serviceRelateID: int
    relatedMapMemberURI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDimensionShape:
    beginDimensionPoint: Incomplete
    endDimensionPoint: Incomplete
    dimensionLinePoint: Incomplete
    textPoint: Incomplete
    extensionLineAngle: float
    textAngle: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDimensionStyle:
    align: bool
    baselineHeight: int
    beginMarkerSymbol: str
    convertUnits: bool
    dimensionLineOption: Incomplete
    dimensionLineSymbol: str
    displayPrecision: int
    displayUnits: Incomplete
    drawLineOnFit: bool
    endMarkerSymbol: str
    expression: Incomplete
    expressionParserName: Incomplete
    expressionTitle: Incomplete
    extendLineOnFit: bool
    extensionLineOffset: int
    extensionLineOption: Incomplete
    extensionLineOvershot: int
    extensionLineSymbol: str
    iD: int
    markerFit: Incomplete
    markerFitTolerance: int
    markerOption: Incomplete
    name: Incomplete
    prefix: Incomplete
    suffix: Incomplete
    textFit: Incomplete
    textOption: Incomplete
    textSymbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDisplayFilter:
    name: Incomplete
    whereClause: Incomplete
    minScale: float
    maxScale: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDisplayTable:
    definitionExpression: Incomplete
    definitionExpressionName: Incomplete
    definitionFilterChoices: Incomplete
    displayField: Incomplete
    editable: bool
    relates: Incomplete
    fieldDescriptions: Incomplete
    timeFields: str
    timeDefinition: str
    timeDisplayDefinition: str
    timeDimensionFields: str
    rangeDefinitions: Incomplete
    activeRangeName: Incomplete
    selectRelatedData: bool
    bindVariables: Incomplete
    subtypeValue: int
    useSubtypeValue: bool
    displayExpressionInfo: str
    selectionSetURI: Incomplete
    floorAwareTableProperties: str
    routeIDFieldName: Incomplete
    databaseRelates: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMENCDisplaySettings:
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMENCSubTable:
    name: Incomplete
    subTableID: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMEditingTemplate:
    description: Incomplete
    name: Incomplete
    tags: Incomplete
    defaultToolGUID: Incomplete
    excludedToolGUIDs: Incomplete
    toolOptions: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMEditingTemplateRelationship:
    tableURI: Incomplete
    name: Incomplete
    relationshipID: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMEditingTemplateToolOptions:
    toolProgID: Incomplete
    options: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFeatureExtrusion:
    extrusionType: Incomplete
    extrusionExpression: Incomplete
    extrusionUnit: Incomplete
    extrusionExpressionInfo: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFeatureReduction:
    enabled: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFeatureSortInfo:
    fieldName: Incomplete
    sortDirection: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFeatureTrajectorySubLayer:
    trajectorySubLayerType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFieldDescription:
    alias: Incomplete
    fieldName: Incomplete
    highlight: bool
    numberFormat: str
    readOnly: bool
    visible: bool
    valueAsRatio: bool
    searchable: bool
    searchMode: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFloorAwareTableProperties:
    floorFilterRank: Incomplete
    floorField: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFolderConnection:
    folderConnectionString: Incomplete
    alias: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGroupEditingTemplatePart:
    layerURI: Incomplete
    name: Incomplete
    transformationID: Incomplete
    options: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMHtmlPopupFormat:
    htmlRedirectField: Incomplete
    htmlRedirectFieldPrefix: Incomplete
    htmlRedirectFieldSuffix: Incomplete
    htmlXSLStyleSheet: Incomplete
    htmlHideFieldNameColumn: bool
    htmlUseCodedDomainValues: bool
    htmlPresentationStyle: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLayerAction:
    name: Incomplete
    activities: Incomplete
    conditions: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLayerRange:
    layerURI: Incomplete
    rangeName: Incomplete
    currentRange: str
    currentRangeRelation: Incomplete
    isExclusion: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMaterializedViewProperties:
    materializedViewQuery: Incomplete
    materializedViewExpiration: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMultipatchFeatureTemplateModel:
    isActive: bool
    modelURI: Incomplete
    modelSourceURI: Incomplete
    thumbnailURI: Incomplete
    camera: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPageDefinition:
    pageFieldName: Incomplete
    excludePages: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMParcelFabricActiveRecord:
    activeRecord: Incomplete
    enabled: bool
    showActiveRecordOnly: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRange:
    min: float
    max: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRangeDefinition:
    name: Incomplete
    fieldName: Incomplete
    endFieldName: Incomplete
    uniqueValues: Incomplete
    currentRange: str
    currentRangeRelation: Incomplete
    customFullExtent: str
    isExclusion: bool
    aliasExpressionInfo: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRelateInfoBase:
    dataConnection: str
    foreignKey: Incomplete
    primaryKey: Incomplete
    cardinality: Incomplete
    name: Incomplete
    serviceRelateID: int
    relatedMapMemberURI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMS52MarinerSettings:
    areaSymbolizationType: Incomplete
    colorScheme: Incomplete
    showDataQuality: bool
    deepContour: int
    showDisplayBase: bool
    showOtherDisplay: bool
    showStandardDisplay: bool
    depthDisplayUnits: Incomplete
    showNOBJNM: bool
    honorSCAMIN: bool
    showIsolatedDangers: bool
    labelContours: bool
    labelSafetyContours: bool
    showLowAccuracy: bool
    pointSymbolizationType: Incomplete
    safetyContour: int
    shallowContour: int
    showShallowDepthPattern: bool
    showTwoDepthShades: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMS52TextGroupVisibilitySettings:
    showBerthNumber: bool
    showCurrentVelocity: bool
    showGeographicNames: bool
    showHeightOfIsletOrLandFeature: bool
    showImportantText: bool
    showLightDescription: bool
    showMagneticVariationAndSweptDepth: bool
    showNamesForPositionReporting: bool
    showNatureOfSeabed: bool
    showNoteOnChartData: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMS52ViewingGroupSettings:
    showAllIsolatedDangers: bool
    showArchipelagicSeaLanes: bool
    showBoundariesAndLimits: bool
    showBuoysBeaconsAidsToNavigation: bool
    showBuoysBeaconsStructures: bool
    showChartScaleBoundaries: bool
    showDepthContours: bool
    showDryingLine: bool
    showLights: bool
    showMagneticVariation: bool
    showOtherMiscellaneous: bool
    showProhibitedAndRestrictedAreas: bool
    showSeabed: bool
    showShipsRoutingSystemsAndFerryRoutes: bool
    showSpotSoundings: bool
    showStandardMiscellaneous: bool
    showSubmarineCablesAndPipelines: bool
    showTidal: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSubtypeGroupTable:
    standaloneTables: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSymbolIdentifier:
    iD: int
    name: Incomplete
    symbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSymbolLayerMasking:
    symbolLayers: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTimeDataDefinition:
    useTime: bool
    timeReference: Incomplete
    customTimeExtent: Incomplete
    hasLiveData: bool
    timeExtentCanChange: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTimeDimensionDefinition:
    timeDimensionName: Incomplete
    timeDimensionFormat: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTimeDisplayDefinition:
    cumulative: bool
    timeInterval: float
    timeIntervalUnits: Incomplete
    timeOffset: float
    timeOffsetUnits: Incomplete
    uniqueTimes: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTimeTableDefinition:
    startTimeField: Incomplete
    endTimeField: Incomplete
    timeValueFormat: Incomplete
    trackIDField: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMAnnotationSubLayer(CIMSubLayerBase):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBasicFeatureLayer(CIMBaseLayer):
    autoGenerateFeatureTemplates: bool
    extrusion: str
    featureElevationExpression: Incomplete
    featureTable: str
    featureTemplates: Incomplete
    htmlPopupEnabled: bool
    htmlPopupFormat: str
    isFlattened: bool
    selectable: bool
    selectionColor: str
    polygonSelectionFillColor: str
    selectionSymbol: str
    useSelectionSymbol: bool
    pageDefinition: str
    featureCacheType: Incomplete
    enableDisplayFilters: bool
    displayFilters: Incomplete
    displayFiltersType: Incomplete
    displayFilterName: Incomplete
    displayFilterChoices: Incomplete
    featureElevationExpressionInfo: str
    featureBlendingMode: Incomplete
    featureSortInfos: Incomplete
    layerEffectsMode: Incomplete
    featureEffects: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBuildingDisciplineLayer(CIMBaseLayer):
    disciplineType: Incomplete
    categoryLayers: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBuildingLayer(CIMBaseLayer):
    filters: Incomplete
    activeFilterID: Incomplete
    buildingDisciplineLayers: Incomplete
    exteriorLayer: Incomplete
    buildingID: Incomplete
    dataConnection: str
    summaryStatisticsURI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMCatalogDynamicGroupLayer(CIMBaseLayer):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMENCLayer(CIMBaseLayer):
    dataConnection: str
    displaySettings: str
    subLayers: Incomplete
    subTables: Incomplete
    selectionSetURI: Incomplete
    selectable: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMENCSubLayer(CIMSubLayerBase):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMParcelFabricLayer(CIMBaseLayer):
    accuracyTable: Incomplete
    allLayers: Incomplete
    adjustmentsTable: Incomplete
    cadastralFabricConnection: str
    controlPointLayer: Incomplete
    controlPointSelectionSymbol: str
    jobsTable: Incomplete
    lineLayer: Incomplete
    linePointLayer: Incomplete
    parcelLayer: Incomplete
    plansTable: Incomplete
    pointLayer: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMParcelLayer(CIMBaseLayer):
    recordsLayer: Incomplete
    parcelConnection: str
    parcelFabricActiveRecord: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStandaloneTable(CIMDefinition):
    definitionExpression: Incomplete
    definitionExpressionName: Incomplete
    definitionFilterChoices: Incomplete
    displayField: Incomplete
    editable: bool
    relates: Incomplete
    fieldDescriptions: Incomplete
    timeFields: str
    timeDefinition: str
    timeDisplayDefinition: str
    timeDimensionFields: str
    rangeDefinitions: Incomplete
    activeRangeName: Incomplete
    selectRelatedData: bool
    bindVariables: Incomplete
    subtypeValue: int
    useSubtypeValue: bool
    displayExpressionInfo: str
    selectionSetURI: Incomplete
    floorAwareTableProperties: str
    routeIDFieldName: Incomplete
    databaseRelates: Incomplete
    dataConnection: str
    description: Incomplete
    autoGenerateRowTemplates: bool
    rowTemplates: Incomplete
    serviceTableID: int
    showPopups: bool
    popupInfo: str
    charts: Incomplete
    pageDefinition: str
    customProperties: Incomplete
    webMapTableID: Incomplete
    searchable: bool
    useVisibilityTimeExtent: bool
    visibilityTimeExtent: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTrajectoryLayer(CIMBaseLayer):
    footprintLayer: Incomplete
    pointLayer: Incomplete
    trajectoryDatasetConnection: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVectorTileLayer(CIMBaseLayer):
    dataConnection: str
    currentStyle: Incomplete
    associatedFeatureLayerURI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMAggregateField(CIMFieldDescription):
    aggregatedFieldName: Incomplete
    statisticType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMAggregationFeatureReduction(CIMFeatureReduction):
    fields: Incomplete
    popupInfo: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMAnnotationLayer(CIMBasicFeatureLayer):
    barrierWeight: Incomplete
    drawGeometry: bool
    drawUnplacedAnnotation: bool
    drawGeometryLineSymbol: str
    drawGeometryPointSymbol: str
    unplacedAnnotationColor: str
    symbolSubstitutionType: Incomplete
    massColorSubstitute: str
    inlineColor: str
    substitutionSymbolCollection: Incomplete
    subLayers: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMAttributeCondition(CIMCondition):
    whereClause: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBasicRowTemplate(CIMEditingTemplate):
    defaultValues: Incomplete
    requiredFields: Incomplete
    hiddenFields: Incomplete
    relationships: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBinningFeatureReduction(CIMAggregationFeatureReduction):
    thresholdType: Incomplete
    maximumScale: int
    featureCount: int
    minimumBinSize: int
    visualization: str
    spatialReference: Incomplete
    fixedLevel: int
    binType: Incomplete
    clientSideBinning: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMCatalogLayer(CIMBasicFeatureLayer):
    footprintLayer: Incomplete
    catalogDynamicGroupLayer: Incomplete
    maximumVisibleSublayers: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMClusteringFeatureReduction(CIMAggregationFeatureReduction):
    maximumScale: int
    clusterRadius: int
    visualization: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDimensionLayer(CIMBasicFeatureLayer):
    barrierWeight: Incomplete
    snappable: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDiscreteVariable(CIMBindVariable):
    defaultValue: Incomplete
    boundValue: Incomplete
    allowMultiple: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMENCDataConnection(CIMDataConnection):
    customParameters: Incomplete
    uRI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFeatureDatasetDataConnection(CIMDataConnection):
    featureDataset: Incomplete
    workspaceConnectionString: Incomplete
    workspaceFactory: Incomplete
    customWorkspaceFactoryCLSID: Incomplete
    dataset: Incomplete
    datasetType: Incomplete
    customParameters: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFeatureTable(CIMDisplayTable):
    dataConnection: str
    studyArea: Incomplete
    studyAreaSpatialRel: Incomplete
    searchOrder: Incomplete
    isLicensedDataSource: bool
    definitionSetURI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeoFeatureLayerBase(CIMBasicFeatureLayer):
    actions: Incomplete
    exclusionSet: Incomplete
    featureMasks: Incomplete
    labelClasses: Incomplete
    labelVisibility: bool
    maskedSymbolLayers: Incomplete
    renderer: str
    scaleSymbols: bool
    snappable: bool
    symbolLayerDrawing: str
    trackLinesRenderer: str
    previousObservationsRenderer: str
    previousObservationsCount: int
    useRealWorldSymbolSizes: bool
    showPreviousObservations: bool
    featureReduction: str
    showTracks: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGroupEditingTemplate(CIMEditingTemplate):
    baseName: Incomplete
    basePart: str
    parts: Incomplete
    createUtilityNetworkAssociations: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMHighlightActivity(CIMActivity):
    highlightSymbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLocationCondition(CIMCondition):
    conditionType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMultipatchFeatureTemplate(CIMBasicRowTemplate):
    galleryMode: bool
    models: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMNetCDFRasterDataConnection(CIMDataConnection):
    workspaceConnectionString: Incomplete
    workspaceFactory: Incomplete
    customWorkspaceFactoryCLSID: Incomplete
    dataset: Incomplete
    datasetType: Incomplete
    bandDimension: Incomplete
    extent: Incomplete
    invertRows: bool
    selectedDimensionIndexes: Incomplete
    selectedDimensions: Incomplete
    selectedDimensionValues: Incomplete
    variable: Incomplete
    verticalDimension: Incomplete
    verticalDimensionUnit: Incomplete
    xDimension: Incomplete
    yDimension: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMNetCDFStandardDataConnection(CIMDataConnection):
    workspaceConnectionString: Incomplete
    workspaceFactory: Incomplete
    customWorkspaceFactoryCLSID: Incomplete
    dataset: Incomplete
    datasetType: Incomplete
    variableList: Incomplete
    rowDimensionList: Incomplete
    xDimension: Incomplete
    yDimension: Incomplete
    zDimension: Incomplete
    mDimension: Incomplete
    selectedDimensions: Incomplete
    selectedDimensionIndexes: Incomplete
    selectedDimensionValues: Incomplete
    shapeFieldName: Incomplete
    verticalDimension: Incomplete
    verticalDimensionUnit: Incomplete
    selectedVolume: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMOrientedImageryLayer(CIMGeoFeatureLayerBase):
    orientedImageryPropertyOverrides: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRangeVariable(CIMBindVariable):
    fieldExpression: Incomplete
    optional: bool
    defaultMin: Incomplete
    defaultMax: Incomplete
    tableName: Incomplete
    valueIfMissing: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRasterTable(CIMDisplayTable):
    joins: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRelQueryTableDataConnection(CIMDataConnection):
    sourceTable: str
    destinationTable: str
    primaryKey: Incomplete
    foreignKey: Incomplete
    name: Incomplete
    cardinality: Incomplete
    joinType: Incomplete
    joinForward: bool
    oneToFirst: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRelateInfo(CIMRelateInfoBase):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRouteEventDataConnection(CIMDataConnection):
    routeFeatureClass: str
    routeIDFieldName: Incomplete
    routeWhereClause: Incomplete
    routeMeasureUnit: Incomplete
    eventMeasureUnit: Incomplete
    eventRouteIDFieldName: Incomplete
    isLineEvent: bool
    lateralOffsetFieldName: Incomplete
    mDirectionOffsetting: bool
    errorFieldName: Incomplete
    addErrorField: bool
    fromMeasureFieldName: Incomplete
    toMeasureFieldName: Incomplete
    addAngleField: bool
    angleFieldName: Incomplete
    asPointFeature: bool
    complementAngle: bool
    normalAngle: bool
    eventTable: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRowTemplate(CIMBasicRowTemplate):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMS52DisplaySettings(CIMENCDisplaySettings):
    marinerSettings: str
    textGroupVisibilitySettings: str
    viewingGroupSettings: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSqlQueryDataConnection(CIMDataConnection):
    workspaceConnectionString: Incomplete
    workspaceFactory: Incomplete
    customWorkspaceFactoryCLSID: Incomplete
    dataset: Incomplete
    datasetType: Incomplete
    sqlQuery: Incomplete
    srid: Incomplete
    spatialReference: Incomplete
    oIDFields: Incomplete
    geometryType: Incomplete
    extent: Incomplete
    queryFields: Incomplete
    spatialStorageType: int
    sridType: int
    spatialIndexDimension: int
    isTableBased: bool
    materializedViewProperties: str
    mappedOIDFieldLength: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStandardDataConnection(CIMDataConnection):
    customParameters: Incomplete
    workspaceConnectionString: Incomplete
    workspaceFactory: Incomplete
    customWorkspaceFactoryCLSID: Incomplete
    dataset: Incomplete
    datasetType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStreamServiceDataConnection(CIMDataConnection):
    workspaceConnectionString: Incomplete
    workspaceFactory: Incomplete
    customWorkspaceFactoryCLSID: Incomplete
    dataset: Incomplete
    datasetType: Incomplete
    featureExpirationMethod: Incomplete
    maximumFeatureCount: int
    maximumFeatureAge: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSubtypeGroupLayer(CIMBasicFeatureLayer):
    subtypeLayers: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSubtypeGroupLayerBase(CIMBasicFeatureLayer):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSuppressActivity(CIMActivity):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTableQueryNameDataConnection(CIMDataConnection):
    workspaceConnectionString: Incomplete
    workspaceFactory: Incomplete
    customWorkspaceFactoryCLSID: Incomplete
    dataset: Incomplete
    datasetType: Incomplete
    subFields: Incomplete
    tables: Incomplete
    whereClause: Incomplete
    primaryKeyFields: Incomplete
    copyLocally: bool
    shapeType: Incomplete
    featureType: Incomplete
    extent: Incomplete
    shapeFieldName: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTemporalDataConnection(CIMDataConnection):
    workspaceConnectionString: Incomplete
    workspaceFactory: Incomplete
    customWorkspaceFactoryCLSID: Incomplete
    dataset: Incomplete
    datasetType: Incomplete
    timeFieldLocaleID: int
    timeFieldAmFormat: Incomplete
    timeFieldPmFormat: Incomplete
    cachingMode: Incomplete
    startTimeField: Incomplete
    endTimeField: Incomplete
    timeValueFormat: Incomplete
    trackIDField: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTrackingServerDataConnection(CIMDataConnection):
    workspaceConnectionString: Incomplete
    workspaceFactory: Incomplete
    customWorkspaceFactoryCLSID: Incomplete
    dataset: Incomplete
    datasetType: Incomplete
    autoPurge: bool
    purgeThreshold: int
    purgePercentage: float
    keepPerTrack: int
    purgeRule: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVectorTileDataConnection(CIMDataConnection):
    customParameters: Incomplete
    uRI: Incomplete
    resourcesURI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMWorkspaceConnection(CIMDataConnection):
    workspaceConnectionString: Incomplete
    workspaceFactory: Incomplete
    customWorkspaceFactoryCLSID: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMXYEventDataConnection(CIMDataConnection):
    xFieldName: Incomplete
    yFieldName: Incomplete
    zFieldName: Incomplete
    spatialReference: Incomplete
    xYEventTableDataConnection: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFeatureLayer(CIMGeoFeatureLayerBase):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeometryLocationCondition(CIMLocationCondition):
    geometries: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...
