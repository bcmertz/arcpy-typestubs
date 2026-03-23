from enum import Enum

class BAVariableListValueType(Enum):
    Number: int
    Percent: int
    Average: int
    Index: int

class ChartAggregationType(Enum):
    eNone: int
    Minimum: int
    Maximum: int
    Mean: int
    Median: int
    Sum: int
    Majority: int
    Minority: int

class ChartColorType(Enum):
    SingleColor: int
    ColorMatch: int
    CustomColor: int

class ChartDataTransformationType(Enum):
    eNone: int
    Logarithmic: int
    SquareRoot: int
    Inverse: int
    BoxCox: int

class ChartDimensionalProfilePlotType(Enum):
    Variables: int
    Bands: int
    DimensionValues: int
    Variable: int
    Band: int
    CCDC: int
    LandTrendr: int
    Dimension: int

class ChartFontWeight(Enum):
    Lighter: int
    Normal: int
    Bold: int

class ChartGuideType(Enum):
    ChartGuideType_Line: int
    ChartGuideType_Range: int

class ChartLegendAlignment(Enum):
    Left: int
    Right: int
    Top: int
    Bottom: int

class ChartLineDashStyle(Enum):
    Solid: int
    Dot: int
    Dash: int
    DashDot: int
    LongDash: int
    LongDashDot: int

class ChartMapSelectionHandling(Enum):
    eNone: int
    Highlight: int
    BuildFromSelectionSet: int

class ChartMarkerSymbolStyle(Enum):
    Circle: int
    Square: int
    Diamond: int
    Triangle: int

class ChartMultiBarType(Enum):
    eNone: int
    SideBySide: int
    Stacked: int
    Stacked100: int

class ChartNullPolicy(Enum):
    Null: int
    Zero: int
    Interpolate: int

class ChartPosition(Enum):
    ChartPosition_Center: int
    ChartPosition_Top: int
    ChartPosition_Bottom: int
    ChartPosition_Left: int
    ChartPosition_Right: int

class ChartProbabilityPlotType(Enum):
    NormalQQPlot: int
    QQPlot: int

class ChartSPMDiagonalOption(Enum):
    eNone: int
    Histogram: int
    FieldName: int

class ChartSPMDisplayOption(Enum):
    eNone: int
    PreviewPlot: int
    ScatterPlots: int
    RSquared: int
    PearsonsR: int

class ChartSPMSortByType(Enum):
    RSquared: int
    PearsonsR: int
    Alphabetical: int
    Custom: int

class ChartSortDirection(Enum):
    Ascending: int
    Descending: int

class ChartSurfaceProfilePlotType(Enum):
    SingleLayer: int
    MultiLayer: int

class ChartTextCase(Enum):
    Normal: int
    Uppercase: int
    Lowercase: int
    Capitalize: int
    SmallCaps: int

class ChartTimeAggregationType(Enum):
    eNone: int
    EqualIntervalsFromStartTime: int
    EqualIntervalsFromEndTime: int
    CalendarIntervals: int
    ReferenceTime: int

class ChartTrajectoryProfilePlotType(Enum):
    Tracks: int
    Track: int
    Points: int
    Layers: int

class ChartTrendLineFitType(Enum):
    ChartTrendLineFitType_Linear: int
    ChartTrendLineFitType_Exponential: int
    ChartTrendLineFitType_Logarithmic: int
    ChartTrendLineFitType_Power: int
    ChartTrendLineFitType_Fourier: int
    ChartTrendLineFitType_Polynomial: int
    ChartTrendLineFitType_MinX: int
    ChartTrendLineFitType_MinY: int
    ChartTrendLineFitType_MaxX: int
    ChartTrendLineFitType_MaxY: int
    ChartTrendLineFitType_AverageX: int
    ChartTrendLineFitType_AverageY: int

class ChartValueType(Enum):
    ChartValueType_Numeric: int
    ChartValueType_Temporal: int

class SpectralProfileDisplayMode(Enum):
    MeanLine: int
    Boxes: int
    BoxesAndMeanLine: int
    ConsolidatedBoxesAndMeanLine: int

class ColorSpaceType(Enum):
    RGB: int
    CMYK: int
    Gray: int
    HSV: int
    HLS: int
    XYZ: int
    LAB: int
    Spot: int

class FixedColorRampArrangementType(Enum):
    Default: int
    Bivariate: int

class PolarDirection(Enum):
    Auto: int
    Clockwise: int
    Counterclockwise: int

class DataEngineeringSourceFilterType(Enum):
    eNone: int
    Selection: int
    Extent: int
    SelectionAndExtent: int

class DataEngineeringStatType(Enum):
    Mean: int
    StandardDeviation: int
    Maximum: int
    Minimum: int
    Median: int
    Mode: int
    FirstQuartile: int
    ThirdQuartile: int
    Sum: int
    NumberOfNulls: int
    Outliers: int
    NumberUniqueValues: int
    LeastCommon: int
    Kurtosis: int
    Skewness: int
    CoefficientOfVariation: int
    Range: int
    IQR: int
    Count: int

class DataEngineeringTreatFieldAsType(Enum):
    Numerical: int
    Categorical: int
    DateTime: int
    Other: int

class DataEngineeringViewLayoutType(Enum):
    FieldsAndStatistics: int
    OnlyStatistics: int

class ProjectThumbnailAutomaticGenerationSource(Enum):
    ActiveMap: int
    SpecifiedMap: int

class ProjectThumbnailGenerationMethod(Enum):
    Manual: int
    Automatic: int

class SceneDrawingMode(Enum):
    Perspective: int
    Isometric: int

class StatisticalDataCollectionSummaryType(Enum):
    Sum: int
    Avg: int
    Min: int
    Max: int
    Script: int

class StatisticalReportFieldFormat(Enum):
    Count: int
    Percent: int
    Currency: int

class TableRowHeightType(Enum):
    eNone: int
    Single: int
    Double: int
    Triple: int

class DepthOfFieldMaxBlur(Enum):
    Small: int
    Medium: int
    Large: int
    VeryLarge: int

class AltitudeMode(Enum):
    ClampToGround: int
    RelativeToGround: int
    Absolute: int

