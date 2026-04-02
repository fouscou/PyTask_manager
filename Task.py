class Task:
    def __init__(self, Id, title, description, start_time, end_time, status):
        self._Id = Id
        self._title = title
        self._description = description
        self._start_time = start_time
        self._end_time = end_time
        self._status = status

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
        self._description = description

    @title.setter
    def title(self, title):
        self._title = title

    @start_time.setter
    def start_time(self, start_time):
        self.start_time = start_time

    @end_time.setter
    def end_time(self, end_time):
        self.end_time = end_time