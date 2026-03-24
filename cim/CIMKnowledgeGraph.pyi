from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from .CIMCore import CIMDefinition as CIMDefinition
from .CIMLayer import CIMBaseLayer as CIMBaseLayer
from .CIMVectorLayers import CIMDataConnection as CIMDataConnection, CIMGeoFeatureLayerBase as CIMGeoFeatureLayerBase
from _typeshed import Incomplete

class CIMFilteredFindPathsConfiguration:
    name: Incomplete
    closedPathPolicy: Incomplete
    originEntities: Incomplete
    destinationEntities: Incomplete
    pathFilters: Incomplete
    defaultTraversalDirectionType: Incomplete
    traversalDirections: Incomplete
    entityUsage: Incomplete
    pathMode: Incomplete
    relationshipCostProperty: Incomplete
    defaultRelationshipCost: float
    negativeCostBehaviour: Incomplete
    minPathLength: int
    maxPathLength: int
    minPathCost: float
    maxPathCost: float
    maxCountPaths: int
    timeFilter: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFilteredFindPathsEntity:
    iD: Incomplete
    entityTypeName: Incomplete
    propertyFilterPredicate: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFilteredFindPathsError:
    error: Incomplete
    detailedErrorMessage: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFilteredFindPathsPathFilter:
    iD: Incomplete
    itemTypeName: Incomplete
    itemType: Incomplete
    filterType: Incomplete
    propertyFilterPredicate: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFilteredFindPathsResult:
    error: str
    configurationWarning: Incomplete
    executionWarnings: Incomplete
    statistics: str
    paths: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFilteredFindPathsStatistics:
    countLocalGraphNodes: int
    countLocalGraphEdges: int
    countOriginExpansionQueries: int
    countDestinationExpansionQueries: int
    countWaypointsExpansionQueries: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKGColorInfo:
    useCustomColors: bool
    defaultItemColor: str
    defaultTextColor: str
    customItemColor: str
    customTextColor: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKGConsecutiveEventsRestrictions:
    restrictMaxOverlap: bool
    maxOverlap: int
    maxOverlapUnit: Incomplete
    restrictMaxGap: bool
    maxGap: int
    maxGapUnit: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKGDataModelVisualization:
    configurationName: Incomplete
    entityTypes: Incomplete
    relationshipTypes: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKGDiagramPosition:
    x: float
    y: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKGDurativeEventsDurationConstraint:
    timeUnit: Incomplete
    minDuration: float
    useMaxDuration: bool
    maxDuration: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKGEventDefinition:
    namedType: Incomplete
    startProperty: Incomplete
    endProperty: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKGEventErrorHandling:
    kGEventMissingAllTimesBehaviour: Incomplete
    kGDurativeEventMissingOneTimeBehaviour: Incomplete
    kGDurativeEventSwappedTimesBehaviour: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKGEventsDefinitions:
    eventDefinitions: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKGPaths:
    entitiesUIDs: Incomplete
    entityTypes: Incomplete
    indexedEntityTypes: Incomplete
    relationshipsGroupsUIDsBuffer: Incomplete
    relationshipTypes: Incomplete
    indexedRelationshipTypes: Incomplete
    relationshipsGroupsUIDsEndIndex: Incomplete
    relationshipsCosts: Incomplete
    relationshipsGroupsFrom: Incomplete
    relationshipsGroupsTo: Incomplete
    relationshipsFrom: Incomplete
    relationshipsTo: Incomplete
    pathsBuffer: Incomplete
    pathsEndIndex: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKGRelationshipTypeEndpoint:
    originEntityTypeName: Incomplete
    destinationEntityTypeName: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKGTimeFilter:
    enabled: bool
    kGPathTimeFlow: Incomplete
    timeWindow: str
    eventsDefinitions: str
    durativeEventsDurationConstraint: str
    eventErrorHandling: str
    consecutiveEventsRestrictions: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKGTimeWindow:
    minTime: Incomplete
    maxTime: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKGTraversalDirection:
    relationshipTypeName: Incomplete
    traversalDirectionType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKGType:
    typeName: Incomplete
    geometryType: Incomplete
    properties: Incomplete
    colorInfo: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKGTypeProperty:
    propertyName: Incomplete
    propertyType: Incomplete
    aliasName: Incomplete
    isNullable: bool
    defaultVisibility: bool
    editable: bool
    domainName: Incomplete
    defaultValue: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphCentralityConfiguration:
    relationshipsInterpretation: Incomplete
    defaultRelationshipImportance: float
    relationshipImportanceProperty: Incomplete
    defaultRelationshipCost: float
    relationshipCostProperty: Incomplete
    multiedgeFactor: float
    normalization: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphDataLoadingConfiguration:
    name: Incomplete
    entities: Incomplete
    relationships: Incomplete
    missingDataOptions: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphDataLoadingEntity:
    name: Incomplete
    entityType: Incomplete
    typeIsFieldName: bool
    entityTypeExpression: str
    multipleTypeLookup: str
    properties: Incomplete
    merge: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphDataLoadingMissingDataOptions:
    allowCreationWhenAllDataMissing: bool
    overwriteWithMissingValuesWhenMerging: bool
    mergePropertiesWithMissingData: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphDataLoadingRelationship:
    name: Incomplete
    sourceEntityName: Incomplete
    relationshipType: Incomplete
    typeIsFieldName: bool
    relationshipTypeExpression: str
    targetEntityName: Incomplete
    properties: Incomplete
    merge: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphInvestigationTypeInfo:
    typeName: Incomplete
    popupInfo: str
    symbol: str
    displayExpressionInfo: str
    propertyInfos: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphLinkChartCentralityConfiguration:
    relationshipsInterpretation: Incomplete
    computeShortestPathsBasedMeasures: bool
    includeDocumentEntities: bool
    defaultRelationshipImportance: float
    relationshipImportanceProperty: Incomplete
    defaultRelationshipCost: float
    relationshipCostProperty: Incomplete
    multiedgeFactor: float
    normalization: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphLinkChartProperties:
    nodesURI: Incomplete
    linksURI: Incomplete
    aggregatedNodesURI: Incomplete
    aggregatedLinksURI: Incomplete
    autoCollapseRelationships: bool
    centralityConfiguration: str
    centralityIsUpToDate: bool
    lastUsedLayout: str
    nonspatialDataDisplay: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphMultipleTypeLookup:
    typeLookups: Incomplete
    defaultTypeName: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphNamedTypeFilter:
    filterType: Incomplete
    namedType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphProperty:
    name: Incomplete
    propertyType: Incomplete
    value: str
    merge: bool
    missingDataValue: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphPropertyValue:
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphQueryDefinition:
    name: Incomplete
    openCypherQuery: Incomplete
    provenanceBehavior: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphSearchDefinition:
    name: Incomplete
    searchString: Incomplete
    filterSetting: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphSearchFilterSetting:
    scope: Incomplete
    typeNames: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphSpatialMerge:
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphSubGraph:
    entityFilters: Incomplete
    relationshipFilters: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphTypeLookup:
    typeName: Incomplete
    properties: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphTypePropertyInfo:
    propertyName: Incomplete
    isVisible: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeLinkChartChronologicalLayoutSettings:
    timeDirection: Incomplete
    timeBannerUTCOffsetInMinutes: int
    eventsTicksVisualization: Incomplete
    showDurationLineForNonZeroDurationEntityEvents: bool
    durationLineWidth: int
    entityPositionAtDurationRatio: float
    showNonZeroDurationIntervalBounds: bool
    separateTimeOverlaps: bool
    separateTimelineOverlaps: bool
    moveFirstBends: bool
    secondBendRatio: float
    lineSeparationMultiplier: float
    spaceSeparatedLinesEvenly: bool
    useBezierCurves: bool
    separatedLineShapeRatio: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeLinkChartLayout:
    algorithm: Incomplete
    organicLayoutSettings: str
    chronologicalLayoutSettings: str
    autoApply: bool
    preserveExtent: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeLinkChartOrganicLayoutSettings:
    computationTimeBudget: float
    absoluteIdealEdgeLength: float
    multiplicativeIdealEdgeLength: float
    idealEdgeLengthType: Incomplete
    autoComputeRepulsionRadius: bool
    repulsionRadiusMultiplier: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeNonspatialDataDisplay:
    mode: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphDataConnection(CIMDataConnection):
    workspaceConnectionString: Incomplete
    workspaceFactory: Incomplete
    customWorkspaceFactoryCLSID: Incomplete
    dataset: Incomplete
    datasetType: Incomplete
    definitionQuery: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphInvestigation(CIMDefinition):
    dataConnection: str
    dataLoadingConfigurations: Incomplete
    searchDefinitions: Incomplete
    queryDefinitions: Incomplete
    filteredFindPathsConfigurations: Incomplete
    typeInfos: Incomplete
    customProperties: Incomplete
    dataModelVisualizations: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphLayer(CIMBaseLayer):
    standaloneTables: Incomplete
    dataConnection: str
    layers: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphTableDataConnection(CIMDataConnection):
    workspaceConnectionString: Incomplete
    workspaceFactory: Incomplete
    customWorkspaceFactoryCLSID: Incomplete
    dataset: Incomplete
    datasetType: Incomplete
    definitionQuery: Incomplete
    inclusionSetURI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLinkChartFeatureLayer(CIMGeoFeatureLayerBase):
    aggregationLayerURI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKGEntityType(CIMKGType):
    diagramPosition: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKGRelationshipType(CIMKGType):
    endpoints: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphCoordinatePropertyValue(CIMKnowledgeGraphPropertyValue):
    fieldNames: Incomplete
    spatialReference: Incomplete
    interpretAsLongitudeLatitude: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphExpressionPropertyValue(CIMKnowledgeGraphPropertyValue):
    expression: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphFieldPropertyValue(CIMKnowledgeGraphPropertyValue):
    fieldName: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphFixedPropertyValue(CIMKnowledgeGraphPropertyValue):
    fixedValue: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphIDPropertyValue(CIMKnowledgeGraphPropertyValue):
    dataLoadingItemName: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphNamedTypeFilterByInstances(CIMKnowledgeGraphNamedTypeFilter):
    instancesIDs: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphNamedTypeFilterByType(CIMKnowledgeGraphNamedTypeFilter):
    propertyFilterPredicate: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphNonspatialProperty(CIMKnowledgeGraphProperty):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphSpatialMergeIntersect(CIMKnowledgeGraphSpatialMerge):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphSpatialMergeWithinDistance(CIMKnowledgeGraphSpatialMerge):
    distance: float
    distanceUnit: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphSpatialMergeWithinDistanceGeodesic(CIMKnowledgeGraphSpatialMerge):
    distance: float
    distanceUnit: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphSpatialProperty(CIMKnowledgeGraphProperty):
    spatialReference: Incomplete
    geometryType: Incomplete
    keepAllWhenMerging: bool
    spatialMerge: str
    def __init__(self, *args, **Kwargs) -> None: ...
