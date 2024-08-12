from pydantic import BaseModel, Field
from typing import Optional
import time


class LogModel(BaseModel):
    sessionEmail: str
    event: str
    timestamp: Optional[int] = Field(
        default_factory=lambda: int(time.time())
    )  # Defaults to current epoch time
