import datetime


class Task:
    task_id = 0

    @classmethod
    def __increment_id(cls):
        cls.task_id += 1

    def __init__(self, description, status="todo") -> None:
        self._id = self.task_id
        self._description = description
        self._status = status
        self._createdAt = datetime.datetime.now()
        self._updatedAt = datetime.datetime.now()

        self.__increment_id()


class Tracker: ...
