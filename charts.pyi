from _typeshed import Incomplete
from arcpy.arcobjects._base import _ObjectWithoutInitCall

__all__ = ['Chart', 'Guide', 'TimeBinningProperties', 'Bar', 'Box', 'CalendarHeat', 'DataClock', 'Histogram', 'Line', 'MatrixHeat', 'Pie', 'QQPlot', 'Scatter', 'ScatterMatrix']

class Chart(_ObjectWithoutInitCall):
    xAxis: Incomplete
    yAxis: Incomplete
    dataSource: Incomplete
    title: Incomplete
    description: Incomplete
    theme: Incomplete
    def __init__(self, name, title: Incomplete | None = None, description: Incomplete | None = None, xTitle: Incomplete | None = None, yTitle: Incomplete | None = None, dataSource: Incomplete | None = None, displaySize: Incomplete | None = None, theme: Incomplete | None = None) -> None: ...
    color: Incomplete
    enableServerSideProcessing: Incomplete
    class _arc_base:
        def __init__(self, parent) -> None: ...
    class _seriesType(_arc_base):
        def __init__(self, parent) -> None: ...
    class _axis(_arc_base):
        class _guide:
            name: Incomplete
            valueFrom: Incomplete
            valueTo: Incomplete
            label: Incomplete
            def __init__(self, _name) -> None: ...
        class _Guides:
            def new(self, name, valueFrom, valueTo: Incomplete | None = None, label: Incomplete | None = None): ...
            def get(self, index): ...
            def update(self, _guides) -> None: ...
            def remove(self, guide) -> None: ...
            def removeByIndex(self, index) -> None: ...
            def removeAll(self) -> None: ...
            def length(self): ...
            def __init__(self, axis) -> None: ...
        title: Incomplete
        field: Incomplete
        sort: Incomplete
        minimum: Incomplete
        maximum: Incomplete
        logarithmic: Incomplete
        useAdaptiveBounds: Incomplete
        invert: Incomplete
        def addGuide(self, guide): ...
        def removeGuide(self, guide): ...
        def listGuides(self, guideName: Incomplete | None = None): ...
        axisId: Incomplete
        guides: Incomplete
        def __init__(self, parent, i) -> None: ...
    class _bar(_seriesType):
        def __init__(self, parent) -> None: ...
        aggregation: Incomplete
        splitCategory: Incomplete
        multiSeriesDisplay: Incomplete
        rotated: Incomplete
        showMovingAverage: Incomplete
        movingAveragePeriod: Incomplete
    class _scatterPlot(_seriesType):
        def __init__(self, parent) -> None: ...
        showTrendLine: Incomplete
        bubbleMinSize: Incomplete
        bubbleMaxSize: Incomplete
    class _qqPlot(_seriesType):
        def __init__(self, parent) -> None: ...
        showReferenceLine: Incomplete
        dataTransformationType: Incomplete
    class _line(_seriesType):
        def __init__(self, parent) -> None: ...
        aggregation: Incomplete
        splitCategory: Incomplete
        timeIntervalUnits: Incomplete
        timeIntervalSize: Incomplete
        trimIncompleteTimeInterval: Incomplete
        timeAggregationType: Incomplete
        nullPolicy: Incomplete
        rotated: Incomplete
    class _histogram(_seriesType):
        def __init__(self, parent) -> None: ...
        binCount: Incomplete
        showMean: Incomplete
        showMedian: Incomplete
        showStandardDeviation: Incomplete
        showComparisonDistribution: Incomplete
        dataTransformationType: Incomplete
    class _boxPlot(_seriesType):
        def __init__(self, parent) -> None: ...
        showOutliers: Incomplete
        standardizeValues: Incomplete
        splitCategory: Incomplete
        splitCategoryAsMeanLine: Incomplete
        rotated: Incomplete
    class _dataClock(_seriesType):
        def __init__(self, parent) -> None: ...
        aggregation: Incomplete
        timeUnitsRingWedge: Incomplete
        nullPolicy: Incomplete
        classificationMethod: Incomplete
        classCount: Incomplete
    class _calendarHeatChart(_seriesType):
        def __init__(self, parent) -> None: ...
        aggregation: Incomplete
        calendarType: Incomplete
        nullPolicy: Incomplete
        classificationMethod: Incomplete
        classCount: Incomplete
        includeLeapDay: Incomplete
    class _matrixHeatChart(_seriesType):
        def __init__(self, parent) -> None: ...
        aggregation: Incomplete
        nullPolicy: Incomplete
        classificationMethod: Incomplete
        classCount: Incomplete
    class _scatterPlotMatrix(_seriesType):
        def __init__(self, parent) -> None: ...
        fields: Incomplete
        showTrendLine: Incomplete
        showHistograms: Incomplete
        showAsRSquared: Incomplete
    class _pie(_seriesType):
        def __init__(self, parent) -> None: ...
        categoryField: Incomplete
        numberFields: Incomplete
        donutSize: Incomplete
        groupingPercent: Incomplete
        sort: Incomplete
    class _legend(_arc_base):
        def __init__(self, parent) -> None: ...
        visible: Incomplete
        title: Incomplete
        alignment: Incomplete
    @property
    def type(self): ...
    @type.setter
    def type(self, val) -> None: ...
    @property
    def legend(self): ...
    def getSVG(self, width, height): ...
    def exportToSVG(self, path, width: Incomplete | None = None, height: Incomplete | None = None) -> None: ...
    def addToLayer(self, layer_or_layerfile): ...
    def updateChart(self): ...
    @property
    def displaySize(self): ...
    @displaySize.setter
    def displaySize(self, val) -> None: ...

