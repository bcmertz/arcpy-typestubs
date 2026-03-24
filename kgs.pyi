from _typeshed import Incomplete
from arcpy.typing.gp import Result2
from typing import Literal

__all__ = ['ServerFilteredFindPaths']

def ServerFilteredFindPaths(in_knowledge_graph_url: Incomplete | None = None, config_type: Literal['FILE', 'STRING'] | None = None, config_string: Incomplete | None = None, in_config_file: Incomplete | None = None, result_type: Literal['FILE', 'STRING'] | None = None, out_results_file: Incomplete | None = None) -> Result2[str, str]: ...
