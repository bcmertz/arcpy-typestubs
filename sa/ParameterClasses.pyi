import CompoundParameter
from _typeshed import Incomplete

__all__ = ['FuzzyGaussian', 'FuzzyLarge', 'FuzzyLinear', 'FuzzyMSLarge', 'FuzzyMSSmall', 'FuzzyNear', 'FuzzySmall', 'HfBinary', 'HfForward', 'HfInverseLinear', 'HfLinear', 'HfTable', 'KrigingModelOrdinary', 'KrigingModelUniversal', 'NbrAnnulus', 'NbrCircle', 'NbrIrregular', 'NbrRectangle', 'NbrWedge', 'NbrWeight', 'RadiusFixed', 'RadiusVariable', 'RemapRange', 'RemapValue', 'TimeMultipleDays', 'TimeSpecialDays', 'TimeWholeYear', 'TimeWithinDay', 'TopoBoundary', 'TopoCliff', 'TopoCoast', 'TopoContour', 'TopoExclusion', 'TopoLake', 'TopoPointElevation', 'TopoSink', 'TopoStream', 'TfExponential', 'TfGaussian', 'TfLarge', 'TfLinear', 'TfLogarithm', 'TfLogisticDecay', 'TfLogisticGrowth', 'TfMSLarge', 'TfMSSmall', 'TfNear', 'TfPower', 'TfSmall', 'TfSymmetricLinear', 'VfBidirHikingTime', 'VfBinary', 'VfCos', 'VfCosSec', 'VfHikingTime', 'VfInverseLinear', 'VfLinear', 'VfSec', 'VfSecCos', 'VfSymInverseLinear', 'VfSymLinear', 'VfTable', 'WOTable', 'WSTable']

class _FuzzyMembership(CompoundParameter._CompoundParameter):
    def __init__(self, keyword) -> None: ...

class FuzzyGaussian(_FuzzyMembership):
    __esri_toolinfo__: Incomplete
    midpoint: Incomplete
    spread: Incomplete
    def __init__(self, midpoint=None, spread=None) -> None: ...

class FuzzyLarge(_FuzzyMembership):
    __esri_toolinfo__: Incomplete
    midpoint: Incomplete
    spread: Incomplete
    def __init__(self, midpoint=None, spread=None) -> None: ...

class FuzzyLinear(_FuzzyMembership):
    __esri_toolinfo__: Incomplete
    minimum: Incomplete
    maximum: Incomplete
    def __init__(self, minimum=None, maximum=None) -> None: ...

class FuzzyMSLarge(_FuzzyMembership):
    __esri_toolinfo__: Incomplete
    meanMultiplier: Incomplete
    STDMultiplier: Incomplete
    def __init__(self, meanMultiplier=None, STDMultiplier=None) -> None: ...

class FuzzyMSSmall(_FuzzyMembership):
    __esri_toolinfo__: Incomplete
    meanMultiplier: Incomplete
    STDMultiplier: Incomplete
    def __init__(self, meanMultiplier=None, STDMultiplier=None) -> None: ...

class FuzzyNear(_FuzzyMembership):
    __esri_toolinfo__: Incomplete
    midpoint: Incomplete
    spread: Incomplete
    def __init__(self, midpoint=None, spread=None) -> None: ...

class FuzzySmall(_FuzzyMembership):
    __esri_toolinfo__: Incomplete
    midpoint: Incomplete
    spread: Incomplete
    def __init__(self, midpoint=None, spread=None) -> None: ...

class _HorizontalFactor(CompoundParameter._CompoundParameter):
    def __init__(self, keyword) -> None: ...

class HfBinary(_HorizontalFactor):
    __esri_toolinfo__: Incomplete
    zeroFactor: Incomplete
    cutAngle: Incomplete
    def __init__(self, zeroFactor=None, cutAngle=None) -> None: ...

class HfForward(_HorizontalFactor):
    __esri_toolinfo__: Incomplete
    zeroFactor: Incomplete
    sideValue: Incomplete
    def __init__(self, zeroFactor=None, sideValue=None) -> None: ...

