from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from .CIMCore import CIMDefinition as CIMDefinition
from .CIMDocument import CIMVersion as CIMVersion, CIMView as CIMView
from _typeshed import Incomplete

class CIMAutoCamera:
    camera: str
    autoCameraType: Incomplete
    extent: Incomplete
    intersectLayerPath: Incomplete
    mapFrameLinkName: Incomplete
    margin: float
    marginType: Incomplete
    marginUnits: Incomplete
    source: Incomplete
    syncRotation: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMAviationArrow:
    lineIndicatorTextSymbol: str
    lineSymbol: str
    defaultPointSymbol: str
    positivePointSymbol: str
    negativePointSymbol: str
    enableArrow: bool
    enableLineIndicator: bool
    arrowLength: float
    lineIndicatorText: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMAviationVariation:
    variationTextSymbol: str
    alignVariationToLine: bool
    variationTextOnLeft: bool
    showYear: bool
    showYearInParenthesis: bool
    variationYearSeparator: Incomplete
    magneticVariationIdentifier: Incomplete
    gridVariationIdentifier: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMAviationVerticalScaleProperties:
    unitTextSymbol: str
    divisionMarkSymbol: str
    subdivisionMarkSymbol: str
    scaleTextSymbol: str
    scaleBarHeight: float
    divisionLineLength: int
    subdivisionLineLength: int
    scaleUnitText: Incomplete
    divisions: int
    subdivisions: int
    visible: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBookmarkMapSeriesPage:
    bookmarkName: Incomplete
    mapURI: Incomplete
    category: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDeclination:
    direction: Incomplete
    degrees: int
    minutes: int
    mils: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMElement:
    anchor: Incomplete
    locked: bool
    name: Incomplete
    visible: bool
    rotation: float
    rotationCenter: Incomplete
    lockedAspectRatio: bool
    customProperties: Incomplete
    expanded: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMExtentIndicator:
    sourceMapFrame: Incomplete
    symbol: str
    leaderType: Incomplete
    leaderSymbol: str
    collapseSize: float
    pointSymbol: str
    name: Incomplete
    isVisible: bool
    avoidLabelConflict: bool
    symbolizeExterior: bool
    extentIndicatorType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGridEndpoint:
    gridLabelTemplate: str
    offset: int
    position: int
    lineSelection: int
    drawLabelsParallel: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGridLabelTemplate:
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGridLine:
    name: Incomplete
    elementType: Incomplete
    gridLineOrientation: Incomplete
    symbol: str
    pattern: str
    fromTick: str
    toTick: str
    interiorTicks: Incomplete
    visibleIndices: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGridPattern:
    interval: int
    start: int
    stop: int
    gap: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGridZoneLabelPosition:
    visible: bool
    offsetX: float
    offsetY: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGuide:
    position: float
    orientation: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLegendItem:
    name: Incomplete
    newColumn: bool
    layerNameSymbol: str
    manualColumn: int
    keepTogetherOption: Incomplete
    showLayerName: bool
    showHeading: bool
    headingSymbol: str
    showLabels: bool
    layer: Incomplete
    showDescription: bool
    labelSymbol: str
    descriptionSymbol: str
    patchWidth: float
    patchHeight: float
    autoVisibility: bool
    useMapSeriesShape: bool
    classIndent: float
    headingIndent: float
    layerNameIndent: float
    showGroupLayerName: bool
    groupLayerNameSymbol: str
    scaleToPatch: bool
    showCounts: bool
    countFormat: str
    countPrefix: Incomplete
    countSuffix: Incomplete
    isVisible: bool
    groupFilter: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMapGrid:
    name: Incomplete
    isVisible: bool
    neatlineSymbol: str
    maxInteriorAngle: int
    edgeMinimumLength: float
    mapGridEdges: Incomplete
    minScale: float
    maxScale: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMapGridEdge:
    partIndex: int
    segmentIndices: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMapProductGridReference:
    gridReferenceFieldName: Incomplete
    precisionLevel: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMapSeries:
    enabled: bool
    mapFrameName: Incomplete
    startingPageNumber: int
    currentPageID: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMargin:
    left: float
    right: float
    top: float
    bottom: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMeterReferenceProperties:
    gridSquareUpperLeft: Incomplete
    gridSquareUpperRight: Incomplete
    gridSquareLowerLeft: Incomplete
    gridSquareLowerRight: Incomplete
    gridSquareUpperLeftDual: Incomplete
    gridSquareUpperRightDual: Incomplete
    gridSquareLowerLeftDual: Incomplete
    gridSquareLowerRightDual: Incomplete
    gridSquareVerticalSeparator: int
    gridSquareHorizontalSeparator: int
    gridSquareHorizontalSeparatorDual: int
    gridZoneUpperLeft: Incomplete
    gridZoneUpperRight: Incomplete
    gridZoneLowerLeft: Incomplete
    gridZoneLowerRight: Incomplete
    gridZoneLatitude: int
    gridZoneLongitude: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPage:
    height: int
    stretchElements: bool
    width: float
    printerPreferences: str
    units: Incomplete
    guides: Incomplete
    showRulers: bool
    showGuides: bool
    smallestRulerDivision: float
    margin: str
    showMargin: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPrinterPreferences:
    printerName: Incomplete
    paperName: Incomplete
    paperSource: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMProfileGrid:
    horizontalScale: int
    horizontalScaleUnits: Incomplete
    verticalScale: int
    verticalScaleUnits: Incomplete
    autoGridExtent: bool
    yMin: int
    yMax: int
    subDivisionsX: int
    subDivisionsY: int
    gridSymbol: str
    subDivisionSymbol: str
    horizontalScaleTextSymbol: str
    verticalScaleLeftTextSymbol: str
    verticalScaleRightTextSymbol: str
    showEntireApproach: bool
    xMax: int
    verticalIntervalInMeters: int
    verticalIntervalInFeet: int
    showAbsoluteHorizontalScale: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMProfileOIS:
    oISDescription: Incomplete
    oISLabel: Incomplete
    showOIS: bool
    isPrimary: bool
    displayOrder: int
    oISSymbol: str
    oISTextSymbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMProfileObstacle:
    showPenetrating: bool
    obstacleLayerName: Incomplete
    symbolSubstitutionType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMProfileRunway:
    precision: int
    elevationChangeThreshold: float
    runwayLineSymbol: str
    runwayTextSymbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMProfileTerrain:
    showOutline: bool
    maxTerrain: str
    minTerrain: str
    centerLineTerrain: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMProfileTerrainDisplay:
    displayOption: Incomplete
    terrainSymbol: str
    penetratingTerrainSymbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMReportDataSource:
    dataConnection: str
    definitionQuery: Incomplete
    fields: Incomplete
    mapMemberURI: Incomplete
    useSelectionSet: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMReportElementFieldProperties:
    element: Incomplete
    field: Incomplete
    format: str
    statistic: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMReportWatermark:
    element: str
    excludePageNumbers: Incomplete
    isBackground: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTableField:
    name: Incomplete
    isVisible: bool
    width: int
    sortInfo: Incomplete
    sortOrder: int
    fieldOrder: int
    group: bool
    displayName: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTick:
    length: float
    offset: float
    isVisible: bool
    symbol: str
    gridEndpoint: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLayout(CIMDefinition):
    elements: Incomplete
    page: str
    dateExported: Incomplete
    datePrinted: Incomplete
    mapSeries: str
    colorModel: Incomplete
    rGBColorProfile: Incomplete
    cMYKColorProfile: Incomplete
    simulateOverprint: bool
    customProperties: Incomplete
    defaultColorVisionDeficiencyMode: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLayoutView(CIMView):
    extent: Incomplete
    defaultMapFrameName: Incomplete
    pauseDrawing: bool
    colorVisionDeficiencyMode: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMReportDocument(CIMVersion):
    binaryReferences: Incomplete
    layerDefinitions: Incomplete
    mapDefinitions: Incomplete
    reportDefinition: str
    tableDefinitions: Incomplete
    layoutDefinitions: Incomplete
    linkChartDefinitions: Incomplete
    timelineDefinitions: Incomplete
    videoDefinitions: Incomplete
    elevationSurfaceLayerDefinitions: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBookmarkMapSeries(CIMMapSeries):
    pages: Incomplete
    scaleRounding: float
    extentOptions: Incomplete
    marginType: Incomplete
    marginUnits: Incomplete
    margin: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMCustomGrid(CIMMapGrid):
    layerURI: Incomplete
    gridLines: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMCustomGridLabelTemplate(CIMGridLabelTemplate):
    labelExpressionInfo: str
    edgeLabelAngles: Incomplete
    symbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMExteriorTick(CIMTick):
    edgeAffinity: Incomplete
    drawPerpendicular: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFrameElement(CIMElement):
    frame: Incomplete
    graphicFrame: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGZDLabelGridLine(CIMGridLine):
    dynamicStringTemplate: Incomplete
    verticalTopPosition: str
    verticalCenterPosition: str
    verticalBottomPosition: str
    horizontalLeftPosition: str
    horizontalCenterPosition: str
    horizontalRightPosition: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGraphicElement(CIMElement):
    graphic: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGraticule(CIMMapGrid):
    customOrigin: Incomplete
    geographicCoordinateSystem: Incomplete
    gridLines: Incomplete
    isAutoScaled: bool
    useMapClipShape: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGroupElement(CIMFrameElement):
    elements: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMHorizontalBarLegendItem(CIMLegendItem):
    arrangement: Incomplete
    angleAbove: int
    angleBelow: int
    patchAlignment: Incomplete
    lineSymbol: str
    lineLength: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMHorizontalLegendItem(CIMLegendItem):
    arrangement: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMInteriorTick(CIMTick):
    pattern: str
    indicateDirection: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLadderGridLine(CIMGridLine):
    dynamicStringTemplate: Incomplete
    gapX: float
    gapY: float
    position: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMGRSGridLine(CIMGridLine):
    xOffset: float
    yOffset: float
    labelPosition: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMapFrame(CIMFrameElement):
    autoCamera: str
    uRI: Incomplete
    view: str
    extentIndicators: Incomplete
    grids: Incomplete
    useMapBackgroundColor: bool
    extentIndicatorsExpanded: bool
    mapGridsExpanded: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMapSurround(CIMFrameElement):
    mapFrame: Incomplete
    minScale: float
    maxScale: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMeasuredGrid(CIMMapGrid):
    customOrigin: Incomplete
    projectedCoordinateSystem: Incomplete
    gridLines: Incomplete
    isAutoScaled: bool
    clipUTMZone: bool
    useMapClipShape: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMNestedLegendItem(CIMLegendItem):
    lineSymbol: str
    lineLength: int
    arrangement: Incomplete
    autoLayout: bool
    labelEnds: bool
    outlineSymbol: str
    showOutlines: bool
    patchAlignment: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMNorthArrow(CIMMapSurround):
    referenceLocation: Incomplete
    calibrationAngle: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMProfileFrame(CIMMapSurround):
    heightOption: Incomplete
    height: int
    heightUnits: Incomplete
    ratio: int
    runwayDesignator: Incomplete
    primaryOISDescription: Incomplete
    secondaryOISDescription: Incomplete
    oISLayerURI: Incomplete
    grid: str
    terrain: str
    runway: str
    oISSurfaces: Incomplete
    obstacles: Incomplete
    profileType: Incomplete
    profileStyle: Incomplete
    runwayEndLeftAsReference: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMProfilePointObstacle(CIMProfileObstacle):
    markerLocation: Incomplete
    obstacleBaseSymbol: str
    obstacleHeightSymbol: str
    obstacleMarkerSymbol: str
    obstacleTextSymbol: str
    showOnlyShadowingObstacles: bool
    substituteObstacleBaseSymbol: str
    substituteObstacleHeightSymbol: str
    substituteObstacleMarkerSymbol: str
    substituteObstacleTextSymbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMProfilePolyObstacle(CIMProfileObstacle):
    groundDisplayOption: Incomplete
    obstacleSymbol: str
    substituteObstacleSymbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMReferenceGrid(CIMMapGrid):
    isAutoScaled: bool
    rowCount: int
    columnCount: int
    gridLines: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMReferenceGridLabelTemplate(CIMGridLabelTemplate):
    name: Incomplete
    values: Incomplete
    delimiter: Incomplete
    symbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMReport(CIMLayout):
    height: int
    startPage: int
    watermarks: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMReportField(CIMTableField):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMReportMapFrameElementProperties(CIMReportElementFieldProperties):
    spatialMapSeries: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMReportSectionElement(CIMGroupElement):
    autoSize: bool
    elementFieldProperties: Incomplete
    excludePageNumberPages: Incomplete
    excludeSectionPages: Incomplete
    startOnNewPage: bool
    autoGrowTextElements: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMScaleBar(CIMMapSurround):
    alignToZeroPoint: bool
    barHeight: float
    division: float
    divisions: int
    divisionsBeforeZero: int
    fittingStrategy: Incomplete
    labelFrequency: Incomplete
    labelGap: float
    labelPosition: Incomplete
    labelSymbol: str
    numberFormat: str
    subdivisions: int
    unitLabel: Incomplete
    unitLabelGap: float
    unitLabelPosition: Incomplete
    unitLabelSymbol: str
    units: Incomplete
    useFractionCharacters: bool
    zeroPoint: Incomplete
    computeAtCenter: bool
    displayFirstOutside: bool
    displayLastOutside: bool
    barWidth: float
    divisionMarkHeight: float
    divisionMarkSymbol: str
    markFrequency: Incomplete
    markPosition: Incomplete
    subdivisionMarkHeight: float
    subdivisionMarkSymbol: str
    midpointMarkHeight: float
    midpointMarkSymbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMScaleLine(CIMScaleBar):
    lineSymbol: str
    stepped: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSimpleGridLabelTemplate(CIMGridLabelTemplate):
    dynamicStringTemplate: Incomplete
    symbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSingleFillScaleBar(CIMScaleBar):
    fillSymbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSpatialMapSeries(CIMMapSeries):
    indexLayerURI: Incomplete
    nameField: Incomplete
    numberField: Incomplete
    categoryField: Incomplete
    rotationField: Incomplete
    sortField: Incomplete
    scaleField: Incomplete
    spatialReferenceField: Incomplete
    sortAscending: bool
    scaleRounding: float
    extentOptions: Incomplete
    marginType: Incomplete
    marginUnits: Incomplete
    margin: float
    clipMapToIndexFeature: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTabGridLine(CIMGridLine):
    alternatingSymbols: bool
    alternatingSymbol: str
    height: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTableFrame(CIMMapSurround):
    fields: Incomplete
    mapMemberURI: Incomplete
    fillingStrategy: Incomplete
    fittingStrategy: Incomplete
    columns: int
    minFontSize: int
    verticalTextGap: int
    horizontalTextGap: int
    headingGap: int
    rowGap: int
    fieldGap: int
    columnGap: int
    headingBackgroundSymbol: str
    headingBorderSymbol: str
    headingLineSymbol: str
    columnBorderSymbol: str
    alternate1RowBackgroundSymbol: str
    alternate1RowBackgroundCount: int
    alternate2RowBackgroundSymbol: str
    alternate2RowBackgroundCount: int
    rowBorderSymbol: str
    customWhereClause: Incomplete
    defaultTableFrameField: str
    balanceColumns: bool
    rowLimit: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTableFrameField(CIMTableField):
    enableWordWrapping: bool
    headingTextSymbol: str
    textSymbol: str
    backgroundSymbol: str
    borderSymbol: str
    verticalLineSymbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTemporalMapSeries(CIMMapSeries):
    timeExtent: Incomplete
    interval: float
    intervalUnits: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMThematicMapSeries(CIMMapSeries):
    groupLayerURI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTopoNorthArrow(CIMNorthArrow):
    date: Incomplete
    zone: Incomplete
    isPrimaryZone: bool
    gMAngle: str
    gridConvergence: str
    directionalNotes: bool
    leadingZero: bool
    roundGMAngle: bool
    roundMils: bool
    autoUpdate: bool
    largeSize: bool
    textSymbol: str
    lineSymbol: str
    trueNorthMarkerSymbol: str
    magneticNorthNegativeSymbol: str
    magneticNorthPositiveSymbol: str
    magneticNorthZeroSymbol: str
    declinationArcSymbol: str
    productSpecification: Incomplete
    drawToSpecification: bool
    dateInterval: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVerticalLegendItem(CIMLegendItem):
    arrangement: Incomplete
    patchAlignment: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMAttachmentFrame(CIMFrameElement):
    maxImages: int
    sortFieldName: Incomplete
    sortOrder: Incomplete
    imageFrame: str
    gridRows: int
    gridColumns: int
    gridRowDirection: bool
    imageHeight: float
    imageWidth: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMAviationNorthArrow(CIMNorthArrow):
    date: Incomplete
    declinationSpatialReference: Incomplete
    gMAngle: str
    gridConvergence: str
    trueNorthArrow: str
    magneticNorthArrow: str
    gridNorthArrow: str
    variation: str
    rateOfChangeTextSymbol: str
    displayVariationDate: bool
    displayRateOfChange: bool
    autoUpdate: bool
    rateOfChangeText: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMAviationVerticalScaleBar(CIMFrameElement):
    verticalLineSymbol: str
    feetScale: str
    meterScale: str
    divisionMarkHeight: float
    divisionsBeforeZero: bool
    feetOnRight: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBaseStreetIndex(CIMMapSurround):
    layerURI: Incomplete
    fields: Incomplete
    titleText: Incomplete
    titleTextSymbol: str
    headerTextSymbol: str
    textSymbol: str
    fittingStrategy: Incomplete
    wrapMethod: Incomplete
    minFontSize: float
    headerGap: float
    groupTextSymbol: str
    groupGap: float
    columns: int
    indexDelimiter: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartFrame(CIMMapSurround):
    mapMemberURI: Incomplete
    chartName: Incomplete
    isDynamic: bool
    useMapSeriesShape: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMCondensedTabGridLine(CIMTabGridLine):
    width: float
    condensedTab: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMContiguousTabGridLine(CIMTabGridLine):
    contiguousTab: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMCruisingAltitudeDiagram(CIMFrameElement):
    diagramType: Incomplete
    altitudeTextSymbol: str
    bearingTextSymbol: str
    titleTextSymbol: str
    bearingArrowLineSymbol: str
    lineSymbol: str
    diameterUnits: Incomplete
    diagramDiameter: float
    diagramTitle: Incomplete
    verticalLeftText: Incomplete
    verticalRightText: Incomplete
    horizontalTopText: Incomplete
    horizontalBottomText: Incomplete
    quadrantalTopLeftText: Incomplete
    quadrantalTopRightText: Incomplete
    quadrantalBottomLeftText: Incomplete
    quadrantalBottomRightText: Incomplete
    autoResizeText: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDoubleFillScaleBar(CIMScaleBar):
    fillSymbol1: str
    fillSymbol2: str
    style: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGroupFooter(CIMReportSectionElement):
    field: Incomplete
    alignSubsectionToBottom: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGroupHeader(CIMReportSectionElement):
    field: Incomplete
    repeatOnEveryPage: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLegend(CIMMapSurround):
    autoAdd: bool
    autoFonts: bool
    autoReorder: bool
    autoVisibility: bool
    defaultPatchHeight: float
    defaultPatchWidth: float
    descriptionWidth: float
    groupGap: float
    headingGap: float
    horizontalItemGap: float
    patchGap: float
    items: Incomplete
    labelWidth: float
    minFontSize: float
    rightToLeft: bool
    scaleSymbols: bool
    showTitle: bool
    textGap: float
    title: Incomplete
    titleGap: float
    titleSymbol: str
    itemGap: float
    classGap: float
    layerNameGap: float
    featureCountPrefix: Incomplete
    featureCountSuffix: Incomplete
    fittingStrategy: Incomplete
    groupLayerNameGap: float
    columns: int
    makeColumnsSameWidth: bool
    defaultLegendItem: str
    excludedLayers: Incomplete
    balanceColumns: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMapProductFeatureGuide(CIMBaseStreetIndex):
    autoUpdate: bool
    productSpecification: Incomplete
    drawToSpecification: bool
    gridReference: str
    iDNumberFieldName: Incomplete
    categoryCodeFieldName: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMapProductGridStreetIndex(CIMBaseStreetIndex):
    autoUpdate: bool
    productSpecification: Incomplete
    drawToSpecification: bool
    gridReference: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMapProductSurround(CIMMapSurround):
    autoUpdate: bool
    productSpecification: Incomplete
    drawToSpecification: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMarkerNorthArrow(CIMNorthArrow):
    pointSymbol: str
    northType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMeterReferenceGuide(CIMMapProductSurround):
    gridSquareType: Incomplete
    isSingleGridZone: bool
    properties: str
    textSymbol: str
    lineSymbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRelatedReportSection(CIMReportSectionElement):
    dataSource: str
    relateName: Incomplete
    expressions: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMReportDetails(CIMReportSectionElement):
    columns: int
    rowBackgroundColors: Incomplete
    rowBackgroundCount: int
    keepRecordTogether: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMReportFooter(CIMReportSectionElement):
    alignSubsectionToBottom: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMReportHeader(CIMReportSectionElement):
    coverPage: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMReportPageFooter(CIMReportSectionElement):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMReportPageHeader(CIMReportSectionElement):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMReportPageSection(CIMReportSectionElement):
    includePageNumber: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMReportSection(CIMReportSectionElement):
    dataSource: str
    expressions: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSlopeGuide(CIMMapProductSurround):
    slopeGuideLayerURI: Incomplete
    contourIntervalField: Incomplete
    mapScale: int
    contourInterval: int
    titleTextSymbol: str
    slopeUnitTextSymbol: str
    slopeTextSymbol: str
    footnoteTextSymbol: str
    verticalLineSymbol: str
    horizontalLineSymbol: str
    tickLineSymbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTMElevationGuideBarElement(CIMMapProductSurround):
    elevationBandLayerURI: Incomplete
    numberOfBands: int
    textSymbol: str
    lineSymbol: str
    highestBandSymbol: str
    highBandSymbol: str
    mediumBandSymbol: str
    lowBandSymbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTopoCompassRose(CIMTopoNorthArrow):
    degreeLabelFrequency: int
    divisionMarkSymbol: str
    subdivisionMarkSymbol: str
    degreeMarkSymbol: str
    divisions: int
    subdivisions: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGlossaryTable(CIMMapProductSurround):
    fittingStrategy: Incomplete
    mapMemberURI: Incomplete
    fields: Incomplete
    title: Incomplete
    titleTextSymbol: str
    rightToLeft: bool
    minFontSize: int
    titleGap: int
    headingGap: int
    rowGap: int
    horizontalTextGap: int
    verticalTextGap: int
    delimiterCharacter: Incomplete
    delimiterTextSymbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMReportLayoutPageSection(CIMReportPageSection):
    layoutURI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...
