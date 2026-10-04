import sys

from PyQt6.QtWidgets import QApplication

from database.database import init_db
from features.Tasks.repository import TaskRepository
from features.Tasks.service import TaskService
from features.Tasks.view import TaskView


def main():
    init_db()

    app = QApplication(sys.argv)

    with open("Style.qss", "r", encoding="utf-8") as file:
        app.setStyleSheet(file.read())

    repository = TaskRepository()
    service = TaskService(repository)

    window = TaskView(service)
    window.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())