class AnimationTransition(Enum):
    eNone: int
    Linear: int
    Stepped: int
    Hop: int
    FixedArc: int
    AdjustableArc: int
    Hold: int

class BaseElevationType(Enum):
    Expression: int
    Surface: int
    Shape: int

class BillboardMode(Enum):
    eNone: int
    SignPost: int
    FaceNearPlane: int

class ColorModel(Enum):
    RGB: int
    CMYK: int

class ColorVisionDeficiencyType(Enum):
    eNone: int
    Deuteranopia: int
    Protanopia: int
    Tritanopia: int

class DominantSizeAxis(Enum):
    Z: int
    X: int
    Y: int

class ElevationMode(Enum):
    BaseGlobeSurface: int
    CustomSurface: int
    eNone: int

class ExtrusionType(Enum):
    eNone: int
    MinZ: int
    MaxZ: int
    Base: int
    Absolute: int

class FaceCulling3D(Enum):
    Backface: int
    Frontface: int
    eNone: int
    FromGeometry: int

class GradientStrokeMethod(Enum):
    AcrossLine: int
    AlongLine: int

class MapLayerType(Enum):
    Operational: int
    BasemapBackground: int
    BasemapTopReference: int
    MapNotes: int

class MapViewingMode(Enum):
    Map: int
    SceneLocal: int
    SceneGlobal: int
    MapStereo: int

class OffsetCurveMethod(Enum):
    Square: int
    Mitered: int
    Bevelled: int
    Rounded: int

class OffsetCurveOption(Enum):
    Fast: int
    Accurate: int

class PrimitiveShapeType(Enum):
    Unknown: int
    Cone: int
    Cube: int
    Cylinder: int
    Diamond: int
    Sphere: int
    Tetrahedron: int

class PrimitiveType3D(Enum):
    TriangleStrip: int
    TriangleFan: int
    TriangleList: int
    PointList: int
    LineList: int

class RangeRelation(Enum):
    Overlaps: int
    OverlapsStartWithinEnd: int
    AfterStartOverlapsEnd: int
    Within: int

class RasterResamplingType(Enum):
    NearestNeighbor: int
    BilinearInterpolation: int
    CubicConvolution: int
    Majority: int
    BilinearInterpolationPlus: int
    BilinearGaussianBlur: int
    BilinearGaussianBlurPlus: int
    Average: int
    Minimum: int
    Maximum: int
    VectorAverage: int

class RasterStretchStatsType(Enum):
    AreaOfView: int
    Dataset: int
    GlobalStats: int

class RasterStretchType(Enum):
    eNone: int
    DefaultFromSource: int
    Custom: int
    StandardDeviations: int
    HistogramEqualize: int
    MinimumMaximum: int
    HistogramSpecification: int
    PercentMinimumMaximum: int
    Count: int
    ESRI: int

class RotationOrder(Enum):
    XYZ: int
    ZXY: int
    YXZ: int

class ColorBalanceMethod(Enum):
    Dodging: int
    Histogram: int
    StdDev: int
    eNone: int

class ColorCorrectionStretchType(Enum):
    eNone: int
    Adaptive: int
    MinMax: int
    StdDev: int

class ColorMatchingMethod(Enum):
    Statistics: int
    Histogram: int
    LinearCorrelation: int
    eNone: int

class ColorizerHillshadeType(Enum):
    Traditional: int
    Multidirectional: int

class ColorizerScalingType(Enum):
    eNone: int
    Adjusted: int

class FlowRepresentationType(Enum):
    From: int
    To: int

class MosaicSubLayerType(Enum):
    Boundary: int
    Footprint: int
    Image: int
    Seamline: int

class PansharpeningType(Enum):
    IHS: int
    Brovey: int
    ESRI: int
    Mean: int

class RasterFootprintDrawMode(Enum):
    All: int
    OnlyPrimary: int

class RasterHistogramEditType(Enum):
    Lines: int
    Splines: int
    Points: int

class RasterMosaicMethod(Enum):
    eNone: int
    Center: int
    Nadir: int
    Viewpoint: int
    Attribute: int
    LockRaster: int
    Northwest: int
    Seamline: int

class RasterMosaicOperatorType(Enum):
    First: int
    Last: int
    Min: int
    Max: int
    Mean: int
    Blend: int
    Sum: int

class SpeedUnitType(Enum):
    Unknown: int
    MetersPerSecond: int
    KilometersPerHour: int
    Knots: int
    FeetPerSecond: int
    MilesPerHour: int

class StretchType(Enum):
    Gamma: int
    MinMax: int
    StdDev: int
    eNone: int

class SymbolTileUnitType(Enum):
    Unknown: int
    Feet: int
    Miles: int
    NauticalMiles: int
    Meters: int
    Kilometers: int
    DecimalDegrees: int
    Pixels: int

class SymbolizationType(Enum):
    Scalar: int
    SingleArrow: int
    WindBarbs: int
    BeaufortWindKnots: int
    BeaufortWindMetersPerSecond: int
    OceanCurrentKnots: int
    OceanCurrentMetersPerSecond: int
    BeaufortWindMilesPerHour: int
    BeaufortWindKilometersPerHour: int
    ClassifiedArrow: int
    Custom: int

class TargetColorSurfaceType(Enum):
    SingleColorPoint: int
    ColorGrid: int
    FirstOrderSurface: int
    SecondOrderSurface: int
    ThirdOrderSurface: int

class CentralityRelationshipInterpretation(Enum):
    Undirected: int
    Directed: int
    Reversed: int

class CentralityScoresNormalization(Enum):
    eNone: int
    Global: int
    ByComponent: int

class FilteredFindPathsEntityUsage(Enum):
    AnyOriginAnyDestination: int
    AnyOriginAllDestinations: int
    AllOriginsAnyDestination: int
    AllOriginsAllDestinations: int

class KGDurativeEventMissingOneTimeBehaviour(Enum):
    Error: int
    Exclude: int
    MakeNonEvent: int
    MakePunctualEvent: int

class KGDurativeEventSwappedTimesBehaviour(Enum):
    Error: int
    Exclude: int
    MakeNonEvent: int
    MakeMinPunctualEvent: int
    MakeMaxPunctualEvent: int
    MakeDurativeEvent: int

