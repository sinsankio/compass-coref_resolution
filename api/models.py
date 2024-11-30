from pydantic import Field, BaseModel


class CorefResolverInput(BaseModel):
    text: str = Field(...)
    conv_dict: dict = Field(..., alias="convDict")


class CorefResolverOutput(BaseModel):
    text: str = Field(...)
