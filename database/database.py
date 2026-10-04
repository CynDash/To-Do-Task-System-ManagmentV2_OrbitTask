from pathlib import Path
import sqlite3


BASE_DIR = Path(__file__).resolve().parent.parent
DB_NAME = BASE_DIR / "tasks.db"


def get_connection():
    connection = sqlite3.connect(DB_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                category TEXT NOT NULL DEFAULT 'General',
                created_date TEXT NOT NULL,
                due_date TEXT NOT NULL,
                is_completed INTEGER NOT NULL DEFAULT 0
            )
        """)

        cursor.execute("PRAGMA table_info(tasks)")
        columns = [row["name"] for row in cursor.fetchall()]

        if "category" not in columns:
            cursor.execute(
                "ALTER TABLE tasks ADD COLUMN category TEXT NOT NULL DEFAULT 'General'"
            )

        if "created_date" not in columns:
            cursor.execute(
                "ALTER TABLE tasks ADD COLUMN created_date TEXT NOT NULL DEFAULT ''"
            )

        if "due_date" not in columns:
            cursor.execute(
                "ALTER TABLE tasks ADD COLUMN due_date TEXT NOT NULL DEFAULT ''"
            )

        if "is_completed" not in columns:
            cursor.execute(
                "ALTER TABLE tasks ADD COLUMN is_completed INTEGER NOT NULL DEFAULT 0"
            )

        cursor.execute("""
            UPDATE tasks
            SET category = 'General'
            WHERE category IS NULL OR category = ''
        """)

        cursor.execute("""
            UPDATE tasks
            SET is_completed = 0
            WHERE is_completed IS NULL
        """)

        connection.commit()