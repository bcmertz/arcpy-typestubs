from json import JSONEncoder

__all__ = ['CimJsonEncoder']

class CimJsonEncoder(JSONEncoder):
    def default(self, o): ...