class HfLinear(_HorizontalFactor):
    __esri_toolinfo__: Incomplete
    zeroFactor: Incomplete
    cutAngle: Incomplete
    slope: Incomplete
    def __init__(self, zeroFactor=None, cutAngle=None, slope=None) -> None: ...

class HfInverseLinear(_HorizontalFactor):
    __esri_toolinfo__: Incomplete
    zeroFactor: Incomplete
    cutAngle: Incomplete
    slope: Incomplete
    def __init__(self, zeroFactor=None, cutAngle=None, slope=None) -> None: ...

class HfTable(_HorizontalFactor):
    __esri_toolinfo__: Incomplete
    inTable: Incomplete
    def __init__(self, inTable) -> None: ...

class _KrigingModel(CompoundParameter._CompoundParameter):
    def __init__(self) -> None: ...

class KrigingModelOrdinary(_KrigingModel):
    __esri_toolinfo__: Incomplete
    semivariogramType: Incomplete
    lagSize: Incomplete
    majorRange: Incomplete
    partialSill: Incomplete
    nugget: Incomplete
    def __init__(self, semivariogramType=None, lagSize=None, majorRange=None, partialSill=None, nugget=None) -> None: ...

class KrigingModelUniversal(_KrigingModel):
    __esri_toolinfo__: Incomplete
    semivariogramType: Incomplete
    lagSize: Incomplete
    majorRange: Incomplete
    partialSill: Incomplete
    nugget: Incomplete
    def __init__(self, semivariogramType=None, lagSize=None, majorRange=None, partialSill=None, nugget=None) -> None: ...

class _Neighborhood(CompoundParameter._CompoundParameter):
    def __init__(self, keyword) -> None: ...

class NbrAnnulus(_Neighborhood):
    __esri_toolinfo__: Incomplete
    innerRadius: Incomplete
    outerRadius: Incomplete
    units: Incomplete
    def __init__(self, innerRadius=None, outerRadius=None, units=None) -> None: ...

class NbrCircle(_Neighborhood):
    __esri_toolinfo__: Incomplete
    radius: Incomplete
    units: Incomplete
    def __init__(self, radius=None, units=None) -> None: ...

class NbrIrregular(_Neighborhood):
    __esri_toolinfo__: Incomplete
    inKernelFile: Incomplete
    def __init__(self, inKernelFile) -> None: ...

class NbrRectangle(_Neighborhood):
    __esri_toolinfo__: Incomplete
    width: Incomplete
    height: Incomplete
    units: Incomplete
    def __init__(self, width=None, height=None, units=None) -> None: ...

class NbrWedge(_Neighborhood):
    __esri_toolinfo__: Incomplete
    radius: Incomplete
    startAngle: Incomplete
    endAngle: Incomplete
    units: Incomplete
    def __init__(self, radius=None, startAngle=None, endAngle=None, units=None) -> None: ...

class NbrWeight(_Neighborhood):
    __esri_toolinfo__: Incomplete
    inKernelFile: Incomplete
    def __init__(self, inKernelFile) -> None: ...

class _Radius(CompoundParameter._CompoundParameter):
    def __init__(self, keyword) -> None: ...

class RadiusVariable(_Radius):
    __esri_toolinfo__: Incomplete
    numberOfPoints: Incomplete
    maxDistance: Incomplete
    def __init__(self, numberOfPoints=None, maxDistance=None) -> None: ...

class RadiusFixed(_Radius):
    __esri_toolinfo__: Incomplete
    distance: Incomplete
    minNumberOfPoints: Incomplete
    def __init__(self, distance=None, minNumberOfPoints=None) -> None: ...

class _Remap(CompoundParameter._CompoundParameter):
    remapTable: Incomplete
    def __init__(self, remapTable) -> None: ...

class RemapRange(_Remap):
    __esri_toolinfo__: Incomplete
    def __init__(self, remapTable) -> None: ...

class RemapValue(_Remap):
    __esri_toolinfo__: Incomplete
    def __init__(self, remapTable) -> None: ...

class _Time(CompoundParameter._CompoundParameter):
    def __init__(self, keyword) -> None: ...

