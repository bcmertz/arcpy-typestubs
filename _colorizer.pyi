from _typeshed import Incomplete
from arcpy.arcobjects._base import pass_parameterized_attr as pass_parameterized_attr, passthrough_attr as passthrough_attr
from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject as convertArcObjectToPythonObject
from arcpy.geoprocessing._base import gp_fixargs as gp_fixargs

class Arc_base:
    def __init__(self, parent) -> None: ...

class Base_raster(Arc_base): ...

class RasterClassifyColorizer(Base_raster):
    breakCount: Incomplete
    classBreaks: Incomplete
    colorRamp: Incomplete
    noDataColor: Incomplete
    classificationField: Incomplete
    classificationMethod: Incomplete
    @property
    def type(self): ...
    def __eq__(self, other): ...

class RasterUniqueValueColorizer(Base_raster):
    colorRamp: Incomplete
    useDefaultSymbol: Incomplete
    field: Incomplete
    groups: Incomplete
    noDataColor: Incomplete
    @property
    def type(self): ...
    def __eq__(self, other): ...

class RasterStretchColorizer(Base_raster):
    colorRamp: Incomplete
    band: Incomplete
    gamma: Incomplete
    invertColorRamp: Incomplete
    stretchType: Incomplete
    minPercent: Incomplete
    maxPercent: Incomplete
    standardDeviation: Incomplete
    minLabel: Incomplete
    maxLabel: Incomplete
    @property
    def type(self): ...
    def __eq__(self, other): ...
