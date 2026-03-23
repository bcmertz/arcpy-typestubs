from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from .CIMCore import CIMDefinition as CIMDefinition
from _typeshed import Incomplete

class CIMAspectRatio:
    width: float
    height: float
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPresentationLayerOverrideSet:
    layerURI: Incomplete
    visibility: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPresentationMapRestingState:
    startDelay: int
    enabled: bool
    viewpoint: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPresentationMapView:
    mapView: str
    layerOverrides: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPresentationPage:
    transition: str
    holdTime: int
    isAutomaticAdvancement: bool
    backgroundColor: str
    showBackgroundBorder: bool
    margin: str
    elementStorageURI: Incomplete
    extent: Incomplete
    thumbnailURI: Incomplete
    visibility: bool
    locked: bool
    colorVisionDeficiencyMode: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPresentationTransition:
    duration: int
    transitionType: Incomplete
    swipeDirection: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPresentation(CIMDefinition):
    pageSettings: str
    pages: Incomplete
    aspectRatio: str
    colorModel: Incomplete
    rGBColorProfile: Incomplete
    cMYKColorProfile: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMImagePresentationPage(CIMPresentationPage):
    imageURI: Incomplete
    sourceURL: Incomplete
    fitType: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMMapPresentationPage(CIMPresentationPage):
    mapView: str
    restingState: str
    autoPlayAnimationName: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPresentationGravityWellRestingState(CIMPresentationMapRestingState):
    travelTime: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPresentationRotateRestingState(CIMPresentationMapRestingState):
    rotationRate: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMVideoPresentationPage(CIMPresentationPage):
    videoSource: str
    fitType: Incomplete
    startTime: int
    endTime: Incomplete
    loop: bool
    def __init__(self, *args, **Kwargs) -> None: ...