class TimeWithinDay(_Time):
    __esri_toolinfo__: Incomplete
    day: Incomplete
    startTime: Incomplete
    endTime: Incomplete
    def __init__(self, day=None, startTime=None, endTime=None) -> None: ...

class TimeSpecialDays(_Time):
    __esri_toolinfo__: Incomplete
    def __init__(self) -> None: ...

class TimeMultipleDays(_Time):
    __esri_toolinfo__: Incomplete
    year: Incomplete
    startDay: Incomplete
    endDay: Incomplete
    def __init__(self, year=None, startDay=None, endDay=None) -> None: ...

class TimeWholeYear(_Time):
    __esri_toolinfo__: Incomplete
    year: Incomplete
    def __init__(self, year=None) -> None: ...

class _TopoInput: ...

class _TopoInputNestedList(_TopoInput, CompoundParameter._CompoundParameter):
    inFeatures: Incomplete
    def __init__(self, keyword, inFeatures) -> None: ...

class _TopoInputList(_TopoInput, CompoundParameter._CompoundParameter):
    inFeatures: Incomplete
    def __init__(self, keyword, inFeatures) -> None: ...

class TopoPointElevation(_TopoInputNestedList):
    __esri_toolinfo__: Incomplete
    def __init__(self, inFeatures) -> None: ...

class TopoContour(_TopoInputNestedList):
    __esri_toolinfo__: Incomplete
    def __init__(self, inFeatures) -> None: ...

class TopoStream(_TopoInputList):
    __esri_toolinfo__: Incomplete
    def __init__(self, inFeatures) -> None: ...

class TopoSink(_TopoInputNestedList):
    __esri_toolinfo__: Incomplete
    def __init__(self, inFeatures) -> None: ...

class TopoBoundary(_TopoInputList):
    __esri_toolinfo__: Incomplete
    def __init__(self, inFeatures) -> None: ...

class TopoLake(_TopoInputList):
    __esri_toolinfo__: Incomplete
    def __init__(self, inFeatures) -> None: ...

class TopoCliff(_TopoInputList):
    __esri_toolinfo__: Incomplete
    def __init__(self, inFeatures) -> None: ...

class TopoCoast(_TopoInputList):
    __esri_toolinfo__: Incomplete
    def __init__(self, inFeatures) -> None: ...

class TopoExclusion(_TopoInputList):
    __esri_toolinfo__: Incomplete
    def __init__(self, inFeatures) -> None: ...

class _TransformationFunction(CompoundParameter._CompoundParameter):
    def __init__(self, keyword) -> None: ...

class TfGaussian(_TransformationFunction):
    __esri_toolinfo__: Incomplete
    midpoint: Incomplete
    spread: Incomplete
    lowerThreshold: Incomplete
    valueBelowThreshold: Incomplete
    upperThreshold: Incomplete
    valueAboveThreshold: Incomplete
    def __init__(self, midpoint=None, spread=None, lowerThreshold=None, valueBelowThreshold=None, upperThreshold=None, valueAboveThreshold=None) -> None: ...

class TfNear(_TransformationFunction):
    __esri_toolinfo__: Incomplete
    midpoint: Incomplete
    spread: Incomplete
    lowerThreshold: Incomplete
    valueBelowThreshold: Incomplete
    upperThreshold: Incomplete
    valueAboveThreshold: Incomplete
    def __init__(self, midpoint=None, spread=None, lowerThreshold=None, valueBelowThreshold=None, upperThreshold=None, valueAboveThreshold=None) -> None: ...

class TfLarge(_TransformationFunction):
    __esri_toolinfo__: Incomplete
    midpoint: Incomplete
    spread: Incomplete
    lowerThreshold: Incomplete
    valueBelowThreshold: Incomplete
    upperThreshold: Incomplete
    valueAboveThreshold: Incomplete
    def __init__(self, midpoint=None, spread=None, lowerThreshold=None, valueBelowThreshold=None, upperThreshold=None, valueAboveThreshold=None) -> None: ...

