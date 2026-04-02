from enum import Enum

class TaskStatus(Enum):
    TO_DO = 1
    IN_PROGRESS = 2
    DONE = 3
    STOPPED = 4
    CANCELLED = 5