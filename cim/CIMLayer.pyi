from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from .CIMCore import CIMDefinition as CIMDefinition
from .CIMVectorLayers import CIMDataConnection as CIMDataConnection
from _typeshed import Incomplete

class CIM3DLayerProperties:
    castShadows: bool
    isLayerLit: bool
    layerFaceCulling: Incomplete
    maxDistance: float
    maxPreloadDistance: float
    minDistance: float
    minPreloadDistance: float
    preloadTextureCutoffHigh: float
    preloadTextureCutoffLow: float
    textureCutoffHigh: float
    textureCutoffLow: float
    textureDownscalingFactor: int
    useCompressedTextures: bool
    verticalExaggeration: float
    exaggerationMode: Incomplete
    verticalUnit: Incomplete
    depthPriority: int
    lighting: Incomplete
    optimizeMarkerTransparency: bool
    useDepthWritingForTransparency: bool
    enable2DSymbolPerspectiveScaling: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDefinitionFilter:
    name: Incomplete
    definitionExpression: Incomplete
    geometryURI: Incomplete
    spatialReference: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDisplayEffect:
    name: Incomplete
    enabled: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMElementStorage:
    elements: Incomplete
    spatialReference: Incomplete
    symbols: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMEyeDomeLighting:
    isEnabled: bool
    strength: float
    radius: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFeatureLayerEffect:
    whereClause: Incomplete
    includedFeaturesEffects: Incomplete
    excludedFeaturesEffects: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLayerEffect:
    effects: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLayerElevationSurface:
    offsetZ: float
    elevationSurfaceLayerURI: Incomplete
    isRelativeToScene: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLayerScaleVisibilityOptions:
    savedMaxScale: float
    savedMinScale: float
    showLayerAtAllScales: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLayerTemplate:
    layerTemplateId: Incomplete
    parameters: Incomplete
    dataURI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSubLayerBase:
    description: Incomplete
    expanded: bool
    maxScale: int
    minScale: int
    name: Incomplete
    showLegends: bool
    subLayerID: Incomplete
    visibility: bool
    serviceLayerID: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSymbolLayerDrawing:
    symbolLayers: Incomplete
    useSymbolLayerDrawing: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSymbolLayerIdentifier:
    symbolLayerName: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBaseLayer(CIMDefinition):
    attribution: Incomplete
    description: Incomplete
    layerElevation: str
    expanded: bool
    layer3DProperties: str
    layerMasks: Incomplete
    layerType: Incomplete
    maxScale: float
    minScale: float
    layerScaleVisibilityOptions: str
    showLegends: bool
    transparency: float
    visibility: bool
    displayCacheType: Incomplete
    maxDisplayCacheAge: float
    layerTemplate: str
    popupInfo: str
    showPopups: bool
    serviceLayerID: int
    charts: Incomplete
    searchable: bool
    refreshRate: float
    refreshRateUnit: Incomplete
    showMapTips: bool
    customProperties: Incomplete
    webMapLayerID: Incomplete
    blendingMode: Incomplete
    allowDrapingOnIntegratedMesh: bool
    rasterizeOnExport: bool
    useVisibilityTimeExtent: bool
    visibilityTimeExtent: Incomplete
    enableLayerEffects: bool
    layerEffects: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKMLDataConnection(CIMDataConnection):
    customParameters: Incomplete
    kMLURI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMColorDisplayEffect(CIMDisplayEffect):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMCompositeSubLayer(CIMSubLayerBase):
    subLayers: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMContrastEffect(CIMColorDisplayEffect):
    strength: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMElevationSurfaceLayer(CIMBaseLayer):
    elevationSourceLayers: Incomplete
    elevationMode: Incomplete
    verticalExaggeration: float
    color: str
    enableSurfaceShading: bool
    surfaceTINShadingMode: Incomplete
    useSurfaceEffect: bool
    surfaceEffect: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGAITErrorLayer(CIMBaseLayer):
    errorWorkspaceConnection: str
    sourceLayers: Incomplete
    pointLayer: Incomplete
    lineLayer: Incomplete
    polygonLayer: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeodatabaseErrorLayer(CIMBaseLayer):
    standaloneTables: Incomplete
    pointLayer: Incomplete
    lineLayer: Incomplete
    polygonLayer: Incomplete
    objectTable: Incomplete
    workspaceConnection: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGraphicsLayer(CIMBaseLayer):
    elementStorageURI: Incomplete
    referenceScale: float
    barrierWeight: Incomplete
    snappable: bool
    selectable: bool
    showInvisibleGraphics: bool
    invisibleGraphicsColor: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGrayScaleEffect(CIMColorDisplayEffect):
    strength: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGroupLayer(CIMBaseLayer):
    standaloneTables: Incomplete
    sublayerVisibilityMode: Incomplete
    layers: Incomplete
    symbolLayerDrawing: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMHueRotateEffect(CIMColorDisplayEffect):
    angle: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMInvertEffect(CIMColorDisplayEffect):
    strength: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKMLLayer(CIMBaseLayer):
    dataConnection: str
    selectable: bool
    selectionColor: str
    useSelectionColor: bool
    labelVisibility: bool
    textSymbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRasterDisplayEffect(CIMDisplayEffect):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSaturateEffect(CIMColorDisplayEffect):
    strength: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMScaleDependentLayerEffect(CIMLayerEffect):
    scale: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSepiaEffect(CIMColorDisplayEffect):
    strength: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSubLayer(CIMSubLayerBase):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTopologyLayer(CIMBaseLayer):
    allLayers: Incomplete
    topologyConnection: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTransparencyEffect(CIMColorDisplayEffect):
    strength: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBloomEffect(CIMRasterDisplayEffect):
    radius: float
    threshold: float
    intensity: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBlurEffect(CIMRasterDisplayEffect):
    blurRadius: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBrightnessEffect(CIMColorDisplayEffect):
    strength: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDropShadowEffect(CIMRasterDisplayEffect):
    xOffset: float
    yOffset: float
    shadowRadius: float
    color: str
    def __init__(self, *args, **Kwargs) -> None: ...
