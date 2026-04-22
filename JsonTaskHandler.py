
from TaskHandler import TaskHandler

class JsonTaskHandler(TaskHandler):
    def __init__(self, task, json_file):
        self._task = task
        self._json_file = json_file
    

    
    