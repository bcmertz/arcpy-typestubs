from enum import Enum

class BABenchmarkAboveAndBelowType(Enum):
    RawValue = 1
    Percentage = 2

class BABenchmarkHighlightExtremesType(Enum):
    IQR = 1
    StandardDeviation = 2

class BABenchmarkMethod(Enum):
    Average = 1
    Median = 2
    Feature = 3
    eNone = 4

class BABenchmarkStyle(Enum):
    AboveOrBelow = 1
    AboveInBetweenOrBelow = 2
    Quartiles = 3
    HighToLow = 4
    TopAndBottom = 5
    Quantiles = 6
    HighlightExtremes = 7
    eNone = 0

class BABenchmarkTopAndBottomType(Enum):
    Rank = 1
    Percentile = 2

class BABoundaryMode(Enum):
    Geographies = 1
    H3Hexagons = 2

class BACombinationMethod(Enum):
    Sum = 1
    Mean = 2
    Product = 3
    GeometricMean = 4

class BACriterionInfluence(Enum):
    Positive = 1
    Inverse = 2
    Ideal = 3
    TargetSite = 4

class BAFinalScoreMethod(Enum):
    eNone = 0
    Method0_1 = 1
    Method0_100 = 2

class BAHistogramSubsetSelectionMethod(Enum):
    Outliers = 1
    Percentage = 2
    StandardDeviation = 3

class BAPointCriterionType(Enum):
    Count = 1
    Weight = 2
    MinDistance = 3

class BAPointStatisticsType(Enum):
    Sum = 1
    Ave = 2
    StdDev = 3
    Min = 4
    Max = 5

class BAPreprocessingMethod(Enum):
    MinMax = 1
    Percentile = 2
    ZScore = 3
    Raw = 4

class BAPresetMethod(Enum):
    CombineValues = 1
    CompoundDifferences = 2
    Custom = 3

class BAScatterplotChartType(Enum):
    Scatterplot = 1
    BubbleChart = 2

class BAVariableListValueType(Enum):
    Number = 0
    Percent = 1
    Average = 2
    Index = 3

class ChartAggregationType(Enum):
    eNone = 0
    Minimum = 1
    Maximum = 2
    Mean = 3
    Median = 4
    Sum = 5
    Majority = 6
    Minority = 7

class ChartColorType(Enum):
    SingleColor = 0
    ColorMatch = 1
    CustomColor = 2

class ChartDataTransformationType(Enum):
    eNone = 0
    Logarithmic = 1
    SquareRoot = 2
    Inverse = 3
    BoxCox = 4

class ChartDimensionalProfilePlotType(Enum):
    Variables = 0
    Bands = 1
    DimensionValues = 2
    Variable = 3
    Band = 4
    CCDC = 5
    LandTrendr = 6
    Dimension = 7

class ChartFontWeight(Enum):
    Lighter = 0
    Normal = 1
    Bold = 2

class ChartGuideType(Enum):
    ChartGuideType_Line = 0
    ChartGuideType_Range = 1
    ChartGuideType_Polyline = 2

class ChartLegendAlignment(Enum):
    Left = 0
    Right = 1
    Top = 2
    Bottom = 3

class ChartLineDashStyle(Enum):
    Solid = 0
    Dot = 1
    Dash = 2
    DashDot = 3
    LongDash = 4
    LongDashDot = 5

class ChartMapSelectionHandling(Enum):
    eNone = 0
    Highlight = 1
    BuildFromSelectionSet = 2

class ChartMarkerSymbolStyle(Enum):
    Circle = 0
    Square = 1
    Diamond = 2
    Triangle = 3
    Star_FourPoint = 4
    Star_FivePoint = 5
    Cross = 6

class ChartMultiBarType(Enum):
    eNone = 0
    SideBySide = 1
    Stacked = 2
    Stacked100 = 3

class ChartNullPolicy(Enum):
    Null = 0
    Zero = 1
    Interpolate = 2

class ChartPosition(Enum):
    ChartPosition_Center = 0
    ChartPosition_Top = 1
    ChartPosition_Bottom = 2
    ChartPosition_Left = 3
    ChartPosition_Right = 4

class ChartProbabilityPlotType(Enum):
    NormalQQPlot = 0
    QQPlot = 1

class ChartSPMDiagonalOption(Enum):
    eNone = 0
    Histogram = 1
    FieldName = 2

class ChartSPMDisplayOption(Enum):
    eNone = 0
    PreviewPlot = 1
    ScatterPlots = 2
    RSquared = 3
    PearsonsR = 4

class ChartSPMSortByType(Enum):
    RSquared = 0
    PearsonsR = 1
    Alphabetical = 2
    Custom = 3

class ChartScatterDisplayOption(Enum):
    ScatterPlots = 0
    RSquared = 1
    PearsonsR = 2

class ChartSortDirection(Enum):
    Ascending = 0
    Descending = 1

class ChartSurfaceProfilePlotType(Enum):
    SingleLayer = 0
    MultiLayer = 1

class ChartTextCase(Enum):
    Normal = 0
    Uppercase = 1
    Lowercase = 2
    Capitalize = 3
    SmallCaps = 4

class ChartTimeAggregationType(Enum):
    eNone = 0
    EqualIntervalsFromStartTime = 1
    EqualIntervalsFromEndTime = 2
    CalendarIntervals = 3
    ReferenceTime = 4

class ChartTrajectoryProfilePlotType(Enum):
    Tracks = 0
    Track = 1
    Points = 2
    Layers = 3

class ChartTrendLineFitType(Enum):
    ChartTrendLineFitType_Linear = 0
    ChartTrendLineFitType_Exponential = 1
    ChartTrendLineFitType_Logarithmic = 2
    ChartTrendLineFitType_Power = 3
    ChartTrendLineFitType_Fourier = 4
    ChartTrendLineFitType_Polynomial = 5
    ChartTrendLineFitType_MinX = 6
    ChartTrendLineFitType_MinY = 7
    ChartTrendLineFitType_MaxX = 8
    ChartTrendLineFitType_MaxY = 9
    ChartTrendLineFitType_AverageX = 10
    ChartTrendLineFitType_AverageY = 11

class ChartType(Enum):
    Basic = 0
    Combo = 1

class ChartValueType(Enum):
    ChartValueType_Numeric = 0
    ChartValueType_Temporal = 1

class ProfileGraphLineSeriesType(Enum):
    ProfileGraphLineSeriesType_LineOnly = 0
    ProfileGraphLineSeriesType_LineAndVertices = 1
    ProfileGraphLineSeriesType_Fill = 2

class ProfileGraphVariableInYAxis(Enum):
    ProfileGraphVariableInYAxis_Z = 0
    ProfileGraphVariableInYAxis_M = 1

class SpectralProfileDisplayMode(Enum):
    MeanLine = 0
    Boxes = 1
    BoxesAndMeanLine = 2
    ConsolidatedBoxesAndMeanLine = 3

class SpectralProfileHorizontalUnit(Enum):
    BandIDs = 0
    Wavelengths = 1
    BandNames = 2

class ColorSpaceType(Enum):
    RGB = 1
    CMYK = 2
    Gray = 3
    HSV = 4
    HLS = 5
    XYZ = 7
    LAB = 8
    Spot = 9

class FixedColorRampArrangementType(Enum):
    Default = 1
    Bivariate = 2

class PolarDirection(Enum):
    Auto = 0
    Clockwise = 1
    Counterclockwise = 2

