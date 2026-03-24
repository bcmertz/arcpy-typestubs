from _typeshed import Incomplete
from enum import Enum

class esriNumericAlignmentEnum(Enum):
    esriAlignRight = 0
    esriAlignLeft = 1

class esriRoundingOptionEnum(Enum):
    esriRoundNumberOfDecimals = 0
    esriRoundNumberOfSignificantDigits = 1

class esriDatasetType(Enum):
    esriDTAny = 0
    esriDTContainer = 1
    esriDTGeo = 2
    esriDTFeatureDataset = 3
    esriDTFeatureClass = 4
    esriDTPlanarGraph = 5
    esriDTGeometricNetwork = 6
    esriDTText = 7
    esriDTTable = 8
    esriDTRelationshipClass = 9
    esriDTRasterDataset = 10
    esriDTRasterBand = 11
    esriDTTin = 12
    esriDTCadDrawing = 13
    esriDTRasterCatalog = 14
    esriDTTopology = 15
    esriDTToolbox = 16
    esriDTTool = 17
    esriDTNetworkDataset = 18
    esriDTTerrain = 19
    esriDTRepresentationClass = 20
    esriDTCadastralFabric = 21
    esriDTSchematicDataset = 22
    esriDTLocator = 23
    esriDTMap = 24
    esriDTLayer = 25
    esriDTStyle = 26
    esriDTMosaicDataset = 27
    esriDTLasDataset = 28
    esriDTLayout = 29
    esriDTStandaloneTable = 30
    esriDTUtilityNetwork = 31
    esriDTDiagramDataset = 32
    esriDTDiagramFolder = 33
    esriDTNetworkDiagram = 34
    esriDTParcelDataset = 35
    esriDTStandaloneVideo = 36
    esriDTReport = 37
    esriDTBIMFile = 38

class esriTimeRelation(Enum):
    esriTimeRelationOverlaps = 0
    esriTimeRelationOverlapsStartWithinEnd = 1
    esriTimeRelationAfterStartOverlapsEnd = 2
    esriTimeRelationWithin = 3

class esriUnits(Enum):
    esriUnknownUnits = 0
    esriInches = 1
    esriPoints = 2
    esriFeet = 3
    esriYards = 4
    esriMiles = 5
    esriNauticalMiles = 6
    esriMillimeters = 7
    esriCentimeters = 8
    esriMeters = 9
    esriKilometers = 10
    esriDecimalDegrees = 11
    esriDecimeters = 12

class esriTimeUnits(Enum):
    esriTimeUnitsUnknown = 0
    esriTimeUnitsMilliseconds = 1
    esriTimeUnitsSeconds = 2
    esriTimeUnitsMinutes = 3
    esriTimeUnitsHours = 4
    esriTimeUnitsDays = 5
    esriTimeUnitsWeeks = 6
    esriTimeUnitsMonths = 7
    esriTimeUnitsYears = 8
    esriTimeUnitsDecades = 9
    esriTimeUnitsCenturies = 10

class esriBGLTextAAlias(Enum):
    esriBGLTextAAliasNone = 0
    esriBGLTextAAliasDefault = 1
    esriBGLTextAAliasForce = 2
    esriBGLTextAAliasForceForTransformed = 3

class esriBGLAntialiasingMode(Enum):
    esriBGLAntialiasingNone = 0
    esriBGLAntialiasingFastest = 1
    esriBGLAntialiasingFast = 3
    esriBGLAntialiasingNormal = 6
    esriBGLAntialiasingBest = 8

class esriGeometryType(Enum):
    esriGeometryNull = 0
    esriGeometryPoint = 1
    esriGeometryMultipoint = 2
    esriGeometryPolyline = 3
    esriGeometryPolygon = 4
    esriGeometryEnvelope = 5
    esriGeometryPath = 6
    esriGeometryAny = 7
    esriGeometryMultiPatch = 9
    esriGeometryRing = 11
    esriGeometryLine = 13
    esriGeometryCircularArc = 14
    esriGeometryBezier3Curve = 15
    esriGeometryEllipticArc = 16
    esriGeometryBag = 17
    esriGeometryTriangleStrip = 18
    esriGeometryTriangleFan = 19
    esriGeometryRay = 20
    esriGeometrySphere = 21
    esriGeometryTriangles = 22

class esriSpatialRelEnum(Enum):
    esriSpatialRelUndefined = 0
    esriSpatialRelIntersects = 1
    esriSpatialRelEnvelopeIntersects = 2
    esriSpatialRelIndexIntersects = 3
    esriSpatialRelTouches = 4
    esriSpatialRelOverlaps = 5
    esriSpatialRelCrosses = 6
    esriSpatialRelWithin = 7
    esriSpatialRelContains = 8
    esriSpatialRelRelation = 9

class esriSearchOrder(Enum):
    esriSearchOrderSpatial = 0
    esriSearchOrderAttribute = 1

class esriRelCardinality(Enum):
    esriRelCardinalityOneToOne = 0
    esriRelCardinalityOneToMany = 1
    esriRelCardinalityManyToMany = 2

