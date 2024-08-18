import json
import sys
import os

from src.tracer import Tracker


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
    print("\tlist done - to print all tasks with status done")
    print("\tlist todo - to print all tasks with status todo")
    print("\tlist in-progress - to print all tasks with status in-progress")
    print("\thelp - to print this help manual")


def main():
    if not os.path.isdir("store"):
        os.mkdir("store")

    if not os.path.isfile("store/tasks.json"):
        with open("store/tasks.json", "w") as file:
            json.dump([], file)
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
                if arhv_len > 2:
                    index = int(sys.argv[2])
                    task_manager.delete_task(index)
                else:
                    print("[-] excepted description as third argument")

            case "mark-in-progress":
                if arhv_len > 2:
                    index = int(sys.argv[2])
                    task_manager.replace_status(index, Tracker.Options.int_progress)
                else:
                    print("[-] excepted index")

            case "mark-done":
                if arhv_len > 2:
                    index = int(sys.argv[2])
                    task_manager.replace_status(index, Tracker.Options.done)
                else:
                    print("[-] excepted index")

            case "list":
                if arhv_len > 2:
                    option = sys.argv[2]
                    if option in ["done", "todo", "in-progress"]:
                        task_manager.print_list(option=option)
                    else:
                        print(
                            f"[-] Unexpected key: {option}. Expected: done, todo, in-progress"
                        )
                else:
                    task_manager.print_list()
            case "help":
                show_avalible_flags()
            case _:
                print("The flag was expected to be entered")
                show_avalible_flags()


if __name__ == "__main__":
    main()