class DataEngineeringSourceFilterType(Enum):
    eNone = 0
    Selection = 1
    Extent = 2
    SelectionAndExtent = 3

class DataEngineeringStatType(Enum):
    Mean = 0
    StandardDeviation = 1
    Maximum = 2
    Minimum = 3
    Median = 4
    Mode = 5
    FirstQuartile = 6
    ThirdQuartile = 7
    Sum = 8
    NumberOfNulls = 9
    Outliers = 10
    NumberUniqueValues = 11
    LeastCommon = 12
    Kurtosis = 13
    Skewness = 14
    CoefficientOfVariation = 15
    Range = 16
    IQR = 17
    Count = 18

class DataEngineeringTreatFieldAsType(Enum):
    Numerical = 0
    Categorical = 1
    DateTime = 2
    Other = 3

class DataEngineeringViewLayoutType(Enum):
    FieldsAndStatistics = 0
    OnlyStatistics = 1

class ProjectThumbnailAutomaticGenerationSource(Enum):
    ActiveMap = 0
    SpecifiedMap = 1

class ProjectThumbnailGenerationMethod(Enum):
    Manual = 0
    Automatic = 1

class SceneDrawingMode(Enum):
    Perspective = 0
    Isometric = 1

class StatisticalDataCollectionSummaryType(Enum):
    Sum = 0
    Avg = 1
    Min = 2
    Max = 3
    Script = 4

class StatisticalReportFieldFormat(Enum):
    Count = 0
    Percent = 1
    Currency = 2

class TableRowHeightType(Enum):
    eNone = 0
    Single = 1
    Double = 2
    Triple = 3

class DepthOfFieldMaxBlur(Enum):
    Small = 0
    Medium = 1
    Large = 2
    VeryLarge = 3

class AltitudeMode(Enum):
    ClampToGround = 0
    RelativeToGround = 1
    Absolute = 2

class AnimationTransition(Enum):
    eNone = 0
    Linear = 1
    Stepped = 2
    Hop = 3
    FixedArc = 4
    AdjustableArc = 5
    Hold = 6

class BaseElevationType(Enum):
    Expression = 0
    Surface = 1
    Shape = 2

class BillboardMode(Enum):
    eNone = 0
    SignPost = 1
    FaceNearPlane = 2

class ColorModel(Enum):
    RGB = 0
    CMYK = 1

class ColorVisionDeficiencyType(Enum):
    eNone = 0
    Deuteranopia = 1
    Protanopia = 2
    Tritanopia = 3
    Achromatopsia = 4

class DominantSizeAxis(Enum):
    Z = 0
    X = 1
    Y = 2

class ElevationMode(Enum):
    BaseGlobeSurface = 0
    CustomSurface = 1
    eNone = 2

class ExtrusionType(Enum):
    eNone = 0
    MinZ = 1
    MaxZ = 2
    Base = 3
    Absolute = 4

class FaceCulling3D(Enum):
    Backface = 0
    Frontface = 1
    eNone = 2
    FromGeometry = 3

class GradientStrokeMethod(Enum):
    AcrossLine = 0
    AlongLine = 1

class MapLayerType(Enum):
    Operational = 0
    BasemapBackground = 1
    BasemapTopReference = 2
    MapNotes = 3

class MapViewingMode(Enum):
    Map = 0
    SceneLocal = 1
    SceneGlobal = 2
    MapStereo = 3

class OffsetCurveMethod(Enum):
    Square = 0
    Mitered = 1
    Bevelled = 2
    Rounded = 3

class OffsetCurveOption(Enum):
    Fast = 0
    Accurate = 1

class PrimitiveShapeType(Enum):
    Unknown = 0
    Cone = 1
    Cube = 2
    Cylinder = 3
    Diamond = 4
    Sphere = 5
    Tetrahedron = 6

class PrimitiveType3D(Enum):
    TriangleStrip = 0
    TriangleFan = 1
    TriangleList = 2
    PointList = 3
    LineList = 4

class RangeRelation(Enum):
    Overlaps = 0
    OverlapsStartWithinEnd = 1
    AfterStartOverlapsEnd = 2
    Within = 3

class RasterResamplingType(Enum):
    NearestNeighbor = 0
    BilinearInterpolation = 1
    CubicConvolution = 2
    Majority = 3
    BilinearInterpolationPlus = 4
    BilinearGaussianBlur = 5
    BilinearGaussianBlurPlus = 6
    Average = 7
    Minimum = 8
    Maximum = 9
    VectorAverage = 10

class RasterStretchStatsType(Enum):
    AreaOfView = 0
    Dataset = 1
    GlobalStats = 2

class RasterStretchType(Enum):
    eNone = 0
    DefaultFromSource = 1
    Custom = 2
    StandardDeviations = 3
    HistogramEqualize = 4
    MinimumMaximum = 5
    HistogramSpecification = 6
    PercentMinimumMaximum = 7
    Count = 8
    ESRI = 9
    SquareRoot = 10
    Logarithm = 11

class RotationOrder(Enum):
    XYZ = 0
    ZXY = 1
    YXZ = 2

class ColorBalanceMethod(Enum):
    Dodging = 0
    Histogram = 1
    StdDev = 2
    eNone = 3

class ColorCorrectionStretchType(Enum):
    eNone = 0
    Adaptive = 1
    MinMax = 2
    StdDev = 3

class ColorMatchingMethod(Enum):
    Statistics = 0
    Histogram = 1
    LinearCorrelation = 2
    eNone = 3

class ColorizerHillshadeType(Enum):
    Traditional = 0
    Multidirectional = 1

class ColorizerScalingType(Enum):
    eNone = 0
    Adjusted = 1

class FlowRepresentationType(Enum):
    From = 0
    To = 1

class MosaicSubLayerType(Enum):
    Boundary = 0
    Footprint = 1
    Image = 2
    Seamline = 3

class PansharpeningType(Enum):
    IHS = 0
    Brovey = 1
    ESRI = 2
    Mean = 3

class RasterFootprintDrawMode(Enum):
    All = 0
    OnlyPrimary = 1

class RasterHistogramEditType(Enum):
    Lines = 0
    Splines = 1
    Points = 2

class RasterMosaicMethod(Enum):
    eNone = 0
    Center = 1
    Nadir = 2
    Viewpoint = 3
    Attribute = 4
    LockRaster = 5
    Northwest = 6
    Seamline = 7

class RasterMosaicOperatorType(Enum):
    First = 0
    Last = 1
    Min = 2
    Max = 3
    Mean = 4
    Blend = 5
    Sum = 6

class SpeedUnitType(Enum):
    Unknown = 0
    MetersPerSecond = 1
    KilometersPerHour = 2
    Knots = 3
    FeetPerSecond = 4
    MilesPerHour = 5

class StretchType(Enum):
    Gamma = 0
    MinMax = 1
    StdDev = 2
    eNone = 3

class SymbolTileUnitType(Enum):
    Unknown = 0
    Feet = 1
    Miles = 2
    NauticalMiles = 3
    Meters = 4
    Kilometers = 5
    DecimalDegrees = 6
    Pixels = 100

class SymbolizationType(Enum):
    Scalar = 0
    SingleArrow = 1
    WindBarbs = 2
    BeaufortWindKnots = 3
    BeaufortWindMetersPerSecond = 4
    OceanCurrentKnots = 5
    OceanCurrentMetersPerSecond = 6
    BeaufortWindMilesPerHour = 7
    BeaufortWindKilometersPerHour = 8
    ClassifiedArrow = 9
    Custom = 100

