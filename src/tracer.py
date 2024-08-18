import datetime
import json

from src.task import Task


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
            self._tasks[index].updatedAt = (
                f"{datetime.datetime.now():%d-%m-%Y %H:%M:%S}"
            )
            self._tasks[index].save_by_id(index)
            print(f"[+] Task updated successfully {self._tasks[index]}")
        except KeyError:
            print(f"[-] Error. Task {index} does not existent")

    def delete_task(self, index):
        index = int(index)
        try:
            self._tasks[index].save_withuot_self(index)
            print(f"[+] Task delete successfully {self._tasks[index]}")
        except KeyError:
            print(f"[-] Error. Task {index} does not existent")

    def print_list(self, option=Options.all):
        if not self._tasks:
            print("[+] your tasks list is empty")
        elif option == self.Options.all:
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
            print(f"\nYour {option} tasks:\n")
            for index, task in self._tasks.items():
                is_printd = False
                if task.status == option:
                    print("=" * 50)
                    print(f"task id: {task.id}")
                    print(f"task: {task.description}")
                    print(f"status: {task.status}")
                    print(f"task created: {task.createdAt}")
                    print(f"task updated: {task.updatedAt}")
                    is_printd = True
                if is_printd:
                    print("=" * 50)

    def replace_status(self, index, status):
        try:
            self._tasks[index].status = status
            self._tasks[index].save_by_id(index)
            print(f"[+] status was successfully replaced by {status}")
        except KeyError:
            print(f"[-] Error. Task {index} does not existent")
