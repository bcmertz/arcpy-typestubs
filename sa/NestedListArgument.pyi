from . import ComplexArgument as ComplexArgument, Utils as Utils
from _typeshed import Incomplete

class NestedListArgument(ComplexArgument.ComplexArgument):
    table: Incomplete
    def __init__(self, nrRequiredValuesPerRecord, maxNrValuesPerRecord, table, keyword: Incomplete | None = None) -> None: ...