class TargetColorSurfaceType(Enum):
    SingleColorPoint = 0
    ColorGrid = 1
    FirstOrderSurface = 2
    SecondOrderSurface = 3
    ThirdOrderSurface = 4

class CentralityRelationshipInterpretation(Enum):
    Undirected = 0
    Directed = 1
    Reversed = 2

class CentralityScoresNormalization(Enum):
    eNone = 0
    Global = 1
    ByComponent = 2

class EventsTicksVisualization(Enum):
    eNone = 0
    StartOnly = 1
    StartAndEnd = 2

class FFPConfigurationWarning(Enum):
    eNone = 0
    AllOriginsAreExcluded = 1
    AllDestinationsAreExcluded = 2
    AllOptionalWaypointsAreExcluded = 3
    AtLeastOneMandatoryEntityWaypointIsExcluded = 4
    AtLeastOneMandatoryRelationshipWaypointIsExcluded = 5
    ReachedMaxPathLength = 6

class FilteredFindPathsEntityUsage(Enum):
    AnyOriginAnyDestination = 0
    AnyOriginAllDestinations = 1
    AllOriginsAnyDestination = 2
    AllOriginsAllDestinations = 3
    EachPair = 4

class KGDurativeEventMissingOneTimeBehaviour(Enum):
    Error = 0
    Exclude = 1
    MakeNonEvent = 2
    MakePunctualEvent = 3

class KGDurativeEventSwappedTimesBehaviour(Enum):
    Error = 0
    Exclude = 1
    MakeNonEvent = 2
    MakeMinPunctualEvent = 3
    MakeMaxPunctualEvent = 4
    MakeDurativeEvent = 5

class KGEventMissingAllTimesBehaviour(Enum):
    Error = 0
    Exclude = 1
    MakeNonEvent = 2

class KGPathFilterItemType(Enum):
    Entity = 0
    Relationship = 1

class KGPathFilterType(Enum):
    IncludeOnly = 0
    Exclude = 1
    MandatoryWaypoint = 2
    OptionalWaypoint = 3

class KGPathFindingError(Enum):
    eNone = 0
    ConfigurationHasTooManyInputEntities = 1
    ConfigurationIsTooComplex = 2
    PunctualEventHasNoTime = 3
    DurativeEventHasNoTime = 4
    DurativeEventHasOneMissingTime = 5
    DurativeEventHasSwappedTimes = 6

class KGPathMode(Enum):
    Shortest = 0
    All = 1

class KGPathTimeFlow(Enum):
    Forward = 0
    Backward = 1
    Unconstrained = 2

class KGTraversalDirectionType(Enum):
    Any = 0
    Forward = 1
    Backward = 2

class KnowledgeGraphSearchFilterScope(Enum):
    Entities = 1
    Relationships = 2
    BothEntitiesAndRelationships = 3
    Provenance = 4

class KnowledgeLinkChartLayoutAlgorithm(Enum):
    Organic_Standard = 0
    Organic_LeafCircle = 1
    Organic_Fusiform = 2
    Organic_Community = 3
    Geographic_Organic_Standard = 4
    Basic_Grid = 5
    Tree_LeftToRight = 6
    Tree_RightToLeft = 7
    Tree_TopToBottom = 8
    Tree_BottomToTop = 9
    Radial_RootCentric = 10
    Radial_NodeCentric = 11
    Hierarchical_TopToBottom = 12
    Hierarchical_BottomToTop = 13
    Chronological_MonoTimeline = 14
    Chronological_MultiTimeline = 15

class KnowledgeNonspatialDataDisplayMode(Enum):
    Visible = 0
    Hidden = 1

class LinkChartLayoutDirection(Enum):
    Top = 0
    Bottom = 1
    Left = 2
    Right = 3

class LinkChartLayoutIdealEdgeLengthType(Enum):
    AbsoluteValue = 0
    Multiplier = 1

class ProvenanceBehavior(Enum):
    Exclude = 0
    Include = 1

class FeaturesToLabel(Enum):
    AllVisibleFeatures = 0
    MostCurrentTrackFeatures = 1

class LabelExpressionEngine(Enum):
    VBScript = 0
    JScript = 1
    Python = 2
    Arcade = 3

class LabelFeatureType(Enum):
    Point = 0
    Line = 1
    Polygon = 2

class MaplexAbbreviationType(Enum):
    Translation = 0
    Keyword = 1
    Ending = 2

class MaplexAnchorPointType(Enum):
    GeometricCenter = 0
    ErodedCenter = 1
    Perimeter = 2
    UnclippedGeometricCenter = 3

class MaplexCenterLabelAnchorType(Enum):
    Symbol = 0
    FeatureGeometry = 1

class MaplexConnectionType(Enum):
    MinimizeLabels = 0
    Unambiguous = 1

class MaplexConstrainOffset(Enum):
    NoConstraint = 0
    AboveLine = 1
    BelowLine = 2
    LeftOfLine = 3
    RightOfLine = 4

class MaplexContourAlignmentType(Enum):
    Uphill = 0
    Page = 1
    Downhill = 2

class MaplexContourLadderType(Enum):
    eNone = 0
    Straight = 1
    Curved = 2

class MaplexGraticuleAlignmentType(Enum):
    Straight = 0
    StraightNoFlip = 1
    Curved = 2
    CurvedNoFlip = 3

class MaplexKeyNumberHorizontalAlignment(Enum):
    Auto = 0
    Left = 1
    Right = 2

class MaplexKeyNumberMethod(Enum):
    PreventUnplacedLabels = 0
    AlwaysNumber = 1

class MaplexKeyNumberResetType(Enum):
    eNone = 0
    Maybe = 1
    Always = 2

class MaplexLabelAnchorPoint(Enum):
    CenterOfLabel = 0
    NearestSideOfLabel = 1
    FurthestSideOfLabel = 2

class MaplexLabelRotationType(Enum):
    Geographic = 0
    Arithmetic = 1
    Radians = 2
    AV3 = 3

class MaplexLineFeatureType(Enum):
    General = 0
    Street = 1
    StreetAddressRange = 2
    Contour = 3
    River = 4

class MaplexLinePlacementMethod(Enum):
    CenteredHorizontalOnLine = 0
    CenteredStraightOnLine = 1
    CenteredCurvedOnLine = 2
    CenteredPerpendicularOnLine = 3
    OffsetHorizontalFromLine = 4
    OffsetStraightFromLine = 5
    OffsetCurvedFromLine = 6
    OffsetPerpendicularFromLine = 7

class MaplexMultiPartOption(Enum):
    OneLabelPerFeature = 0
    OneLabelPerPart = 1
    OneLabelPerSegment = 2

class MaplexOffsetAlongLineMethod(Enum):
    BestPositionAlongLine = 0
    BeforeStartOfLine = 1
    AlongLineFromStart = 2
    AlongLineFromEnd = 3
    AfterEndOfLine = 4

class MaplexPointPlacementMethod(Enum):
    AroundPoint = 0
    CenteredOnPoint = 1
    NorthOfPoint = 2
    NorthEastOfPoint = 3
    EastOfPoint = 4
    SouthEastOfPoint = 5
    SouthOfPoint = 6
    SouthWestOfPoint = 7
    WestOfPoint = 8
    NorthWestOfPoint = 9

class MaplexPolygonFeatureType(Enum):
    General = 0
    LandParcel = 1
    River = 2
    Boundary = 3

