from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from .CIMCore import CIMDefinition as CIMDefinition
from .CIMLayer import CIMBaseLayer as CIMBaseLayer
from .CIMVectorLayers import CIMDataConnection as CIMDataConnection, CIMGeoFeatureLayerBase as CIMGeoFeatureLayerBase
from _typeshed import Incomplete

class CIMFilteredFindPathsConfiguration:
    name: Incomplete
    originEntities: Incomplete
    destinationEntities: Incomplete
    pathFilters: Incomplete
    defaultTraversalDirectionType: Incomplete
    traversalDirections: Incomplete
    entityUsage: Incomplete
    pathMode: Incomplete
    minPathLength: int
    maxPathLength: int
    maxCountPaths: int
    timeFilter: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFilteredFindPathsEntity:
    iD: Incomplete
    entityTypeName: Incomplete
    propertyFilterPredicate: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFilteredFindPathsPathFilter:
    iD: Incomplete
    itemTypeName: Incomplete
    itemType: Incomplete
    filterType: Incomplete
    propertyFilterPredicate: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKGConsecutiveEventsRestrictions:
    restrictMaxOverlap: bool
    maxOverlap: int
    maxOverlapUnit: Incomplete
    restrictMaxGap: bool
    maxGap: int
    maxGapUnit: Incomplete
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

class CIMKnowledgeGraphDataLoadingConfiguration:
    name: Incomplete
    entities: Incomplete
    relationships: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphDataLoadingEntity:
    name: Incomplete
    entityType: Incomplete
    typeIsFieldName: bool
    entityTypeExpression: str
    properties: Incomplete
    merge: bool
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
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphLinkChartCentralityConfiguration:
    relationshipsInterpretation: Incomplete
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

class CIMKnowledgeGraphProperty:
    name: Incomplete
    propertyType: Incomplete
    value: str
    merge: bool
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
    scope: str
    typeNames: Incomplete
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

class CIMKnowledgeGraphNonspatialProperty(CIMKnowledgeGraphProperty):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKnowledgeGraphSpatialProperty(CIMKnowledgeGraphProperty):
    spatialReference: Incomplete
    geometryType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...
