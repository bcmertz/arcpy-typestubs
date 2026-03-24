from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from .CIMCore import CIMDefinition as CIMDefinition
from .CIMLayer import CIMBaseLayer as CIMBaseLayer
from .CIMLayout import CIMGraphicElement as CIMGraphicElement
from .CIMVectorLayers import CIMDataConnection as CIMDataConnection, CIMFeatureLayer as CIMFeatureLayer, CIMGeoFeatureLayerBase as CIMGeoFeatureLayerBase
from _typeshed import Incomplete

class CIMAuxiliaryRasterProperties:
    bandIndexes: Incomplete
    extent: Incomplete
    height: int
    width: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMosaicRule:
    ascending: bool
    fIDs: Incomplete
    lockRasterID: Incomplete
    mosaicMethod: Incomplete
    mosaicOperatorType: Incomplete
    orderByBaseValue: Incomplete
    orderByFieldName: Incomplete
    timeValue: Incomplete
    viewpoint: Incomplete
    whereClause: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPansharpeningFilter:
    panImage: str
    pansharpeningType: Incomplete
    infraredImage: str
    rWeight: float
    gWeight: float
    bWeight: float
    iWeight: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRangeDimensionValue:
    rangeDimensionName: Incomplete
    rangeDimensionValue: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRasterClassBreak:
    criticalBreak: bool
    upperBound: float
    label: Incomplete
    description: Incomplete
    color: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRasterColorCorrection:
    preStretchType: Incomplete
    colorBalanceMethod: Incomplete
    colorMatchingMethod: Incomplete
    needContrastAdjustment: bool
    targetColorSurfaceType: Incomplete
    targetColorRaster: str
    userDefinedReference: bool
    referenceOID: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRasterColorizer:
    resamplingType: Incomplete
    contrast: int
    brightness: int
    noDataColor: str
    name: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRasterColorizerMapping:
    rasterOID: int
    colorizerIndex: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRasterDimensionalDefinition:
    variableName: Incomplete
    dimensionName: Incomplete
    minimumValues: Incomplete
    maximumValues: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRasterHistogramEditInfo:
    breakPointsX: Incomplete
    breakPointsY: Incomplete
    editType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRasterMultidimensionalDisplayDefinition:
    variableName: Incomplete
    timeValue: Incomplete
    hasRangeDimension: bool
    rangeDimensionName: Incomplete
    rangeDimensionValue: str
    additionalDimensionValues: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRasterMultidimensionalExtentDefinition:
    subsetDefinitions: Incomplete
    areaOfInterest: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRasterStretchClass:
    label: Incomplete
    value: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRasterUniqueValueClass:
    values: Incomplete
    label: Incomplete
    description: Incomplete
    color: str
    editable: bool
    visible: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRasterUniqueValueGroup:
    classes: Incomplete
    heading: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRenderingRule:
    description: Incomplete
    name: Incomplete
    variableName: Incomplete
    arguments: Incomplete
    definition: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVideoTimelineIndicator:
    label: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFeatureMosaicSubLayer(CIMFeatureLayer):
    mosaicSubLayerType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMosaicLayer(CIMBaseLayer):
    boundaryLayer: Incomplete
    footprintLayer: Incomplete
    imageLayer: Incomplete
    seamlineLayer: Incomplete
    mosaicDatasetConnection: str
    timeDefinition: str
    timeDisplayDefinition: str
    timeFields: str
    definitionExpression: Incomplete
    definitionExpressionName: Incomplete
    definitionFilterChoices: Incomplete
    rangeDefinitions: Incomplete
    activeRangeName: Incomplete
    activeVariables: Incomplete
    pageDefinition: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMNITFDataConnection(CIMDataConnection):
    uRI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMNitfFeatureSubLayer(CIMFeatureLayer):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMNitfGroupSubLayer(CIMBaseLayer):
    standaloneTables: Incomplete
    layers: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMNitfLayer(CIMBaseLayer):
    standaloneTables: Incomplete
    dataConnection: str
    layers: Incomplete
    extraItems: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRasterBandDataConnection(CIMDataConnection):
    workspaceConnectionString: Incomplete
    workspaceFactory: Incomplete
    customWorkspaceFactoryCLSID: Incomplete
    dataset: Incomplete
    datasetType: Incomplete
    rasterBandName: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRasterCatalogLayer(CIMGeoFeatureLayerBase):
    displayRastersThreshold: int
    drawRastersOnly: bool
    fixedLabelPositions: bool
    colorizerMapping: Incomplete
    colorizers: Incomplete
    resamplingType: Incomplete
    transitionScale: float
    useColorCorrection: bool
    useScale: bool
    wireFrameSymbol: str
    sortFieldAscending: bool
    sortField: Incomplete
    colorCorrection: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRasterLayer(CIMBaseLayer):
    dataConnection: str
    colorizer: str
    attributeTable: str
    timeDisplayDefinition: str
    timeDimensionFields: str
    timeDefinition: str
    auxiliaryRasterProperties: str
    autoComputeStatsHistogram: bool
    rangeDefinitions: Incomplete
    activeRangeName: Incomplete
    activeVariables: Incomplete
    multidimensionalExtent: str
    activeSlice: str
    renderingRule: str
    activeCustomColorizer: Incomplete
    customColorizers: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStandaloneVideo(CIMDefinition):
    dataConnection: str
    footprintColor: str
    elapsedTime: float
    visibility: bool
    expanded: bool
    frameCenterGraphic: str
    frameOutlineGraphic: str
    platformTrailGraphic: str
    platformPositionGraphic: str
    bookmarkIndicators: Incomplete
    exportFrameIndicators: Incomplete
    exportToPPTIndicators: Incomplete
    exportFramesIndicators: Incomplete
    metadataToCSVIndicators: Incomplete
    recordVideoIndicators: Incomplete
    exportSegmentIndicators: Incomplete
    recordSegmentsIndicators: Incomplete
    selectedKLVChannels: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVideoDataConnection(CIMDataConnection):
    uRI: Incomplete
    anonymous: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVideoGraphicElement(CIMGraphicElement):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMImageServiceLayer(CIMRasterLayer):
    compression: Incomplete
    compressionQuality: int
    drawFootprints: bool
    featureTable: str
    footprintDrawMode: Incomplete
    footprintSymbol: str
    mosaicRule: str
    selectable: bool
    selectionColor: str
    selectionSymbol: str
    useSelectionSymbol: bool
    ignoreRenderingRuleOnIdentify: bool
    useServiceCache: bool
    pageDefinition: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMNitfImageSubLayer(CIMRasterLayer):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMNitfScreenOverlaySubLayer(CIMNitfImageSubLayer):
    top: float
    left: float
    width: float
    height: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRasterCMYKColorizer(CIMRasterColorizer):
    backgroundColor: str
    backgroundValueBlack: int
    backgroundValueCyan: int
    backgroundValueMagenta: int
    backgroundValueYellow: int
    blackBandIndex: int
    cyanBandIndex: int
    displayBackgroundValue: bool
    invert: bool
    magentaBandIndex: int
    specificationHistogramBlack: Incomplete
    specificationHistogramCyan: Incomplete
    specificationHistogramMagenta: Incomplete
    specificationHistogramYellow: Incomplete
    standardDeviationParam: float
    stretchStatsBlack: Incomplete
    stretchStatsCyan: Incomplete
    stretchStatsMagenta: Incomplete
    stretchStatsType: Incomplete
    stretchStatsYellow: Incomplete
    stretchType: Incomplete
    useBlackMapping: bool
    useCyanMapping: bool
    useDefaultMapping: bool
    useMagentaMapping: bool
    useYellowMapping: bool
    yellowBandIndex: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRasterClassifyColorizer(CIMRasterColorizer):
    normalizationField: Incomplete
    normalizationTotal: float
    normalizationType: Incomplete
    classBreaks: Incomplete
    classificationMethod: Incomplete
    colorRamp: str
    exclusionColor: str
    exclusionDescription: Incomplete
    exclusionLabel: Incomplete
    exclusionRanges: Incomplete
    exclusionValues: Incomplete
    field: Incomplete
    minimumBreak: float
    showClassGaps: bool
    showInAscendingOrder: bool
    useExclusionColor: bool
    numberFormat: str
    heading: Incomplete
    alwaysUpdateClassLabels: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRasterColorMapColorizer(CIMRasterColorizer):
    colors: Incomplete
    bandID: int
    labels: Incomplete
    min: int
    max: int
    numberFormat: str
    values: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRasterDiscreteColorColorizer(CIMRasterColorizer):
    numColors: int
    colormap: Incomplete
    colorRamp: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRasterRGBColorizer(CIMRasterColorizer):
    alphaBandIndex: int
    backgroundColor: str
    backgroundValueBlue: int
    backgroundValueGreen: int
    backgroundValueRed: int
    blueBandIndex: int
    blueLookup: Incomplete
    displayBackgroundValue: bool
    eSRIStretchContrastB: int
    eSRIStretchContrastG: int
    eSRIStretchContrastR: int
    eSRIStretchMeanB: int
    eSRIStretchMeanG: int
    eSRIStretchMeanR: int
    gammaB: float
    gammaG: float
    gammaR: float
    greenBandIndex: int
    greenLookup: Incomplete
    invert: bool
    lumLookup: Incomplete
    maxPercent: float
    minPercent: float
    pansharpeningFilter: str
    redBandIndex: int
    redLookup: Incomplete
    specificationHistogramBlue: Incomplete
    specificationHistogramGreen: Incomplete
    specificationHistogramRed: Incomplete
    standardDeviationsParam: float
    stretchStatsBlue: Incomplete
    stretchStatsGreen: Incomplete
    stretchStatsRed: Incomplete
    stretchStatsType: Incomplete
    stretchType: Incomplete
    useAlphaBand: bool
    useBlueBand: bool
    useDefaultMapping: bool
    useGammaStretch: bool
    useGreenBand: bool
    useRedBand: bool
    heading: Incomplete
    useCustomStretchMinMax: bool
    customStretchMinRed: float
    customStretchMinGreen: float
    customStretchMinBlue: float
    customStretchMaxRed: float
    customStretchMaxGreen: float
    customStretchMaxBlue: float
    histogramEditInfoRed: str
    histogramEditInfoGreen: str
    histogramEditInfoBlue: str
    saturation: int
    sharpening: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRasterShadedReliefColorizer(CIMRasterColorizer):
    colorRamp: str
    hillShadeType: Incomplete
    scalingType: Incomplete
    pixelSizePower: float
    pixelSizeFactor: float
    azimuth: float
    altitude: float
    removeEdgeEffect: bool
    useMapIlluminationProperties: bool
    zFactor: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRasterStretchColorizer(CIMRasterColorizer):
    backgroundColor: str
    backgroundValue: float
    bandIndex: int
    colorRamp: str
    colorScheme: Incomplete
    customStretchMax: float
    customStretchMin: float
    displayBackgroundValue: bool
    eSRIStretchContrast: int
    eSRIStretchMean: int
    gammaValue: float
    invert: bool
    lookup: Incomplete
    maxPercent: float
    minPercent: float
    standardDeviationParam: float
    statsType: Incomplete
    stretchClasses: Incomplete
    stretchStats: Incomplete
    stretchType: Incomplete
    useCustomStretchMinMax: bool
    useGammaStretch: bool
    numberFormat: str
    heading: Incomplete
    specificationHistogram: Incomplete
    histogramEditInfo: str
    useAdvancedLabeling: bool
    sharpening: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRasterUniqueValueColorizer(CIMRasterColorizer):
    defaultColor: str
    useDefaultColor: bool
    fieldName: Incomplete
    groups: Incomplete
    colorRamp: str
    defaultLabel: Incomplete
    defaultDescription: Incomplete
    numberFormat: str
    isDefaultColorVisible: bool
    showClassVisibility: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRasterVectorFieldColorizer(CIMRasterColorizer):
    magnitudeBandIndex: int
    directionBandIndex: int
    isUVComponents: bool
    referenceSystem: Incomplete
    flowRepresentation: Incomplete
    symbolTileSize: float
    symbolTileSizeUnits: Incomplete
    symbolizationType: Incomplete
    symbol: str
    classBreaks: Incomplete
    minimumClassBreak: int
    minimumMagnitude: Incomplete
    maximumMagnitude: Incomplete
    minimumSymbolSize: float
    maximumSymbolSize: float
    fromUnit: Incomplete
    toUnit: Incomplete
    numberFormat: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVideoTimelineEventIndicator(CIMVideoTimelineIndicator):
    time: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVideoTimelineRangeIndicator(CIMVideoTimelineIndicator):
    minimum: int
    maximum: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMImageMosaicSubLayer(CIMImageServiceLayer):
    mosaicSubLayerType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...