class TfSmall(_TransformationFunction):
    __esri_toolinfo__: Incomplete
    midpoint: Incomplete
    spread: Incomplete
    lowerThreshold: Incomplete
    valueBelowThreshold: Incomplete
    upperThreshold: Incomplete
    valueAboveThreshold: Incomplete
    def __init__(self, midpoint=None, spread=None, lowerThreshold=None, valueBelowThreshold=None, upperThreshold=None, valueAboveThreshold=None) -> None: ...

class TfMSLarge(_TransformationFunction):
    __esri_toolinfo__: Incomplete
    meanMultiplier: Incomplete
    STDMultiplier: Incomplete
    lowerThreshold: Incomplete
    valueBelowThreshold: Incomplete
    upperThreshold: Incomplete
    valueAboveThreshold: Incomplete
    def __init__(self, meanMultiplier=None, STDMultiplier=None, lowerThreshold=None, valueBelowThreshold=None, upperThreshold=None, valueAboveThreshold=None) -> None: ...

class TfMSSmall(_TransformationFunction):
    __esri_toolinfo__: Incomplete
    meanMultiplier: Incomplete
    STDMultiplier: Incomplete
    lowerThreshold: Incomplete
    valueBelowThreshold: Incomplete
    upperThreshold: Incomplete
    valueAboveThreshold: Incomplete
    def __init__(self, meanMultiplier=None, STDMultiplier=None, lowerThreshold=None, valueBelowThreshold=None, upperThreshold=None, valueAboveThreshold=None) -> None: ...

class TfLinear(_TransformationFunction):
    __esri_toolinfo__: Incomplete
    minimum: Incomplete
    maximum: Incomplete
    lowerThreshold: Incomplete
    valueBelowThreshold: Incomplete
    upperThreshold: Incomplete
    valueAboveThreshold: Incomplete
    def __init__(self, minimum=None, maximum=None, lowerThreshold=None, valueBelowThreshold=None, upperThreshold=None, valueAboveThreshold=None) -> None: ...

class TfSymmetricLinear(_TransformationFunction):
    __esri_toolinfo__: Incomplete
    minimum: Incomplete
    maximum: Incomplete
    lowerThreshold: Incomplete
    valueBelowThreshold: Incomplete
    upperThreshold: Incomplete
    valueAboveThreshold: Incomplete
    def __init__(self, minimum=None, maximum=None, lowerThreshold=None, valueBelowThreshold=None, upperThreshold=None, valueAboveThreshold=None) -> None: ...

class TfExponential(_TransformationFunction):
    __esri_toolinfo__: Incomplete
    shift: Incomplete
    baseFactor: Incomplete
    lowerThreshold: Incomplete
    valueBelowThreshold: Incomplete
    upperThreshold: Incomplete
    valueAboveThreshold: Incomplete
    def __init__(self, shift=None, baseFactor=None, lowerThreshold=None, valueBelowThreshold=None, upperThreshold=None, valueAboveThreshold=None) -> None: ...

class TfLogarithm(_TransformationFunction):
    __esri_toolinfo__: Incomplete
    shift: Incomplete
    factor: Incomplete
    lowerThreshold: Incomplete
    valueBelowThreshold: Incomplete
    upperThreshold: Incomplete
    valueAboveThreshold: Incomplete
    def __init__(self, shift=None, factor=None, lowerThreshold=None, valueBelowThreshold=None, upperThreshold=None, valueAboveThreshold=None) -> None: ...

class TfPower(_TransformationFunction):
    __esri_toolinfo__: Incomplete
    shift: Incomplete
    exponent: Incomplete
    lowerThreshold: Incomplete
    valueBelowThreshold: Incomplete
    upperThreshold: Incomplete
    valueAboveThreshold: Incomplete
    def __init__(self, shift=None, exponent=None, lowerThreshold=None, valueBelowThreshold=None, upperThreshold=None, valueAboveThreshold=None) -> None: ...

class TfLogisticGrowth(_TransformationFunction):
    __esri_toolinfo__: Incomplete
    minimum: Incomplete
    maximum: Incomplete
    yInterceptPercent: Incomplete
    lowerThreshold: Incomplete
    valueBelowThreshold: Incomplete
    upperThreshold: Incomplete
    valueAboveThreshold: Incomplete
    def __init__(self, minimum=None, maximum=None, yInterceptPercent=None, lowerThreshold=None, valueBelowThreshold=None, upperThreshold=None, valueAboveThreshold=None) -> None: ...