class TimeBinningProperties(_ObjectWithoutInitCall):
    intervalSize: Incomplete
    intervalUnits: Incomplete
    timeAggregationType: Incomplete
    referenceTime: Incomplete
    trimIncompleteInterval: Incomplete
    def __init__(self, intervalSize: Incomplete | None = None, intervalUnits: Incomplete | None = None, timeAggregationType: Incomplete | None = None, trimIncompleteInterval: Incomplete | None = None, referenceTime: Incomplete | None = None) -> None: ...

class Guide(_ObjectWithoutInitCall):
    guideType: Incomplete
    name: Incomplete
    label: Incomplete
    valueFrom: Incomplete
    valueTo: Incomplete
    polyline: Incomplete
    fillColor: Incomplete
    lineColor: Incomplete
    lineWidth: Incomplete
    lineDashStyle: Incomplete
    def __init__(self, guideType, *, name: Incomplete | None = None, label: Incomplete | None = None, valueFrom: Incomplete | None = None, valueTo: Incomplete | None = None, polyline: Incomplete | None = None, lineColor: Incomplete | None = None, lineWidth: Incomplete | None = None, lineDashStyle: Incomplete | None = None, fillColor: Incomplete | None = None) -> None: ...

class Bar(Chart):
    type: str
    x: Incomplete
    y: Incomplete
    aggregation: Incomplete
    splitCategory: Incomplete
    multiSeriesDisplay: Incomplete
    miniChartsPerRow: Incomplete
    showPreviewChart: Incomplete
    showMovingAverage: Incomplete
    movingAveragePeriod: Incomplete
    rotated: Incomplete
    timeBinningProperties: Incomplete
    nullPolicy: Incomplete
    def __init__(self, x, *, y: Incomplete | None = None, aggregation: Incomplete | None = None, splitCategory: Incomplete | None = None, multiSeriesDisplay: Incomplete | None = None, miniChartsPerRow: Incomplete | None = None, showPreviewChart: Incomplete | None = None, showMovingAverage: Incomplete | None = None, movingAveragePeriod: Incomplete | None = None, rotated: Incomplete | None = None, title: Incomplete | None = None, description: Incomplete | None = None, xTitle: Incomplete | None = None, yTitle: Incomplete | None = None, dataSource: Incomplete | None = None, displaySize: Incomplete | None = None, theme: Incomplete | None = None, timeBinningProperties: Incomplete | None = None, nullPolicy: Incomplete | None = None) -> None: ...
    sortSeries: Incomplete
    showNullCategory: Incomplete
    nullCategoryLabel: Incomplete
    nullCategoryColor: Incomplete

class Box(Chart):
    type: str
    x: Incomplete
    y: Incomplete
    splitCategory: Incomplete
    splitCategoryAsMeanLine: Incomplete
    standardizeValues: Incomplete
    showOutliers: Incomplete
    rotated: Incomplete
    def __init__(self, y, *, x: Incomplete | None = None, splitCategory: Incomplete | None = None, splitCategoryAsMeanLine: Incomplete | None = None, standardizeValues: Incomplete | None = None, showOutliers: Incomplete | None = None, rotated: Incomplete | None = None, title: Incomplete | None = None, description: Incomplete | None = None, xTitle: Incomplete | None = None, yTitle: Incomplete | None = None, dataSource: Incomplete | None = None, displaySize: Incomplete | None = None, theme: Incomplete | None = None) -> None: ...
    sortSeries: Incomplete

