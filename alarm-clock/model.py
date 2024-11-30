from sqlmodel import SQLModel, Field

class Alarm(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hour: int = Field(ge=0, lt=23)
    minute: int = Field(ge=0, lt=60)
    active: bool = Field(default=True)