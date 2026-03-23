from . import CompoundParameter
from _typeshed import Incomplete

__all__ = ['FuzzyGaussian', 'FuzzyLarge', 'FuzzyLinear', 'FuzzyMSLarge', 'FuzzyMSSmall', 'FuzzyNear', 'FuzzySmall']

class FuzzyMembership(CompoundParameter._CompoundParameter):
    def __init__(self, keyword) -> None: ...

class FuzzyGaussian(FuzzyMembership):
    __esri_toolinfo__: Incomplete
    midpoint: Incomplete
    spread: Incomplete
    def __init__(self, midpoint: Incomplete | None = None, spread: Incomplete | None = None) -> None: ...

class FuzzyLarge(FuzzyMembership):
    __esri_toolinfo__: Incomplete
    midpoint: Incomplete
    spread: Incomplete
    def __init__(self, midpoint: Incomplete | None = None, spread: Incomplete | None = None) -> None: ...

class FuzzyLinear(FuzzyMembership):
    __esri_toolinfo__: Incomplete
    min: Incomplete
    max: Incomplete
    def __init__(self, min: Incomplete | None = None, max: Incomplete | None = None) -> None: ...

class FuzzyMSLarge(FuzzyMembership):
    __esri_toolinfo__: Incomplete
    meanMultiplier: Incomplete
    STDMultiplier: Incomplete
    def __init__(self, meanMultiplier: Incomplete | None = None, STDMultiplier: Incomplete | None = None) -> None: ...

class FuzzyMSSmall(FuzzyMembership):
    __esri_toolinfo__: Incomplete
    meanMultiplier: Incomplete
    STDMultiplier: Incomplete
    def __init__(self, meanMultiplier: Incomplete | None = None, STDMultiplier: Incomplete | None = None) -> None: ...

class FuzzyNear(FuzzyMembership):
    __esri_toolinfo__: Incomplete
    midpoint: Incomplete
    spread: Incomplete
    def __init__(self, midpoint: Incomplete | None = None, spread: Incomplete | None = None) -> None: ...

class FuzzySmall(FuzzyMembership):
    __esri_toolinfo__: Incomplete
    midpoint: Incomplete
    spread: Incomplete
    def __init__(self, midpoint: Incomplete | None = None, spread: Incomplete | None = None) -> None: ...