class Pie(Chart):
    type: str
    categoryField: Incomplete
    numberFields: Incomplete
    splitCategory: Incomplete
    miniChartsPerRow: Incomplete
    showPreviewChart: Incomplete
    groupingPercent: Incomplete
    donutSize: Incomplete
    sort: Incomplete
    showDataLabels: Incomplete
    dataLabelsDisplay: Incomplete
    def __init__(self, *, categoryField: Incomplete | None = None, numberFields: Incomplete | None = None, splitCategory: Incomplete | None = None, miniChartsPerRow: Incomplete | None = None, showPreviewChart: Incomplete | None = None, groupingPercent: Incomplete | None = None, donutSize: Incomplete | None = None, sort: Incomplete | None = None, showDataLabels: Incomplete | None = None, dataLabelsDisplay: Incomplete | None = None, title: Incomplete | None = None, description: Incomplete | None = None, dataSource: Incomplete | None = None, displaySize: Incomplete | None = None, theme: Incomplete | None = None) -> None: ...
    sortSeries: Incomplete

class Line(Chart):
    type: str
    x: Incomplete
    y: Incomplete
    splitCategory: Incomplete
    multiSeriesDisplay: Incomplete
    miniChartsPerRow: Incomplete
    showPreviewChart: Incomplete
    aggregation: Incomplete
    timeAggregationType: Incomplete
    referenceTime: Incomplete
    timeIntervalUnits: Incomplete
    timeIntervalSize: Incomplete
    trimIncompleteTimeInterval: Incomplete
    nullPolicy: Incomplete
    rotated: Incomplete
    def __init__(self, x, *, y: Incomplete | None = None, splitCategory: Incomplete | None = None, multiSeriesDisplay: Incomplete | None = None, miniChartsPerRow: Incomplete | None = None, showPreviewChart: Incomplete | None = None, aggregation: Incomplete | None = None, timeIntervalUnits: Incomplete | None = None, timeIntervalSize: Incomplete | None = None, trimIncompleteTimeInterval: Incomplete | None = None, timeAggregationType: Incomplete | None = None, referenceTime: Incomplete | None = None, nullPolicy: Incomplete | None = None, rotated: Incomplete | None = None, title: Incomplete | None = None, description: Incomplete | None = None, xTitle: Incomplete | None = None, yTitle: Incomplete | None = None, dataSource: Incomplete | None = None, displaySize: Incomplete | None = None, theme: Incomplete | None = None) -> None: ...
    sortSeries: Incomplete

class Histogram(Chart):
    type: str
    x: Incomplete
    splitCategory: Incomplete
    miniChartsPerRow: Incomplete
    showPreviewChart: Incomplete
    binCount: Incomplete
    showMean: Incomplete
    showMedian: Incomplete
    showStandardDeviation: Incomplete
    showComparisonDistribution: Incomplete
    dataTransformationType: Incomplete
    dataTransformationParameters: Incomplete
    def __init__(self, x, *, splitCategory: Incomplete | None = None, miniChartsPerRow: Incomplete | None = None, showPreviewChart: Incomplete | None = None, binCount: Incomplete | None = None, showMean: Incomplete | None = None, showMedian: Incomplete | None = None, showStandardDeviation: Incomplete | None = None, showComparisonDistribution: Incomplete | None = None, dataTransformationType: Incomplete | None = None, dataTransformationParameters: Incomplete | None = None, title: Incomplete | None = None, description: Incomplete | None = None, xTitle: Incomplete | None = None, yTitle: Incomplete | None = None, dataSource: Incomplete | None = None, displaySize: Incomplete | None = None, theme: Incomplete | None = None) -> None: ...
    sortSeries: Incomplete

class Scatter(Chart):
    type: str
    x: Incomplete
    y: Incomplete
    splitCategory: Incomplete
    sizeField: Incomplete
    sizeMin: Incomplete
    sizeMax: Incomplete
    multiSeriesDisplay: Incomplete
    miniChartsPerRow: Incomplete
    showPreviewChart: Incomplete
    showTrendLine: Incomplete
    def __init__(self, x, y, *, splitCategory: Incomplete | None = None, sizeField: Incomplete | None = None, sizeMin: Incomplete | None = None, sizeMax: Incomplete | None = None, multiSeriesDisplay: Incomplete | None = None, miniChartsPerRow: Incomplete | None = None, showPreviewChart: Incomplete | None = None, showTrendLine: Incomplete | None = None, title: Incomplete | None = None, description: Incomplete | None = None, xTitle: Incomplete | None = None, yTitle: Incomplete | None = None, dataSource: Incomplete | None = None, displaySize: Incomplete | None = None, theme: Incomplete | None = None) -> None: ...
    sortSeries: Incomplete

