from _typeshed import Incomplete
from arcpy.arcobjects._base import _ObjectWithoutInitCall

__all__ = ['Chart', 'Guide', 'Series', 'TimeBinningProperties', 'Bar', 'Box', 'CalendarHeat', 'DataClock', 'Histogram', 'Line', 'MatrixHeat', 'Pie', 'QQPlot', 'Scatter', 'ScatterMatrix', 'Combo']

class Chart(_ObjectWithoutInitCall):
    xAxis: Incomplete
    yAxis: Incomplete
    dataSource: Incomplete
    title: Incomplete
    description: Incomplete
    theme: Incomplete
    def __init__(self, name, title=None, description=None, xTitle=None, yTitle=None, dataSource=None, displaySize=None, theme=None, **kwargs) -> None: ...
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
            def new(self, name, valueFrom, valueTo=None, label=None): ...
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
        def listGuides(self, guideName=None): ...
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
    class _comboChart(_seriesType):
        def __init__(self, parent) -> None: ...
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
    def exportToSVG(self, path, width=None, height=None) -> None: ...
    def getPNG(self, width, height): ...
    def exportToPNG(self, path, width=None, height=None) -> None: ...
    def getJPEG(self, width, height): ...
    def exportToJPEG(self, path, width=None, height=None) -> None: ...
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
    def __init__(self, intervalSize=None, intervalUnits=None, timeAggregationType=None, trimIncompleteInterval=None, referenceTime=None) -> None: ...

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
    valueFromField: Incomplete
    valueFromFieldAggregationType: Incomplete
    symbolStyle: Incomplete
    symbolSize: Incomplete
    def __init__(self, guideType, *, name=None, label=None, valueFrom=None, valueTo=None, valueFromField=None, valueFromFieldAggregationType=None, polyline=None, lineColor=None, lineWidth=None, lineDashStyle=None, fillColor=None, symbolStyle=None, symbolSize=None) -> None: ...

class Series(_ObjectWithoutInitCall):
    y: Incomplete
    seriesType: Incomplete
    aggregation: Incomplete
    def __init__(self, y, seriesType=None, *, aggregation=None) -> None: ...

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
    def __init__(self, x, *, y=None, aggregation=None, splitCategory=None, multiSeriesDisplay=None, miniChartsPerRow=None, showPreviewChart=None, showMovingAverage=None, movingAveragePeriod=None, rotated=None, title=None, description=None, xTitle=None, yTitle=None, dataSource=None, displaySize=None, theme=None, timeBinningProperties=None, nullPolicy=None, **kwargs) -> None: ...
    sortSeries: Incomplete
    showNullCategory: Incomplete
    nullCategoryLabel: Incomplete
    nullCategoryColor: Incomplete

class Combo(Chart):
    type: str
    x: Incomplete
    seriesLeft: Incomplete
    seriesRight: Incomplete
    timeBinningProperties: Incomplete
    nullPolicy: Incomplete
    yAxisLeft: Incomplete
    yAxisRight: Incomplete
    def __init__(self, x, *, seriesLeft=None, seriesRight=None, title=None, description=None, xTitle=None, yTitleLeft=None, yTitleRight=None, dataSource=None, displaySize=None, theme=None, timeBinningProperties=None, nullPolicy=None, **kwargs) -> None: ...

