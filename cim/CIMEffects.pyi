from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from _typeshed import Incomplete

class CIMCameraEffect:
    isActive: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPostprocessingEffect:
    isActive: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVisualEffect:
    isActive: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMWeatherEffect:
    isActive: bool
    seed: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBlackAndWhiteEffect(CIMVisualEffect):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBloomPostprocessingEffect(CIMPostprocessingEffect):
    strength: float
    threshold: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMBlueprintEffect(CIMVisualEffect):
    outlineStrength: float
    gridSize: int
    gridSubdivisions: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMCloudyWeatherEffect(CIMWeatherEffect):
    cloudCover: float
    cloudBaseElevation: int
    windSpeed: int
    windDirection: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMColorGradingPostprocessingEffect(CIMPostprocessingEffect):
    saturation: int
    brightness: int
    contrast: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMCrossMosaicEffect(CIMVisualEffect):
    size: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDepthOfFieldEffect(CIMCameraEffect):
    focusDistance: float
    focusDepth: float
    maxBlur: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFoggyWeatherEffect(CIMWeatherEffect):
    fogStrength: float
    fogColor: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMGrainPostprocessingEffect(CIMPostprocessingEffect):
    strength: float
    size: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMHalftoneEffect(CIMVisualEffect):
    dotSize: int
    dotStrength: float
    invertTone: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMHexMosaicEffect(CIMVisualEffect):
    size: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMonochromaticEffect(CIMVisualEffect):
    color: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMOutlineEffect(CIMVisualEffect):
    outlineStrength: float
    outlineColor: str
    backgroundColor: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPencilSketchEffect(CIMVisualEffect):
    grayscale: bool
    crosshatchStrength: float
    crosshatchAngleCount: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPixelatedEffect(CIMVisualEffect):
    pixelSize: int
    colorFactor: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRainyWeatherEffect(CIMWeatherEffect):
    cloudCover: float
    precipitation: float
    cloudBaseElevation: int
    windSpeed: int
    windDirection: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSnowyWeatherEffect(CIMWeatherEffect):
    cloudCover: float
    precipitation: float
    snowCover: bool
    cloudBaseElevation: int
    windSpeed: int
    windDirection: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMSunnyWeatherEffect(CIMWeatherEffect):
    cloudCover: float
    cloudBaseElevation: int
    windSpeed: int
    windDirection: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTiltShiftEffect(CIMCameraEffect):
    blurStrength: float
    leftOffset: float
    rightOffset: float
    topOffset: float
    bottomOffset: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMToonEffect(CIMVisualEffect):
    lineStrength: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVignettePostprocessingEffect(CIMPostprocessingEffect):
    size: float
    strength: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMWatercolorEffect(CIMVisualEffect):
    marginWidth: float
    marginGradient: float
    drawMarginOutlines: bool
    backgroundColor: str
    def __init__(self, *args, **Kwargs) -> None: ...
