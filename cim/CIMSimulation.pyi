from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from .CIMLayer import CIMBaseLayer as CIMBaseLayer
from _typeshed import Incomplete

class CIMFloodSimulationObject:
    name: Incomplete
    visible: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFloodSimulationStorage:
    waterSourceAreas: Incomplete
    waterSources: Incomplete
    barriers: Incomplete
    culverts: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRateDuration:
    duration: int
    rate: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSimulationLayer(CIMBaseLayer):
    isActive: bool
    areaOfInterest: Incomplete
    areaOfInterestSymbol: str
    useAutomaticCellResolution: bool
    manualCellResolution: int
    maxAOIEdgeCellCount: int
    elevationDownscalingFactor: int
    duration: int
    currentTime: int
    playbackSpeed: int
    playbackStep: int
    useDefaultNumberOfCacheSlices: bool
    secondsPerSimulationCacheSlice: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFloodSimulationBarrier(CIMFloodSimulationObject):
    path: Incomplete
    height: int
    width: int
    unit: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFloodSimulationCulvert(CIMFloodSimulationObject):
    path: Incomplete
    height: int
    width: int
    unit: Incomplete
    profileType: Incomplete
    materialRoughness: Incomplete
    openTop: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFloodSimulationDepthRaster(CIMFloodSimulationObject):
    rasterDataConnection: str
    linearUnit: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFloodSimulationLayer(CIMSimulationLayer):
    rainfallRate: Incomplete
    rainfallTransitionTime: int
    rainfallDisplayUnits: Incomplete
    evaporationRate: int
    dEMSourceLayers: Incomplete
    colorRamp: str
    valueRangeType: Incomplete
    displayValueRange: str
    initialWaterDepthRaster: str
    infiltrationMaxRaster: str
    infiltrationRateRaster: str
    floodSimulationStorageURI: Incomplete
    waterColorizer: str
    waterDisplayType: Incomplete
    containWaterInAOI: bool
    overrideWeatherEffects: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFloodSimulationRateRaster(CIMFloodSimulationDepthRaster):
    timeUnit: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFloodSimulationWaterSource(CIMFloodSimulationObject):
    location: Incomplete
    waterFlowRate: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFloodSimulationWaterSourceArea(CIMFloodSimulationObject):
    area: Incomplete
    waterFlowRate: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...
