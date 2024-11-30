from sqlmodel import SQLModel, Field

class Alarm(SQLModel, table=True):
    hour: int = Field(ge=0, lt=23)
    minute: int = Field(ge=0, lt=60)