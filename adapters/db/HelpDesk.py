from sqlmodel import SQLModel, Field
from datetime import datetime


class HelpDesk(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(default=None)
    case: str = Field()
    email: str = Field(max_length=100)
    status: str = Field(default="FK001")
    country: str = Field(default="MX")
    created_at: datetime = Field(default_factory=datetime.now)
    update_at: datetime = Field(default_factory=datetime.now)
    delete_at: datetime = Field(default=None, nullable=True)
