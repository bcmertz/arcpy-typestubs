from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from _typeshed import Incomplete

class CIM3DMarkerGraphic:
    primitiveType: Incomplete
    diffuseColor: str
    shapeVerticesCollectionIndex: int
    isSubstitutionAllowed: bool
    materialProperties: str
    entityID: int
    offsetIntoShapeVertices: int
    countOfShapeVertices: int
    patchPriority: int
    textureIndex: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIM3DMarkerLOD:
    markerGraphics: Incomplete
    entityNames: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIM3DSymbolProperties:
    dominantSizeAxis3D: Incomplete
    rotationOrder3D: Incomplete
    scaleZ: float
    scaleY: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMAnimatedSymbolProperties:
    playAnimation: bool
    reverseAnimation: bool
    randomizeStartTime: bool
    randomizeStartSeed: int
    startTimeOffset: int
    duration: float
    endingDuration: float
    useEndingDuration: bool
    repeatType: Incomplete
    repeatDelay: float
    primitiveName: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMCGAAttribute:
    name: Incomplete
    cGAAttributeType: Incomplete
    value: Incomplete
    values: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMCallout:
    leaderTolerance: int
    leaderOffset: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartPart:
    value: float
    polygonSymbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMClippingPath:
    clippingType: Incomplete
    path: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMColorSubstitution:
    oldColor: str
    newColor: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMCompositeTextPartPosition:
    horizontalAlignment: Incomplete
    verticalAlignment: Incomplete
    xOffset: float
    yOffset: float
    splitOffset: float
    isPartWithinCalloutBox: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFontVariation:
    tagName: Incomplete
    value: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeometricEffect:
    primitiveName: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMarkerGraphic:
    geometry: Incomplete
    symbol: str
    textString: Incomplete
    primitiveName: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMarkerPlacement:
    primitiveName: Incomplete
    placePerPart: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMaterialProperties:
    specularColor: str
    shininess: float
    externalColorMixMode: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMObjectMarker3DLOD:
    faceCount: int
    modelURI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMShapeVertex:
    position: Incomplete
    normalVector: Incomplete
    textureCoordinate: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMShapeVertices:
    indices: int
    shapes: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSymbol:
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSymbolLayer:
    effects: Incomplete
    enable: bool
    name: Incomplete
    colorLocked: bool
    primitiveName: Incomplete
    overprint: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTextMargin:
    left: float
    right: float
    top: float
    bottom: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBalloonCallout(CIMCallout):
    balloonStyle: Incomplete
    backgroundSymbol: str
    margin: str
    useFixedDartWidth: bool
    fixedDartWidth: float
    useDartSymbol: bool
    dartSymbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMCompositeCallout(CIMCallout):
    cornerRadius: float
    backgroundSymbol: str
    margin: str
    dartWidth: float
    dartSymbol: str
    snapLeaderToCornersOnly: bool
    leaderLinePercentage: float
    leaderLineSymbol: str
    shadowSymbol: str
    shadowXOffset: float
    shadowYOffset: float
    middle: str
    topLeft: str
    top: str
    topRight: str
    right: str
    left: str
    bottomLeft: str
    bottom: str
    bottomRight: str
    floating: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFill(CIMSymbolLayer):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeometricEffectAddControlPoints(CIMGeometricEffect):
    angleTolerance: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeometricEffectArrow(CIMGeometricEffect):
    arrowType: Incomplete
    width: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeometricEffectBuffer(CIMGeometricEffect):
    size: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeometricEffectCircularSector(CIMGeometricEffect):
    startAngle: int
    endAngle: int
    radius: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeometricEffectControlMeasureLine(CIMGeometricEffect):
    rule: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeometricEffectCut(CIMGeometricEffect):
    beginCut: int
    endCut: int
    middleCut: int
    invert: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeometricEffectDashes(CIMGeometricEffect):
    customEndingOffset: float
    dashTemplate: Incomplete
    lineDashEnding: Incomplete
    offsetAlongLine: int
    controlPointEnding: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeometricEffectDonut(CIMGeometricEffect):
    method: Incomplete
    option: Incomplete
    width: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeometricEffectEnclosingPolygon(CIMGeometricEffect):
    method: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeometricEffectExtension(CIMGeometricEffect):
    deflection: int
    origin: Incomplete
    length: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeometricEffectJog(CIMGeometricEffect):
    angle: float
    length: float
    position: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeometricEffectLocalizerFeather(CIMGeometricEffect):
    style: Incomplete
    length: int
    width: int
    angle: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeometricEffectMove(CIMGeometricEffect):
    offsetX: int
    offsetY: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeometricEffectOffset(CIMGeometricEffect):
    method: Incomplete
    offset: int
    option: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeometricEffectOffsetHatch(CIMGeometricEffect):
    length: int
    spacing: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeometricEffectOffsetTangent(CIMGeometricEffect):
    method: Incomplete
    offset: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeometricEffectRadial(CIMGeometricEffect):
    angle: int
    length: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeometricEffectRegularPolygon(CIMGeometricEffect):
    angle: int
    edges: int
    radius: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeometricEffectReverse(CIMGeometricEffect):
    reverse: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeometricEffectRotate(CIMGeometricEffect):
    angle: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeometricEffectScale(CIMGeometricEffect):
    xScaleFactor: float
    yScaleFactor: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeometricEffectSuppress(CIMGeometricEffect):
    suppress: bool
    invert: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeometricEffectTaperedPolygon(CIMGeometricEffect):
    fromWidth: int
    length: int
    toWidth: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeometricEffectWave(CIMGeometricEffect):
    amplitude: int
    period: int
    seed: int
    waveform: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGradientFill(CIMFill):
    angle: int
    colorRamp: str
    gradientMethod: Incomplete
    gradientSize: float
    gradientSizeUnits: Incomplete
    gradientType: Incomplete
    interval: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMHatchFill(CIMFill):
    lineSymbol: str
    offsetX: int
    rotation: int
    separation: int
    offsetY: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLineCallout(CIMCallout):
    leaderLineSymbol: str
    gap: int
    lineStyle: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMarker(CIMSymbolLayer):
    anchorPoint: Incomplete
    anchorPointUnits: Incomplete
    angleX: float
    angleY: float
    dominantSizeAxis3D: Incomplete
    offsetX: float
    offsetY: float
    offsetZ: float
    rotateClockwise: bool
    rotation: float
    size: float
    billboardMode3D: Incomplete
    markerPlacement: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMarker3D(CIMMarker):
    lODLevels: Incomplete
    lODDistances: Incomplete
    width: float
    depth: float
    color: str
    isRestricted: bool
    shapeVertices: Incomplete
    textures: Incomplete
    thumbnail: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMarkerFillPlacement(CIMMarkerPlacement):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMarkerPlacementAroundPolygon(CIMMarkerFillPlacement):
    position: Incomplete
    offset: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMarkerPlacementInsidePolygon(CIMMarkerFillPlacement):
    gridAngle: int
    gridType: Incomplete
    offsetX: int
    randomness: int
    seed: int
    shiftOddRows: bool
    stepX: int
    stepY: int
    offsetY: int
    clipping: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMarkerPlacementPolygonCenter(CIMMarkerFillPlacement):
    method: Incomplete
    offsetX: int
    offsetY: int
    clipAtBoundary: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMarkerStrokePlacement(CIMMarkerPlacement):
    angleToLine: bool
    keepUpright: bool
    offset: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMaterialSymbolLayer(CIMSymbolLayer):
    color: str
    materialMode: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMeshEdge(CIMSymbolLayer):
    color: str
    thresholdAngle: int
    applyThresholdAngleToBothSidesOfFaces: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMultiLayerSymbol(CIMSymbol):
    effects: Incomplete
    symbolLayers: Incomplete
    thumbnailURI: Incomplete
    useRealWorldSymbolSizes: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMObjectMarker3D(CIMMarker):
    modelURI: Incomplete
    width: float
    depth: float
    tintColor: str
    isRestricted: bool
    thumbnail: Incomplete
    useAnchorPoint: bool
    lODs: Incomplete
    primitiveShapeType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPictureFill(CIMFill):
    url: Incomplete
    offsetX: int
    offsetY: int
    rotation: int
    scaleX: int
    height: int
    textureFilter: Incomplete
    colorSubstitutions: Incomplete
    tintColor: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPictureMarker(CIMMarker):
    colorSubstitutions: Incomplete
    depth3D: float
    invertBackfaceTexture: bool
    scaleX: float
    textureFilter: Incomplete
    tintColor: str
    url: Incomplete
    verticalOrientation3D: bool
    animatedSymbolProperties: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPointSymbol(CIMMultiLayerSymbol):
    callout: str
    haloSize: float
    haloSymbol: str
    primitiveName: Incomplete
    scaleX: int
    symbol3DProperties: str
    angle: float
    angleAlignment: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPointSymbolCallout(CIMLineCallout):
    pointSymbol: str
    backgroundScale: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPolygonSymbol(CIMMultiLayerSymbol):
    angleAlignment: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMProceduralSymbolLayer(CIMSymbolLayer):
    attributes: Incomplete
    rulePackage: Incomplete
    rulePackageName: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSimpleLineCallout(CIMCallout):
    lineSymbol: str
    autoSnap: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSolidFill(CIMFill):
    color: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSolidMeshEdge(CIMMeshEdge):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStroke(CIMSymbolLayer):
    capStyle: Incomplete
    joinStyle: Incomplete
    lineStyle3D: Incomplete
    miterLimit: float
    width: int
    closeCaps3D: bool
    height3D: float
    anchor3D: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTextSymbol(CIMSymbol):
    angle: float
    angleX: float
    angleY: float
    blockProgression: Incomplete
    callout: str
    compatibilityMode: bool
    countryISO: Incomplete
    depth3D: float
    drawGlyphsAsGeometry: bool
    drawSoftHyphen: bool
    extrapolateBaselines: bool
    flipAngle: float
    fontEffects: Incomplete
    fontEncoding: Incomplete
    fontFamilyName: Incomplete
    fontStyleName: Incomplete
    fontType: Incomplete
    fontVariationSettings: Incomplete
    glyphRotation: float
    haloSize: float
    haloSymbol: str
    height: float
    hinting: Incomplete
    horizontalAlignment: Incomplete
    indentAfter: float
    indentBefore: float
    indentFirstLine: float
    kerning: bool
    languageISO: Incomplete
    letterSpacing: float
    letterWidth: float
    ligatures: bool
    lineGap: float
    lineGapType: Incomplete
    offsetX: float
    offsetY: float
    offsetZ: float
    shadowColor: str
    shadowOffsetX: float
    shadowOffsetY: float
    smallCaps: bool
    strikethrough: bool
    symbol: str
    symbol3DProperties: str
    textCase: Incomplete
    textDirection: Incomplete
    underline: bool
    verticalAlignment: Incomplete
    verticalGlyphOrientation: Incomplete
    wordSpacing: float
    billboardMode3D: Incomplete
    overprint: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVectorMarker(CIMMarker):
    depth3D: float
    frame: Incomplete
    markerGraphics: Incomplete
    verticalOrientation3D: bool
    scaleSymbolsProportionally: bool
    respectFrame: bool
    clippingPath: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMWaterFill(CIMFill):
    color: str
    waveStrength: Incomplete
    waterbodySize: Incomplete
    waveHasDirection: bool
    waveDirection: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMglTFMarker3D(CIMMarker):
    modelURI: Incomplete
    additionalModelURIs: Incomplete
    width: float
    depth: float
    tintColor: str
    isRestricted: bool
    thumbnail: Incomplete
    useAnchorPoint: bool
    animatedSymbolProperties: str
    primitiveShapeType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBackgroundCallout(CIMLineCallout):
    backgroundSymbol: str
    accentBarSymbol: str
    margin: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMCharacterMarker(CIMMarker):
    characterIndex: int
    depth3D: float
    fontFamilyName: Incomplete
    fontStyleName: Incomplete
    fontType: Incomplete
    fontVariationSettings: Incomplete
    scaleX: float
    symbol: str
    verticalOrientation3D: bool
    scaleSymbolsProportionally: bool
    respectFrame: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMChartMarker(CIMMarker):
    display3D: bool
    parts: Incomplete
    thickness3D: float
    tilt3D: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGradientStroke(CIMStroke):
    colorRamp: str
    gradientMethod: Incomplete
    gradientSize: float
    gradientSizeUnits: Incomplete
    gradientType: Incomplete
    interval: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLineSymbol(CIMMultiLayerSymbol):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMarkerPlacementAlongLine(CIMMarkerStrokePlacement):
    customEndingOffset: float
    endings: Incomplete
    offsetAlongLine: float
    placementTemplate: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMarkerPlacementAlongLineRandomSize(CIMMarkerPlacementAlongLine):
    randomization: Incomplete
    seed: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMarkerPlacementAlongLineSameSize(CIMMarkerPlacementAlongLine):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMarkerPlacementAlongLineVariableSize(CIMMarkerStrokePlacement):
    placementTemplate: Incomplete
    endings: Incomplete
    controlPointPlacement: Incomplete
    maxRandomOffset: int
    maxZoom: float
    minZoom: float
    numberOfSizes: int
    seed: int
    variationMethod: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMarkerPlacementAtExtremities(CIMMarkerStrokePlacement):
    extremityPlacement: Incomplete
    offsetAlongLine: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMarkerPlacementAtMeasuredUnits(CIMMarkerStrokePlacement):
    interval: int
    skipMarkerRate: int
    placeAtExtremities: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMarkerPlacementAtRatioPositions(CIMMarkerStrokePlacement):
    beginPosition: int
    endPosition: int
    flipFirst: bool
    positionArray: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMarkerPlacementOnLine(CIMMarkerStrokePlacement):
    relativeTo: Incomplete
    startPointOffset: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMarkerPlacementOnVertices(CIMMarkerStrokePlacement):
    placeOnControlPoints: bool
    placeOnEndPoints: bool
    placeOnRegularVertices: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMeshSymbol(CIMMultiLayerSymbol):
    animatedSymbolProperties: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPictureStroke(CIMStroke):
    colorSubstitutions: Incomplete
    textureFilter: Incomplete
    url: Incomplete
    tintColor: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPieChartMarker(CIMChartMarker):
    clockwise: bool
    showOutline: bool
    outlineSymbol: str
    aggregateSmallSlices: bool
    sliceAggregationThreshold: float
    aggregateSliceSymbol: str
    aggregateSliceLabel: Incomplete
    showInvalidValues: bool
    invalidValuesSymbol: str
    invalidValuesLabel: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSolidStroke(CIMStroke):
    color: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStackedBarChartMarker(CIMChartMarker):
    fixedLength: bool
    showOutline: bool
    outlineSymbol: str
    verticalBar: bool
    width: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBarChartMarker(CIMChartMarker):
    axesSymbol: str
    spacing: float
    verticalBars: bool
    width: float
    showAxes: bool
    def __init__(self, *args, **Kwargs) -> None: ...
