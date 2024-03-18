from pydantic import BaseModel, Field
class DiaryEntry(BaseModel):
    title: str = Field(min_length=1, examples=['diary entry title']);
    description: str = Field(min_length=1, examples=['description']);
