from bapy import *
from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['ListDatasets', 'ListVariables', 'ListGeographyLevels']

class CountryInfo:
    ISO2: Incomplete
    ISO3: Incomplete
    Name: Incomplete
    def __init__(self, name: Incomplete | None = None, iso2: Incomplete | None = None, iso3: Incomplete | None = None) -> None: ...

class Dataset:
    ID: Incomplete
    DataSourceID: Incomplete
    CountryInfo: Incomplete
    Version: Incomplete
    def __init__(self, id, countryName, countryIso2, countryIso3, vintage, directory: Incomplete | None = None, installDirectory: Incomplete | None = None, networkDatasetPath: Incomplete | None = None, hasMoe: Incomplete | None = None) -> None: ...

class Variable:
    Name: Incomplete
    FullName: Incomplete
    Alias: Incomplete
    DataCollectionID: Incomplete
    OutputFieldName: Incomplete
    Units: Incomplete
    Vintage: Incomplete
    PercentBase: Incomplete
    AverageBase: Incomplete
    def __init__(self, data_collection, name, alias, units, vintage, percentbase, averagebase) -> None: ...

class GeographyLevel:
    LevelID: Incomplete
    LevelName: Incomplete
    IsWholeCountry: Incomplete
    LayerID: Incomplete
    IDField: Incomplete
    NameField: Incomplete
    StateNameField: Incomplete
    StateAbbrevField: Incomplete
    DisplayName: Incomplete
    SingularName: Incomplete
    PluralName: Incomplete
    AdminLevel: Incomplete
    def __init__(self, levelID, levelName, isWholeCountry, layerID, idField, nameField, stateNameField, stateAbbrevField, displayName, singularName, pluralName, adminLevel) -> None: ...

class StandardGeography:
    Name: Incomplete
    ID: Incomplete
    def __init__(self, id, name) -> None: ...

def ListDatasets() -> Generator[Incomplete]: ...
def ListVariables(dataset, include_derivatives: bool = False) -> Generator[Incomplete]: ...
def ListGeographyLevels(dataset) -> Generator[Incomplete]: ...
