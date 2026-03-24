from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from .CIMDocument import CIMVersion as CIMVersion
from _typeshed import Incomplete

class CIMBAAreaOfInterest:
    areaOfInterestDataConnection: str
    areaOfInterestItems: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBAAreaOfInterestItem:
    name: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBABenchmarkComparisonsProperties:
    nameField: Incomplete
    siteAttributes: Incomplete
    variables: Incomplete
    addDifferenceField: bool
    addPercentDifferenceField: bool
    addAverageRow: bool
    addMedianRow: bool
    addStandardDeviationRow: bool
    isTableTransposed: bool
    benchmarkMethod: Incomplete
    topAndBottomType: Incomplete
    aboveAndBelowType: Incomplete
    highlightExtremesType: Incomplete
    topRecordsNumber: int
    bottomRecordsNumber: int
    benchmarkFeatureID: Incomplete
    numberOfQuantiles: int
    lowerExtremeLimit: float
    higherExtremeLimit: float
    mapVariable: Incomplete
    benchmarkStyle: Incomplete
    fillColor: str
    colorRamp: str
    outlineColor: str
    outlineSize: float
    aboveColor: str
    belowColor: str
    inBetweenColor: str
    quartile1Color: str
    quartile2Color: str
    quartile3Color: str
    quartile4Color: str
    topColor: str
    bottomColor: str
    geographyLevels: Incomplete
    neighboringGeographies: Incomplete
    dataSource: Incomplete
    resultsPaneSettings: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBAColorCodedLayerParameters:
    dataSource: Incomplete
    rendererProperties: str
    variable: Incomplete
    secondaryVariable: Incomplete
    areaOfInterest: str
    activeLevelOfDetail: Incomplete
    levelsOfDetail: Incomplete
    boundaryMode: Incomplete
    resultsPaneSettings: str
    activeLevelsGroup: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBALevelOfDetail:
    levelID: Incomplete
    dataConnection: str
    levelOfDetailDataConnection: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBANeighboringGeographyInfo:
    geographyLevelId: Incomplete
    itemIds: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBARendererProperties:
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBAResultsPaneSettings:
    matchTopBottomChartToLayerSymbology: bool
    histogramSubsetSelectionMethod: Incomplete
    histogramSubsetSelectionValue: int
    histogramBinCount: int
    histogramFillSymbolProperties: str
    tableSortDirection: Incomplete
    tableSortField: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBASuitabilityAnalysisCriterion:
    iD: Incomplete
    title: Incomplete
    valueField: Incomplete
    weight: int
    isEnabled: bool
    isLocked: bool
    influence: Incomplete
    min: int
    max: int
    idealValue: int
    targetValue: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBASuitabilityAnalysisLayer:
    suitabilityAnalysisSubLayer: str
    targetSite: str
    criteria: Incomplete
    presetMethod: Incomplete
    preprocessingMethod: Incomplete
    combinationMethod: Incomplete
    finalScoreScale: Incomplete
    rendererProperties: str
    classificationTransparency: int
    outlineColor: str
    outlineWidth: int
    resultsPaneSettings: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBASuitabilityAnalysisSubLayer:
    featureClassDataConnection: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBAVariableListVariable:
    names: Incomplete
    valueTypes: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMHuffModelAttractivenessVariable:
    name: Incomplete
    exponent: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMHuffModelDistanceParameters:
    exponent: int
    dataSource: Incomplete
    distanceUnits: Incomplete
    useTimeUnits: bool
    timeUnits: Incomplete
    useNetworkDistance: bool
    travelModeId: Incomplete
    towardsFacility: bool
    timeOfDay: Incomplete
    timeZone: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSegmentationProfile:
    name: Incomplete
    segmentationSystem: Incomplete
    segmentationBase: Incomplete
    hasVolumetricData: bool
    author: Incomplete
    creationDate: Incomplete
    lastRevisionDate: Incomplete
    counts: Incomplete
    volumetricValues: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSegmentationTarget:
    name: Incomplete
    segmentIDs: Incomplete
    color: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSegmentationTargetGroup:
    name: Incomplete
    segmentationSystem: Incomplete
    description: Incomplete
    author: Incomplete
    creationDate: Incomplete
    lastRevisionDate: Incomplete
    targets: Incomplete
    visualizationProperties: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSegmentationTargetGroupVisualizationProperties:
    targetProfile: str
    baseProfile: str
    thresholdIndex: int
    thresholdComposition: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBAVariableList(CIMVersion):
    name: Incomplete
    iconData: Incomplete
    author: Incomplete
    tags: Incomplete
    dataSource: Incomplete
    creationDate: Incomplete
    lastRevisionDate: Incomplete
    variables: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMHuffModelCalibrationDocument(CIMVersion):
    rMSError: int
    rMSErrorLinear: int
    attractivenessVariables: Incomplete
    distanceParameters: str
    facilities: str
    facilitiesIDFieldName: Incomplete
    customers: str
    customersIDFieldName: Incomplete
    customerWeightFieldName: Incomplete
    salesPotential: str
    salesPotentialIDFieldName: Incomplete
    author: Incomplete
    creationDate: Incomplete
    lastRevisionDate: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSegmentationProfileDocument(CIMVersion):
    profile: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSegmentationTargetGroupDocument(CIMVersion):
    targetGroup: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBABenchmarkComparisonsResultsPaneSettings(CIMBAResultsPaneSettings):
    statisticsVariable: Incomplete
    histogramVariable: Incomplete
    showRegressionLineOnScatterplot: bool
    scatterplotChartType: Incomplete
    scatterplotXAxisField: Incomplete
    scatterplotYAxisField: Incomplete
    scatterplotDotSizeField: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBABivariateColorsRendererProperties(CIMBARendererProperties):
    gridSize: Incomplete
    orientationType: Incomplete
    classificationMethod: Incomplete
    colorRamp: str
    classificationFields: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBAColorCodedLayerResultsPaneSettings(CIMBAResultsPaneSettings):
    histogramVariable: Incomplete
    showRegressionLineOnScatterplot: bool
    scatterplotXAxisVariableName: Incomplete
    scatterplotYAxisVariableName: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBAFeatureClassAreaOfInterestItem(CIMBAAreaOfInterestItem):
    dataConnection: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBAFeatureLayerAreaOfInterestItem(CIMBAAreaOfInterestItem):
    uRI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBAFieldBasedCriterion(CIMBASuitabilityAnalysisCriterion):
    fieldName: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBAGraduatedColorsRendererProperties(CIMBARendererProperties):
    numBreaks: int
    classificationMethod: Incomplete
    standardDeviationMultiplier: Incomplete
    colorRamp: str
    classificationField: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBAGraduatedSymbolsRendererProperties(CIMBARendererProperties):
    numBreaks: int
    classificationMethod: Incomplete
    minSymbolSize: int
    maxSymbolSize: int
    standardDeviationMultiplier: Incomplete
    colorRamp: str
    templateColor: str
    classificationFields: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBAPointLayerBasedCriterion(CIMBASuitabilityAnalysisCriterion):
    dataSource: Incomplete
    siteLayerIdField: Incomplete
    pointLayerDataConnection: str
    pointCriterionType: Incomplete
    weightField: Incomplete
    statisticsType: Incomplete
    distanceUnits: Incomplete
    useTimeUnits: bool
    timeUnits: Incomplete
    travelModeId: Incomplete
    useNetworkDistance: bool
    siteCentersLayerDataConnection: str
    siteCentersLayerId: Incomplete
    cutoffDistance: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBAStdGeoAreaOfInterestItem(CIMBAAreaOfInterestItem):
    levelID: Incomplete
    geographyID: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBASuitabilityAnalysisResultsPaneSettings(CIMBAResultsPaneSettings):
    histogramCriterionID: Incomplete
    showRegressionLineOnScatterplot: bool
    scatterplotChartType: Incomplete
    scatterplotXAxisCriterionID: Incomplete
    scatterplotYAxisCriterionID: Incomplete
    scatterplotDotSizeCriterionID: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBASuitabilityAnalysisTargetSiteSubLayer(CIMBASuitabilityAnalysisSubLayer):
    sourceTargetSiteDataConnection: str
    selectedSourceTargetSiteObjectID: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBAUnclassedColorsRendererProperties(CIMBARendererProperties):
    colorRamp: str
    classificationField: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBAUniqueValueRendererProperties(CIMBARendererProperties):
    colorRamp: str
    classificationField: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBAVariableBasedCriterion(CIMBASuitabilityAnalysisCriterion):
    dataSource: Incomplete
    variable: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...
