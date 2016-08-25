# Stubs for django.core.files.uploadedfile (Python 3.5)

from typing import Any, Dict, IO, Iterator, Optional, Union
from django.core.files import temp as tempfile
from django.core.files.base import File

class UploadedFile(File):
    content_type = ...  # type: Optional[str]
    charset = ...  # type: Optional[str]
    content_type_extra = ...  # type: Optional[Dict[str, str]]
    def __init__(self, file: IO=None, name: str=None, content_type: str=None, size: int=None, charset: str=None, content_type_extra: Dict[str, str]=None) -> None: ...

class TemporaryUploadedFile(UploadedFile):
    def __init__(self, name: str, content_type: str, size: int, charset: str, content_type_extra: Dict[str, str]=None) -> None: ...
    def temporary_file_path(self) -> str: ...

class InMemoryUploadedFile(UploadedFile):
    field_name = ...  # type: Optional[str]
    def __init__(self, file: Any, field_name: Optional[str], name: str, content_type: Optional[str], size: int, charset: Optional[str], content_type_extra: Dict[str, str]=None) -> None: ...
    def chunks(self, chunk_size: Any=None) -> Iterator[bytes]: ...
    def multiple_chunks(self, chunk_size: int=None) -> bool: ...

class SimpleUploadedFile(InMemoryUploadedFile):
    def __init__(self, name: str, content: bytes, content_type: str='') -> None: ...
    @classmethod
    def from_dict(cls: Any, file_dict: Dict[str, Union[str, bytes]]) -> Any: ...
