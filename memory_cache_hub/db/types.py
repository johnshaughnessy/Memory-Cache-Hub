from typing import Optional
from sqlmodel import Field, SQLModel

class Project(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    is_removed: bool = Field(default=False)

class ProjectDirectory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    path: str
    project_id: Optional[int] = Field(default=None, foreign_key="project.id")
    is_removed: bool = Field(default=False)
