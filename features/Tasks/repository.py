from typing import List

from database.database import get_connection
from features.Tasks.model import Task


class TaskRepository:

    def add_task(self, task: Task) -> Task:
        with get_connection() as connection:
            cursor = connection.cursor()

            cursor.execute(
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
                    1 if task.is_completed else 0,
                ),
            )

            connection.commit()
            task.id = cursor.lastrowid

        return task

    def get_tasks_by_date(self, created_date: str) -> List[Task]:
        with get_connection() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT
                    id,
                    title,
                    category,
                    created_date,
                    due_date,
                    is_completed
                FROM tasks
                WHERE created_date = ?
                ORDER BY id DESC
                """,
                (created_date,),
            )

            rows = cursor.fetchall()

        return [
            Task(
                id=row["id"],
                title=row["title"],
                category=row["category"],
                created_date=row["created_date"],
                due_date=row["due_date"],
                is_completed=bool(row["is_completed"]),
            )
            for row in rows
        ]

    def get_all_tasks(self) -> List[Task]:
        with get_connection() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT
                    id,
                    title,
                    category,
                    created_date,
                    due_date,
                    is_completed
                FROM tasks
                ORDER BY id DESC
                """
            )

            rows = cursor.fetchall()

        return [
            Task(
                id=row["id"],
                title=row["title"],
                category=row["category"],
                created_date=row["created_date"],
                due_date=row["due_date"],
                is_completed=bool(row["is_completed"]),
            )
            for row in rows
        ]

    def update_task(
        self,
        task_id: int,
        title: str,
        category: str,
        due_date: str
    ):
        with get_connection() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                UPDATE tasks
                SET title = ?,
                    category = ?,
                    due_date = ?
                WHERE id = ?
                """,
                (
                    title,
                    category,
                    due_date,
                    task_id,
                ),
            )

            connection.commit()

    def complete_task(self, task_id: int):
        with get_connection() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                UPDATE tasks
                SET is_completed = 1
                WHERE id = ?
                """,
                (task_id,),
            )

            connection.commit()

    def delete_task(self, task_id: int):
        with get_connection() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                DELETE FROM tasks
                WHERE id = ?
                """,
                (task_id,),
            )

            connection.commit()