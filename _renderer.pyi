from _typeshed import Incomplete
from arcpy.arcobjects._base import pass_parameterized_attr as pass_parameterized_attr, passthrough_attr as passthrough_attr
from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject as convertArcObjectToPythonObject
from arcpy.geoprocessing._base import gp_fixargs as gp_fixargs

class Arc_base:
    def __init__(self, parent) -> None: ...

class Base_renderer(Arc_base): ...

class UniqueValueRenderer(Base_renderer):
    colorRamp: Incomplete
    groups: Incomplete
    fields: Incomplete
    defaultSymbol: Incomplete
    useDefaultSymbol: Incomplete
    @property
    def type(self): ...
    def listMissingValues(self): ...
    def removeValues(self, values_or_items): ...
    def addValues(self, values_or_items): ...
    def __eq__(self, other): ...

class SimpleRenderer(Base_renderer):
    label: Incomplete
    description: Incomplete
    symbol: Incomplete
    @property
    def type(self): ...
    def __eq__(self, other): ...

class Graduated_colors_renderer(Base_renderer):
    classificationField: Incomplete
    normalizationField: Incomplete
    normalizationType: Incomplete
    classificationMethod: Incomplete
    breakCount: Incomplete
    classBreaks: Incomplete
    colorRamp: Incomplete
    intervalSize: Incomplete
    deviationInterval: Incomplete
    @property
    def type(self): ...
    def __eq__(self, other): ...

class Graduated_symbols_renderer(Base_renderer):
    classificationField: Incomplete
    normalizationField: Incomplete
    normalizationType: Incomplete
    classificationMethod: Incomplete
    breakCount: Incomplete
    classBreaks: Incomplete
    minimumSymbolSize: Incomplete
    maximumSymbolSize: Incomplete
    symbolTemplate: Incomplete
    backgroundSymbol: Incomplete
    colorRamp: Incomplete
    intervalSize: Incomplete
    deviationInterval: Incomplete
    def updateSymbolTemplate(self, symbol_template): ...
    @property
    def type(self): ...
    def __eq__(self, other): ...

class Unclassed_colors_renderer(Base_renderer):
    field: Incomplete
    expression: Incomplete
    normalizationField: Incomplete
    colorRamp: Incomplete
    upperLabel: Incomplete
    lowerLabel: Incomplete
    symbolTemplate: Incomplete
    def updateSymbolTemplate(self, symbol_template): ...
    @property
    def type(self): ...
    def __eq__(self, other): ...
