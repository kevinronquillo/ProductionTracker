from datetime import datetime
from pydantic import Field

class TimestampMixin:
    createdAt: str = Field(default_factory=lambda: datetime.isoformat())
    modifiedAt: str = Field(default_factory=lambda: datetime.isoformat())

    def update_deleted_at(self):
        self.modifiedAt = datetime.isoformat().utcnow()