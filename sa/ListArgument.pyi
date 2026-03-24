from . import ComplexArgument as ComplexArgument, Utils as Utils
from _typeshed import Incomplete

class ListArgument(ComplexArgument.ComplexArgument):
    list: Incomplete
    def __init__(self, nrRequiredValues, list_, keyword=None) -> None: ...
