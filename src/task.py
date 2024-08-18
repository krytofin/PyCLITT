import datetime
import json


class Task:
    task_id = 0

    @classmethod
    def __increment_id(cls) -> None:
        cls.task_id += 1

    def __str__(self) -> str:
        return f"(ID: {self._id})"

    def __repr__(self) -> str:
        return f"(ID: {self._id})"

    def __init__(self, new=False, description="", status="todo", task=None) -> None:
        if new:
            self._id: int = self.task_id
            self.description = description
            self.status = status
            self.createdAt = f"{datetime.datetime.now():%d-%m-%Y %H:%M:%S}"
            self.updatedAt = f"{datetime.datetime.now():%d-%m-%Y %H:%M:%S}"
            self.__increment_id()
        else:
            self._load(task)

    def _load(self, json_data) -> None:
        self._id: int = json_data["id"]
        self.description: int = json_data["description"]
        self.status: int = json_data["status"]
        self.createdAt: int = json_data["createdAt"]
        self.updatedAt: int = json_data["updatedAt"]

        self.__class__.task_id = self._id
        self.__increment_id()

    @property
    def id(self):
        return self._id

    def save(self):
        try:
            with open("store/tasks.json", "+r") as json_file:
                data = json.load(json_file)
        except json.decoder.JSONDecodeError:
            data = []
        data.append(
            {
                "id": self._id,
                "description": self.description,
                "status": self.status,
                "createdAt": self.createdAt,
                "updatedAt": self.updatedAt,
            }
        )
        with open("store/tasks.json", "+w") as json_file:
            json.dump(data, json_file, indent=4)

    def save_by_id(self, id):
        try:
            with open("store/tasks.json", "+r") as json_file:
                data = json.load(json_file)
        except json.decoder.JSONDecodeError:
            data = []
        if data:
            data[id] = {
                "id": self._id,
                "description": self.description,
                "status": self.status,
                "createdAt": self.createdAt,
                "updatedAt": self.updatedAt
            }
        with open("store/tasks.json", "+w") as json_file:
            json.dump(data, json_file, indent=4)

    def save_withuot_self(self, index):
        try:
            with open("store/tasks.json", "+r") as json_file:
                data = json.load(json_file)
        except json.decoder.JSONDecodeError:
            data = []
        if data:
            try:
                data.pop(index)
            except KeyError:
                raise
        with open("store/tasks.json", "+w") as json_file:
            json.dump(data, json_file, indent=4)