class MaplexPolygonPlacementMethod(Enum):
    HorizontalInPolygon = 0
    StraightInPolygon = 1
    CurvedInPolygon = 2
    HorizontalAroundPolygon = 3
    RepeatAlongBoundary = 4
    CurvedAroundPolygon = 5

class MaplexQualityType(Enum):
    Low = 0
    Medium = 1
    High = 2

class MaplexRemoveAmbiguousLabelsType(Enum):
    All = 0
    WithinLabelClass = 1
    eNone = 2

class MaplexRotationAlignmentType(Enum):
    Straight = 0
    Horizontal = 1
    Perpendicular = 2

class MaplexStackingAlignment(Enum):
    ChooseBest = 0
    ConstrainLeftOrRight = 1
    ConstrainLeft = 2
    ConstrainRight = 3
    ConstrainCenter = 4

class MaplexUnit(Enum):
    Map = 0
    MM = 1
    Inch = 2
    Point = 3
    Percentage = 4

class StandardFeatureWeight(Enum):
    eNone = 0
    Low = 1
    Medium = 2
    High = 3

class StandardLabelRotationType(Enum):
    Geographic = 0
    Arithmetic = 1
    Radians = 2
    AV3 = 3

class StandardLabelWeight(Enum):
    Low = 0
    Medium = 1
    High = 2

class StandardNumLabelsOption(Enum):
    NoLabelRestrictions = 0
    OneLabelPerName = 1
    OneLabelPerShape = 2
    OneLabelPerPart = 3

class StandardPointPlacementMethod(Enum):
    AroundPoint = 0
    OnTopPoint = 1
    SpecifiedAngles = 2
    RotationField = 3

class StandardPolygonPlacementMethod(Enum):
    AlwaysHorizontal = 0
    AlwaysStraight = 1
    MixedStrategy = 2

class DisplayCacheType(Enum):
    Permanent = 0
    InSession = 1
    eNone = 2
    MaxAge = 3

class ExaggerationMode(Enum):
    ScaleZ = 0
    ScaleVoxelHeight = 1

class LayerEffectsMode(Enum):
    Layer = 0
    Feature = 1

class Lighting3D(Enum):
    OneSideDataNormal = 0
    OneSideResetNormal = 1
    TwoSideDataNormal = 2
    TwoSideResetNormal = 3
    TwoSideDataNormalFromWindingOrder = 4
    TwoSideResetNormalFromWindingOrder = 5

class SortOrderType(Enum):
    Ascending = 0
    Descending = 1

class SublayerVisibilityMode(Enum):
    Independent = 0
    Exclusive = 1

class Anchor(Enum):
    Unspecified = 0
    TopLeftCorner = 1
    TopMidPoint = 2
    TopRightCorner = 3
    LeftMidPoint = 4
    CenterPoint = 5
    RightMidPoint = 6
    BottomLeftCorner = 7
    BottomMidPoint = 8
    BottomRightCorner = 9

class AutoCameraSource(Enum):
    eNone = 0
    Fixed = 1
    MapFrameLink = 2
    MapSeriesLink = 3

class AutoCameraType(Enum):
    Center = 0
    Scale = 1
    CenterAndScale = 2
    Extent = 3

class CondensedTabType(Enum):
    Round = 0
    Rectangle = 1
    RoundedRectangle = 2

class ContiguousTabType(Enum):
    Continuous = 0
    Rounded = 1
    Squared = 2

class CruisingAltitudeDiagramType(Enum):
    Vertical = 1
    Horizontal = 2
    Quadrantal = 3

class DeclinationDirection(Enum):
    West = 0
    East = 1

class DoubleFillScaleBarStyle(Enum):
    Hollow = 0
    Alternating = 1
    DoubleAlternating = 2

class EndPointPosition(Enum):
    eNone = 0
    FromPoint = 1
    ToPoint = 2

class EndPointSelection(Enum):
    First = 1
    Interior = 2
    Last = 4

class ExtentFitType(Enum):
    BestFit = 0
    ExtentCenter = 1
    DataDriven = 2

class ExtentIndicatorType(Enum):
    Frame = 0
    Rectangle = 1
    IndexFeatureFromDDP = 2

class FieldSortInfo(Enum):
    eNone = 0
    Asc = 1
    AscCase = 2
    Desc = 4
    DescCase = 8

class FieldStatisticsFlag(Enum):
    NoStatistics = 0
    Count = 1
    Minimum = 2
    Maximum = 4
    Range = 8
    Sum = 16
    Mean = 32
    Median = 64
    Mode = 128
    StandardDeviation = 256

class GridElementType(Enum):
    Line = 0
    Tick = 1
    Label = 2
    Corner = 3
    IntersectionPoint = 4

class GridLadderLabelPosition(Enum):
    Half = 0
    Third = 1
    Quarter = 2

class GridLineOrientation(Enum):
    NorthSouth = 0
    EastWest = 1

class GridReferencePrecisionLevel(Enum):
    GridZoneDesignator = 0
    PrecisionLevel100km = 1
    PrecisionLevel10km = 2
    PrecisionLevel1km = 3
    PrecisionLevel100m = 4
    PrecisionLevel10m = 5
    PrecisionLevel1m = 6
    ICM = 7

class LeaderType(Enum):
    eNone = 0
    LineToNearestPoint = 1
    LineToMidpoint = 2
    LineThroughCenters = 3
    CalloutToCenter = 4
    CalloutToEdge = 5
    CalloutToEdges = 6

class LegendFittingStrategy(Enum):
    AdjustSize = 0
    AdjustColumns = 1
    AdjustColumnsAndSize = 2
    AdjustFrame = 3
    ManualColumns = 4

class LegendItemArrangement(Enum):
    PatchLabelDescription = 0
    PatchDescriptionLabel = 1
    LabelPatchDescription = 2
    LabelDescriptionPatch = 3
    DescriptionPatchLabel = 4
    DescriptionLabelPatch = 5

class LegendKeepTogetherOption(Enum):
    eNone = 0
    Items = 1
    Groups = 2

class MGRSLabelPosition(Enum):
    Corner = 1
    Center = 2

class MapProductSpecType(Enum):
    Unset = -1
    TLM = 0
    ICM = 1
    JOG = 2
    USTOPO = 3
    GNC = 4
    JNC = 5
    ONC = 6
    TPC = 7
    EVC = 8

class MeterReferenceSquareType(Enum):
    Single = 0
    Multiple = 1
    DualGrid = 2

class NorthType(Enum):
    SimpleNorth = 0
    TrueNorth = 1
    GridNorth = 2
    MagneticNorth = 3

class Orientation(Enum):
    Horizontal = 0
    Vertical = 1

class PageOrientation(Enum):
    Portrait = 0
    Landscape = 1

class ProfileFrameHeightOption(Enum):
    ConstantHeight = 0
    ConstantRatio = 1

class ProfileFrameStyle(Enum):
    AOC = 0
    PATC = 1

class ProfileFrameType(Enum):
    Straight = 0
    Curved = 1

class ProfileObstacleGroundDisplayOption(Enum):
    Actual = 0
    Max = 1
    Min = 2
    Average = 3

class ProfileObstacleMarkerLocation(Enum):
    Surface = 0
    Top = 1
    Base = 2

class ProfileObstacleSymbolSubstitutionType(Enum):
    eNone = 0
    Penetrating = 1
    Protruding = 2

class ProfileTerrainDisplayOption(Enum):
    All = 0
    PenetratingOnly = 1
    Highlight = 2
    eNone = 3

