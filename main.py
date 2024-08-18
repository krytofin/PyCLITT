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
                "updatedAt": self.updatedAt,
            }
        with open("store/tasks.json", "+w") as json_file:
            json.dump(data, json_file, indent=4)


class Tracker:

    class Options:
        all = "all"
        done = "done"
        todo = "todo"
        int_progress = "in-progress"

    def __init__(self) -> None:
        self._tasks = {}
        try:
            with open("store/tasks.json") as json_file:
                json_file = json.load(json_file)
            for task in json_file:
                self._tasks[task["id"]] = Task(task=task)
        except json.decoder.JSONDecodeError:
            # tasks list is empty
            pass

    def add(self, description) -> None:
        new_task = Task(new=True, description=description)
        task_id = new_task.id
        self._tasks[task_id] = new_task
        new_task.save()
        print(f"[+] Task added successfully {new_task}")

    def update(self, index, description) -> None:
        index = int(index)
        try:
            self._tasks[index].description = description
            self._tasks[index].updatedAt = f"{datetime.datetime.now():%d-%m-%Y %H:%M:%S}"
            self._tasks[index].save_by_id(index)
            print(f"[+] Task updated successfully {self._tasks[index]}")
        except KeyError:
            print(f'[-] Error. Task {index} does not existent')
        
    def print_list(self, option=Options.all):
        if option == self.Options.all:
            if self._tasks:
                print("\nYour tasks:\n")
                for index, task in self._tasks.items():
                    print("=" * 50)
                    print(f"task id: {task.id}")
                    print(f"{task.description}")
                    print(f"Status: {task.status}")
                    print(f"task created: {task.createdAt}")
                    print(f"task updated: {task.updatedAt}")
                print("=" * 50)
            else:
                print("[+] your tasks list is empty")


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
    print("\thelp - to print this help manual")


if __name__ == "__main__":
    task_manager = Tracker()

    # ==============================
    # Flags
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
                    task_manager.add(description)
                else:
                    print("[-] excepted description as third argument")

            case "update":
                if arhv_len > 3:
                    index = sys.argv[2]
                    description = " ".join(sys.argv[3:])
                    task_manager.update(index, description)
                else:
                    print("[-] excepted index and description as arguments")

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
                    task_manager.print_list()
            case "help":
                show_avalible_flags()
            case _:
                print("The flag was expected to be entered")
                show_avalible_flags()
