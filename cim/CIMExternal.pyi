from _typeshed import Incomplete
from enum import Enum

class esriNumericAlignmentEnum(Enum):
    esriAlignRight: int
    esriAlignLeft: int

class esriRoundingOptionEnum(Enum):
    esriRoundNumberOfDecimals: int
    esriRoundNumberOfSignificantDigits: int

class esriDatasetType(Enum):
    esriDTAny: int
    esriDTContainer: int
    esriDTGeo: int
    esriDTFeatureDataset: int
    esriDTFeatureClass: int
    esriDTPlanarGraph: int
    esriDTGeometricNetwork: int
    esriDTText: int
    esriDTTable: int
    esriDTRelationshipClass: int
    esriDTRasterDataset: int
    esriDTRasterBand: int
    esriDTTin: int
    esriDTCadDrawing: int
    esriDTRasterCatalog: int
    esriDTTopology: int
    esriDTToolbox: int
    esriDTTool: int
    esriDTNetworkDataset: int
    esriDTTerrain: int
    esriDTRepresentationClass: int
    esriDTCadastralFabric: int
    esriDTSchematicDataset: int
    esriDTLocator: int
    esriDTMap: int
    esriDTLayer: int
    esriDTStyle: int
    esriDTMosaicDataset: int
    esriDTLasDataset: int
    esriDTLayout: int
    esriDTStandaloneTable: int
    esriDTUtilityNetwork: int
    esriDTDiagramDataset: int
    esriDTDiagramFolder: int
    esriDTNetworkDiagram: int
    esriDTParcelDataset: int
    esriDTStandaloneVideo: int
    esriDTReport: int
    esriDTBIMFile: int

class esriTimeRelation(Enum):
    esriTimeRelationOverlaps: int
    esriTimeRelationOverlapsStartWithinEnd: int
    esriTimeRelationAfterStartOverlapsEnd: int
    esriTimeRelationWithin: int

class esriUnits(Enum):
    esriUnknownUnits: int
    esriInches: int
    esriPoints: int
    esriFeet: int
    esriYards: int
    esriMiles: int
    esriNauticalMiles: int
    esriMillimeters: int
    esriCentimeters: int
    esriMeters: int
    esriKilometers: int
    esriDecimalDegrees: int
    esriDecimeters: int

class esriTimeUnits(Enum):
    esriTimeUnitsUnknown: int
    esriTimeUnitsMilliseconds: int
    esriTimeUnitsSeconds: int
    esriTimeUnitsMinutes: int
    esriTimeUnitsHours: int
    esriTimeUnitsDays: int
    esriTimeUnitsWeeks: int
    esriTimeUnitsMonths: int
    esriTimeUnitsYears: int
    esriTimeUnitsDecades: int
    esriTimeUnitsCenturies: int

class esriBGLTextAAlias(Enum):
    esriBGLTextAAliasNone: int
    esriBGLTextAAliasDefault: int
    esriBGLTextAAliasForce: int
    esriBGLTextAAliasForceForTransformed: int

class esriBGLAntialiasingMode(Enum):
    esriBGLAntialiasingNone: int
    esriBGLAntialiasingFastest: int
    esriBGLAntialiasingFast: int
    esriBGLAntialiasingNormal: int
    esriBGLAntialiasingBest: int

class esriGeometryType(Enum):
    esriGeometryNull: int
    esriGeometryPoint: int
    esriGeometryMultipoint: int
    esriGeometryPolyline: int
    esriGeometryPolygon: int
    esriGeometryEnvelope: int
    esriGeometryPath: int
    esriGeometryAny: int
    esriGeometryMultiPatch: int
    esriGeometryRing: int
    esriGeometryLine: int
    esriGeometryCircularArc: int
    esriGeometryBezier3Curve: int
    esriGeometryEllipticArc: int
    esriGeometryBag: int
    esriGeometryTriangleStrip: int
    esriGeometryTriangleFan: int
    esriGeometryRay: int
    esriGeometrySphere: int
    esriGeometryTriangles: int

class esriSpatialRelEnum(Enum):
    esriSpatialRelUndefined: int
    esriSpatialRelIntersects: int
    esriSpatialRelEnvelopeIntersects: int
    esriSpatialRelIndexIntersects: int
    esriSpatialRelTouches: int
    esriSpatialRelOverlaps: int
    esriSpatialRelCrosses: int
    esriSpatialRelWithin: int
    esriSpatialRelContains: int
    esriSpatialRelRelation: int