class RectanglePosition(Enum):
    TopSide = 0
    BottomSide = 1
    LeftSide = 2
    RightSide = 3

class ScaleBarFittingStrategy(Enum):
    AdjustDivision = 0
    AdjustDivisions = 1
    AdjustDivisionAndDivisions = 2
    AdjustFrame = 3
    FixedWidth = 4
    FixedHeight = 5
    FixedBarWidth = 6

class ScaleBarFrequency(Enum):
    eNone = 0
    One = 1
    MajorDivisions = 2
    Divisions = 3
    DivisionsAndFirstMidpoint = 4
    DivisionsAndFirstSubdivisions = 5
    DivisionsAndSubdivisions = 6
    DivisionsFirstSubdivisionFirstMidpoint = 7

class ScaleBarLabelPosition(Enum):
    Above = 0
    BeforeLabels = 1
    AfterLabels = 2
    BeforeBar = 3
    AfterBar = 4
    Below = 5
    AboveLeft = 6
    AboveRight = 7
    AboveEnds = 8
    BeforeAndAfterLabels = 9
    BeforeAndAfterBar = 10
    BelowLeft = 11
    BelowRight = 12
    BelowEnds = 13
    OnBarAfterFirstDivision = 14

class ScaleBarVerticalPosition(Enum):
    Above = 0
    Top = 1
    On = 2
    Bottom = 3
    Below = 4
    OnRight = 5
    OnLeft = 6

class StreetIndexDelimiter(Enum):
    Period = 0
    Space = 1
    Hyphen = 2
    Underscore = 3

class StreetIndexWrapMethod(Enum):
    Wrap = 0
    GroupWrap = 1

class TableFrameFillingStrategy(Enum):
    ShowAllRows = 0
    ShowVisibleRows = 1
    ShowMapSeriesRows = 2
    CustomWhereClause = 3

class TableFrameFittingStrategy(Enum):
    AdjustSize = 0
    AdjustColumns = 1
    AdjustColumnsAndSize = 2
    AdjustFrame = 3

class UnitType(Enum):
    Percent = 0
    MapUnits = 1
    PageUnits = 2

class LinkChartFilterPropertyDataType(Enum):
    EntityKeyValue = 0
    LabelValue = 1

class LinkChartFilterScope(Enum):
    Entities = 0
    Relationships = 1
    Both = 2

class LinkChartFilterStage(Enum):
    Unknown = 0
    Data = 1
    Visual = 2

class LinkChartFilterType(Enum):
    Unknown = 0
    FieldData = 1
    PropertyData = 2

class LinkChartLayoutAlgorithm(Enum):
    Clustered = 0
    Organic = 1
    Hierarchy_TopToBottom = 2
    Hierarchy_BottomToTop = 3
    Hierarchy_LeftToRight = 4
    Hierarchy_RightToLeft = 5
    Circular_Default = 6
    Circular_Substructures = 7
    Organic_Substructures = 8
    Organic_Clustered_Substructures = 9
    Organic_Clustered = 10
    Tree_Multi_Parent_Tree_TopToBottom = 11
    Tree_Multi_Parent_Tree_BottomToTop = 12
    Tree_Multi_Parent_Tree_LeftToRight = 13
    Tree_Multi_Parent_Tree_RightToLeft = 14
    Tree_Mindmap_TopToBottom = 15
    Tree_Mindmap_BottomToTop = 16
    Tree_Mindmap_LeftToRight = 17
    Tree_Mindmap_RightToLeft = 18
    Tree_Compact_TopToBottom = 19
    Tree_Compact_BottomToTop = 20
    Tree_Compact_LeftToRight = 21
    Tree_Compact_RightToLeft = 22
    Balloon_Default = 23
    Balloon_Ray_Like = 24
    Radial_Default = 25
    Radial_Dendrogram = 26
    Hierarchy_Curves_TopToBottom = 27
    Hierarchy_Curves_BottomToTop = 28
    Hierarchy_Curves_LeftToRight = 29
    Hierarchy_Curves_RightToLeft = 30
    Hierarchy_Flowchart_TopToBottom = 31
    Hierarchy_Flowchart_BottomToTop = 32
    Hierarchy_Flowchart_LeftToRight = 33
    Hierarchy_Flowchart_RightToLeft = 34

class LinkChartLinkDashStyle(Enum):
    Solid = 0
    Dot = 1
    Dash = 2
    DashDot = 3
    DashDotDot = 4

class LinkChartLinkLabelPlacement(Enum):
    Parallel = 0
    Perpendicular = 1

class LinkChartRelationshipKeyType(Enum):
    eNone = 0
    Entities = 1
    Foreign = 2

class LinkChartSymbolizationSource(Enum):
    MapSymbology = 0
    SingleSymbology = 1

class ClipDistanceMode(Enum):
    Automatic = 0
    Manual = 1

class ClippingMode(Enum):
    eNone = 0
    MapExtent = 1
    CustomShape = 2
    MapSeries = 3

class ComparisonOperator(Enum):
    IsEqual = 1
    NotEqual = 2
    LessThanOrEqualTo = 3
    LessThan = 4
    GreaterThanOrEqualTo = 5
    GreaterThan = 6

class CullDirection(Enum):
    Inward = 0
    Outward = 1
    Camera = 2

class EditingElevationCaptureMode(Enum):
    Off = 0
    Constant = 1
    Surface = 2

class GeoFenceEnterExitRule(Enum):
    EnterContainsAndExitDoesNotIntersect = 0
    EnterContainsAndExitDoesNotContain = 1
    EnterIntersectsAndExitDoesNotIntersect = 2

class GeoFenceNotificationRule(Enum):
    Enter = 0
    EnterOrExit = 1
    Exit = 2

class GeotriggerAccuracyMode(Enum):
    UseGeometry = 0
    UseGeometryWithAccuracy = 1

class GroundToGridScaleType(Enum):
    ConstantFactor = 0
    ComputeUsingElevation = 1

class IlluminationSource(Enum):
    NoonAtCameraPosition = 0
    DateTime = 1
    AbsoluteSunPosition = 2
    MapTime = 3

class JoinOperator(Enum):
    And = 1
    Or = 2
    eNone = 3

class LocatorType(Enum):
    Locator = 0
    Layer = 1
    Table = 2

class MapType(Enum):
    Map = 0
    Scene = 1
    Basemap = 2
    NetworkDiagram = 3
    ContainmentMap = 4
    LinkChart = 5

class ReviewerMonotonicityDirection(Enum):
    NoneAsError = 0
    DecreasingValueAsError = 1
    IncreasingValueAsError = 2

class ReviewerMonotonicityEvaluationType(Enum):
    EvaluateNone = 0
    EvaluateZ = 1
    EvaluateM = 2

class ScaleDisplayFormat(Enum):
    Value = 0
    Alias = 1
    ValueAndAlias = 2
    AliasAndValue = 3

class ScaleFormatType(Enum):
    Absolute = 0
    Imperial = 1

class SliderExtentType(Enum):
    AllLayers = 0
    VisibleLayers = 1
    SingleLayer = 2
    CustomRange = 3

class SliderInteractionMode(Enum):
    Slider = 0
    Picker = 1

class SliderStepType(Enum):
    Interval = 0
    Count = 1
    Feature = 2

class SnapRequestType(Enum):
    SnapRequestType_None = 0
    SnapRequestType_GeometricSnapping = 1
    SnapRequestType_VisualSnapping = 2
    SnapRequestType_GeometricAndVisualSnapping = 3

