from _typeshed import Incomplete
from enum import IntEnum

__all__ = ['Attribute', 'AttributeParameter', 'NetworkElement', 'Junction', 'Turn', 'Edge', 'NetworkQuery', 'AttributeEvaluator', 'NetworkTimeUsage', 'AttributeUsage', 'AttributeParameterUsage']

NetworkQuery: Incomplete
AttributeEvaluator: Incomplete
NetworkElement: Incomplete
Junction: Incomplete
Turn: Incomplete
Edge: Incomplete
Attribute: Incomplete
AttributeParameter: Incomplete

class NetworkTimeUsage(IntEnum):
    BeforeTraversal: int
    AfterTraversal: int

class AttributeUsage(IntEnum):
    Cost: int
    Descriptor: int
    Restriction: int
    Hierarchy: int

class AttributeParameterUsage(IntEnum):
    General: int
    Restriction: int
