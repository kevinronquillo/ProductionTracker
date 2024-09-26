from pydantic import Field
from datetime import datetime


class SoftDeleteMixin:
    deletedAt: str = Field(None)
    isDeleted: bool = Field(None)

    def update_deleted_at(self):
        self.deletedAt = datetime.isoformat()