class SnapTipDisplayPart(Enum):
    SnapTipDisplayNone = 0
    SnapTipDisplayLayer = 1
    SnapTipDisplayType = 2

class SnapXYToleranceUnit(Enum):
    SnapXYToleranceUnitPixel = 0
    SnapXYToleranceUnitMap = 1

class StereoModelDisplayMode(Enum):
    Default = 0
    OnlyLeftImage = 1
    OnlyRightImage = 2
    eNone = 3

class StereoOrientation(Enum):
    UpOrRight = 0
    UpOrLeft = 1
    DownOrRight = 2
    DownOrLeft = 3

class StereoSourceType(Enum):
    StereoModel = 0
    StereoModelCollection = 1

class SurfaceTINShadingMode(Enum):
    Smooth = 0
    Flat = 1

class SwipeDirection(Enum):
    eNone = 0
    Top = 1
    Bottom = 2
    Left = 3
    Right = 4

class TimeOffsetDirection(Enum):
    Past = 0
    Future = 1
    PastAndFuture = 2

class TimeSnapMode(Enum):
    Automatic = 0
    Single = 1
    Interval = 2

class NDSRendererTarget(Enum):
    Edges = 0
    UserJunctions = 1
    SystemJunctions = 2
    Turns = 3
    Traffic = 4
    DirtyAreas = 5

class NetworkTravelModeSourceType(Enum):
    NetworkDataset = 0
    Layer = 1
    Custom = 2

class RestrictionStatus(Enum):
    GeneralTraversable = 0
    NeutralPreferenceLevelTraversable = 1
    Prohibited = 2
    AvoidPreferenceLevelTraversable = 3
    PreferPreferenceLevelTraversable = 4
    MixedPreferenceLevelTraversable = 5
    Invalid = 6

class TraversableDirections(Enum):
    Prohibited = 0
    Traversable = 1
    OneWay = 2

class ValueType(Enum):
    Short = 2
    Long = 3
    Float = 4
    Double = 5
    Date = 7
    String = 8
    Bool = 11

class DirectionFormatOption(Enum):
    DegreesMinutesSeconds = 0
    QuadrantBearing = 1

class DirectionType(Enum):
    NorthAzimuth = 0
    SouthAzimuth = 1
    Polar = 2
    QuadrantBearing = 3

class DirectionUnits(Enum):
    Radians = 0
    DecimalDegrees = 1
    DegreesMinutesSeconds = 2
    Gradians = 3
    Gons = 4

class FractionOption(Enum):
    Digits = 0
    Denominator = 1

class NumericAlignment(Enum):
    AlignRight = 0
    AlignLeft = 1

class RoundingOption(Enum):
    NumberOfDecimals = 0
    NumberOfSignificantDigits = 1

class AttachmentDisplayType(Enum):
    PreviewFirst = 0
    PreviewAll = 1
    List = 2
    Auto = 3

class PresentationMediaContentFitType(Enum):
    eNone = 0
    Fill = 1
    StretchToFill = 2
    Center = 3

class PresentationTransitionType(Enum):
    eNone = 0
    Swipe = 1
    Fade = 2
    Fly = 3

class ConnectionMode(Enum):
    Consumer = 0
    Admin = 1
    Publisher = 2

class IndexedSceneLayerType(Enum):
    IntegratedMesh = 0
    Point = 1
    Object3D = 2

class Object3DRenderingMode(Enum):
    eNone = 0
    Wireframe = 1

class ServerType(Enum):
    AGS = 0
    WMS = 1
    WCS = 2
    WMTS = 3
    WFS = 4
    OGCAPI = 5

class Tiles3DLayerType(Enum):
    IntegratedMesh = 0
    Object3D = 1

class VoxelAlignment(Enum):
    Origin = 0
    Center = 1

class VoxelInterpolationMode(Enum):
    Linear = 0
    Nearest = 1

class VoxelLayerOptimization(Enum):
    Visualization = 0
    Size = 1

class VoxelScalarFormat(Enum):
    I1 = 0
    U1 = 1
    I2 = 2
    U2 = 3
    I4 = 4
    U4 = 5
    I8 = 6
    U8 = 7
    F4 = 8
    F8 = 9

class VoxelValueFilterMode(Enum):
    Exclude = 0
    Include = 1

class VoxelVariableDataType(Enum):
    Continuous = 0
    Discrete = 1

class VoxelVariablePrecision(Enum):
    InputData = 0
    Low = 1
    Medium = 2
    High = 3

class VoxelVisualization(Enum):
    Volume = 0
    Surface = 1

class FloodSimulationCalibrationMode(Enum):
    Slow = 0
    Moderate = 1
    Fast = 2

class FloodSimulationCulvertProfileType(Enum):
    Elliptical = 0
    Rectangular = 1
    Arched = 2

class FloodSimulationValueRangeType(Enum):
    FlowIntensity = 0
    WaterDepth = 1
    WaterSpeed = 2

class FloodSimulationWaterDisplayType(Enum):
    Fill = 0
    Edges = 1
    FillAndEdges = 2

class BivariateGridLegendLabelStrategy(Enum):
    Corners = 0
    Sides = 1

class BivariateGridLegendOrientationType(Enum):
    eNone = 0
    High = 1
    Low = 2
    HighLow = 3
    LowHigh = 4

class BivariateGridSizeOption(Enum):
    TwoByTwo = 0
    ThreeByThree = 1
    FourByFour = 2

class ClassBreakType(Enum):
    GraduatedColor = 0
    GraduatedSymbol = 1
    UnclassedColor = 2

class ClassBreaksLegendVisualVariableOptions(Enum):
    ShowVisualVariableSymbolClasses = 0
    ShowClassesForEachPrimarySymbol = 1

class ClassificationMethod(Enum):
    DefinedInterval = 0
    EqualInterval = 1
    GeometricalInterval = 2
    Manual = 3
    NaturalBreaks = 4
    Quantile = 5
    StandardDeviation = 6

class ColorChannelTarget(Enum):
    SV = 0
    All = 1

class DataNormalizationMethod(Enum):
    Field = 0
    Log = 1
    PercentOfTotal = 2
    Nothing = 3

class ExpressionReturnType(Enum):
    Default = 0
    String = 1
    Numeric = 2

class PatchShape(Enum):
    Default = 0
    Point = 1
    LineHorizontal = 2
    LineZigZag = 3
    LineAngles = 4
    LineArc = 5
    LineCurve = 6
    LineTrail = 7
    LineHydro = 8
    LineVertical3D = 9
    LineZigZag3D = 10
    LineCorkscrew3D = 11
    AreaRectangle = 12
    AreaRoundedRectangle = 13
    AreaPolygon = 14
    AreaCircle = 15
    AreaEllipse = 16
    AreaFootprint = 17
    AreaBoundary = 18
    AreaHydroPoly = 19
    AreaNaturalPoly = 20
    AreaSquare = 21
    AreaHexagonFlat = 22
    AreaHexagonPointy = 23
    AreaTrapezium = 24
    Custom = 100

class PolygonSymbolColorTarget(Enum):
    Fill = 0
    Outline = 1
    FillOutline = 2

class SizeVisualVariableAxis(Enum):
    HeightAxis = 0
    WidthAxis = 1
    DepthAxis = 2
    WidthAndDepthAxes = 3
    AllAxes = 4

class SizeVisualVariableType(Enum):
    eNone = 0
    Expression = 1
    Random = 2
    Proportional = 3
    Graduated = 4