class esriSearchOrder(Enum):
    esriSearchOrderSpatial: int
    esriSearchOrderAttribute: int

class esriRelCardinality(Enum):
    esriRelCardinalityOneToOne: int
    esriRelCardinalityOneToMany: int
    esriRelCardinalityManyToMany: int

class esriNetworkAttributeUnits(Enum):
    esriNAUUnknown: int
    esriNAUInches: int
    esriNAUFeet: int
    esriNAUYards: int
    esriNAUMiles: int
    esriNAUNauticalMiles: int
    esriNAUMillimeters: int
    esriNAUCentimeters: int
    esriNAUMeters: int
    esriNAUKilometers: int
    esriNAUDecimalDegrees: int
    esriNAUDecimeters: int
    esriNAUSeconds: int
    esriNAUMinutes: int
    esriNAUHours: int
    esriNAUDays: int
    esriNAUMilesPerHour: int
    esriNAUKilometersPerHour: int

class esriNetworkForwardStarBacktrack(Enum):
    esriNFSBNoBacktrack: int
    esriNFSBAllowBacktrack: int
    esriNFSBAtDeadEndsOnly: int
    esriNFSBAtDeadEndsAndIntersections: int

class esriFeatureType(Enum):
    esriFTSimple: int
    esriFTSimpleJunction: int
    esriFTSimpleEdge: int
    esriFTComplexJunction: int
    esriFTComplexEdge: int
    esriFTAnnotation: int
    esriFTCoverageAnnotation: int
    esriFTDimension: int
    esriFTRasterCatalogItem: int

class esriTransformDirection(Enum):
    esriTransformForward: int
    esriTransformReverse: int

class esriDataStatType(Enum):
    esriDataStatTypeCount: int
    esriDataStatTypeSum: int
    esriDataStatTypeMin: int
    esriDataStatTypeMax: int
    esriDataStatTypeAverage: int
    esriDataStatTypeStdDev: int
    esriDataStatTypeVariance: int

class esriAttributeRuleType(Enum):
    esriARTCalculation: int
    esriARTConstraint: int
    esriARTValidation: int
    esriARTSession: int

class esriFeatureBinType(Enum):
    esriFeatureBinTypeUnknown: int
    esriFeatureBinTypeGeohash: int
    esriFeatureBinTypeGeohexFlat: int
    esriFeatureBinTypeGeosquare: int
    esriFeatureBinTypeGeohexPointy: int

class esriTopoErrorType(Enum):
    esriTopoPointError: int
    esriTopoLineError: int
    esriTopoPolyError: int

class esriAnimationTransitionMode(Enum):
    esriAnimationTransitionModeAuto: int
    esriAnimationTransitionModeCartesian: int
    esriAnimationTransitionModeGeodesic: int

class esriDiagramDatasetFeatureClass(Enum):
    esriDiagramEdgeFeatureClass: int
    esriDiagramJunctionFeatureClass: int
    esriDiagramContainerFeatureClass: int
    esriTemporaryDiagramEdgeFeatureClass: int
    esriTemporaryDiagramJunctionFeatureClass: int
    esriTemporaryDiagramContainerFeatureClass: int
    esriNetworkDiagramFeatureClass: int

class esriImageFormat(Enum):
    esriImageNone: int
    esriImageBMP: int
    esriImageJPG: int
    esriImageDIB: int
    esriImageTIFF: int
    esriImagePNG: int
    esriImagePNG24: int
    esriImageEMF: int
    esriImagePS: int
    esriImagePDF: int
    esriImageAI: int
    esriImageGIF: int
    esriImageSVG: int
    esriImageSVGZ: int
    esriImagePNG32: int
    esriImageJPGPNG: int
    esriImageOptimalPNG: int
    esriImageLERC: int
    esriImageRaw: int
    esriImageBSQ: int
    esriImageBIP: int

class esriJoinType(Enum):
    esriLeftOuterJoin: int
    esriLeftInnerJoin: int

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
    esriFieldTypeSmallInteger: int
    esriFieldTypeInteger: int
    esriFieldTypeSingle: int
    esriFieldTypeDouble: int
    esriFieldTypeString: int
    esriFieldTypeDate: int
    esriFieldTypeOID: int
    esriFieldTypeGeometry: int
    esriFieldTypeBlob: int
    esriFieldTypeRaster: int
    esriFieldTypeGUID: int
    esriFieldTypeGlobalID: int
    esriFieldTypeXML: int
