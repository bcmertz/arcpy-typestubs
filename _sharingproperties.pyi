from _typeshed import Incomplete

def rsetattr(object, attr_name, val): ...
def rgetattr(object, attr_name, *args): ...

class _ParameterChecker:
    def __init__(self) -> None: ...

class _PackageSharing(_ParameterChecker):
    sharingLevel: Incomplete
    groups: Incomplete
    def __init__(self, sharingLevel: str = '', groups: str = '') -> None: ...

class _ZDefault(_ParameterChecker):
    value: Incomplete
    enable: Incomplete
    def __init__(self, enable: bool = True, value: int = 0) -> None: ...

class _Timezone(_ParameterChecker):
    ID: Incomplete
    DaylightSavingTime: Incomplete
    preferredTimezoneID: Incomplete
    preferredTimezoneIDDaylightSavingTime: Incomplete
    def __init__(self, ID: Incomplete | None = None, DaylightSavingTime: Incomplete | None = None, preferredTimezoneID: Incomplete | None = None, preferredTimezoneIDDaylightSavingTime: Incomplete | None = None) -> None: ...

class _Cache(_ParameterChecker):
    exportTilesCount: Incomplete
    configuration: Incomplete
    exportTiles: Incomplete
    cacheOnDemand: Incomplete
    useExistingCache: Incomplete
    def __init__(self, configuration: str = '', exportTiles: bool = False, exportTilesCount: int = 100000, cacheOnDemand: Incomplete | None = None, useExistingCache: Incomplete | None = None) -> None: ...

class _ExtensionProperties(_ParameterChecker):
    isEnabled: Incomplete
    def __init__(self, isEnabled: bool = False) -> None: ...

class _ExtensionFeatureServer(_ExtensionProperties):
    featureCapabilities: Incomplete
    allowTrueCurvesUpdates: Incomplete
    onlyAllowTrueCurveUpdatesByTrueCurveClients: Incomplete
    allowUpdateWithoutMValues: Incomplete
    zDefault: Incomplete
    def __init__(self, featureCapabilities: str = '', allowTrueCurvesUpdates: bool = True, onlyAllowTrueCurveUpdatesByTrueCurveClients: bool = True, allowUpdateWithoutMValues: bool = False, zDefaultEnable: bool = False, zDefaultValue: int = 0) -> None: ...

class _Extension(_ParameterChecker):
    feature: Incomplete
    def __init__(self, sharingDraftType) -> None: ...

class _Pooling(_ParameterChecker):
    minInstances: Incomplete
    maxInstances: Incomplete
    type: Incomplete
    def __init__(self, poolingType: str = '', minInstances: int = 1, maxInstances: int = 2) -> None: ...
