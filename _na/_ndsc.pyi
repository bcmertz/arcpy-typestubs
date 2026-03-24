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
    BeforeTraversal = 1
    AfterTraversal = 2

class AttributeUsage(IntEnum):
    Cost = 0
    Descriptor = 1
    Restriction = 2
    Hierarchy = 3

class AttributeParameterUsage(IntEnum):
    General = 0
    Restriction = 1