class KGEventMissingAllTimesBehaviour(Enum):
    Error: int
    Exclude: int
    MakeNonEvent: int

class KGPathFilterItemType(Enum):
    Entity: int
    Relationship: int

class KGPathFilterType(Enum):
    IncludeOnly: int
    Exclude: int
    MandatoryWaypoint: int
    OptionalWaypoint: int

class KGPathMode(Enum):
    Shortest: int
    All: int

class KGPathTimeFlow(Enum):
    Forward: int
    Backward: int
    Unconstrained: int

class KGTraversalDirectionType(Enum):
    Any: int
    Forward: int
    Backward: int

class KnowledgeGraphSearchFilterScope(Enum):
    Entities: int
    Relationships: int
    BothEntitiesAndRelationships: int
    Provenance: int

class KnowledgeLinkChartLayoutAlgorithm(Enum):
    Organic_Standard: int
    Organic_LeafCircle: int
    Organic_Fusiform: int
    Organic_Community: int
    Geographic_Organic_Standard: int
    Basic_Grid: int
    Tree_LeftToRight: int
    Tree_RightToLeft: int
    Tree_TopToBottom: int
    Tree_BottomToTop: int
    Radial_RootCentric: int
    Radial_NodeCentric: int
    Hierarchical_TopToBottom: int
    Hierarchical_BottomToTop: int

class ProvenanceBehavior(Enum):
    Exclude: int
    Include: int

class FeaturesToLabel(Enum):
    AllVisibleFeatures: int
    MostCurrentTrackFeatures: int

class LabelExpressionEngine(Enum):
    VBScript: int
    JScript: int
    Python: int
    Arcade: int

class LabelFeatureType(Enum):
    Point: int
    Line: int
    Polygon: int

class MaplexAbbreviationType(Enum):
    Translation: int
    Keyword: int
    Ending: int

class MaplexAnchorPointType(Enum):
    GeometricCenter: int
    ErodedCenter: int
    Perimeter: int
    UnclippedGeometricCenter: int

class MaplexCenterLabelAnchorType(Enum):
    Symbol: int
    FeatureGeometry: int

class MaplexConnectionType(Enum):
    MinimizeLabels: int
    Unambiguous: int

class MaplexConstrainOffset(Enum):
    NoConstraint: int
    AboveLine: int
    BelowLine: int
    LeftOfLine: int
    RightOfLine: int

class MaplexContourAlignmentType(Enum):
    Uphill: int
    Page: int
    Downhill: int

class MaplexContourLadderType(Enum):
    eNone: int
    Straight: int
    Curved: int

class MaplexGraticuleAlignmentType(Enum):
    Straight: int
    StraightNoFlip: int
    Curved: int
    CurvedNoFlip: int

class MaplexKeyNumberHorizontalAlignment(Enum):
    Auto: int
    Left: int
    Right: int

class MaplexKeyNumberMethod(Enum):
    PreventUnplacedLabels: int
    AlwaysNumber: int

class MaplexKeyNumberResetType(Enum):
    eNone: int
    Maybe: int
    Always: int

class MaplexLabelAnchorPoint(Enum):
    CenterOfLabel: int
    NearestSideOfLabel: int
    FurthestSideOfLabel: int

class MaplexLabelRotationType(Enum):
    Geographic: int
    Arithmetic: int
    Radians: int
    AV3: int

class MaplexLineFeatureType(Enum):
    General: int
    Street: int
    StreetAddressRange: int
    Contour: int
    River: int

class MaplexLinePlacementMethod(Enum):
    CenteredHorizontalOnLine: int
    CenteredStraightOnLine: int
    CenteredCurvedOnLine: int
    CenteredPerpendicularOnLine: int
    OffsetHorizontalFromLine: int
    OffsetStraightFromLine: int
    OffsetCurvedFromLine: int
    OffsetPerpendicularFromLine: int

class MaplexMultiPartOption(Enum):
    OneLabelPerFeature: int
    OneLabelPerPart: int
    OneLabelPerSegment: int

class MaplexOffsetAlongLineMethod(Enum):
    BestPositionAlongLine: int
    BeforeStartOfLine: int
    AlongLineFromStart: int
    AlongLineFromEnd: int
    AfterEndOfLine: int

class MaplexPointPlacementMethod(Enum):
    AroundPoint: int
    CenteredOnPoint: int
    NorthOfPoint: int
    NorthEastOfPoint: int
    EastOfPoint: int
    SouthEastOfPoint: int
    SouthOfPoint: int
    SouthWestOfPoint: int
    WestOfPoint: int
    NorthWestOfPoint: int

class MaplexPolygonFeatureType(Enum):
    General: int
    LandParcel: int
    River: int
    Boundary: int

class MaplexPolygonPlacementMethod(Enum):
    HorizontalInPolygon: int
    StraightInPolygon: int
    CurvedInPolygon: int
    HorizontalAroundPolygon: int
    RepeatAlongBoundary: int
    CurvedAroundPolygon: int

class MaplexQualityType(Enum):
    Low: int
    Medium: int
    High: int

class MaplexRemoveAmbiguousLabelsType(Enum):
    All: int
    WithinLabelClass: int
    eNone: int

class MaplexRotationAlignmentType(Enum):
    Straight: int
    Horizontal: int
    Perpendicular: int

class MaplexStackingAlignment(Enum):
    ChooseBest: int
    ConstrainLeftOrRight: int
    ConstrainLeft: int
    ConstrainRight: int
    ConstrainCenter: int

class MaplexUnit(Enum):
    Map: int
    MM: int
    Inch: int
    Point: int
    Percentage: int

class StandardFeatureWeight(Enum):
    eNone: int
    Low: int
    Medium: int
    High: int

class StandardLabelRotationType(Enum):
    Geographic: int
    Arithmetic: int
    Radians: int
    AV3: int

class StandardLabelWeight(Enum):
    Low: int
    Medium: int
    High: int

class StandardNumLabelsOption(Enum):
    NoLabelRestrictions: int
    OneLabelPerName: int
    OneLabelPerShape: int
    OneLabelPerPart: int

class StandardPointPlacementMethod(Enum):
    AroundPoint: int
    OnTopPoint: int
    SpecifiedAngles: int
    RotationField: int

