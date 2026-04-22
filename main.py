from Task import Task
from datetime import datetime
from TaskStatus import TaskStatus
from TaskHandler import TaskHandler
import uuid, logging


logging.basicConfig(
    filename="task_manager_journal.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


# strftime("%b %d, %Y, %I:%M %p")
# Create a new 4 new task
task_1 = Task(uuid.uuid4(), "First Task", "My First Task description", datetime(2026, 4, 2, 15, 0), datetime(2026, 4, 3, 15, 0), TaskStatus.PENDING)
task_2 = Task(uuid.uuid4(), "Second Task", "My Second Task description", datetime(2026, 4, 2, 15, 0), datetime(2026, 4, 3, 15, 0), TaskStatus.PENDING)
task_3 = Task(uuid.uuid4(), "Third Task", "My Third Task description", datetime(2026, 4, 2, 15, 0), datetime(2026, 4, 3, 15, 0), TaskStatus.PENDING)
task_4 = Task(uuid.uuid4(), "Fourth Task", "My Fourth Task description", datetime(2026, 4, 2, 15, 0), datetime(2026, 4, 3, 15, 0), TaskStatus.PENDING)

def create_tasks():
    # Add these 4 new task to the list of task
    task_handler = TaskHandler()
    
    task_handler.add_task(task_1)
    task_handler.add_task(task_2)
    task_handler.add_task(task_3)
    task_handler.add_task(task_4)

    return task_handler

def update_tasks_randomly(task_handler):
    # Change the description of the first task
    task_handler.update_task_description("My New First Task Description", task_1)

    # change the title of the second task
    task_handler.update_task_title("My New Second Task Title", task_2)

    # change the status of the third task
    task_handler.update_task_status(TaskStatus.IN_PROGRESS, task_3)

    # delete the fourth task
    task_handler.delete_task(task_4)

    # Check the number of task at the end.


def main():
    task_handler = create_tasks()
    update_tasks_randomly(task_handler)

if __name__ == "__main__": 
    main()