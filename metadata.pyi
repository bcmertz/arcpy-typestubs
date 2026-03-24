from _typeshed import Incomplete
from arcpy.arcobjects._base import _ObjectWithoutInitCall
from arcpy.utils import ArgAdaptor as _ArgAdaptor

class _metadata_constants(_ArgAdaptor):
    __args__: Incomplete

class Metadata(_ObjectWithoutInitCall):
    uri: Incomplete
    xml: Incomplete
    isReadOnly: Incomplete
    title: Incomplete
    summary: Incomplete
    description: Incomplete
    tags: Incomplete
    credits: Incomplete
    accessConstraints: Incomplete
    thumbnailUri: Incomplete
    minScale: Incomplete
    maxScale: Incomplete
    xMin: Incomplete
    xMax: Incomplete
    yMin: Incomplete
    yMax: Incomplete
    def __init__(self, uri: str = '') -> None: ...
    def copy(self, inputMetadata): ...
    @_metadata_constants.maskargs
    def importMetadata(self, sourceUri, metadata_import_option: str = 'DEFAULT', customStylesheetPath: str = ''): ...
    @_metadata_constants.maskargs
    def exportMetadata(self, outputPath, metadata_export_option: str = 'ISO19139', metadata_removal_option: str = 'REMOVE_ALL_SENSITIVE_INFO', customStylesheetPath: str = ''): ...
    @_metadata_constants.maskargs
    def synchronize(self, metadata_sync_option: str = 'ALWAYS', interval: int = 0): ...
    def reload(self): ...
    def save(self): ...
    @_metadata_constants.maskargs
    def saveAsXML(self, outputPath, metadata_save_as_xml_option: str = 'EXACT_COPY'): ...
    def saveAsUsingCustomXSLT(self, outputPath, customStylesheetPath): ...
    @_metadata_constants.maskargs
    def upgrade(self, metadata_upgrade_option): ...
    @_metadata_constants.maskargs
    def deleteContent(self, metadata_delete_content_option): ...
