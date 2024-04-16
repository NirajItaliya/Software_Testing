from events.Events import *
import random
import time

class QUIC:
    def __init__(self):
        self.password = "t"
        self.singup = False
        self.login = False
        self.task = False
        self.runtsak = False
        self.tasks = []  # List to store tasks
        self.task_history = []  # List to store task history

    def reset(self, reset_run=True):
        if reset_run:
            self.singup = False
            self.login = False
            self.task = False
            self.runtsak = False

    def Login(self):
        if self.singup:
            self.login = True
            return b"Dashboard"
        else:
            self.login = False
            return b"Error"

    def Loginfailed(self):
        self.login = False
        return b"Login"

    def SignUp(self, only_reset):
        self.reset(only_reset)
        self.singup = True
        return b"Dashboard"

    def add_task(self, task_name, priority=0, notes="", attachments=[]):
        if self.singup or self.login:
            task = {"name": task_name, "priority": priority, "notes": notes, "attachments": attachments}
            self.tasks.append(task)
            self.task = True
            return b"Task added successfully"
        else:
            return b"Error: Please sign up or login first"

    def remove_task(self, task_index):
        if self.login and self.task:
            if 0 <= task_index < len(self.tasks):
                removed_task = self.tasks.pop(task_index)
                self.task_history.append({"action": "remove_task", "task": removed_task})
                return b"Task removed successfully"
            else:
                return b"Error: Invalid task index"
        else:
            return b"Error: Please sign up or login first"

    def run_task(self):
        if self.login and self.task:
            self.runtsak = True
            return b"Task started"
        else:
            return b"Error: Please sign up or login first and add a task"

    def stop_task(self):
        if self.login and self.runtsak:
            self.runtsak = False
            return b"Task stopped"
        else:
            return b"Error: Please login first and start a task"

    def send(self, command):
        try:
            if isinstance(command, SendLoginEvent):
                print("Send Login")
                return self.Login()
            elif isinstance(command, SendSignUpEvent):
                print("send Signup")
                return self.SignUp(True)
            elif isinstance(command, Loginfailed):
                print("send Loginfailed")
                return self.Loginfailed()
            elif isinstance(command, AddTask):
                print("send addtask")
                return self.add_task(command.task_name, command.priority, command.notes, command.attachments)
            elif isinstance(command, RemoveTask):
                print("send removetask")
                return self.remove_task(command.task_index)
            elif isinstance(command, RunTask):
                print("send RunTask")
                return self.run_task()
            elif isinstance(command, StopTask):
                print("send StopTask")
                return self.stop_task()
        except Exception as err:
            print("Error:", err)

    def filter_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task["priority"] == priority]

    def sort_tasks_by_priority(self):
        return sorted(self.tasks, key=lambda x: x["priority"], reverse=True)

    def track_task_history(self):
        return self.task_history

    def set_task_reminder(self, task_index, reminder_time):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            # Code to set reminder using reminder_time
            return b"Reminder set successfully"
        else:
            return b"Error: Invalid task index"

    def get_task_notifications(self):
        # Code to generate task notifications based on task deadlines or other criteria
        notifications = b"Task notifications"
        return notifications