class StandardPolygonPlacementMethod(Enum):
    AlwaysHorizontal: int
    AlwaysStraight: int
    MixedStrategy: int

class DisplayCacheType(Enum):
    Permanent: int
    InSession: int
    eNone: int
    MaxAge: int

class ExaggerationMode(Enum):
    ScaleZ: int
    ScaleVoxelHeight: int

class LayerEffectsMode(Enum):
    Layer: int
    Feature: int

class Lighting3D(Enum):
    OneSideDataNormal: int
    OneSideResetNormal: int
    TwoSideDataNormal: int
    TwoSideResetNormal: int
    TwoSideDataNormalFromWindingOrder: int
    TwoSideResetNormalFromWindingOrder: int

class SortOrderType(Enum):
    Ascending: int
    Descending: int

class SublayerVisibilityMode(Enum):
    Independent: int
    Exclusive: int

class Anchor(Enum):
    Unspecified: int
    TopLeftCorner: int
    TopMidPoint: int
    TopRightCorner: int
    LeftMidPoint: int
    CenterPoint: int
    RightMidPoint: int
    BottomLeftCorner: int
    BottomMidPoint: int
    BottomRightCorner: int

class AutoCameraSource(Enum):
    eNone: int
    Fixed: int
    MapFrameLink: int
    MapSeriesLink: int

class AutoCameraType(Enum):
    Center: int
    Scale: int
    CenterAndScale: int
    Extent: int

class CondensedTabType(Enum):
    Round: int
    Rectangle: int
    RoundedRectangle: int

class ContiguousTabType(Enum):
    Continuous: int
    Rounded: int
    Squared: int

class CruisingAltitudeDiagramType(Enum):
    Vertical: int
    Horizontal: int
    Quadrantal: int

class DeclinationDirection(Enum):
    West: int
    East: int

class DoubleFillScaleBarStyle(Enum):
    Hollow: int
    Alternating: int
    DoubleAlternating: int

class EndPointPosition(Enum):
    eNone: int
    FromPoint: int
    ToPoint: int

class EndPointSelection(Enum):
    First: int
    Interior: int
    Last: int

class ExtentFitType(Enum):
    BestFit: int
    ExtentCenter: int
    DataDriven: int

class ExtentIndicatorType(Enum):
    Frame: int
    Rectangle: int
    IndexFeatureFromDDP: int

class FieldSortInfo(Enum):
    eNone: int
    Asc: int
    AscCase: int
    Desc: int
    DescCase: int

class FieldStatisticsFlag(Enum):
    NoStatistics: int
    Count: int
    Minimum: int
    Maximum: int
    Range: int
    Sum: int
    Mean: int
    Median: int
    Mode: int
    StandardDeviation: int

class GridElementType(Enum):
    Line: int
    Tick: int
    Label: int
    Corner: int
    IntersectionPoint: int

class GridLadderLabelPosition(Enum):
    Half: int
    Third: int
    Quarter: int

class GridLineOrientation(Enum):
    NorthSouth: int
    EastWest: int

class GridReferencePrecisionLevel(Enum):
    GridZoneDesignator: int
    PrecisionLevel100km: int
    PrecisionLevel10km: int
    PrecisionLevel1km: int
    PrecisionLevel100m: int
    PrecisionLevel10m: int
    PrecisionLevel1m: int
    ICM: int

class LeaderType(Enum):
    eNone: int
    LineToNearestPoint: int
    LineToMidpoint: int
    LineThroughCenters: int
    CalloutToCenter: int
    CalloutToEdge: int
    CalloutToEdges: int

class LegendFittingStrategy(Enum):
    AdjustSize: int
    AdjustColumns: int
    AdjustColumnsAndSize: int
    AdjustFrame: int
    ManualColumns: int

class LegendItemArrangement(Enum):
    PatchLabelDescription: int
    PatchDescriptionLabel: int
    LabelPatchDescription: int
    LabelDescriptionPatch: int
    DescriptionPatchLabel: int
    DescriptionLabelPatch: int

class LegendKeepTogetherOption(Enum):
    eNone: int
    Items: int
    Groups: int

class MGRSLabelPosition(Enum):
    Corner: int
    Center: int

class MapProductSpecType(Enum):
    Unset: int
    TLM: int
    ICM: int
    JOG: int
    USTOPO: int
    GNC: int
    JNC: int
    ONC: int
    TPC: int

class MeterReferenceSquareType(Enum):
    Single: int
    Multiple: int
    DualGrid: int

class NorthType(Enum):
    SimpleNorth: int
    TrueNorth: int
    GridNorth: int
    MagneticNorth: int

class Orientation(Enum):
    Horizontal: int
    Vertical: int

class PageOrientation(Enum):
    Portrait: int
    Landscape: int

class ProfileFrameHeightOption(Enum):
    ConstantHeight: int
    ConstantRatio: int

class ProfileFrameStyle(Enum):
    AOC: int
    PATC: int

class ProfileFrameType(Enum):
    Straight: int
    Curved: int

class ProfileObstacleGroundDisplayOption(Enum):
    Actual: int
    Max: int
    Min: int
    Average: int

class ProfileObstacleMarkerLocation(Enum):
    Surface: int
    Top: int
    Base: int

class ProfileObstacleSymbolSubstitutionType(Enum):
    eNone: int
    Penetrating: int
    Protruding: int

class ProfileTerrainDisplayOption(Enum):
    All: int
    PenetratingOnly: int
    Highlight: int
    eNone: int

class RectanglePosition(Enum):
    TopSide: int
    BottomSide: int
    LeftSide: int
    RightSide: int

class ScaleBarFittingStrategy(Enum):
    AdjustDivision: int
    AdjustDivisions: int
    AdjustDivisionAndDivisions: int
    AdjustFrame: int
    FixedWidth: int
    FixedHeight: int

class ScaleBarFrequency(Enum):
    eNone: int
    One: int
    MajorDivisions: int
    Divisions: int
    DivisionsAndFirstMidpoint: int
    DivisionsAndFirstSubdivisions: int
    DivisionsAndSubdivisions: int
    DivisionsFirstSubdivisionFirstMidpoint: int

