from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from .CIMDocument import CIMVersion as CIMVersion
from _typeshed import Incomplete

class CIMBAAreaOfInterest:
    areaOfInterestDataConnection: str
    areaOfInterestItems: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBAAreaOfInterestItem:
    name: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBAColorCodedLayerParameters:
    dataSource: Incomplete
    rendererProperties: str
    variable: Incomplete
    areaOfInterest: str
    activeLevelOfDetail: Incomplete
    levelsOfDetail: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBAFeatureClassAreaOfInterestItem:
    dataConnection: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBAFeatureLayerAreaOfInterestItem:
    uRI: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBALevelOfDetail:
    levelID: Incomplete
    dataConnection: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBARendererProperties:
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBAStdGeoAreaOfInterestItem:
    levelID: Incomplete
    geographyID: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBAVariableListVariable:
    names: Incomplete
    valueTypes: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMHuffModelAttractivenessVariable:
    name: Incomplete
    exponent: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMHuffModelDistanceParameters:
    exponent: int
    dataSource: Incomplete
    distanceUnits: Incomplete
    useTimeUnits: bool
    timeUnits: Incomplete
    useNetworkDistance: bool
    travelModeId: Incomplete
    towardsFacility: bool
    timeOfDay: Incomplete
    timeZone: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSegmentationProfile:
    name: Incomplete
    segmentationSystem: Incomplete
    segmentationBase: Incomplete
    hasVolumetricData: bool
    author: Incomplete
    creationDate: Incomplete
    lastRevisionDate: Incomplete
    counts: Incomplete
    volumetricValues: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSegmentationTarget:
    name: Incomplete
    segmentIDs: Incomplete
    color: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSegmentationTargetGroup:
    name: Incomplete
    segmentationSystem: Incomplete
    description: Incomplete
    author: Incomplete
    creationDate: Incomplete
    lastRevisionDate: Incomplete
    targets: Incomplete
    visualizationProperties: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSegmentationTargetGroupVisualizationProperties:
    targetProfile: str
    baseProfile: str
    thresholdIndex: int
    thresholdComposition: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBAVariableList(CIMVersion):
    name: Incomplete
    iconData: Incomplete
    author: Incomplete
    tags: Incomplete
    dataSource: Incomplete
    creationDate: Incomplete
    lastRevisionDate: Incomplete
    variables: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMHuffModelCalibrationDocument(CIMVersion):
    rMSError: int
    rMSErrorLinear: int
    attractivenessVariables: Incomplete
    distanceParameters: str
    facilities: str
    facilitiesIDFieldName: Incomplete
    customers: str
    customersIDFieldName: Incomplete
    customerWeightFieldName: Incomplete
    salesPotential: str
    salesPotentialIDFieldName: Incomplete
    author: Incomplete
    creationDate: Incomplete
    lastRevisionDate: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSegmentationProfileDocument(CIMVersion):
    profile: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSegmentationTargetGroupDocument(CIMVersion):
    targetGroup: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBAGraduatedColorsRendererProperties(CIMBARendererProperties):
    numBreaks: int
    classificationMethod: Incomplete
    colorRamp: str
    classificationField: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBAUniqueValueRendererProperties(CIMBARendererProperties):
    colorRamp: str
    classificationField: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...
