import datetime
import json

class Task:
    task_id = 0

    @classmethod
    def __increment_id(cls):
        cls.task_id += 1

    def __str__(self) -> str:
        return f'(ID: {self._id})'
    
    def __init__(self, description, status="todo") -> None:
        self._id = self.task_id
        self._description = description
        self._status = status
        self._createdAt = datetime.datetime.now()
        self._updatedAt = datetime.datetime.now()

        self.__increment_id()
    
    def save(self):
        ...
        
    def delete(self):
        ...
        
    def update(self):
        ...
        
    def get(self):
        ...    

class Tracker: ...