class Box(Chart):
    type: str
    x: Incomplete
    y: Incomplete
    splitCategory: Incomplete
    splitCategoryAsMeanLine: Incomplete
    standardizeValues: Incomplete
    showOutliers: Incomplete
    rotated: Incomplete
    def __init__(self, y, *, x=None, splitCategory=None, splitCategoryAsMeanLine=None, standardizeValues=None, showOutliers=None, rotated=None, title=None, description=None, xTitle=None, yTitle=None, dataSource=None, displaySize=None, theme=None, **kwargs) -> None: ...
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
    def __init__(self, *, categoryField=None, numberFields=None, splitCategory=None, miniChartsPerRow=None, showPreviewChart=None, groupingPercent=None, donutSize=None, sort=None, showDataLabels=None, dataLabelsDisplay=None, title=None, description=None, dataSource=None, displaySize=None, theme=None, **kwargs) -> None: ...
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
    showMovingAverage: Incomplete
    movingAveragePeriod: Incomplete
    def __init__(self, x, *, y=None, splitCategory=None, multiSeriesDisplay=None, miniChartsPerRow=None, showPreviewChart=None, aggregation=None, timeIntervalUnits=None, timeIntervalSize=None, trimIncompleteTimeInterval=None, timeAggregationType=None, referenceTime=None, nullPolicy=None, showMovingAverage=None, movingAveragePeriod=None, rotated=None, title=None, description=None, xTitle=None, yTitle=None, dataSource=None, displaySize=None, theme=None, **kwargs) -> None: ...
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
    def __init__(self, x, *, splitCategory=None, miniChartsPerRow=None, showPreviewChart=None, binCount=None, showMean=None, showMedian=None, showStandardDeviation=None, showComparisonDistribution=None, dataTransformationType=None, dataTransformationParameters=None, title=None, description=None, xTitle=None, yTitle=None, dataSource=None, displaySize=None, theme=None, **kwargs) -> None: ...
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
    def __init__(self, x, y, *, splitCategory=None, sizeField=None, sizeMin=None, sizeMax=None, multiSeriesDisplay=None, miniChartsPerRow=None, showPreviewChart=None, showTrendLine=None, title=None, description=None, xTitle=None, yTitle=None, dataSource=None, displaySize=None, theme=None, **kwargs) -> None: ...
    sortSeries: Incomplete

class QQPlot(Chart):
    type: str
    x: Incomplete
    y: Incomplete
    showReferenceLine: Incomplete
    dataTransformationType: Incomplete
    dataTransformationParameters: Incomplete
    def __init__(self, x, *, y=None, showReferenceLine=None, dataTransformationType=None, dataTransformationParameters=None, title=None, description=None, xTitle=None, yTitle=None, dataSource=None, displaySize=None, theme=None, **kwargs) -> None: ...

class ScatterMatrix(Chart):
    type: str
    fields: Incomplete
    showTrendLine: Incomplete
    lowerLeft: Incomplete
    upperRight: Incomplete
    diagonal: Incomplete
    sort: Incomplete
    sortBy: Incomplete
    def __init__(self, fields, *, showTrendLine=None, lowerLeft=None, upperRight=None, diagonal=None, sort=None, sortBy=None, title=None, description=None, dataSource=None, displaySize=None, theme=None, **kwargs) -> None: ...

class DataClock(Chart):
    type: str
    dateField: Incomplete
    numberField: Incomplete
    timeUnitsRingWedge: Incomplete
    aggregation: Incomplete
    nullPolicy: Incomplete
    classificationMethod: Incomplete
    classCount: Incomplete
    def __init__(self, dateField, *, numberField=None, timeUnitsRingWedge=None, aggregation=None, nullPolicy=None, classificationMethod=None, classCount=None, title=None, description=None, dataSource=None, displaySize=None, theme=None, **kwargs) -> None: ...

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
    def __init__(self, dateField, *, numberField=None, calendarType=None, viewType=None, invertViews=None, includeLeapDay=None, aggregation=None, nullPolicy=None, classificationMethod=None, classCount=None, title=None, description=None, xTitle=None, yTitle=None, dataSource=None, displaySize=None, theme=None, **kwargs) -> None: ...

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
    def __init__(self, x, y, *, numberField=None, aggregation=None, nullPolicy=None, classificationMethod=None, classCount=None, title=None, description=None, xTitle=None, yTitle=None, dataSource=None, displaySize=None, theme=None, timeBinningPropertiesCol=None, timeBinningPropertiesRow=None, **kwargs) -> None: ...
