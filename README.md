# PyCLITT


PyCLITT(Python CLI Task Tracker) is task list management from the command line. This program allows you to manage the task list directly from the terminal.

[project url](https://github.com/krytofin/PyCLITT)


## Install

That you need:

* Python 3
* git

```
git clone https://github.com/krytofin/PyCLITT.git
cd PyCLITT
python main.py help
```

## Avalible arguments

---



* `add [str:description](str:description) - add new task to your tasks`
* `update [int:id](int:id) [str:description](str:description) - update task by id. Replace old to new description`
* `delete [int:id](int:id) - delete task by id`
* `mark-in-progress [int:id](int:id) - replace old status on mark-in-progress`
* `mark-done [int:id](int:id) - replace old status on mark-done`
* `list - to print all tasks`
* `list done - to print all tasks with status done`
* `list todo - to print all tasks with status todo`
* `list in-progress - to print all tasks with status in-progress`
* `help - to print this help manual`

---
