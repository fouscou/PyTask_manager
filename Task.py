from TaskStatus import TaskStatus
import logging


class Task:
    def __init__(self, Id, title, description, start_time, end_time, status):
        self.logger = logging.getLogger(self.__class__.__name__)
        self._Id = Id
        self._title = title
        self._description = description
        self._start_time = start_time
        self._end_time = end_time
        self._status = status
        self.logger.info("New Task created (%s; %s ;%s ;%s ;%s ;%s)", Id, title, description, start_time, end_time, status)

    def start_task(self):
        self._status = TaskStatus.IN_PROGRESS
        #self._start_time = datetime.now(timezone.utc)
        #print(f"Started at: {self.start_time:%b %d, %Y, %I:%M %p}")

    def finish_task(self):
        self._status = TaskStatus.COMPLETED
        #self._end_time = datetime.now(timezone.utc)
        #print(f"Finished at: {self.end_time:%b %d, %Y, %I:%M %p}")

    def cancel_task(self):
        self._status = TaskStatus.CANCELLED

    def pause_task(self):
        self._status = TaskStatus.PAUSED

    def task_duration(self):
        pass

    @property
    def Id(self):
        return self._Id

    @property
    def title(self):
        return self._title   

    @property
    def description(self):
        return self._description

    @property
    def start_time(self):
        return self._start_time
    
    @property
    def end_time(self):
        return self._end_time
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, status):
        self._status = status
    
    @description.setter
    def description(self, description):
        if type(description) == str:
            self._description = description
        else:
            self._description = str(description)
    
    @title.setter
    def title(self, title):
        if type(title) == str:
            self._title = title
        else :
            self._title = str(title)
    
    @start_time.setter
    def start_time(self, start_time):
        self.start_time = start_time

    @end_time.setter
    def end_time(self, end_time):
        self.end_time = end_time