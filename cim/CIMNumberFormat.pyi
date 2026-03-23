from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from _typeshed import Incomplete

class CIMNumberFormat:
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMCurrencyFormat(CIMNumberFormat):
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMCustomNumberFormat(CIMNumberFormat):
    formatString: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDateFormat(CIMNumberFormat):
    format: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMDirectionFormat(CIMNumberFormat):
    decimalPlaces: int
    format: Incomplete
    directionType: Incomplete
    units: Incomplete
    useNegativeAngles: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMFractionFormat(CIMNumberFormat):
    option: Incomplete
    factor: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMNumericFormatBase(CIMNumberFormat):
    alignmentOption: Incomplete
    alignmentWidth: int
    roundingOption: Incomplete
    roundingValue: int
    showPlusSign: bool
    useSeparator: bool
    zeroPad: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMPercentageFormat(CIMNumericFormatBase):
    adjustPercentage: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRateFormat(CIMNumericFormatBase):
    factor: float
    label: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMScientificNumberFormat(CIMNumberFormat):
    decimalPlaces: int
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMAngleFormat(CIMNumericFormatBase):
    angleInDegrees: bool
    displayDegrees: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMLatLonFormat(CIMNumericFormatBase):
    showDirections: bool
    isLatitude: bool
    showZeroMinutes: bool
    showZeroSeconds: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMNumericFormat(CIMNumericFormatBase):
    suffix: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...
