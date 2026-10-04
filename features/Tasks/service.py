from typing import List

from features.Tasks.model import Task
from features.Tasks.repository import TaskRepository


class TaskService:

    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def add_task(
        self,
        title: str,
        category: str,
        created_date: str,
        due_date: str
    ) -> Task:

        if not title or not title.strip():
            raise ValueError("Task description cannot be empty.")

        task = Task(
            id=None,
            title=title.strip(),
            category=category,
            created_date=created_date,
            due_date=due_date,
            is_completed=False,
        )

        return self.repository.add_task(task)

    def get_tasks_by_date(self, created_date: str) -> List[Task]:
        return self.repository.get_tasks_by_date(created_date)

    def get_all_tasks(self) -> List[Task]:
        return self.repository.get_all_tasks()

    def update_task(
        self,
        task_id: int,
        title: str,
        category: str,
        due_date: str
    ):
        if not title or not title.strip():
            raise ValueError("Task description cannot be empty.")

        self.repository.update_task(
            task_id,
            title.strip(),
            category,
            due_date
        )

    def complete_task(self, task_id: int):
        self.repository.complete_task(task_id)

    def delete_task(self, task_id: int):
        self.repository.delete_task(task_id)