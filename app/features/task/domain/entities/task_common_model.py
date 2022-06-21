from pydantic import Field, BaseModel


class TaskBaseModel(BaseModel):
    title: str = Field(example='Example title')
    owner_id: int = Field(example=1)