class ScaleBarLabelPosition(Enum):
    Above: int
    BeforeLabels: int
    AfterLabels: int
    BeforeBar: int
    AfterBar: int
    Below: int
    AboveLeft: int
    AboveRight: int
    AboveEnds: int
    BeforeAndAfterLabels: int
    BeforeAndAfterBar: int
    BelowLeft: int
    BelowRight: int
    BelowEnds: int
    OnBarAfterFirstDivision: int

class ScaleBarVerticalPosition(Enum):
    Above: int
    Top: int
    On: int
    Bottom: int
    Below: int
    OnRight: int
    OnLeft: int

class StreetIndexDelimiter(Enum):
    Period: int
    Space: int
    Hyphen: int
    Underscore: int

class StreetIndexWrapMethod(Enum):
    Wrap: int
    GroupWrap: int

class TableFrameFillingStrategy(Enum):
    ShowAllRows: int
    ShowVisibleRows: int
    ShowMapSeriesRows: int
    CustomWhereClause: int

class TableFrameFittingStrategy(Enum):
    AdjustSize: int
    AdjustColumns: int
    AdjustColumnsAndSize: int
    AdjustFrame: int

class UnitType(Enum):
    Percent: int
    MapUnits: int
    PageUnits: int

class LinkChartFilterPropertyDataType(Enum):
    EntityKeyValue: int
    LabelValue: int

class LinkChartFilterScope(Enum):
    Entities: int
    Relationships: int
    Both: int

class LinkChartFilterStage(Enum):
    Unknown: int
    Data: int
    Visual: int

class LinkChartFilterType(Enum):
    Unknown: int
    FieldData: int
    PropertyData: int

class LinkChartLayoutAlgorithm(Enum):
    Clustered: int
    Organic: int
    Hierarchy_TopToBottom: int
    Hierarchy_BottomToTop: int
    Hierarchy_LeftToRight: int
    Hierarchy_RightToLeft: int

class LinkChartLinkDashStyle(Enum):
    Solid: int
    Dot: int
    Dash: int
    DashDot: int
    DashDotDot: int

class LinkChartLinkLabelPlacement(Enum):
    Parallel: int
    Perpendicular: int

class LinkChartRelationshipKeyType(Enum):
    eNone: int
    Entities: int
    Foreign: int

class LinkChartSymbolizationSource(Enum):
    MapSymbology: int
    SingleSymbology: int

class ClipDistanceMode(Enum):
    Automatic: int
    Manual: int

class ClippingMode(Enum):
    eNone: int
    MapExtent: int
    CustomShape: int
    MapSeries: int

class ComparisonOperator(Enum):
    IsEqual: int
    NotEqual: int
    LessThanOrEqualTo: int
    LessThan: int
    GreaterThanOrEqualTo: int
    GreaterThan: int

class CullDirection(Enum):
    Inward: int
    Outward: int
    Camera: int

class EditingElevationCaptureMode(Enum):
    Off: int
    Constant: int
    Surface: int

class GeoFenceEnterExitRule(Enum):
    EnterContainsAndExitDoesNotIntersect: int
    EnterContainsAndExitDoesNotContain: int
    EnterIntersectsAndExitDoesNotIntersect: int

class GeoFenceNotificationRule(Enum):
    Enter: int
    EnterOrExit: int
    Exit: int

class GeotriggerAccuracyMode(Enum):
    UseGeometry: int
    UseGeometryWithAccuracy: int

class GroundToGridScaleType(Enum):
    ConstantFactor: int
    ComputeUsingElevation: int

class IlluminationSource(Enum):
    NoonAtCameraPosition: int
    DateTime: int
    AbsoluteSunPosition: int
    MapTime: int

class JoinOperator(Enum):
    And: int
    Or: int
    eNone: int

class LocatorType(Enum):
    Locator: int
    Layer: int
    Table: int

class MapType(Enum):
    Map: int
    Scene: int
    Basemap: int
    NetworkDiagram: int
    ContainmentMap: int
    LinkChart: int

class ReviewerMonotonicityDirection(Enum):
    NoneAsError: int
    DecreasingValueAsError: int
    IncreasingValueAsError: int

class ReviewerMonotonicityEvaluationType(Enum):
    EvaluateNone: int
    EvaluateZ: int
    EvaluateM: int

class ScaleDisplayFormat(Enum):
    Value: int
    Alias: int
    ValueAndAlias: int
    AliasAndValue: int

class ScaleFormatType(Enum):
    Absolute: int
    Imperial: int

class SliderExtentType(Enum):
    AllLayers: int
    VisibleLayers: int
    SingleLayer: int
    CustomRange: int

class SliderInteractionMode(Enum):
    Slider: int
    Picker: int

class SliderStepType(Enum):
    Interval: int
    Count: int
    Feature: int

class SnapRequestType(Enum):
    SnapRequestType_None: int
    SnapRequestType_GeometricSnapping: int
    SnapRequestType_VisualSnapping: int
    SnapRequestType_GeometricAndVisualSnapping: int

class SnapTipDisplayPart(Enum):
    SnapTipDisplayNone: int
    SnapTipDisplayLayer: int
    SnapTipDisplayType: int

class SnapXYToleranceUnit(Enum):
    SnapXYToleranceUnitPixel: int
    SnapXYToleranceUnitMap: int

class StereoModelDisplayMode(Enum):
    Default: int
    OnlyLeftImage: int
    OnlyRightImage: int
    eNone: int

class StereoOrientation(Enum):
    UpOrRight: int
    UpOrLeft: int
    DownOrRight: int
    DownOrLeft: int

class StereoSourceType(Enum):
    StereoModel: int
    StereoModelCollection: int

class SurfaceTINShadingMode(Enum):
    Smooth: int
    Flat: int

class SwipeDirection(Enum):
    eNone: int
    Top: int
    Bottom: int
    Left: int
    Right: int

class TimeOffsetDirection(Enum):
    Past: int
    Future: int
    PastAndFuture: int

class TimeSnapMode(Enum):
    Automatic: int
    Single: int
    Interval: int

class NDSRendererTarget(Enum):
    Edges: int
    UserJunctions: int
    SystemJunctions: int
    Turns: int
    Traffic: int
    DirtyAreas: int

class NetworkTravelModeSourceType(Enum):
    NetworkDataset: int
    Layer: int
    Custom: int

