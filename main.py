import sys
from pathlib import Path

from PyQt6.QtWidgets import QApplication

from database.database import init_db
from features.Tasks.repository import TaskRepository
from features.Tasks.service import TaskService
from features.Tasks.view import TaskView


def main():
    init_db()

    app = QApplication(sys.argv)

    stylesheet_path = Path(__file__).resolve().with_name("Style.qss")
    if stylesheet_path.exists():
        app.setStyleSheet(stylesheet_path.read_text(encoding="utf-8"))

    repository = TaskRepository()
    service = TaskService(repository)
    window = TaskView(service)
    window.show()

    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
