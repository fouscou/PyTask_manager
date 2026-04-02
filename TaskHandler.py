import logging


class TaskHandler:

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.info("Task handler creation begins")
        self._list_of_tasks = []
        self.logger.info("Task handler creation finished")
    
    @property
    def list_of_tasks(self):
        return self._list_of_tasks
    
    @list_of_tasks.setter
    def list_of_tasks(self, list_of_tasks):
        self._list_of_tasks = list_of_tasks

    def update_task_description(self, description, task):
        self.logger.info("Task %s description update started ", task.Id)
        for current_task in self._list_of_tasks:
            if current_task.Id == task.Id:
                current_task.description = description
                self.logger.info("Task %s description has been updated. The new value is => %s ", current_task.Id, current_task.description)

    def update_task_title(self, title, task):
        self.logger.info("Task %s title update started ", task.Id)
        for current_task in self._list_of_tasks:
            if current_task.Id == task.Id:
                current_task.title = title
                self.logger.info("Task %s title has been updated. The new value is => %s", current_task.Id, current_task.title)
    
    def update_task_start_time(self, start_time, task):
        self.logger.info("Task %s start_time update started ", task.Id)
        for current_task in self._list_of_tasks:
            if current_task.Id == task.Id:
                current_task.start_time = start_time
                self.logger.info("Task %s start time updated. The new value is => %s", current_task.Id, current_task.start_time)

    def update_task_end_time(self, end_time, task):
        self.logger.info("Task %s end_time update started ", task.Id)
        for current_task in self._list_of_tasks:
            if current_task.Id == task.Id:
                current_task.end_time = end_time
                self.logger.info("Task %s start time has been updated. The new value is => %s", current_task.Id, current_task.end_time)

    def update_task_status(self, status, task):
        self.logger.info("Task %s status update started ", task.Id)
        for current_task in self._list_of_tasks:
            if current_task.Id == task.Id:
                current_task.status = status
                self.logger.info("Task %s start time has been updated. The new value is  => %s", current_task.Id, current_task.status)

    def delete_task(self, task):
        self.logger.info("Task %s deletion started ", task.Id)
        for current_task in self._list_of_tasks:
            if current_task.Id == task.Id:
                self.logger.info("Task %s has been deleted", current_task.Id)
                del current_task

    def add_task(self, task):
        self._list_of_tasks.append(task)
        self.logger.info("Task %s has been added to the list", task.Id)