class RestrictionStatus(Enum):
    GeneralTraversable: int
    NeutralPreferenceLevelTraversable: int
    Prohibited: int
    AvoidPreferenceLevelTraversable: int
    PreferPreferenceLevelTraversable: int
    MixedPreferenceLevelTraversable: int
    Invalid: int

class TraversableDirections(Enum):
    Prohibited: int
    Traversable: int
    OneWay: int

class ValueType(Enum):
    Short: int
    Long: int
    Float: int
    Double: int
    Date: int
    String: int
    Bool: int

class DirectionFormatOption(Enum):
    DegreesMinutesSeconds: int
    QuadrantBearing: int

class DirectionType(Enum):
    NorthAzimuth: int
    SouthAzimuth: int
    Polar: int
    QuadrantBearing: int

class DirectionUnits(Enum):
    Radians: int
    DecimalDegrees: int
    DegreesMinutesSeconds: int
    Gradians: int
    Gons: int

class FractionOption(Enum):
    Digits: int
    Denominator: int

class NumericAlignment(Enum):
    AlignRight: int
    AlignLeft: int

class RoundingOption(Enum):
    NumberOfDecimals: int
    NumberOfSignificantDigits: int

class AttachmentDisplayType(Enum):
    PreviewFirst: int
    PreviewAll: int
    List: int
    Auto: int

class PresentationMediaContentFitType(Enum):
    eNone: int
    Fill: int
    StretchToFill: int
    Center: int

class PresentationTransitionType(Enum):
    eNone: int
    Swipe: int
    Fade: int

class ConnectionMode(Enum):
    Consumer: int
    Admin: int
    Publisher: int

class IndexedSceneLayerType(Enum):
    IntegratedMesh: int
    Point: int
    Object3D: int

class Object3DRenderingMode(Enum):
    eNone: int
    Wireframe: int

class ServerType(Enum):
    AGS: int
    WMS: int
    WCS: int
    WMTS: int
    WFS: int
    OGCAPI: int

class Tiles3DLayerType(Enum):
    IntegratedMesh: int
    Object3D: int

class VoxelAlignment(Enum):
    Origin: int
    Center: int

class VoxelInterpolationMode(Enum):
    Linear: int
    Nearest: int

class VoxelLayerOptimization(Enum):
    Visualization: int
    Size: int

class VoxelScalarFormat(Enum):
    I1: int
    U1: int
    I2: int
    U2: int
    I4: int
    U4: int
    I8: int
    U8: int
    F4: int
    F8: int

class VoxelValueFilterMode(Enum):
    Exclude: int
    Include: int

class VoxelVariableDataType(Enum):
    Continuous: int
    Discrete: int

class VoxelVariablePrecision(Enum):
    InputData: int
    Low: int
    Medium: int
    High: int

class VoxelVisualization(Enum):
    Volume: int
    Surface: int

class FloodSimulationCulvertProfileType(Enum):
    Elliptical: int
    Rectangular: int
    Arched: int

class FloodSimulationValueRangeType(Enum):
    FlowIntensity: int
    WaterDepth: int

class FloodSimulationWaterDisplayType(Enum):
    Fill: int
    Edges: int
    FillAndEdges: int

class BivariateGridLegendLabelStrategy(Enum):
    Corners: int
    Sides: int

class BivariateGridLegendOrientationType(Enum):
    eNone: int
    High: int
    Low: int
    HighLow: int
    LowHigh: int

class BivariateGridSizeOption(Enum):
    TwoByTwo: int
    ThreeByThree: int
    FourByFour: int

class ClassBreakType(Enum):
    GraduatedColor: int
    GraduatedSymbol: int
    UnclassedColor: int

class ClassBreaksLegendVisualVariableOptions(Enum):
    ShowVisualVariableSymbolClasses: int
    ShowClassesForEachPrimarySymbol: int

class ClassificationMethod(Enum):
    DefinedInterval: int
    EqualInterval: int
    GeometricalInterval: int
    Manual: int
    NaturalBreaks: int
    Quantile: int
    StandardDeviation: int

class ColorChannelTarget(Enum):
    SV: int
    All: int

class DataNormalizationMethod(Enum):
    Field: int
    Log: int
    PercentOfTotal: int
    Nothing: int

class ExpressionReturnType(Enum):
    Default: int
    String: int
    Numeric: int

class PatchShape(Enum):
    Default: int
    Point: int
    LineHorizontal: int
    LineZigZag: int
    LineAngles: int
    LineArc: int
    LineCurve: int
    LineTrail: int
    LineHydro: int
    LineVertical3D: int
    LineZigZag3D: int
    LineCorkscrew3D: int
    AreaRectangle: int
    AreaRoundedRectangle: int
    AreaPolygon: int
    AreaCircle: int
    AreaEllipse: int
    AreaFootprint: int
    AreaBoundary: int
    AreaHydroPoly: int
    AreaNaturalPoly: int
    AreaSquare: int
    AreaHexagonFlat: int
    AreaHexagonPointy: int
    AreaTrapezium: int

class PolygonSymbolColorTarget(Enum):
    Fill: int
    Outline: int
    FillOutline: int

class SizeVisualVariableAxis(Enum):
    HeightAxis: int
    WidthAxis: int
    DepthAxis: int
    WidthAndDepthAxes: int
    AllAxes: int

class SizeVisualVariableType(Enum):
    eNone: int
    Expression: int
    Random: int
    Proportional: int
    Graduated: int

class SymbolRotationType(Enum):
    Geographic: int
    Arithmetic: int

class SymbolShapes(Enum):
    Unknown: int
    Circle: int
    Square: int

class ValueRepresentations(Enum):
    Radius: int
    Area: int
    Distance: int
    Width: int

class VisualVariableInfoType(Enum):
    eNone: int
    Expression: int
    Random: int

class AngleAlignment(Enum):
    Display: int
    Map: int

class AnimatedSymbolRepeatType(Enum):
    eNone: int
    Loop: int
    Oscillate: int

class BalloonCalloutStyle(Enum):
    Rectangle: int
    RoundedRectangle: int
    Oval: int