class SymbolRotationType(Enum):
    Geographic = 0
    Arithmetic = 1

class SymbolShapes(Enum):
    Unknown = 0
    Circle = 1
    Square = 2

class ValueRepresentations(Enum):
    Radius = 0
    Area = 1
    Distance = 2
    Width = 3

class VisualVariableInfoType(Enum):
    eNone = 0
    Expression = 1
    Random = 2

class AngleAlignment(Enum):
    Display = 0
    Map = 1

class AnimatedSymbolEasingType(Enum):
    Linear = 0
    EaseIn = 1
    EaseOut = 2
    EaseInOut = 3

class AnimatedSymbolRepeatType(Enum):
    eNone = 0
    Loop = 1
    Oscillate = 2

class BalloonCalloutStyle(Enum):
    Rectangle = 0
    RoundedRectangle = 1
    Oval = 2

class BlendingMode(Enum):
    eNone = 0
    Alpha = 1
    Screen = 2
    Multiply = 3
    Add = 4
    Color = 5
    ColorBurn = 6
    ColorDodge = 7
    Darken = 8
    Difference = 9
    Exclusion = 10
    HardLight = 11
    Hue = 12
    Lighten = 13
    Luminosity = 14
    Normal = 15
    Overlay = 16
    Saturation = 17
    SoftLight = 18
    LinearBurn = 19
    LinearDodge = 20
    LinearLight = 21
    PinLight = 22
    VividLight = 23

class BlockProgression(Enum):
    TTB = 0
    RTL = 1
    BTT = 2

class CGAAttributeType(Enum):
    Float = 0
    String = 1
    Boolean = 2
    Float_Array = 3
    String_Array = 4
    Boolean_Array = 5

class ClippingType(Enum):
    Intersect = 0
    Subtract = 1

class ExternalColorMixMode(Enum):
    Tint = 0
    Ignore = 1
    Multiply = 99

class ExtremityPlacement(Enum):
    Both = 0
    JustBegin = 1
    JustEnd = 2
    eNone = 3

class FillMode(Enum):
    Mosaic = 0
    Centered = 1

class FontEffects(Enum):
    Normal = 0
    Superscript = 1
    Subscript = 2

class FontEncoding(Enum):
    MSSymbol = 0
    Unicode = 1

class FontType(Enum):
    Unspecified = 0
    TrueType = 1
    PSOpenType = 2
    TTOpenType = 3
    Type1 = 4

class GeometricEffectArrowType(Enum):
    OpenEnded = 0
    Block = 1
    Crossed = 2

class GeometricEffectControlMeasureLineRule(Enum):
    FullGeometry = 0
    PerpendicularFromFirstSegment = 1
    ReversedFirstSegment = 2
    PerpendicularToSecondSegment = 3
    SecondSegmentWithTicks = 4
    DoublePerpendicular = 5
    OppositeToFirstSegment = 6
    TriplePerpendicular = 7
    HalfCircleFirstSegment = 8
    HalfCircleSecondSegment = 9
    HalfCircleExtended = 10
    OpenCircle = 11
    CoverageEdgesWithTicks = 12
    GapExtentWithDoubleTicks = 13
    GapExtentMidline = 14
    Chevron = 15
    PerpendicularWithArc = 16
    ClosedHalfCircle = 17
    TripleParallelExtended = 18
    ParallelWithTicks = 19
    Parallel = 20
    PerpendicularToFirstSegment = 21
    ParallelOffset = 22
    OffsetOpposite = 23
    OffsetSame = 24
    CircleWithArc = 25
    DoubleJog = 26
    PerpendicularOffset = 27
    LineExcludingLastSegment = 28
    MultivertexArrow = 29
    CrossedArrow = 30
    ChevronArrow = 31
    ChevronArrowOffset = 32
    PartialFirstSegment = 33
    Arch = 34
    CurvedParallelTicks = 35
    Arc90Degrees = 36
    TipWithPerpendicularAndTicks = 37
    ConcentricCircles = 38
    DoubleJogArrow = 39
    LinkedChevrons = 40
    SegmentThenHalfCircle = 41
    LineWithStraightTicks = 42
    DoubleCurve = 43
    ParallelWithTicksByWidth = 44
    EnclosingRoundedRectangle = 45

class GeometricEffectDonutMethod(Enum):
    Mitered = 0
    Bevelled = 1
    Rounded = 2
    Square = 3
    TrueBuffer = 4

class GeometricEffectEnclosingPolygonMethod(Enum):
    ClosePath = 0
    ConvexHull = 1
    RectangularBox = 2

class GeometricEffectExtensionOrigin(Enum):
    BeginningOfLine = 0
    EndOfLine = 1

class GeometricEffectLocalizerFeatherStyle(Enum):
    Complete = 0
    Left = 1
    Right = 2

class GeometricEffectOffsetMethod(Enum):
    Mitered = 0
    Bevelled = 1
    Rounded = 2
    Square = 3

class GeometricEffectOffsetOption(Enum):
    Fast = 0
    Accurate = 1

class GeometricEffectOffsetTangentMethod(Enum):
    BeginningOfLine = 0
    EndOfLine = 1

class GeometricEffectWaveform(Enum):
    Sinus = 0
    Square = 1
    Triangle = 2
    Random = 3

class GlyphHinting(Enum):
    eNone = 0
    Default = 1
    Force = 2

class GradientAlignment(Enum):
    Buffered = 0
    Left = 1
    Right = 2
    AlongLine = 3

class GradientFillMethod(Enum):
    Linear = 0
    Rectangular = 1
    Circular = 2
    Buffered = 3

class GradientStrokeType(Enum):
    Discrete = 0
    Continuous = 1

class HorizontalAlignment(Enum):
    Left = 0
    Right = 1
    Center = 2
    Justify = 3

class LeaderLineStyle(Enum):
    Base = 0
    MidPoint = 1
    ThreePoint = 2
    FourPoint = 3
    Underline = 4
    CircularCW = 5
    CircularCCW = 6

class LineCapStyle(Enum):
    Butt = 0
    Round = 1
    Square = 2

class LineDashEnding(Enum):
    NoConstraint = 0
    HalfPattern = 1
    HalfGap = 2
    FullPattern = 3
    FullGap = 4
    Custom = 5

class LineDecorationStyle(Enum):
    eNone = -1
    Custom = 0
    Circle = 1
    OpenArrow = 2
    ClosedArrow = 3
    Diamond = 4

class LineGapType(Enum):
    ExtraLeading = 0
    Multiple = 1
    Exact = 2

class LineJoinStyle(Enum):
    Bevel = 0
    Round = 1
    Miter = 2

class MarkerPlacementType(Enum):
    InsidePolygon = 0
    PolygonCenter = 1
    RandomlyInsidePolygon = 2

class MaterialMode(Enum):
    Tint = 0
    Replace = 1
    Multiply = 2

class PlacementAroundPolygonPosition(Enum):
    Top = 0
    Bottom = 1
    Left = 2
    Right = 3
    TopLeft = 4
    TopRight = 5
    BottomLeft = 6
    BottomRight = 7

class PlacementClip(Enum):
    ClipAtBoundary = 0
    RemoveIfCenterOutsideBoundary = 1
    DoNotTouchBoundary = 2
    DoNotClip = 3

class PlacementEndings(Enum):
    NoConstraint = 0
    WithMarkers = 1
    WithFullGap = 2
    WithHalfGap = 3
    Custom = 4

class PlacementGridType(Enum):
    Fixed = 0
    Random = 1
    RandomFixedQuantity = 2

