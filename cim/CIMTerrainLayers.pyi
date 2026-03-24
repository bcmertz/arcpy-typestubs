from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from .CIMLayer import CIMBaseLayer as CIMBaseLayer
from .CIMVectorLayers import CIMDataConnection as CIMDataConnection
from _typeshed import Incomplete

class CIMColorClassBreak:
    upperBound: float
    label: Incomplete
    description: Incomplete
    color: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMColorModulationInfo:
    field: Incomplete
    minValue: float
    maxValue: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMColorUniqueValue:
    value: Incomplete
    label: Incomplete
    description: Incomplete
    color: str
    visible: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMContourIntervalScaleBreak:
    upperBound: int
    contourInterval: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLASPointSplatter:
    pointSizingMethod: Incomplete
    splatMinimumSize: float
    splatScale: float
    useSplatHighlight: bool
    pointSize: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLASStretchClass:
    label: Incomplete
    value: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLASStretchInput:
    colorRamp: str
    stretchMax: float
    stretchMin: float
    gammaValue: float
    invert: bool
    lookup: Incomplete
    maxPercent: float
    minPercent: float
    numberFormat: str
    standardDeviationParam: float
    statsType: Incomplete
    stretchAttribute: Incomplete
    stretchClasses: Incomplete
    stretchStats: Incomplete
    stretchType: Incomplete
    useCustomStretchMinMax: bool
    useGammaStretch: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPointCloudAlgorithm:
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPointCloudFilter:
    field: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPointCloudRenderer:
    pointShape: Incomplete
    pointSizeAlgorithm: str
    colorModulation: str
    fieldTransformType: Incomplete
    field: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTinRenderer:
    illuminate: bool
    maxScale: int
    minScale: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLASDatasetLayer(CIMBaseLayer):
    analysisToolsResolution: float
    dataConnection: str
    displayField: Incomplete
    fileExtentSymbol: str
    fileNameSymbol: str
    fullResolutionScale: float
    isFlattened: bool
    lASDatasetFilter: Incomplete
    maintainCurrentSurface: bool
    pointBudget: int
    pointCountPerCentimeter: int
    renderers: Incomplete
    scaleSymbols: bool
    showFileExtent: bool
    showFileName: bool
    showResolution: bool
    useFullResolutionScale: bool
    selectable: bool
    eyeDomeLighting: str
    useDynamicLOD: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPointCloudLayer(CIMBaseLayer):
    renderer: str
    dataConnection: str
    pointsPerInch: int
    pointsBudget: int
    filters: Incomplete
    snappable: bool
    eyeDomeLighting: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSceneDataConnection(CIMDataConnection):
    customParameters: Incomplete
    uRI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTerrainLayer(CIMBaseLayer):
    analysisToolsResolution: int
    autoLOR: bool
    currentResolution: int
    dataConnection: str
    displayField: Incomplete
    lockCurrentSurface: bool
    pointBudget: int
    pyramidHonored: bool
    scaleSymbols: bool
    showResolution: bool
    renderers: Incomplete
    targetResolution: int
    useOverviewTerrain: bool
    usePointBudget: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTinLayer(CIMBaseLayer):
    dataConnection: str
    displayField: Incomplete
    renderers: Incomplete
    scaleSymbols: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPointCloudBitFieldFilter(CIMPointCloudFilter):
    requiredSetBits: Incomplete
    requiredClearBits: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPointCloudClassBreaksRenderer(CIMPointCloudRenderer):
    breaks: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPointCloudFixedSizeAlgorithm(CIMPointCloudAlgorithm):
    useRealWorldSymbolSizes: bool
    size: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPointCloudRGBRenderer(CIMPointCloudRenderer):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPointCloudReturnFilter(CIMPointCloudFilter):
    includedReturnsBitmask: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPointCloudSplatAlgorithm(CIMPointCloudAlgorithm):
    scaleFactor: float
    minSize: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPointCloudStretchRenderer(CIMPointCloudRenderer):
    rangeMin: float
    rangeMax: float
    colorRamp: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPointCloudUniqueValueRenderer(CIMPointCloudRenderer):
    classes: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPointCloudValueFilter(CIMPointCloudFilter):
    values: Incomplete
    mode: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTerrainAttributeRenderer(CIMTinRenderer):
    attributeFieldName: Incomplete
    embeddedDataSources: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTinColorRampRenderer(CIMTerrainAttributeRenderer):
    breaks: Incomplete
    classificationMethod: Incomplete
    colorRamp: str
    cursorType: Incomplete
    description: Incomplete
    heading: Incomplete
    label: Incomplete
    minimumBreak: int
    numberFormat: str
    showClassGaps: bool
    sortClassesAscending: bool
    symbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTinContourRenderer(CIMTinRenderer):
    contourDescription: Incomplete
    contourInterval: int
    contourLabel: Incomplete
    contourSymbol: str
    indexContourDescription: Incomplete
    indexContourFactor: int
    indexContourLabel: Incomplete
    indexContourSymbol: str
    referenceContourHeight: int
    useIntervalScaleBreaks: bool
    contourIntervalScaleBreaks: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTinFaceClassBreaksRenderer(CIMTinColorRampRenderer):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTinNodeElevationRenderer(CIMTinColorRampRenderer):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTinSimpleRenderer(CIMTinRenderer):
    description: Incomplete
    label: Incomplete
    symbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTinUniqueValueRenderer(CIMTerrainAttributeRenderer):
    colorScheme: Incomplete
    description: Incomplete
    groups: Incomplete
    heading: Incomplete
    label: Incomplete
    lookupStyleset: Incomplete
    symbol: str
    useDefaultSymbol: bool
    colorRamp: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLASPointElevationRenderer(CIMTinColorRampRenderer):
    modulateIntensity: bool
    pointSplatter: str
    useSplat: bool
    colorModulation: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLASStretchRenderer(CIMTerrainAttributeRenderer):
    modulationInput: str
    modulationWeight: float
    pointSplatter: str
    stretchDrawingType: Incomplete
    stretchSourceInput: str
    tintSymbol: str
    useModulation: bool
    useSplat: bool
    colorModulation: str
    heading: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLASUniqueValueRenderer(CIMTinUniqueValueRenderer):
    attribute: int
    modulateIntensity: bool
    pointSplatter: str
    useSplat: bool
    colorModulation: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTerrainDirtyAreaRenderer(CIMTinSimpleRenderer):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTerrainPointAttributeGraduatedRenderer(CIMTinColorRampRenderer):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTerrainPointAttributeUniqueRenderer(CIMTinUniqueValueRenderer):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTerrainPointElevationRenderer(CIMTinColorRampRenderer):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTinBreaklineRenderer(CIMTinUniqueValueRenderer):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTinEdgeRenderer(CIMTinSimpleRenderer):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTinFaceRenderer(CIMTinSimpleRenderer):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTinFaceValueRenderer(CIMTinUniqueValueRenderer):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTinNodeRenderer(CIMTinSimpleRenderer):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTinNodeValueRenderer(CIMTinUniqueValueRenderer):
    def __init__(self, *args, **Kwargs) -> None: ...
