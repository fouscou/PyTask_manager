from enum import Enum

class TaskStatus(Enum):
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    PAUSED = 4
    CANCELLED = 5