from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from _typeshed import Incomplete

class CIMGeneralPlacementProperties:
    drawUnplacedLabels: bool
    invertedLabelTolerance: float
    rotateLabelWithDisplay: bool
    unplacedLabelColor: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLabelClass:
    expressionTitle: Incomplete
    expression: Incomplete
    expressionEngine: Incomplete
    featuresToLabel: Incomplete
    maplexLabelPlacementProperties: str
    maximumScale: float
    minimumScale: float
    name: Incomplete
    priority: int
    standardLabelPlacementProperties: str
    textSymbol: str
    useCodedValue: bool
    whereClause: Incomplete
    visibility: bool
    iD: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLabelClassProperties:
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLabelPlacementProperties:
    featureType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMaplexDictionary:
    name: Incomplete
    maplexDictionary: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMaplexDictionaryEntry:
    abbreviation: Incomplete
    text: Incomplete
    maplexAbbreviationType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMaplexExternalZonePriorities:
    aboveLeft: int
    aboveCenter: int
    aboveRight: int
    centerRight: int
    belowRight: int
    belowCenter: int
    belowLeft: int
    centerLeft: int
    center: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMaplexInternalZonePriorities:
    aboveLeft: int
    aboveCenter: int
    aboveRight: int
    centerRight: int
    belowRight: int
    belowCenter: int
    belowLeft: int
    centerLeft: int
    center: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMaplexKeyNumberGroup:
    delimiterCharacter: Incomplete
    horizontalAlignment: Incomplete
    maximumNumberOfLines: int
    minimumNumberOfLines: int
    name: Incomplete
    numberResetType: Incomplete
    keyNumberMethod: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMaplexLabelStackingProperties:
    stackAlignment: Incomplete
    maximumNumberOfLines: int
    minimumNumberOfCharsPerLine: int
    maximumNumberOfCharsPerLine: int
    separators: Incomplete
    trimStackingSeparators: bool
    preferToStackLongLabels: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMaplexOffsetAlongLineProperties:
    placementMethod: Incomplete
    labelAnchorPoint: Incomplete
    distance: float
    tolerance: float
    distanceUnit: Incomplete
    useLineDirection: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMaplexRotationProperties:
    enable: bool
    rotationType: Incomplete
    rotationField: Incomplete
    perpendicularToAngle: bool
    alignLabelToAngle: bool
    alignmentType: Incomplete
    additionalAngle: int
    rotationExpressionInfo: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMaplexStackingSeparator:
    separator: Incomplete
    visible: bool
    splitForced: bool
    splitAfter: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMaplexStrategyPriorities:
    stacking: int
    overrun: int
    fontCompression: int
    fontReduction: int
    abbreviation: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStandardLineLabelPosition:
    produceCurvedLabels: bool
    above: bool
    below: bool
    onTop: bool
    left: bool
    right: bool
    inLine: bool
    atStart: bool
    atEnd: bool
    parallel: bool
    perpendicular: bool
    horizontal: bool
    offset: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStandardLineLabelPriorities:
    aboveBefore: int
    aboveStart: int
    aboveAlong: int
    aboveEnd: int
    aboveAfter: int
    centerBefore: int
    centerStart: int
    centerAlong: int
    centerEnd: int
    centerAfter: int
    belowBefore: int
    belowStart: int
    belowAlong: int
    belowEnd: int
    belowAfter: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStandardPointPlacementPriorities:
    aboveLeft: int
    aboveCenter: int
    aboveRight: int
    centerLeft: int
    centerRight: int
    belowLeft: int
    belowCenter: int
    belowRight: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMaplexGeneralPlacementProperties(CIMGeneralPlacementProperties):
    allowBorderOverlap: bool
    dictionaries: Incomplete
    keyNumberGroups: Incomplete
    placementQuality: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMaplexLabelPlacementProperties(CIMLabelPlacementProperties):
    alignLabelToLineDirection: bool
    allowAsymmetricOverrun: bool
    allowStraddleStacking: bool
    alternateLabelExpressionInfo: str
    avoidOverlappingLabeledPolygonsAsIfHoles: bool
    avoidPolygonHoles: bool
    backgroundLabel: bool
    boundaryLabelingAllowHoles: bool
    boundaryLabelingAllowSingleSided: bool
    boundaryLabelingSingleSidedOnLine: bool
    canAbbreviateLabel: bool
    canFlipStackedStreetLabel: bool
    canKeyNumberLabel: bool
    canOverrunFeature: bool
    canPlaceLabelOnTopOfFeature: bool
    canPlaceLabelOutsidePolygon: bool
    canReduceFontSize: bool
    canReduceLeading: bool
    canRemoveOverlappingLabel: bool
    canShiftPointLabel: bool
    canStackLabel: bool
    canTruncateLabel: bool
    canUseAlternateLabelExpression: bool
    centerLabelAnchorType: Incomplete
    connectionType: Incomplete
    constrainOffset: Incomplete
    contourAlignmentType: Incomplete
    contourLadderType: Incomplete
    contourMaximumAngle: int
    dictionaryName: Incomplete
    enableConnection: bool
    enablePointPlacementPriorities: bool
    enablePolygonFixedPosition: bool
    enableSecondaryOffset: bool
    featureWeight: int
    fontHeightReductionLimit: float
    fontHeightReductionStep: float
    fontWidthReductionLimit: float
    fontWidthReductionStep: float
    graticuleAlignment: bool
    graticuleAlignmentType: Incomplete
    isLabelBufferHardConstraint: bool
    isMinimumSizeBasedOnArea: bool
    isOffsetFromFeatureGeometry: bool
    keyNumberGroupName: Incomplete
    labelBuffer: int
    labelLargestPolygon: bool
    labelPriority: int
    labelStackingProperties: str
    lineFeatureType: Incomplete
    linePlacementMethod: Incomplete
    maximumCharacterSpacing: float
    maximumLabelOverrun: float
    maximumLabelOverrunUnit: Incomplete
    maximumWordSpacing: float
    measureFromClippedFeatureGeometry: bool
    minimumEndOfStreetClearance: float
    minimumFeatureSizeUnit: Incomplete
    minimumRepetitionInterval: float
    minimumSizeForLabeling: float
    multiPartOption: Incomplete
    neverRemoveLabel: bool
    offsetAlongLineProperties: str
    pointExternalZonePriorities: str
    pointPlacementMethod: Incomplete
    polygonAnchorPointType: Incomplete
    polygonBoundaryWeight: int
    polygonExternalZones: str
    polygonFeatureType: Incomplete
    polygonInternalZones: str
    polygonPlacementMethod: Incomplete
    preferHorizontalPlacement: bool
    preferLabelNearJunction: bool
    preferLabelNearJunctionClearance: float
    preferLabelNearMapBorder: bool
    preferLabelNearMapBorderClearance: float
    preferredEndOfStreetClearance: float
    primaryOffset: float
    primaryOffsetUnit: Incomplete
    removeAmbiguousLabels: Incomplete
    removeExtraLineBreaks: bool
    removeExtraWhiteSpace: bool
    repeatLabel: bool
    repetitionIntervalUnit: Incomplete
    rotationProperties: str
    secondaryOffset: float
    secondaryOffsetMaximum: float
    secondaryOffsetMinimum: float
    secondaryOffsetUnit: Incomplete
    spreadCharacters: bool
    spreadWords: bool
    strategyPriorities: str
    thinDuplicateLabels: bool
    thinningDistance: float
    thinningDistanceUnit: Incomplete
    truncationMarkerCharacter: Incomplete
    truncationMinimumLength: int
    truncationPreferredCharacters: Incomplete
    useExactSymbolOutline: bool
    truncationExcludedCharacters: Incomplete
    polygonAnchorPointPerimeterInset: float
    polygonAnchorPointPerimeterInsetUnit: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStandardGeneralPlacementProperties(CIMGeneralPlacementProperties):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMStandardLabelPlacementProperties(CIMLabelPlacementProperties):
    featureWeight: Incomplete
    labelWeight: Incomplete
    numLabelsOption: Incomplete
    lineLabelPosition: str
    lineLabelPriorities: str
    pointPlacementMethod: Incomplete
    pointPlacementPriorities: str
    pointPlacementAngles: Incomplete
    bufferRatio: float
    lineOffset: float
    maxDistanceFromTarget: float
    rotationType: Incomplete
    rotationField: Incomplete
    perpendicularToAngle: bool
    polygonPlacementMethod: Incomplete
    placeOnlyInsidePolygon: bool
    allowOverlappingLabels: bool
    def __init__(self, *args, **Kwargs) -> None: ...
