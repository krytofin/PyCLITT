import datetime
import json
import sys


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
            self._description = description
            self._status = status
            self._createdAt = datetime.datetime.now().isoformat()
            self._updatedAt = datetime.datetime.now().isoformat()
            self.__increment_id()
        else:
            self._load(task)

    def _load(self, json_data) -> None:
        self._id: int = json_data["id"]
        self._description: int = json_data["description"]
        self._status: int = json_data["status"]
        self._createdAt: int = json_data["createdAt"]
        self._updatedAt: int = json_data["updatedAt"]

        self.__class__.task_id = self._id
        self.__increment_id()

    def save(self):
        try:
            with open("store/tasks.json", '+r') as json_file:
                data = json.load(json_file)
        except json.decoder.JSONDecodeError:
            data = []
        data.append(
            {
                "id": self._id,
                "description": self._description,
                "status": self._status,
                "createdAt": self._createdAt,
                "updatedAt": self._updatedAt,
            }
        )
        with open("store/tasks.json", '+w') as json_file: 
            json.dump(data, json_file, indent=4)

    def delete(self): ...

    def update(self): ...

    def get(self): ...


class Tracker:
    def __init__(self) -> None:
        self._tasks = {}
        with open("store/tasks.json") as json_file:
            json_file = json.load(json_file)
        for task in json_file:
            self._tasks[task["id"]] = Task(task=task)

        print(self._tasks)


def show_avalible_flags() -> None:
    print("Possible flags:\n")
    print("\tadd <str:description> - add new task to your tasks")
    print(
        "\tupdate <int:id> <str:description> - update task by id. Replace old to new description"
    )
    print("\tdelete <int:id> - delete task by id")
    print("\tmark-in-progress <int:id> - replace old status on mark-in-progress")
    print("\tmark-done <int:id> - replace old status on mark-done")
    print("\tlist - to print all tasks")
    print("\tlist <str:done> - to print all tasks with status done")
    print("\tlist <str:todo> - to print all tasks with status todo")
    print("\tlist <str:in-progress> - to print all tasks with status in-progress")
    print("\t-h - to print this help manual")


if __name__ == "__main__":
    task_manager = Tracker()
    for _ in range(10):
        task = Task(new=True, description='Test task')
        task.save()
    
    arhv_len = len(sys.argv)
    if arhv_len < 2:
        print("The flag was expected to be entered")
        show_avalible_flags()
    else:
        command = sys.argv[1]

        match command:
            case "add":
                if arhv_len > 2:
                    description = " ".join(sys.argv[2:])
                    print(description)
                else:
                    print("[-] excepted description as third argument")

            case "update":
                print("update task")
            case "delete":
                print("delete task")
            case "mark-in-progress":
                print("replace to mark-in-progress")
            case "mark-done":
                print("mark-done")
            case "list":
                if arhv_len > 2:
                    ...
                else:
                    print("list")
            case "-h":
                show_avalible_flags()
            case _:
                print("The flag was expected to be entered")
                show_avalible_flags()
