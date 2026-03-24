from . import CompoundParameter
from _typeshed import Incomplete

__all__ = ['FuzzyGaussian', 'FuzzyLarge', 'FuzzyLinear', 'FuzzyMSLarge', 'FuzzyMSSmall', 'FuzzyNear', 'FuzzySmall']

class FuzzyMembership(CompoundParameter._CompoundParameter):
    def __init__(self, keyword) -> None: ...

class FuzzyGaussian(FuzzyMembership):
    __esri_toolinfo__: Incomplete
    midpoint: Incomplete
    spread: Incomplete
    def __init__(self, midpoint=None, spread=None) -> None: ...

class FuzzyLarge(FuzzyMembership):
    __esri_toolinfo__: Incomplete
    midpoint: Incomplete
    spread: Incomplete
    def __init__(self, midpoint=None, spread=None) -> None: ...

class FuzzyLinear(FuzzyMembership):
    __esri_toolinfo__: Incomplete
    min: Incomplete
    max: Incomplete
    def __init__(self, min=None, max=None) -> None: ...

class FuzzyMSLarge(FuzzyMembership):
    __esri_toolinfo__: Incomplete
    meanMultiplier: Incomplete
    STDMultiplier: Incomplete
    def __init__(self, meanMultiplier=None, STDMultiplier=None) -> None: ...

class FuzzyMSSmall(FuzzyMembership):
    __esri_toolinfo__: Incomplete
    meanMultiplier: Incomplete
    STDMultiplier: Incomplete
    def __init__(self, meanMultiplier=None, STDMultiplier=None) -> None: ...

class FuzzyNear(FuzzyMembership):
    __esri_toolinfo__: Incomplete
    midpoint: Incomplete
    spread: Incomplete
    def __init__(self, midpoint=None, spread=None) -> None: ...

class FuzzySmall(FuzzyMembership):
    __esri_toolinfo__: Incomplete
    midpoint: Incomplete
    spread: Incomplete
    def __init__(self, midpoint=None, spread=None) -> None: ...
