from .CIMEnum import *
from .CIMExternal import *
from .ArcpyHelper import GetPythonClass as GetPythonClass
from .CIMLayer import CIMBaseLayer as CIMBaseLayer
from .CIMVectorLayers import CIMDataConnection as CIMDataConnection
from _typeshed import Incomplete

class CIMNALocatorOverrideClass:
    className: Incomplete
    locator: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMNetworkAttributeParameterDefinitionValue:
    networkAttributeName: Incomplete
    networkParameterName: Incomplete
    isRestrictionUsage: bool
    valueType: Incomplete
    value: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMNetworkDatasetRenderer:
    label: Incomplete
    visible: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMNetworkSourceDisplayFilter:
    networkSource: Incomplete
    visible: bool
    definitionExpression: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMNetworkTraceConfiguration:
    name: Incomplete
    iD: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMNetworkTravelModeDefinition:
    name: Incomplete
    modeType: Incomplete
    description: Incomplete
    impedanceAttributeName: Incomplete
    timeAttributeName: Incomplete
    distanceAttributeName: Incomplete
    restrictionAttributeNames: Incomplete
    attributeParameterValues: Incomplete
    useHierarchy: bool
    uTurnAtJunctionsPolicy: Incomplete
    useOutputGeometryPrecision: bool
    outputGeometryPrecisionValue: float
    outputGeometryPrecisionUnits: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMNetworkTravelModeDefinitionContext:
    name: Incomplete
    sourceType: Incomplete
    sourceLayerURI: Incomplete
    travelMode: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRestrictionStatusSymbolClass:
    status: Incomplete
    label: Incomplete
    symbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTraversableDirectionsAdornerPointSymbolClass:
    traversableDirections: Incomplete
    label: Incomplete
    adornerPointSymbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMInMemoryDatasetDataConnection(CIMDataConnection):
    dataset: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMInMemoryWorkspaceDataConnection(CIMDataConnection):
    binaryReferencePath: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMNALayer(CIMBaseLayer):
    standaloneTables: Incomplete
    layers: Incomplete
    symbolLayerDrawing: str
    nAWorkspace: str
    networkDataset: str
    solver: Incomplete
    locator: Incomplete
    locatorOverrides: Incomplete
    agents: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMNetworkDatasetLayer(CIMBaseLayer):
    dataConnection: str
    dirtyAreaRenderer: str
    displayNetworkAttribute: Incomplete
    edgeRenderer: str
    junctionRenderer: str
    missingElementRenderer: str
    networkSourceDisplayFilters: Incomplete
    oneWayRenderer: str
    restrictionNetworkAttributes: Incomplete
    restrictionRenderer: str
    systemJunctionRenderer: str
    trafficNetworkAttribute: Incomplete
    trafficRenderer: str
    traversableRenderer: str
    turnRenderer: str
    travelModeContext: str
    restrictionStatusRenderers: Incomplete
    classifyRestrictionsByPreferenceLevel: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMTraceNetworkLayer(CIMBaseLayer):
    dataConnection: str
    pointErrorLayer: Incomplete
    lineErrorLayer: Incomplete
    systemJunctionsLayer: Incomplete
    dirtyAreaLayer: Incomplete
    connectivityAssociationSymbol: str
    activeTraceConfigurations: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMUtilityNetworkLayer(CIMBaseLayer):
    dataConnection: str
    pointErrorLayer: Incomplete
    lineErrorLayer: Incomplete
    polygonErrorLayer: Incomplete
    dirtyAreaLayer: Incomplete
    connectivityAssociationSymbol: str
    structuralAttachmentAssociationSymbol: str
    containerAssociationSymbol: str
    activeTraceConfigurations: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMNetworkDatasetElementCompositeRenderer(CIMNetworkDatasetRenderer):
    edgeLineRenderer: str
    edgePointRenderer: str
    junctionPointRenderer: str
    turnLineRenderer: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMNetworkDatasetSimpleRenderer(CIMNetworkDatasetRenderer):
    description: Incomplete
    symbol: str
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMNetworkDatasetTrafficRenderer(CIMNetworkDatasetRenderer):
    breaks: Incomplete
    defaultDescription: Incomplete
    defaultLabel: Incomplete
    defaultSymbol: str
    showLiveTrafficOnly: bool
    useDefaultSymbol: bool
    drawLineWidthByHierarchyLevelIndex: bool
    exteriorLineWidthIncrement: int
    interiorLineWidthsByHierarchyLevelIndex: Incomplete
    lineCasingsColor: str
    scaleFilters: Incomplete
    useDerivedLineCasingsColor: bool
    useLineCasings: bool
    useScaleFilters: bool
    def __init__(self, *args, **Kwargs) -> None: ...

class CIMRestrictionStatusRenderer(CIMNetworkDatasetRenderer):
    rendererTarget: Incomplete
    restrictionStatusSymbolClasses: Incomplete
    traversableDirectionsAdornerPointSymbolClasses: Incomplete
    def __init__(self, *args, **Kwargs) -> None: ...
