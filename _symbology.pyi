from _typeshed import Incomplete
from arcpy._colorizer import RasterClassifyColorizer as RasterClassifyColorizer, RasterStretchColorizer as RasterStretchColorizer, RasterUniqueValueColorizer as RasterUniqueValueColorizer
from arcpy._renderer import Graduated_colors_renderer as Graduated_colors_renderer, Graduated_symbols_renderer as Graduated_symbols_renderer, SimpleRenderer as SimpleRenderer, Unclassed_colors_renderer as Unclassed_colors_renderer, UniqueValueRenderer as UniqueValueRenderer
from arcpy.arcobjects._base import _ObjectWithoutInitCall, _ObjectWithoutInitCallWrapper, pass_parameterized_attr as pass_parameterized_attr, passthrough_attr as passthrough_attr
from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject as convertArcObjectToPythonObject
from arcpy.geoprocessing._base import gp_fixargs as gp_fixargs
from arcpy.utils import ArgAdaptor as ArgAdaptor

class constants(ArgAdaptor):
    __args__: Incomplete

class Symbology(_ObjectWithoutInitCallWrapper):
    def __new__(cls, wrap_object): ...

class Symbol(_ObjectWithoutInitCall):
    name: Incomplete
    color: Incomplete
    angle: Incomplete
    outlineColor: Incomplete
    outlineWidth: Incomplete
    useRealWorldUnits: Incomplete
    size: Incomplete
    def listSymbolsFromGallery(self, wildcard: Incomplete | None = None): ...
    def applySymbolFromGallery(self, wildcard, index: int = 0): ...

class ColorRamp(_ObjectWithoutInitCall):
    name: Incomplete
    def __init__(self, color_ramp_name, index: int = 0) -> None: ...

class ClassBreak(_ObjectWithoutInitCall):
    symbol: Incomplete
    upperBound: Incomplete
    label: Incomplete
    description: Incomplete

class RasterClassBreak(_ObjectWithoutInitCall):
    color: Incomplete
    upperBound: Incomplete
    label: Incomplete
    description: Incomplete

class Item(_ObjectWithoutInitCall):
    symbol: Incomplete
    label: Incomplete
    description: Incomplete
    values: Incomplete

class RasterItem(_ObjectWithoutInitCall):
    color: Incomplete
    label: Incomplete
    description: Incomplete
    values: Incomplete

class ItemGroup(_ObjectWithoutInitCall):
    heading: Incomplete
    items: Incomplete
