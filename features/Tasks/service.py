from datetime import date
from typing import List

from features.Tasks.model import Task
from features.Tasks.repository import TaskRepository


class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    @staticmethod
    def _validate_task(title: str, category: str, created_date: str, due_date: str):
        if not title or not title.strip():
            raise ValueError("Task description cannot be empty.")

        category = (category or "").strip() or "General"

        try:
            created = date.fromisoformat(created_date)
            due = date.fromisoformat(due_date)
        except (TypeError, ValueError):
            raise ValueError("Please enter valid created and due dates in YYYY-MM-DD format.")

        if due < created:
            raise ValueError("Due date cannot be earlier than the created date.")

        return title.strip(), category, created.isoformat(), due.isoformat()

    def add_task(
        self, title: str, category: str, created_date: str, due_date: str
    ) -> Task:
        title, category, created_date, due_date = self._validate_task(
            title, category, created_date, due_date
        )
        task = Task(
            id=None,
            title=title,
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

    def get_categories(self) -> List[str]:
        return self.repository.get_categories()

    def update_task(
        self,
        task_id: int,
        title: str,
        category: str,
        created_date: str,
        due_date: str,
    ):
        title, category, created_date, due_date = self._validate_task(
            title, category, created_date, due_date
        )
        self.repository.update_task(
            task_id, title, category, created_date, due_date
        )

    def complete_task(self, task_id: int):
        self.repository.complete_task(task_id)

    def delete_task(self, task_id: int):
        self.repository.delete_task(task_id)
