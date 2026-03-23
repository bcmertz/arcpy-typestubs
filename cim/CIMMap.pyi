from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from .CIMCore import CIMDefinition as CIMDefinition
from _typeshed import Incomplete

class CIMAltitudeParams:
    altitudeValue: int
    mode: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMAnimationScreenGraphic:
    graphic: str
    alias: Incomplete
    keyframes: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMAnimationScreenGraphicKeyframe:
    trackTime: float
    anchorX: float
    anchorY: float
    transparency: float
    scale: float
    elementWidth: float
    elementHeight: float
    rotation: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBookmark:
    name: Incomplete
    groupName: Incomplete
    thumbnailImagePath: Incomplete
    camera: str
    location: Incomplete
    timeExtent: Incomplete
    timeRelation: Incomplete
    rangeExtent: str
    layerRangeExtents: Incomplete
    description: Incomplete
    videoURI: Incomplete
    videoElapsedTime: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDatumTransform:
    forward: bool
    geoTransformation: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMEditingElevation:
    captureMode: Incomplete
    constantValue: float
    constantValueUnit: Incomplete
    elevationSurfaceLayerURI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMEditingTemplateCollectionItem:
    name: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMExploratoryAnalysisDefinition:
    iD: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFacilityLayerProperties:
    layerURI: Incomplete
    subLayerID: int
    siteIDField: Incomplete
    facilityIDField: Incomplete
    nameField: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFieldMapping:
    sourceURI: Incomplete
    targetURI: Incomplete
    mappingExpressionInfo: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFloorAwareMapProperties:
    siteLayerProperties: str
    facilityLayerProperties: str
    levelLayerProperties: str
    defaultFloorFilterSettings: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFloorFilterSettings:
    selectedSiteID: Incomplete
    selectedFacilityID: Incomplete
    selectedLevelID: Incomplete
    enabled: bool
    minimized: bool
    longNames: bool
    pinnedLevels: bool
    siteFacilityIDs: Incomplete
    siteLevelIDs: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeotrigger:
    name: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeotriggerFeed:
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeotriggerFenceFilter:
    whereClause: Incomplete
    geometryURI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeotriggerFenceParameters:
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeotriggerNotificationProperties:
    expressionInfo: str
    requestedActions: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGroundToGridCorrection:
    enabled: bool
    useDirection: bool
    useScale: bool
    direction: float
    scaleType: Incomplete
    constantScaleFactor: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMIPSAppleIPSConfiguration:
    enabled: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMIPSAwareMapProperties:
    iPSRecordingsLayerURI: Incomplete
    iPSPositioningTableProperties: str
    iPSPositioningDataServiceProperties: str
    iPSConfiguration: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMIPSConfiguration:
    pathSnapping: str
    smoothing: str
    gNSS: str
    appleIPS: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMIPSGNSSConfiguration:
    enabled: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMIPSPathSnappingConfiguration:
    enabled: bool
    distance: float
    distanceUnit: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMIPSPositioningDataServiceProperties:
    portalItem: str
    workspaceConnection: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMIPSPositioningTableProperties:
    tableURI: Incomplete
    selectedGlobalID: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMIPSSmoothingConfiguration:
    enabled: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMIlluminationProperties:
    ambientLight: float
    sunPositionX: float
    sunPositionY: float
    sunPositionZ: float
    showAtmosphericEffects: bool
    showShadows3D: bool
    dateTime: Incomplete
    illuminationSource: Incomplete
    sunAzimuth: float
    sunAltitude: float
    showStars: bool
    enableAmbientOcclusion: bool
    enableEyeDomeLighting: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKeyframeAnalysis:
    analysis: str
    transition: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKeyframeCamera:
    camera: str
    headingTransition: Incomplete
    pitchTransition: Incomplete
    rollTransition: Incomplete
    scaleTransition: Incomplete
    xTransition: Incomplete
    yTransition: Incomplete
    zTransition: Incomplete
    transitionScale: float
    cameraTransitionMode: Incomplete
    lookAt: Incomplete
    adjustedCameraPath: Incomplete
    fieldOfView: float
    fieldOfViewTransition: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKeyframeElevationSource:
    sourceID: Incomplete
    visible: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKeyframeLayer:
    layerURI: Incomplete
    transparency: float
    transparencyTransition: Incomplete
    visible: bool
    swipeDirection: Incomplete
    swipePercent: float
    verticalExaggeration: float
    zOffset: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKeyframeRange:
    range: str
    rangeRelation: Incomplete
    minTransition: Incomplete
    maxTransition: Incomplete
    isExclusion: bool
    layerRangeExtents: Incomplete
    layerRangeTransition: Incomplete
    activeRangeLayer: Incomplete
    activeRangeName: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKeyframeSurface:
    surfaceID: Incomplete
    transition: Incomplete
    verticalExaggeration: float
    visible: bool
    swipeDirection: Incomplete
    swipePercent: float
    baseSources: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKeyframeTime:
    time: Incomplete
    timeRelation: Incomplete
    endTimeTransition: Incomplete
    startTimeTransition: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKeyframeVoxelPlane:
    visible: bool
    position: float
    orientation: float
    tilt: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLevelLayerProperties:
    layerURI: Incomplete
    subLayerID: int
    facilityIDField: Incomplete
    levelIDField: Incomplete
    shortNameField: Incomplete
    longNameField: Incomplete
    levelNumberField: Incomplete
    verticalOrderField: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLocator:
    locatorType: Incomplete
    name: Incomplete
    locatorURI: Incomplete
    suggestionsEnabled: bool
    enabled: bool
    suggestionsSupported: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMapGeotriggerProperties:
    geotriggers: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMapStereoProperties:
    leftImage: str
    rightImage: str
    sourceType: Incomplete
    stereoModelCollection: str
    leftImageID: int
    rightImageID: int
    leftImageColorizer: str
    rightImageColorizer: str
    adjustColorizersInSync: bool
    isInverted: bool
    stereoModelDisplayMode: Incomplete
    orientation: Incomplete
    terrainFollowingDEM: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMapTimeDisplay:
    currentTimeExtent: Incomplete
    defaultTimeInterval: float
    defaultTimeIntervalUnits: Incomplete
    defaultTimeWindow: float
    fullTimeExtent: Incomplete
    timeReference: Incomplete
    timeValue: Incomplete
    hasLiveData: bool
    timeRelation: Incomplete
    uniqueTimes: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMScale:
    value: float
    alias: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMScaleFormat:
    formatType: Incomplete
    separator: Incomplete
    reverseOrder: bool
    decimalPlacesThreshold: float
    decimalPlaces: int
    showThousandSeparator: bool
    pageUnits: Incomplete
    pageUnitValue: float
    equalsSign: Incomplete
    mapUnits: Incomplete
    capitalizeUnits: bool
    abbreviateUnits: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSiteLayerProperties:
    layerURI: Incomplete
    subLayerID: int
    siteIDField: Incomplete
    nameField: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSliderSettings:
    sliderExtent: str
    sliderExtentLocked: bool
    startValueLocked: bool
    endValueLocked: bool
    flipVertically: bool
    useWindowValue: bool
    windowValue: float
    windowUnit: Incomplete
    stepUsesWindow: bool
    stepIntervalValue: float
    stepIntervalUnit: Incomplete
    stepCount: float
    stepOption: Incomplete
    stepLayerURI: Incomplete
    playWaitSeconds: float
    playForward: bool
    playRepeats: bool
    playReverses: bool
    fullExtentOption: Incomplete
    fullExtentLayerURI: Incomplete
    fullExtentCustomRange: str
    interactionMode: Incomplete
    useTimeSnapping: bool
    timeSnapMode: Incomplete
    singleTimeSnapUnit: Incomplete
    aliasExpressionLayerURI: Incomplete
    isMinimized: bool
    ignoreInactiveValues: bool
    liveMode: bool
    liveModeOffsetDirection: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSnappingProperties:
    xYTolerance: float
    xYToleranceUnit: Incomplete
    zTolerance: float
    zToleranceEnabled: bool
    snapToSketchEnabled: bool
    snapRequestType: Incomplete
    geometricFeedbackColor: str
    visualFeedbackColor: str
    isZSnappingEnabled: bool
    snapTipDisplayParts: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSurfaceEffect:
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMViewCamera:
    heading: int
    pitch: int
    roll: int
    scale: int
    x: int
    y: int
    z: int
    viewportHeight: float
    viewportWidth: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMViewKeyframe:
    trackTime: float
    camera: str
    layers: Incomplete
    range: str
    time: str
    surfaces: Incomplete
    exploratoryAnalysis: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMViewTrack:
    name: Incomplete
    keyframes: Incomplete
    screenGraphics: Incomplete
    referenceResolutionWidth: int
    referenceResolutionHeight: int
    exportType: Incomplete
    frameRate: int
    dataRateFactor: int
    startFrameTime: int
    endFrameTime: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMap(CIMDefinition):
    defaultCamera: str
    illumination: str
    layers: Incomplete
    stereoProperties: str
    defaultViewingMode: Incomplete
    mapType: Incomplete
    rangeSliderSettings: str
    timeSliderSettings: str
    animationViewTracks: Incomplete
    animationActiveTrackName: Incomplete
    locators: Incomplete
    mapContexts: Incomplete
    standaloneVideos: Incomplete
    customProperties: Incomplete
    linkCharts: Incomplete
    timelines: Incomplete
    knowledgeGraphLinkChartProperties: str
    groundElevationSurfaceLayer: Incomplete
    customElevationSurfaceLayers: Incomplete
    defaultVisualEffect: str
    defaultCameraEffect: str
    defaultPostprocessingEffects: Incomplete
    defaultColorVisionDeficiencyMode: Incomplete
    weatherEffect: str
    standaloneTables: Incomplete
    backgroundColor: str
    bookmarks: Incomplete
    clipToFullExtent: bool
    attribution: Incomplete
    customFullExtent: Incomplete
    datumTransforms: Incomplete
    defaultExtent: Incomplete
    defaultScale: float
    defaultGlobeTransparency: float
    defaultRotation: float
    description: Incomplete
    generalPlacementProperties: str
    snappingProperties: str
    spatialReference: Incomplete
    surfaceColor: str
    timeDisplay: str
    enableNavigationBelowGround: bool
    referenceScale: float
    enableWraparound: bool
    includeMaximumInScaleRanges: bool
    colorModel: Incomplete
    scales: Incomplete
    snapToScales: bool
    scaleFormat: str
    scaleDisplayFormat: Incomplete
    hVDatumTransforms: Incomplete
    useServiceLayerIDs: bool
    groundToGridCorrection: str
    clippingMode: Incomplete
    customClippingShapeURI: Incomplete
    layersExcludedFromClipping: Incomplete
    surfacesExcludedFromClipping: Incomplete
    clippingAreaBorderSymbol: str
    nearPlaneClipDistanceMode: Incomplete
    nearPlaneClipDistance: float
    editingElevation: str
    editingTemplateCollection: str
    fieldMappings: Incomplete
    rGBColorProfile: Incomplete
    cMYKColorProfile: Incomplete
    simulateOverprint: bool
    floorAwareMapProperties: str
    iPSAwareMapProperties: str
    autoFillFeatureCache: bool
    geotriggerProperties: str
    useMasking: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMAnimationScreenGraphicGroup(CIMAnimationScreenGraphic):
    children: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBorderlandsEffect(CIMSurfaceEffect):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMContouringEffect(CIMSurfaceEffect):
    distance: float
    useRealWorldSizeThickness: bool
    thickness: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMCutAndFillEADefinition(CIMExploratoryAnalysisDefinition):
    cutFillPlane: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMEditingTemplateCollection(CIMEditingTemplateCollectionItem):
    contents: Incomplete
    expanded: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMEditingTemplateReference(CIMEditingTemplateCollectionItem):
    layerURI: Incomplete
    templateName: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFenceGeotrigger(CIMGeotrigger):
    feed: str
    fenceNotificationRule: Incomplete
    feedAccuracyMode: Incomplete
    enterExitRule: Incomplete
    fenceParameters: str
    notificationOptions: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeotriggerDeviceLocationFeed(CIMGeotriggerFeed):
    filterExpression: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGeotriggerFeatureFenceParameters(CIMGeotriggerFenceParameters):
    bufferDistance: float
    sourceDataConnection: str
    sourceLayer: Incomplete
    filter: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMKeyframeVoxelLayer(CIMKeyframeLayer):
    variableName: Incomplete
    showSurface: bool
    dataFilterMax: float
    dataFilterMin: float
    isosurfaces: Incomplete
    sections: Incomplete
    lockedSections: Incomplete
    slices: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLineOfSightEADefinition(CIMExploratoryAnalysisDefinition):
    observer: Incomplete
    targets: Incomplete
    maximumDistance: float
    minimumDistance: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSliceBoxEADefinition(CIMExploratoryAnalysisDefinition):
    centerPoint: Incomplete
    heading: int
    height: int
    width: int
    depth: int
    cullDirection: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSliceCylinderEADefinition(CIMExploratoryAnalysisDefinition):
    centerPoint: Incomplete
    heading: float
    pitch: float
    height: float
    width: float
    cullDirection: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSlicePlaneEADefinition(CIMExploratoryAnalysisDefinition):
    centerPoint: Incomplete
    heading: float
    pitch: float
    height: float
    width: float
    cullDirection: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSliceSphereEADefinition(CIMExploratoryAnalysisDefinition):
    centerPoint: Incomplete
    radius: float
    cullDirection: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMViewDomeEADefinition(CIMExploratoryAnalysisDefinition):
    observer: Incomplete
    maximumDistance: float
    minimumDistance: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMViewshedEADefinition(CIMExploratoryAnalysisDefinition):
    observer: Incomplete
    heading: float
    pitch: float
    horizontalAngle: float
    verticalAngle: float
    maximumDistance: float
    minimumDistance: float
    def __init__(self, *args, **Kwargs) -> None: ...
