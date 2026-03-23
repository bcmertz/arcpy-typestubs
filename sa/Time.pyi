from . import CompoundParameter
from _typeshed import Incomplete

__all__ = ['TimeWithinDay', 'TimeSpecialDays', 'TimeMultipleDays', 'TimeWholeYear']

class Time(CompoundParameter._CompoundParameter):
    def __init__(self, keyword) -> None: ...

class TimeWithinDay(Time):
    __esri_toolinfo__: Incomplete
    day: Incomplete
    startTime: Incomplete
    endTime: Incomplete
    def __init__(self, day: Incomplete | None = None, startTime: Incomplete | None = None, endTime: Incomplete | None = None) -> None: ...

class TimeSpecialDays(Time):
    __esri_toolinfo__: Incomplete
    def __init__(self) -> None: ...

class TimeMultipleDays(Time):
    __esri_toolinfo__: Incomplete
    year: Incomplete
    startDay: Incomplete
    endDay: Incomplete
    def __init__(self, year: Incomplete | None = None, startDay: Incomplete | None = None, endDay: Incomplete | None = None) -> None: ...

class TimeWholeYear(Time):
    __esri_toolinfo__: Incomplete
    year: Incomplete
    def __init__(self, year: Incomplete | None = None) -> None: ...