class PlacementOnLineRelativeTo(Enum):
    LineMiddle = 0
    LineBeginning = 1
    LineEnd = 2
    SegmentMidpoint = 3

class PlacementPolygonCenterMethod(Enum):
    OnPolygon = 0
    CenterOfMass = 1
    BoundingBoxCenter = 2

class PlacementRandomlyAlongLineRandomization(Enum):
    Low = 0
    Medium = 1
    High = 2

class PlacementStepPosition(Enum):
    MarkerCenter = 0
    MarkerBounds = 1

class PointSymbolCalloutScale(Enum):
    eNone = 0
    PropUniform = 1
    PropNonuniform = 2
    DifUniform = 3
    DifNonuniform = 4

class Simple3DLineAnchor(Enum):
    Center = 0
    Bottom = 1
    Top = 2

class Simple3DLineStyle(Enum):
    Tube = 0
    Strip = 1
    Wall = 2
    Square = 3
    Rectangle = 4

class SimplePlacementEndings(Enum):
    WithHalfGap = 0
    WithMarkers = 1

class SizeVariationMethod(Enum):
    Random = 0
    Increasing = 1
    Decreasing = 2
    IncreasingThenDecreasing = 3

class SymbolUnits(Enum):
    Relative = 0
    Absolute = 1

class TextCase(Enum):
    Normal = 0
    LowerCase = 1
    Allcaps = 2

class TextReadingDirection(Enum):
    LTR = 0
    RTL = 1

class TextureFilter(Enum):
    Draft = 0
    Picture = 1
    Text = 2

class VerticalAlignment(Enum):
    Top = 0
    Center = 1
    Baseline = 2
    Bottom = 3

class VerticalGlyphOrientation(Enum):
    Right = 0
    Upright = 1
    Mixed = 2

class WaterbodySize(Enum):
    Small = 0
    Medium = 1
    Large = 2

class WaveStrength(Enum):
    Calm = 0
    Rippled = 1
    Slight = 2
    Moderate = 3

class LASStretchAttribute(Enum):
    Elevation = 0
    RGB = 1
    Red = 2
    Green = 3
    Blue = 4
    NearInfrared = 5
    Intensity = 6
    ScanAngle = 7
    GPSTime = 8
    eNone = 9

class LASStretchDrawingType(Enum):
    Symbol = 0
    Splat = 1
    SymbolTint = 2

class LASStretchStatsType(Enum):
    AreaOfView = 0
    Dataset = 1
    GlobalStats = 2

class LASStretchType(Enum):
    DefaultFromSource = 0
    Custom = 1
    MinimumMaximum = 2
    StandardDeviations = 3
    Histogram = 4
    PercentMinMax = 5

class PointCloudFieldTransformType(Enum):
    eNone = 0
    LowFourBit = 1
    HighFourBit = 2
    AbsoluteValue = 3
    ModuloTen = 4

class PointCloudReturnType(Enum):
    Last = 1
    FirstOfMany = 2
    LastOfMany = 4
    Single = 8
    All = -1

class PointCloudShapeType(Enum):
    DiskFlat = 0
    DiskShaded = 1

class PointCloudValueFilterMode(Enum):
    Exclude = 0
    Include = 1

class TerrainDrawCursorType(Enum):
    Composite = 0
    NodeSimple = 1
    NodeValue = 2
    NodeElevation = 3
    EdgeSimple = 4
    EdgeType = 5
    FaceSimple = 6
    FaceElevation = 7
    FaceSlope = 8
    FaceAspect = 9
    FaceValue = 10
    TerrainPointElevation = 11
    TerrainPointAttributeGraduated = 12
    TerrainPointAttributeUnique = 13
    TerrainDirtyArea = 14

class TimelineViewType(Enum):
    DefaultView = 0
    SummaryView = 1

class BarrierWeight(Enum):
    eNone = 0
    Low = 1
    Medium = 2
    High = 3

class BindVariableType(Enum):
    String = 0
    Integer = 1
    Double = 2
    Date = 3
    Geometry = 4

class BinsToPointsThresholdType(Enum):
    MaxScale = 0
    FeatureCount = 1

class DataSearchMode(Enum):
    Contains = 0
    Exact = 1
    StartsWith = 2
    FullTextSearchStartsWith = 3
    FullTextSearchExact = 4

class DimensionMarkerFit(Enum):
    eNone = 0
    Tolerance = 1
    Text = 2

class DimensionPartOptions(Enum):
    Begin = 1
    End = 2
    eNone = 3
    Both = 0

class DimensionTextFit(Enum):
    eNone = 0
    MoveBegin = 1
    MoveEnd = 2

class DimensionTextOption(Enum):
    Only = 0
    Suffix = 1
    Expression = 2
    eNone = 3

class DimensionType(Enum):
    Aligned = 0
    Linear = 1

class DisciplineType(Enum):
    Architectural = 0
    Electrical = 1
    Mechanical = 2
    Piping = 3
    Structural = 4
    Infrastructure = 5

class DisplayFilterType(Enum):
    ByChoice = 0
    ByScale = 1

class FeatureCacheType(Enum):
    eNone = 0
    Session = 1

class FeatureExpirationMethod(Enum):
    MaximumFeatureCount = 0
    MaximumFeatureAge = 1

class FloorFilterRank(Enum):
    eNone = 0
    Site = 1
    Facility = 2
    Level = 3

class HtmlPopupStyle(Enum):
    TwoColumnTable = 0
    RedirectedHTML = 1
    XSLStyleSheet = 2

class LocationConditionType(Enum):
    In = 0
    Depart = 1
    Out = 2
    Arrive = 3
    Cross = 4
    Crossover = 5

class MappedOIDFieldType(Enum):
    OID32Bit = 4
    OID64Bit = 8

class S52AreaSymbolizationType(Enum):
    Plain = 0
    Symbolized = 1

class S52ColorScheme(Enum):
    Day = 0
    Dusk = 1
    Night = 2

class S52DepthDisplayUnits(Enum):
    Meters = 0
    Feet = 1
    Fathoms = 2

class S52PointSymbolizationType(Enum):
    PaperChart = 0
    Simplified = 1

class StandardDeviationMultiplier(Enum):
    eNone = 0
    OneFourth = 1
    OneThird = 2
    OneHalf = 3
    One = 4
    Two = 5
    Custom = 6

class SymbolSubstitutionType(Enum):
    eNone = 0
    Color = 1
    IndividualSubordinate = 2
    IndividualDominant = 3

class TemporalFeatureClassCachingMode(Enum):
    All = 0
    eNone = 1

class TemporalFeatureClassPurgeRule(Enum):
    KeepLatestPerTrack = 0
    PurgeOldest = 1

class TrajectorySubLayerType(Enum):
    Footprint = 0
    Point = 1

class WorkspaceFactory(Enum):
    SDE = 0
    FileGDB = 1
    Raster = 2
    Shapefile = 3
    OLEDB = 4
    Access = 5
    DelimitedTextFile = 6
    Custom = 7
    Sql = 8
    Tin = 9
    TrackingServer = 10
    NetCDF = 11
    LASDataset = 12
    SQLite = 13
    FeatureService = 14
    ArcInfo = 15
    Cad = 16
    Excel = 17
    WFS = 18
    StreamService = 19
    BIMFile = 20
    InMemoryDB = 21
    NoSQL = 22
    BigDataConnection = 23
    KnowledgeGraph = 24
    NITF = 25
    VPF = 26
    Parquet = 27
