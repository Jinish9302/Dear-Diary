from pydantic import BaseModel, Field
class Todo(BaseModel):
    title: str = Field(min_length=2, examples=['todo title']);
    description: str = Field(min_length=2, examples=['todo title']);
    done: bool = Field(examples = [False], default=False);