class BlendingMode(Enum):
    eNone: int
    Alpha: int
    Screen: int
    Multiply: int
    Add: int
    Color: int
    ColorBurn: int
    ColorDodge: int
    Darken: int
    Difference: int
    Exclusion: int
    HardLight: int
    Hue: int
    Lighten: int
    Luminosity: int
    Normal: int
    Overlay: int
    Saturation: int
    SoftLight: int
    LinearBurn: int
    LinearDodge: int
    LinearLight: int
    PinLight: int
    VividLight: int

class BlockProgression(Enum):
    TTB: int
    RTL: int
    BTT: int

class CGAAttributeType(Enum):
    Float: int
    String: int
    Boolean: int
    Float_Array: int
    String_Array: int
    Boolean_Array: int

class ClippingType(Enum):
    Intersect: int
    Subtract: int

class ExternalColorMixMode(Enum):
    Tint: int
    Ignore: int
    Multiply: int

class ExtremityPlacement(Enum):
    Both: int
    JustBegin: int
    JustEnd: int
    eNone: int

class FillMode(Enum):
    Mosaic: int
    Centered: int

class FontEffects(Enum):
    Normal: int
    Superscript: int
    Subscript: int

class FontEncoding(Enum):
    MSSymbol: int
    Unicode: int

class FontType(Enum):
    Unspecified: int
    TrueType: int
    PSOpenType: int
    TTOpenType: int
    Type1: int

class GeometricEffectArrowType(Enum):
    OpenEnded: int
    Block: int
    Crossed: int

class GeometricEffectControlMeasureLineRule(Enum):
    FullGeometry: int
    PerpendicularFromFirstSegment: int
    ReversedFirstSegment: int
    PerpendicularToSecondSegment: int
    SecondSegmentWithTicks: int
    DoublePerpendicular: int
    OppositeToFirstSegment: int
    TriplePerpendicular: int
    HalfCircleFirstSegment: int
    HalfCircleSecondSegment: int
    HalfCircleExtended: int
    OpenCircle: int
    CoverageEdgesWithTicks: int
    GapExtentWithDoubleTicks: int
    GapExtentMidline: int
    Chevron: int
    PerpendicularWithArc: int
    ClosedHalfCircle: int
    TripleParallelExtended: int
    ParallelWithTicks: int
    Parallel: int
    PerpendicularToFirstSegment: int
    ParallelOffset: int
    OffsetOpposite: int
    OffsetSame: int
    CircleWithArc: int
    DoubleJog: int
    PerpendicularOffset: int
    LineExcludingLastSegment: int
    MultivertexArrow: int
    CrossedArrow: int
    ChevronArrow: int
    ChevronArrowOffset: int
    PartialFirstSegment: int
    Arch: int
    CurvedParallelTicks: int
    Arc90Degrees: int
    TipWithPerpendicularAndTicks: int

class GeometricEffectDonutMethod(Enum):
    Mitered: int
    Bevelled: int
    Rounded: int
    Square: int
    TrueBuffer: int

class GeometricEffectEnclosingPolygonMethod(Enum):
    ClosePath: int
    ConvexHull: int
    RectangularBox: int

class GeometricEffectExtensionOrigin(Enum):
    BeginningOfLine: int
    EndOfLine: int

class GeometricEffectLocalizerFeatherStyle(Enum):
    Complete: int
    Left: int
    Right: int

class GeometricEffectOffsetMethod(Enum):
    Mitered: int
    Bevelled: int
    Rounded: int
    Square: int

class GeometricEffectOffsetOption(Enum):
    Fast: int
    Accurate: int

class GeometricEffectOffsetTangentMethod(Enum):
    BeginningOfLine: int
    EndOfLine: int

class GeometricEffectWaveform(Enum):
    Sinus: int
    Square: int
    Triangle: int
    Random: int

class GlyphHinting(Enum):
    eNone: int
    Default: int
    Force: int

class GradientAlignment(Enum):
    Buffered: int
    Left: int
    Right: int
    AlongLine: int

class GradientFillMethod(Enum):
    Linear: int
    Rectangular: int
    Circular: int
    Buffered: int

class GradientStrokeType(Enum):
    Discrete: int
    Continuous: int

class HorizontalAlignment(Enum):
    Left: int
    Right: int
    Center: int
    Justify: int

class LeaderLineStyle(Enum):
    Base: int
    MidPoint: int
    ThreePoint: int
    FourPoint: int
    Underline: int
    CircularCW: int
    CircularCCW: int

class LineCapStyle(Enum):
    Butt: int
    Round: int
    Square: int

class LineDashEnding(Enum):
    NoConstraint: int
    HalfPattern: int
    HalfGap: int
    FullPattern: int
    FullGap: int
    Custom: int

class LineDecorationStyle(Enum):
    eNone: int
    Custom: int
    Circle: int
    OpenArrow: int
    ClosedArrow: int
    Diamond: int

class LineGapType(Enum):
    ExtraLeading: int
    Multiple: int
    Exact: int

class LineJoinStyle(Enum):
    Bevel: int
    Round: int
    Miter: int

class MarkerPlacementType(Enum):
    InsidePolygon: int
    PolygonCenter: int
    RandomlyInsidePolygon: int

class MaterialMode(Enum):
    Tint: int
    Replace: int
    Multiply: int

class PlacementAroundPolygonPosition(Enum):
    Top: int
    Bottom: int
    Left: int
    Right: int
    TopLeft: int
    TopRight: int
    BottomLeft: int
    BottomRight: int

class PlacementClip(Enum):
    ClipAtBoundary: int
    RemoveIfCenterOutsideBoundary: int
    DoNotTouchBoundary: int
    DoNotClip: int

class PlacementEndings(Enum):
    NoConstraint: int
    WithMarkers: int
    WithFullGap: int
    WithHalfGap: int
    Custom: int

class PlacementGridType(Enum):
    Fixed: int
    Random: int
    RandomFixedQuantity: int

class PlacementOnLineRelativeTo(Enum):
    LineMiddle: int
    LineBeginning: int
    LineEnd: int
    SegmentMidpoint: int

class PlacementPolygonCenterMethod(Enum):
    OnPolygon: int
    CenterOfMass: int
    BoundingBoxCenter: int

class PlacementRandomlyAlongLineRandomization(Enum):
    Low: int
    Medium: int
    High: int

