from datetime import datetime
from typing import Optional

class SoftDeleteMixin():
    deletedAt: Optional[str] = None
    isDeleted: bool = False

    def update_deleted_at(self):
        self.deletedAt = datetime.now().isoformat()
