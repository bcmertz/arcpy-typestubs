from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from _typeshed import Incomplete

class CIMChart:
    name: Incomplete
    series: Incomplete
    generalProperties: str
    legend: str
    axes: Incomplete
    mapSelectionHandling: Incomplete
    metaData: Incomplete
    multiSeriesChartProperties: str
    enableServerSideProcessing: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartAxis:
    visible: bool
    isLogarithmic: bool
    title: Incomplete
    showTitle: bool
    useAutomaticTitle: bool
    valueFormat: Incomplete
    valueNumberFormat: str
    dateTimeFormat: Incomplete
    calculateAutomaticMinimum: bool
    calculateAutomaticMaximum: bool
    minimum: Incomplete
    maximum: Incomplete
    titleText: str
    labelText: str
    axisLineSymbolProperties: str
    guides: Incomplete
    labelCharacterLimit: int
    zoomStartPosition: float
    zoomEndPosition: float
    inverted: bool
    labelAngle: float
    useAutomaticLabelAngle: bool
    useAutomaticInterval: bool
    interval: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartDimensionalProfileBand:
    bandID: int
    symbol: str
    label: Incomplete
    locationID: int
    dimension: Incomplete
    dimensionValues: Incomplete
    dimensionValuesSymbols: Incomplete
    dimensionValuesLabels: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartDimensionalProfileBands:
    variable: Incomplete
    bands: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartDimensionalProfileCCDCArguments:
    temporalMaskBandIDs: Incomplete
    updatingFrequency: Incomplete
    chiSquaredThreshold: Incomplete
    minimumAnomaly: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartDimensionalProfileDimensionValue:
    value: Incomplete
    symbol: str
    label: Incomplete
    locationID: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartDimensionalProfileDimensionValues:
    variable: Incomplete
    dimension: Incomplete
    values: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartDimensionalProfileLandTrendrArguments:
    snappingDate: Incomplete
    maximumSegments: int
    vertexCountOvershoot: int
    spikeThreshold: Incomplete
    recoveryThreshold: Incomplete
    preventOneYearRecovery: bool
    recoveryIncreasingTrend: bool
    outputOtherBands: bool
    minimumObservations: int
    bestModelProportion: Incomplete
    pValueThreshold: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartDimensionalProfileVariable:
    name: Incomplete
    symbol: str
    label: Incomplete
    dimension: Incomplete
    dimensionValues: Incomplete
    dimensionValuesSymbols: Incomplete
    dimensionValuesLabels: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartFillSymbolProperties:
    color: str
    opacity: int
    lineSymbolProperties: str
    visible: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartGeneralProperties:
    title: Incomplete
    showTitle: bool
    useAutomaticTitle: bool
    subTitle: Incomplete
    showSubTitle: bool
    footer: Incomplete
    showFooter: bool
    theme: Incomplete
    titleText: str
    subTitleText: str
    footerText: str
    backgroundSymbolProperties: str
    gridLineSymbolProperties: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartGuide:
    name: Incomplete
    label: Incomplete
    labelText: str
    labelPosition: Incomplete
    valueFrom: float
    valueTo: float
    timeFrom: Incomplete
    timeTo: Incomplete
    visible: bool
    guideType: Incomplete
    guideValueType: Incomplete
    fillSymbolProperties: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartLegend:
    visible: bool
    title: Incomplete
    showTitle: bool
    alignment: Incomplete
    valueFormat: Incomplete
    legendText: str
    legendTitle: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartLineSymbolProperties:
    visible: bool
    width: int
    style: Incomplete
    color: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartLocationDefinition:
    geometry: Incomplete
    symbol: str
    label: Incomplete
    enabled: bool
    mapLocationSymbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartMarkerSymbolProperties:
    visible: bool
    width: int
    height: int
    style: Incomplete
    color: str
    lineSymbolProperties: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartPieSlice:
    value: Incomplete
    symbol: str
    label: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartSeries:
    name: Incomplete
    uniqueName: Incomplete
    fields: Incomplete
    orderFields: Incomplete
    groupFields: Incomplete
    whereClause: Incomplete
    showLabels: bool
    horizontalAxis: int
    verticalAxis: int
    colorType: Incomplete
    fieldAggregation: Incomplete
    orderFieldsSortTypes: Incomplete
    visible: bool
    dataLabelText: str
    multiSeries: bool
    locations: Incomplete
    fieldExpressions: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartSurfaceProfileBand:
    bandID: int
    symbol: str
    label: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartSurfaceProfileDimensionValue:
    value: Incomplete
    time: Incomplete
    symbol: str
    label: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartSurfaceProfileDimensionValues:
    variable: Incomplete
    values: Incomplete
    dimension: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartSurfaceProfileLayer:
    uRI: Incomplete
    bandID: int
    symbol: str
    label: Incomplete
    dimensionValue: Incomplete
    time: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartTextProperties:
    fontFillColor: str
    fontOutlineColor: str
    fontFamilyName: Incomplete
    fontItalic: bool
    fontSize: int
    fontWeight: Incomplete
    textCase: Incomplete
    textUnderline: bool
    textStrikethrough: bool
    textOverline: bool
    visible: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartTimeBinningProperties:
    timeAggregationType: Incomplete
    referenceTime: Incomplete
    timeIntervalUnits: Incomplete
    timeIntervalSize: float
    calculateAutomaticTimeInterval: bool
    trimIncompleteTimeInterval: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartTrajectoryProfileFeature:
    iD: int
    symbol: str
    label: Incomplete
    enabled: bool
    trajectoryID: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartTrajectoryProfileLayer:
    uRI: Incomplete
    iD: int
    symbol: str
    label: Incomplete
    enabled: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartTrajectoryProfileVariable:
    name: Incomplete
    symbol: str
    label: Incomplete
    enabled: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGridChartProperties:
    miniChartsPerRow: int
    selectedMiniChart: int
    showPreviewChart: bool
    useSeriesMinMaxForAxisX: bool
    useSeriesMinMaxForAxisY: bool
    selectionLineSymbolProperties: str
    miniChartOutlineSymbolProperties: str
    miniChartTitleText: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMultiSeriesChartProperties:
    enabled: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartBarSeries(CIMChartSeries):
    multipleBarType: Incomplete
    barSize: int
    fillSymbolProperties: str
    verticalOrientation: bool
    sortedCategoryValues: Incomplete
    showMovingAverage: bool
    movingAverageLineSymbolProperties: str
    movingAveragePeriod: int
    timeBinningProperties: str
    nullPolicy: Incomplete
    matchLayerSymbology: bool
    showNullCategory: bool
    nullCategoryFillSymbolProperties: str
    nullCategoryLabel: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartBoxPlotSeries(CIMChartSeries):
    fillSymbolProperties: str
    verticalOrientation: bool
    showOutliers: bool
    showInnerPoints: bool
    showMean: bool
    standardizeValues: bool
    sortedCategoryValues: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartCalendarHeatSeries(CIMChartSeries):
    columnTimeUnits: Incomplete
    rowTimeUnits: Incomplete
    nullPolicy: Incomplete
    noDataColor: str
    classificationMethod: Incomplete
    breaksCount: int
    minimumBreak: float
    breaks: Incomplete
    breakColors: Incomplete
    colorRamp: str
    includeLeapDay: bool
    aggregateCalendarView: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartDataClockSeries(CIMChartSeries):
    wedgeTimeUnits: Incomplete
    ringTimeUnits: Incomplete
    trimIncompleteTimeInterval: bool
    nullPolicy: Incomplete
    noDataColor: str
    classificationMethod: Incomplete
    breaksCount: int
    minimumBreak: float
    breaks: Incomplete
    breakColors: Incomplete
    colorRamp: str
    showWedgeLabel: bool
    wedgeLabelText: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartDimensionalProfileSeries(CIMChartSeries):
    plotType: Incomplete
    variables: Incomplete
    bands: str
    dimensionValues: str
    standardizeValues: bool
    timeIntervalSize: float
    timeIntervalUnits: Incomplete
    timeAggregationType: Incomplete
    trimIncompleteTimeInterval: bool
    dateTimeFormat: Incomplete
    trendLineSymbolProperties: str
    showTrendLine: bool
    trendLineFitType: Incomplete
    trendOrder: int
    showTrendEquation: bool
    spatialAggregationType: Incomplete
    cCDCArguments: str
    landTrendrArguments: str
    timeExtent: Incomplete
    verticalOrientation: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartHistogramSeries(CIMChartSeries):
    binCount: int
    showMean: bool
    showMedian: bool
    showStandardDeviation: bool
    fillSymbolProperties: str
    meanLineSymbolProperties: str
    medianLineSymbolProperties: str
    standardDeviationLineSymbolProperties: str
    showComparisonDistribution: bool
    dataTransformationType: Incomplete
    dataTransformationParameters: Incomplete
    distributionLineSymbolProperties: str
    countField: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartLineSeries(CIMChartSeries):
    lineSymbolProperties: str
    markerSymbolProperties: str
    timeAggregationType: Incomplete
    referenceTime: Incomplete
    timeIntervalUnits: Incomplete
    timeIntervalSize: float
    calculateAutomaticTimeInterval: bool
    trimIncompleteTimeInterval: bool
    nullPolicy: Incomplete
    verticalOrientation: bool
    sortedCategoryValues: Incomplete
    smoothLine: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartMatrixHeatSeries(CIMChartSeries):
    nullPolicy: Incomplete
    noDataColor: str
    classificationMethod: Incomplete
    breaksCount: int
    minimumBreak: float
    breaks: Incomplete
    breakColors: Incomplete
    colorRamp: str
    columnSortedCategoryValues: Incomplete
    rowSortedCategoryValues: Incomplete
    rowsTimeBinningProperties: str
    columnsTimeBinningProperties: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartPieSeries(CIMChartSeries):
    sliceAggregationThreshold: float
    holePercentage: float
    showLabelValue: bool
    showLabelPercentage: bool
    percentageDecimalPlaces: int
    slices: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartProbabilityPlotSeries(CIMChartSeries):
    probabilityPlotType: Incomplete
    dataTransformationType: Incomplete
    dataTransformationParameters: Incomplete
    showReferenceLine: bool
    markerSymbolProperties: str
    referenceLineSymbolProperties: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartProfileGraphSeries(CIMChartSeries):
    lineSymbolProperties: str
    markerSymbolProperties: str
    horizontalUnit: Incomplete
    verticalUnit: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartScatterPlotMatrixSeries(CIMChartSeries):
    showHistograms: bool
    showTrendLine: bool
    showAsRSquared: bool
    fieldLabels: Incomplete
    scatterMarkerSymbolProperties: str
    trendLineSymbolProperties: str
    histogramFillSymbolProperties: str
    selectedMiniPlot: int
    rSquareText: str
    selectionLineSymbolProperties: str
    displayOption: Incomplete
    lowerLeftDisplayOption: Incomplete
    lowerLeftColorRamp: str
    lowerLeftBreakColors: Incomplete
    upperRightColorRamp: str
    upperRightBreakColors: Incomplete
    diagonalOption: Incomplete
    sortByType: Incomplete
    sortDirection: Incomplete
    trendLineFitType: Incomplete
    trendOrder: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartScatterSeries(CIMChartSeries):
    markerSymbolProperties: str
    showTrendLine: bool
    trendLineSymbolProperties: str
    trendLineFitType: Incomplete
    trendOrder: int
    showTrendEquation: bool
    bubbleMinimumSize: float
    bubbleMaximumSize: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartSpectralProfileSeries(CIMChartSeries):
    displayMode: Incomplete
    showOutliers: bool
    standardizeValues: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartSurfaceProfileSeries(CIMChartSeries):
    plotType: Incomplete
    sampleDistance: Incomplete
    bands: Incomplete
    dimensionValues: str
    layers: Incomplete
    horizontalUnit: Incomplete
    verticalScale: float
    variable: Incomplete
    dimension: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartTrajectoryProfileSeries(CIMChartSeries):
    plotType: Incomplete
    variables: Incomplete
    features: Incomplete
    layers: Incomplete
    timeIntervalSize: float
    timeIntervalUnits: Incomplete
    timeAggregationType: Incomplete
    trimIncompleteTimeInterval: bool
    dateTimeFormat: Incomplete
    areaOfInterestURI: Incomplete
    verticalOrientation: bool
    trajectoryIDsURI: Incomplete
    nullPolicy: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...
