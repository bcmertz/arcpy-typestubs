from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from _typeshed import Incomplete

class CIMBivariateFieldInfo:
    normalizationField: Incomplete
    normalizationTotal: float
    normalizationType: Incomplete
    classificationMethod: Incomplete
    field: Incomplete
    valueExpressionInfo: str
    defaultLabel: Incomplete
    minimumBreak: int
    upperBounds: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMClassBreak:
    criticalBreak: bool
    description: Incomplete
    label: Incomplete
    patch: Incomplete
    symbol: str
    upperBound: int
    alternateSymbols: Incomplete
    customPatch: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMExpressionInfo:
    title: Incomplete
    expression: Incomplete
    name: Incomplete
    returnType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLegendPatch:
    geometryURI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPrimitiveOverride:
    primitiveName: Incomplete
    propertyName: Incomplete
    expression: Incomplete
    valueExpressionInfo: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMProportionalPieSizeOptions:
    flanneryCompensation: bool
    minimumSize: float
    minimumValue: int
    maximumSize: int
    maximumValue: int
    proportionalBySum: bool
    proportionalFieldName: Incomplete
    proportionalExpressionInfo: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRenderer:
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRendererAuthoringInfo:
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRuleSymbolLayerNames:
    ruleID: int
    symbolLayerNames: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMScaleDependentSizeVariation:
    scale: float
    size: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStringMap:
    key: Incomplete
    value: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSymbolReference:
    primitiveOverrides: Incomplete
    stylePath: Incomplete
    symbol: str
    symbolName: Incomplete
    minScale: float
    maxScale: float
    scaleDependentSizeVariation: Incomplete
    minDistance: float
    maxDistance: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSymbolizationRule:
    minScale: float
    maxScale: float
    filter: Incomplete
    symbol: str
    label: Incomplete
    description: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMUniqueValue:
    fieldValues: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMUniqueValueClass:
    description: Incomplete
    editable: bool
    label: Incomplete
    patch: Incomplete
    symbol: str
    values: Incomplete
    visible: bool
    alternateSymbols: Incomplete
    customPatch: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMUniqueValueGroup:
    classes: Incomplete
    heading: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMUnitSymbolization:
    valueRepresentation: Incomplete
    valueUnit: Incomplete
    symbolShape: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVisualVariable:
    authoringInfo: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVisualVariableAuthoringInfo:
    minSliderValue: float
    maxSliderValue: float
    theme: Incomplete
    showLegend: bool
    heading: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVisualVariableInfo:
    expression: Incomplete
    randomMax: float
    randomMin: float
    visualVariableInfoType: Incomplete
    valueExpressionInfo: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVisualVariableLevel:
    iD: int
    minValue: float
    maxValue: float
    mean: float
    standardDeviation: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMAreaLegendPatch(CIMLegendPatch):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartRenderer(CIMRenderer):
    normalizationField: Incomplete
    normalizationTotal: float
    normalizationType: Incomplete
    barrierWeight: Incomplete
    baseSymbol: str
    chartSymbol: str
    fieldNames: Incomplete
    fieldTotals: Incomplete
    label: Incomplete
    maxValue: int
    preventChartOverlap: bool
    proportionalPieSizeOptions: str
    colorRamp: str
    fieldLabels: Incomplete
    showSizeLegend: bool
    sizeLegendOutlineColor: str
    sizeLegendLeaderlineColor: str
    drawChartSymbolsAboveAllLayers: bool
    exclusionClause: Incomplete
    exclusionDescription: Incomplete
    exclusionLabel: Incomplete
    exclusionSymbol: str
    useExclusionSymbol: bool
    exclusionSymbolPatch: Incomplete
    exclusionSymbolCustomPatch: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMClassBreaksRendererBase(CIMRenderer):
    sampleSize: int
    classificationMethod: Incomplete
    breaks: Incomplete
    minimumBreak: float
    showClassGaps: bool
    showInAscendingOrder: bool
    useDefaultSymbol: bool
    defaultSymbolPatch: Incomplete
    defaultSymbol: str
    defaultLabel: Incomplete
    defaultDescription: Incomplete
    numberFormat: str
    defaultSymbolCustomPatch: str
    alwaysUpdateClassLabels: bool
    backgroundSymbol: str
    barrierWeight: Incomplete
    classBreakType: Incomplete
    colorRamp: str
    field: Incomplete
    heading: Incomplete
    minimumLabel: Incomplete
    valueExpressionInfo: str
    polygonSymbolColorTarget: Incomplete
    drawGraduatedSymbolsAboveAllLayers: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMColorVisualVariable(CIMVisualVariable):
    expression: Incomplete
    minValue: float
    maxValue: float
    colorRamp: str
    normalizationField: Incomplete
    normalizationType: Incomplete
    valueExpressionInfo: str
    polygonSymbolColorTarget: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDictionaryRenderer(CIMRenderer):
    dictionaryName: Incomplete
    fieldMap: Incomplete
    scalingExpressionInfo: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDotDensityRenderer(CIMRenderer):
    sampleSize: int
    visualVariables: Incomplete
    exclusionClause: Incomplete
    exclusionDescription: Incomplete
    exclusionLabel: Incomplete
    exclusionSymbol: str
    useExclusionSymbol: bool
    exclusionSymbolPatch: Incomplete
    exclusionSymbolCustomPatch: str
    colorRamp: str
    dotDensitySymbol: str
    dotSize: float
    dotValue: float
    excludeDotsFromMaskedArea: bool
    fieldNames: Incomplete
    fieldLabels: Incomplete
    maintainDensity: bool
    maskingLayer: Incomplete
    randomSeed: int
    referenceScale: float
    useMasking: bool
    valueExpressionInfos: Incomplete
    symbolLabel: Incomplete
    unitLabel: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMHeatMapRenderer(CIMRenderer):
    colorScheme: str
    field: Incomplete
    radius: int
    rendererQuality: int
    heading: Incomplete
    minLabel: Incomplete
    maxLabel: Incomplete
    maxPixelIntensity: float
    pixelIntensityStops: Incomplete
    autoAdjustPixelIntensity: bool
    maxPixelIntensityReferenceScale: float
    referenceScale: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLineLegendPatch(CIMLegendPatch):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMultilevelVisualVariable(CIMVisualVariable):
    levels: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMProportionalRenderer(CIMRenderer):
    sampleSize: int
    visualVariables: Incomplete
    normalizationField: Incomplete
    normalizationTotal: float
    normalizationType: Incomplete
    exclusionClause: Incomplete
    exclusionDescription: Incomplete
    exclusionLabel: Incomplete
    exclusionSymbol: str
    useExclusionSymbol: bool
    exclusionSymbolPatch: Incomplete
    exclusionSymbolCustomPatch: str
    backgroundSymbol: str
    barrierWeight: Incomplete
    field: Incomplete
    flanneryCompensation: bool
    legendSymbolCount: int
    maxDataValue: int
    minDataValue: int
    minSymbol: str
    unitSymbolization: str
    heading: Incomplete
    useDefaultSymbol: bool
    defaultSymbol: str
    defaultSymbolPatch: Incomplete
    defaultLabel: Incomplete
    defaultDescription: Incomplete
    showInAscendingOrder: bool
    valueExpressionInfo: str
    drawProportionalSymbolsAboveAllLayers: bool
    defaultSymbolCustomPatch: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRepresentationRenderer(CIMRenderer):
    drawInvalidRule: bool
    drawInvisibleRepresentation: bool
    invalidRuleColor: str
    invisibleRepresentationColor: str
    representationClassName: Incomplete
    ruleLegendVisibility: Incomplete
    symbolLayerNameMapping: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRotationVisualVariable(CIMVisualVariable):
    visualVariableInfoX: str
    visualVariableInfoY: str
    visualVariableInfoZ: str
    rotationTypeZ: Incomplete
    normalToSurface: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRuleRenderer(CIMRenderer):
    visualVariables: Incomplete
    rules: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSimpleRenderer(CIMRenderer):
    sampleSize: int
    visualVariables: Incomplete
    description: Incomplete
    label: Incomplete
    patch: Incomplete
    symbol: str
    alternateSymbols: Incomplete
    customPatch: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSizeVisualVariable(CIMVisualVariable):
    expression: Incomplete
    randomMin: float
    randomMax: float
    minSize: float
    maxSize: float
    minValue: float
    maxValue: float
    valueUnits: Incomplete
    valueRepresentation: Incomplete
    variableType: Incomplete
    valueShape: Incomplete
    axis: Incomplete
    target: Incomplete
    normalizationField: Incomplete
    normalizationType: Incomplete
    sizeValues: Incomplete
    dataValues: Incomplete
    valueExpressionInfo: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTransparencyVisualVariable(CIMVisualVariable):
    field: Incomplete
    transparencyValues: Incomplete
    dataValues: Incomplete
    normalizationField: Incomplete
    normalizationTotal: float
    normalizationType: Incomplete
    valueExpressionInfo: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMUniqueValueRenderer(CIMRenderer):
    sampleSize: int
    visualVariables: Incomplete
    colorRamp: str
    defaultDescription: Incomplete
    defaultLabel: Incomplete
    defaultSymbol: str
    defaultSymbolPatch: Incomplete
    fields: Incomplete
    groups: Incomplete
    useDefaultSymbol: bool
    isDefaultSymbolVisible: bool
    styleGallery: Incomplete
    valueExpressionInfo: str
    polygonSymbolColorTarget: Incomplete
    authoringInfo: str
    defaultSymbolCustomPatch: str
    showClassVisibility: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMUniqueValueRendererAuthoringInfo(CIMRendererAuthoringInfo):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBivariateRendererAuthoringInfo(CIMUniqueValueRendererAuthoringInfo):
    sampleSize: int
    fieldInfos: Incomplete
    gridSize: Incomplete
    gridOrientation: Incomplete
    gridLabelOption: Incomplete
    templateSymbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMClassBreaksRenderer(CIMClassBreaksRendererBase):
    normalizationField: Incomplete
    normalizationTotal: float
    normalizationType: Incomplete
    exclusionClause: Incomplete
    exclusionDescription: Incomplete
    exclusionLabel: Incomplete
    exclusionSymbol: str
    useExclusionSymbol: bool
    exclusionSymbolPatch: Incomplete
    exclusionSymbolCustomPatch: str
    visualVariables: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMColorClassBreaksVisualVariable(CIMColorVisualVariable):
    classificationMethod: Incomplete
    breaks: Incomplete
    minimumBreak: float
    showClassGaps: bool
    showInAscendingOrder: bool
    useDefaultSymbol: bool
    defaultSymbolPatch: Incomplete
    defaultSymbol: str
    defaultLabel: Incomplete
    defaultDescription: Incomplete
    numberFormat: str
    defaultSymbolCustomPatch: str
    alwaysUpdateClassLabels: bool
    colorChannelTarget: Incomplete
    classBreaksLegendVisualVariableOptions: Incomplete
    useClassBreaks: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMultilevelColorVisualVariable(CIMMultilevelVisualVariable):
    colorRamp: str
    normalizationField: Incomplete
    normalizationType: Incomplete
    valueExpressionInfo: str
    polygonSymbolColorTarget: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMultilevelSizeVisualVariable(CIMMultilevelVisualVariable):
    minSize: float
    maxSize: float
    valueRepresentation: Incomplete
    variableType: Incomplete
    valueShape: Incomplete
    axis: Incomplete
    target: Incomplete
    normalizationField: Incomplete
    normalizationType: Incomplete
    valueExpressionInfo: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSizeClassBreaksVisualVariable(CIMSizeVisualVariable):
    classBreaksLegendVisualVariableOptions: Incomplete
    useClassBreaks: bool
    classificationMethod: Incomplete
    breaks: Incomplete
    minimumBreak: float
    showClassGaps: bool
    showInAscendingOrder: bool
    useDefaultSymbol: bool
    defaultSymbolPatch: Incomplete
    defaultSymbol: str
    defaultLabel: Incomplete
    defaultDescription: Incomplete
    numberFormat: str
    defaultSymbolCustomPatch: str
    alwaysUpdateClassLabels: bool
    templateSymbol: str
    drawSizeMarkerSymbolsAboveAllLayers: bool
    def __init__(self, *args, **Kwargs) -> None: ...
