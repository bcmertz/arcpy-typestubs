from arcpy.typing.gp import Result2
from typing import Literal

__all__ = ['ServerFilteredFindPaths']

def ServerFilteredFindPaths(in_knowledge_graph_url=None, config_type: Literal['FILE', 'STRING'] | None = None, config_string=None, in_config_file=None, result_type: Literal['FILE', 'STRING'] | None = None, out_results_file=None) -> Result2[str, str]: ...
