import datetime
import json
import sys

class Task:
    task_id = 0

    @classmethod
    def __increment_id(cls):
        cls.task_id += 1

    def __str__(self) -> str:
        return f'(ID: {self._id})'
    
    def __init__(self, new=False, description='', status="todo", task=None) -> None:
        if new:
            self._id = self.task_id
            self._description = description
            self._status = status
            self._createdAt = datetime.datetime.now()
            self._updatedAt = datetime.datetime.now()
            self.__increment_id()
        else:
            self._load()
    
    def _load(self, dict):
        ...
    
    def save(self):
        ...
        
    def delete(self):
        ...
        
    def update(self):
        ...
        
    def get(self):
        ...    

class Tracker: ...

def show_avalible_flags() -> None:
    print('Possible flags:\n')
    print('\tadd <str:description> - add new task to your tasks')
    print('\tupdate <int:id> <str:description> - update task by id. Replace old to new description')
    print('\tdelete <int:id> - delete task by id')
    print('\tmark-in-progress <int:id> - replace old status on mark-in-progress')
    print('\tmark-done <int:id> - replace old status on mark-done')
    print('\tlist - to print all tasks')
    print('\tlist <str:done> - to print all tasks with status done')
    print('\tlist <str:todo> - to print all tasks with status todo')
    print('\tlist <str:in-progress> - to print all tasks with status in-progress')
    print('\t-h - to print this help manual')
    

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('The flag was expected to be entered')
        show_avalible_flags()
    else:   
        command = sys.argv[1]
        
        match command:
            case 'add':
                print('add task')
            case 'update':
                print('update task')
            case 'delete':
                print('delete task')
            case 'mark-in-progress':
                print('replace to mark-in-progress')
            case 'mark-done':
                print('mark-done')
            case 'list':
                if len(sys.argv) > 2:
                    ...
                else:
                    print('list')
            case '-h':
                show_avalible_flags()  
            case _:
                print('The flag was expected to be entered')  
                show_avalible_flags() 