class QQPlot(Chart):
    type: str
    x: Incomplete
    y: Incomplete
    showReferenceLine: Incomplete
    dataTransformationType: Incomplete
    dataTransformationParameters: Incomplete
    def __init__(self, x, *, y: Incomplete | None = None, showReferenceLine: Incomplete | None = None, dataTransformationType: Incomplete | None = None, dataTransformationParameters: Incomplete | None = None, title: Incomplete | None = None, description: Incomplete | None = None, xTitle: Incomplete | None = None, yTitle: Incomplete | None = None, dataSource: Incomplete | None = None, displaySize: Incomplete | None = None, theme: Incomplete | None = None) -> None: ...

class ScatterMatrix(Chart):
    type: str
    fields: Incomplete
    showTrendLine: Incomplete
    lowerLeft: Incomplete
    upperRight: Incomplete
    diagonal: Incomplete
    sort: Incomplete
    sortBy: Incomplete
    def __init__(self, fields, *, showTrendLine: Incomplete | None = None, lowerLeft: Incomplete | None = None, upperRight: Incomplete | None = None, diagonal: Incomplete | None = None, sort: Incomplete | None = None, sortBy: Incomplete | None = None, title: Incomplete | None = None, description: Incomplete | None = None, dataSource: Incomplete | None = None, displaySize: Incomplete | None = None, theme: Incomplete | None = None) -> None: ...

class DataClock(Chart):
    type: str
    dateField: Incomplete
    numberField: Incomplete
    timeUnitsRingWedge: Incomplete
    aggregation: Incomplete
    nullPolicy: Incomplete
    classificationMethod: Incomplete
    classCount: Incomplete
    def __init__(self, dateField, *, numberField: Incomplete | None = None, timeUnitsRingWedge: Incomplete | None = None, aggregation: Incomplete | None = None, nullPolicy: Incomplete | None = None, classificationMethod: Incomplete | None = None, classCount: Incomplete | None = None, title: Incomplete | None = None, description: Incomplete | None = None, dataSource: Incomplete | None = None, displaySize: Incomplete | None = None, theme: Incomplete | None = None) -> None: ...

class CalendarHeat(Chart):
    type: str
    dateField: Incomplete
    numberField: Incomplete
    calendarType: Incomplete
    viewType: Incomplete
    invertViews: Incomplete
    includeLeapDay: Incomplete
    aggregation: Incomplete
    nullPolicy: Incomplete
    classificationMethod: Incomplete
    classCount: Incomplete
    def __init__(self, dateField, *, numberField: Incomplete | None = None, calendarType: Incomplete | None = None, viewType: Incomplete | None = None, invertViews: Incomplete | None = None, includeLeapDay: Incomplete | None = None, aggregation: Incomplete | None = None, nullPolicy: Incomplete | None = None, classificationMethod: Incomplete | None = None, classCount: Incomplete | None = None, title: Incomplete | None = None, description: Incomplete | None = None, xTitle: Incomplete | None = None, yTitle: Incomplete | None = None, dataSource: Incomplete | None = None, displaySize: Incomplete | None = None, theme: Incomplete | None = None) -> None: ...

class MatrixHeat(Chart):
    type: str
    x: Incomplete
    y: Incomplete
    numberField: Incomplete
    aggregation: Incomplete
    nullPolicy: Incomplete
    classificationMethod: Incomplete
    classCount: Incomplete
    timeBinningPropertiesCol: Incomplete
    timeBinningPropertiesRow: Incomplete
    def __init__(self, x, y, *, numberField: Incomplete | None = None, aggregation: Incomplete | None = None, nullPolicy: Incomplete | None = None, classificationMethod: Incomplete | None = None, classCount: Incomplete | None = None, title: Incomplete | None = None, description: Incomplete | None = None, xTitle: Incomplete | None = None, yTitle: Incomplete | None = None, dataSource: Incomplete | None = None, displaySize: Incomplete | None = None, theme: Incomplete | None = None, timeBinningPropertiesCol: Incomplete | None = None, timeBinningPropertiesRow: Incomplete | None = None) -> None: ...
