from arcpy.typing.gp import Result1
from typing import Literal

__all__ = ['CreateKnowledgeGraph', 'LoadTableToKnowledgeGraph']

def CreateKnowledgeGraph(service_name=None, summary=None, tags=None, portal_folder=None, share_with_org: Literal['SHARE', 'NO_SHARE'] | None = None, sharing_groups: list[Literal['Group']] | Literal['Group'] | str | None = None, data_store: Literal['Hosted graph store'] | None = None, data_managed: Literal['ARCGIS_MANAGED', 'USER_MANAGED'] | None = None, unique_id=None, enable_editing: Literal['ENABLE_EDITING', 'DO_NOT_ENABLE_EDITING'] | None = None, enable_add: Literal['ENABLE_ADD', 'DO_NOT_ENABLE_ADD'] | None = None, enable_delete: Literal['ENABLE_DELETE', 'DO_NOT_ENABLE_DELETE'] | None = None, enable_update: Literal['ENABLE_UPDATE', 'DO_NOT_ENABLE_UPDATE'] | None = None, update_options: Literal['PROPERTIES_AND_GEOMETRIES', 'PROPERTIES_ONLY'] | None = None, enable_search: Literal['ENABLE_SEARCH', 'DO_NOT_ENABLE_SEARCH'] | None = None, document_entity_name=None, has_document_relationship_name=None, document_properties=None, max_records=None, max_records_search=None) -> Result1[str]: ...
def LoadTableToKnowledgeGraph(target_knowledge_graph=None, in_dataset=None, data_loading_configuration=None) -> Result1[str]: ...