class PlacementStepPosition(Enum):
    MarkerCenter: int
    MarkerBounds: int

class PointSymbolCalloutScale(Enum):
    eNone: int
    PropUniform: int
    PropNonuniform: int
    DifUniform: int
    DifNonuniform: int

class Simple3DLineAnchor(Enum):
    Center: int
    Bottom: int
    Top: int

class Simple3DLineStyle(Enum):
    Tube: int
    Strip: int
    Wall: int
    Square: int
    Rectangle: int

class SimplePlacementEndings(Enum):
    WithHalfGap: int
    WithMarkers: int

class SizeVariationMethod(Enum):
    Random: int
    Increasing: int
    Decreasing: int
    IncreasingThenDecreasing: int

class SymbolUnits(Enum):
    Relative: int
    Absolute: int

class TextCase(Enum):
    Normal: int
    LowerCase: int
    Allcaps: int

class TextReadingDirection(Enum):
    LTR: int
    RTL: int

class TextureFilter(Enum):
    Draft: int
    Picture: int
    Text: int

class VerticalAlignment(Enum):
    Top: int
    Center: int
    Baseline: int
    Bottom: int

class VerticalGlyphOrientation(Enum):
    Right: int
    Upright: int

class WaterbodySize(Enum):
    Small: int
    Medium: int
    Large: int

class WaveStrength(Enum):
    Calm: int
    Rippled: int
    Slight: int
    Moderate: int

class LASStretchAttribute(Enum):
    Elevation: int
    RGB: int
    Red: int
    Green: int
    Blue: int
    NearInfrared: int
    Intensity: int
    ScanAngle: int
    GPSTime: int
    eNone: int

class LASStretchDrawingType(Enum):
    Symbol: int
    Splat: int
    SymbolTint: int

class LASStretchStatsType(Enum):
    AreaOfView: int
    Dataset: int
    GlobalStats: int

class LASStretchType(Enum):
    DefaultFromSource: int
    Custom: int
    MinimumMaximum: int
    StandardDeviations: int
    Histogram: int
    PercentMinMax: int

class PointCloudFieldTransformType(Enum):
    eNone: int
    LowFourBit: int
    HighFourBit: int
    AbsoluteValue: int
    ModuloTen: int

class PointCloudReturnType(Enum):
    Last: int
    FirstOfMany: int
    LastOfMany: int
    Single: int
    All: int

class PointCloudShapeType(Enum):
    DiskFlat: int
    DiskShaded: int

class PointCloudValueFilterMode(Enum):
    Exclude: int
    Include: int

class TerrainDrawCursorType(Enum):
    Composite: int
    NodeSimple: int
    NodeValue: int
    NodeElevation: int
    EdgeSimple: int
    EdgeType: int
    FaceSimple: int
    FaceElevation: int
    FaceSlope: int
    FaceAspect: int
    FaceValue: int
    TerrainPointElevation: int
    TerrainPointAttributeGraduated: int
    TerrainPointAttributeUnique: int
    TerrainDirtyArea: int

class TimelineViewType(Enum):
    DefaultView: int
    SummaryView: int

class BarrierWeight(Enum):
    eNone: int
    Low: int
    Medium: int
    High: int

class BindVariableType(Enum):
    String: int
    Integer: int
    Double: int
    Date: int
    Geometry: int

class BinsToPointsThresholdType(Enum):
    MaxScale: int
    FeatureCount: int

class DataSearchMode(Enum):
    Contains: int
    Exact: int
    StartsWith: int

class DimensionMarkerFit(Enum):
    eNone: int
    Tolerance: int
    Text: int

class DimensionPartOptions(Enum):
    Begin: int
    End: int
    eNone: int
    Both: int

class DimensionTextFit(Enum):
    eNone: int
    MoveBegin: int
    MoveEnd: int

class DimensionTextOption(Enum):
    Only: int
    Suffix: int
    Expression: int
    eNone: int

class DimensionType(Enum):
    Aligned: int
    Linear: int

class DisciplineType(Enum):
    Architectural: int
    Electrical: int
    Mechanical: int
    Piping: int
    Structural: int
    Infrastructure: int

class DisplayFilterType(Enum):
    ByChoice: int
    ByScale: int

class FeatureCacheType(Enum):
    eNone: int
    Session: int

class FeatureExpirationMethod(Enum):
    MaximumFeatureCount: int
    MaximumFeatureAge: int

class FloorFilterRank(Enum):
    eNone: int
    Site: int
    Facility: int
    Level: int

class HtmlPopupStyle(Enum):
    TwoColumnTable: int
    RedirectedHTML: int
    XSLStyleSheet: int

class LocationConditionType(Enum):
    In: int
    Depart: int
    Out: int
    Arrive: int
    Cross: int
    Crossover: int

class MappedOIDFieldType(Enum):
    OID32Bit: int
    OID64Bit: int

class S52AreaSymbolizationType(Enum):
    Plain: int
    Symbolized: int

class S52ColorScheme(Enum):
    Day: int
    Dusk: int
    Night: int

class S52DepthDisplayUnits(Enum):
    Meters: int
    Feet: int
    Fathoms: int

class S52PointSymbolizationType(Enum):
    PaperChart: int
    Simplified: int

class SymbolSubstitutionType(Enum):
    eNone: int
    Color: int
    IndividualSubordinate: int
    IndividualDominant: int

class TemporalFeatureClassCachingMode(Enum):
    All: int
    eNone: int

class TemporalFeatureClassPurgeRule(Enum):
    KeepLatestPerTrack: int
    PurgeOldest: int

class TrajectorySubLayerType(Enum):
    Footprint: int
    Point: int

class WorkspaceFactory(Enum):
    SDE: int
    FileGDB: int
    Raster: int
    Shapefile: int
    OLEDB: int
    Access: int
    DelimitedTextFile: int
    Custom: int
    Sql: int
    Tin: int
    TrackingServer: int
    NetCDF: int
    LASDataset: int
    SQLite: int
    FeatureService: int
    ArcInfo: int
    Cad: int
    Excel: int
    WFS: int
    StreamService: int
    BIMFile: int
    InMemoryDB: int
    NoSQL: int
    BigDataConnection: int
    KnowledgeGraph: int
    NITF: int
    VPF: int
