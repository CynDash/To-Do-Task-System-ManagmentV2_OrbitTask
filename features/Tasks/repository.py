from typing import List

from database.database import get_connection
from features.Tasks.model import Task


class TaskRepository:
    @staticmethod
    def _row_to_task(row) -> Task:
        return Task(
            id=row["id"],
            title=row["title"],
            category=row["category"],
            created_date=row["created_date"],
            due_date=row["due_date"],
            is_completed=bool(row["is_completed"]),
        )

    def add_task(self, task: Task) -> Task:
        with get_connection() as connection:
            cursor = connection.execute(
                """
                INSERT INTO tasks
                    (title, category, created_date, due_date, is_completed)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    task.title,
                    task.category,
                    task.created_date,
                    task.due_date,
                    int(task.is_completed),
                ),
            )
            task.id = cursor.lastrowid
        return task

    def get_tasks_by_date(self, created_date: str) -> List[Task]:
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT * FROM tasks WHERE created_date = ? ORDER BY id DESC",
                (created_date,),
            ).fetchall()
        return [self._row_to_task(row) for row in rows]

    def get_all_tasks(self) -> List[Task]:
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT * FROM tasks ORDER BY id DESC"
            ).fetchall()
        return [self._row_to_task(row) for row in rows]

    def get_categories(self) -> List[str]:
        with get_connection() as connection:
            rows = connection.execute(
                """
                SELECT DISTINCT category
                FROM tasks
                WHERE category IS NOT NULL AND TRIM(category) <> ''
                ORDER BY category COLLATE NOCASE
                """
            ).fetchall()
        return [row["category"] for row in rows]

    def update_task(
        self,
        task_id: int,
        title: str,
        category: str,
        created_date: str,
        due_date: str,
    ):
        with get_connection() as connection:
            connection.execute(
                """
                UPDATE tasks
                SET title = ?, category = ?, created_date = ?, due_date = ?
                WHERE id = ?
                """,
                (title, category, created_date, due_date, task_id),
            )

    def complete_task(self, task_id: int):
        with get_connection() as connection:
            connection.execute(
                "UPDATE tasks SET is_completed = 1 WHERE id = ?",
                (task_id,),
            )

    def delete_task(self, task_id: int):
        with get_connection() as connection:
            connection.execute(
                "DELETE FROM tasks WHERE id = ?",
                (task_id,),
            )