class TfLogisticDecay(_TransformationFunction):
    __esri_toolinfo__: Incomplete
    minimum: Incomplete
    maximum: Incomplete
    yInterceptPercent: Incomplete
    lowerThreshold: Incomplete
    valueBelowThreshold: Incomplete
    upperThreshold: Incomplete
    valueAboveThreshold: Incomplete
    def __init__(self, minimum=None, maximum=None, yInterceptPercent=None, lowerThreshold=None, valueBelowThreshold=None, upperThreshold=None, valueAboveThreshold=None) -> None: ...

class _VerticalFactor(CompoundParameter._CompoundParameter):
    def __init__(self, keyword) -> None: ...

class VfBinary(_VerticalFactor):
    __esri_toolinfo__: Incomplete
    zeroFactor: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    def __init__(self, zeroFactor=None, lowCutAngle=None, highCutAngle=None) -> None: ...

class VfLinear(_VerticalFactor):
    __esri_toolinfo__: Incomplete
    zeroFactor: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    slope: Incomplete
    def __init__(self, zeroFactor=None, lowCutAngle=None, highCutAngle=None, slope=None) -> None: ...

class VfInverseLinear(_VerticalFactor):
    __esri_toolinfo__: Incomplete
    zeroFactor: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    slope: Incomplete
    def __init__(self, zeroFactor=None, lowCutAngle=None, highCutAngle=None, slope=None) -> None: ...

class VfSymLinear(_VerticalFactor):
    __esri_toolinfo__: Incomplete
    zeroFactor: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    slope: Incomplete
    def __init__(self, zeroFactor: float = 1.0, lowCutAngle: float = -90.0, highCutAngle: float = 90.0, slope: float = 0.011111) -> None: ...

class VfSymInverseLinear(_VerticalFactor):
    __esri_toolinfo__: Incomplete
    zeroFactor: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    slope: Incomplete
    def __init__(self, zeroFactor=None, lowCutAngle=None, highCutAngle=None, slope=None) -> None: ...

class VfCos(_VerticalFactor):
    __esri_toolinfo__: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    cosPower: Incomplete
    def __init__(self, lowCutAngle=None, highCutAngle=None, cosPower=None) -> None: ...

class VfSec(_VerticalFactor):
    __esri_toolinfo__: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    secPower: Incomplete
    def __init__(self, lowCutAngle=None, highCutAngle=None, secPower=None) -> None: ...

class VfCosSec(_VerticalFactor):
    __esri_toolinfo__: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    cosPower: Incomplete
    secPower: Incomplete
    def __init__(self, lowCutAngle=None, highCutAngle=None, cosPower=None, secPower=None) -> None: ...

class VfSecCos(_VerticalFactor):
    __esri_toolinfo__: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    secPower: Incomplete
    cosPower: Incomplete
    def __init__(self, lowCutAngle=None, highCutAngle=None, secPower=None, cosPower=None) -> None: ...

class VfTable(_VerticalFactor):
    __esri_toolinfo__: Incomplete
    inTable: Incomplete
    def __init__(self, inTable) -> None: ...

class VfHikingTime(_VerticalFactor):
    __esri_toolinfo__: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    def __init__(self, lowCutAngle=None, highCutAngle=None) -> None: ...

class VfBidirHikingTime(_VerticalFactor):
    __esri_toolinfo__: Incomplete
    lowCutAngle: Incomplete
    highCutAngle: Incomplete
    def __init__(self, lowCutAngle=None, highCutAngle=None) -> None: ...

class WOTable(CompoundParameter._CompoundParameter):
    __esri_toolinfo__: Incomplete
    weightedOverlayTable: Incomplete
    evaluationScale: Incomplete
    def __init__(self, weightedOverlayTable, evaluationScale) -> None: ...

class WSTable(CompoundParameter._CompoundParameter):
    __esri_toolinfo__: Incomplete
    weightedSumTable: Incomplete
    def __init__(self, weightedSumTable) -> None: ...
