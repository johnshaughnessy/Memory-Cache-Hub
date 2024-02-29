from pydantic import BaseModel
from typing import List, Optional
from dataclasses import dataclass
from memory_cache_hub.core.types import Chroma

@dataclass
class ApiConfig:
    host: str
    port: int
    chroma_db_path: str
    file_store_path: str
    llamafile_store_path: str
    completions_url: str
    completions_model: str
    embedding_device: str
    embedding_model: str
    normalize_embeddings: bool

Project = str

class ListProjectsResponse(BaseModel):
    projects: List[Project]

class GetOrCreateProjectRequest(BaseModel):
    project_name: str

class DeleteProjectRequest(BaseModel):
    project_name: str

class FileUpload(BaseModel):
    project_name: str
    file_path: str

class SummarizeFileRequest(BaseModel):
    project_name: str
    file_path: str

class SummarizeFileResponse(BaseModel):
    project_name: str
    summary_file_path: str
    summary: str

class IngestProjectFilesRequest(BaseModel):
    project_name: str

class IngestProjectFilesResponse(BaseModel):
    num_files: int
    num_fragments: int

class RagAskRequest(BaseModel):
    project_name: str
    prompt: str

class RagAskResponse(BaseModel):
    response: str

class DownloadLlamafileByNameRequest(BaseModel):
    llamafile_filename: str

class DownloadLlamafileByNameResponse(BaseModel):
    status: str
    message: Optional[str] = None

class LlamafileDownloadStatusResponse(BaseModel):
    status: str
    message: Optional[str] = None
    progress: Optional[int] = None
    content_length: Optional[int] = None
    written: Optional[int] = None

class StartLlamafileResponse(BaseModel):
    status: str
    message: Optional[str] = None

class StopLlamafileResponse(BaseModel):
    status: str
    message: Optional[str] = None