class esriNetworkAttributeUnits(Enum):
    esriNAUUnknown = 0
    esriNAUInches = 1
    esriNAUFeet = 3
    esriNAUYards = 4
    esriNAUMiles = 5
    esriNAUNauticalMiles = 6
    esriNAUMillimeters = 7
    esriNAUCentimeters = 8
    esriNAUMeters = 9
    esriNAUKilometers = 10
    esriNAUDecimalDegrees = 11
    esriNAUDecimeters = 12
    esriNAUSeconds = 20
    esriNAUMinutes = 21
    esriNAUHours = 22
    esriNAUDays = 23
    esriNAUMilesPerHour = 30
    esriNAUKilometersPerHour = 31

class esriNetworkForwardStarBacktrack(Enum):
    esriNFSBNoBacktrack = 0
    esriNFSBAllowBacktrack = 1
    esriNFSBAtDeadEndsOnly = 2
    esriNFSBAtDeadEndsAndIntersections = 3

class esriFeatureType(Enum):
    esriFTSimple = 0
    esriFTSimpleJunction = 1
    esriFTSimpleEdge = 2
    esriFTComplexJunction = 3
    esriFTComplexEdge = 4
    esriFTAnnotation = 5
    esriFTCoverageAnnotation = 6
    esriFTDimension = 7
    esriFTRasterCatalogItem = 8

class esriTransformDirection(Enum):
    esriTransformForward = 0
    esriTransformReverse = 1

class esriDataStatType(Enum):
    esriDataStatTypeCount = 0
    esriDataStatTypeSum = 1
    esriDataStatTypeMin = 2
    esriDataStatTypeMax = 3
    esriDataStatTypeAverage = 4
    esriDataStatTypeStdDev = 5
    esriDataStatTypeVariance = 6

class esriAttributeRuleType(Enum):
    esriARTCalculation = 0
    esriARTConstraint = 1
    esriARTValidation = 2
    esriARTSession = 3

class esriFeatureBinType(Enum):
    esriFeatureBinTypeUnknown = 0
    esriFeatureBinTypeGeohash = 1
    esriFeatureBinTypeGeohexFlat = 2
    esriFeatureBinTypeGeosquare = 3
    esriFeatureBinTypeGeohexPointy = 4

class esriTopoErrorType(Enum):
    esriTopoPointError = 0
    esriTopoLineError = 1
    esriTopoPolyError = 2

class esriAnimationTransitionMode(Enum):
    esriAnimationTransitionModeAuto = 0
    esriAnimationTransitionModeCartesian = 1
    esriAnimationTransitionModeGeodesic = 2

class esriDiagramDatasetFeatureClass(Enum):
    esriDiagramEdgeFeatureClass = 0
    esriDiagramJunctionFeatureClass = 1
    esriDiagramContainerFeatureClass = 2
    esriTemporaryDiagramEdgeFeatureClass = 3
    esriTemporaryDiagramJunctionFeatureClass = 4
    esriTemporaryDiagramContainerFeatureClass = 5
    esriNetworkDiagramFeatureClass = 6

class esriImageFormat(Enum):
    esriImageNone = -1
    esriImageBMP = 0
    esriImageJPG = 1
    esriImageDIB = 2
    esriImageTIFF = 3
    esriImagePNG = 4
    esriImagePNG24 = 5
    esriImageEMF = 6
    esriImagePS = 7
    esriImagePDF = 8
    esriImageAI = 9
    esriImageGIF = 10
    esriImageSVG = 11
    esriImageSVGZ = 12
    esriImagePNG32 = 13
    esriImageJPGPNG = 14
    esriImageOptimalPNG = 15
    esriImageLERC = 16
    esriImageRaw = 17
    esriImageBSQ = 18
    esriImageBIP = 19

class esriJoinType(Enum):
    esriLeftOuterJoin = 0
    esriLeftInnerJoin = 1

class CIMObject:
    def __init__(self, *args, **Kwargs) -> None: ...

class TimeReference:
    timeZoneNameID: Incomplete
    respectsDaylightSavingTime: bool
    respectsDynamicAdjustmentRules: bool
    timeZone: Incomplete
    timeZoneIANA: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class TimeValue(CIMObject):
    timeReference: str
    def __init__(self, *args, **Kwargs) -> None: ...

class TimeInstant(TimeValue):
    time: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class TimeExtent:
    start: str
    end: str
    empty: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class StatsHistogram(CIMObject):
    stddevSpecified: bool
    nBands: Incomplete
    resolutionSpecified: bool
    resolution: Incomplete
    nsamplesSpecified: bool
    nsamples: Incomplete
    histogram: Incomplete
    limitMaxSpecified: bool
    limitMax: Incomplete
    limitMinSpecified: bool
    limitMin: Incomplete
    covariances: Incomplete
    stddev: Incomplete
    meanSpecified: bool
    mean: Incomplete
    maxSpecified: bool
    max: Incomplete
    minSpecified: bool
    min: Incomplete
    nBandsSpecified: bool
    def __init__(self, *args, **kwargs) -> None: ...

class RasterColormap(CIMObject):
    colormapSize: Incomplete
    values: Incomplete
    colors: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class esriFieldType(Enum):
    esriFieldTypeSmallInteger = 0
    esriFieldTypeInteger = 1
    esriFieldTypeSingle = 2
    esriFieldTypeDouble = 3
    esriFieldTypeString = 4
    esriFieldTypeDate = 5
    esriFieldTypeOID = 6
    esriFieldTypeGeometry = 7
    esriFieldTypeBlob = 8
    esriFieldTypeRaster = 9
    esriFieldTypeGUID = 10
    esriFieldTypeGlobalID = 11
    esriFieldTypeXML = 12
