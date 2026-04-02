
class TaskHandler:

    def __init__(self):
        self._list_of_tasks = []

    @property
    def list_of_tasks(self):
        return self._list_of_tasks
    
    @list_of_tasks.setter
    def list_of_tasks(self, list_of_tasks):
        self._list_of_tasks = list_of_tasks

    def update_task_description(self, description, task):
        for current_task in self._list_of_tasks:
            if current_task.Id == task.Id:
                current_task.description = description

    def update_task_title(self, title, task):
        for current_task in self._list_of_tasks:
            if current_task.Id == task.Id:
                current_task.title = title
    
    def update_task_start_time(self, start_time, task):
        for current_task in self._list_of_tasks:
            if current_task.Id == task.Id:
                current_task.start_time = start_time

    def update_task_end_time(self, end_time, task):
        for current_task in self._list_of_tasks:
            if current_task.Id == task.Id:
                current_task.end_time = end_time

    def update_task_status(self, status, task):
        for current_task in self._list_of_tasks:
            if current_task.Id == task.Id:
                current_task.status = status

    def delete_task(self, task):
        for current_task in self._list_of_tasks:
            if current_task.Id == task.Id:
                del current_task

    def add_task(self, task):
        self._list_of_tasks.append(task)