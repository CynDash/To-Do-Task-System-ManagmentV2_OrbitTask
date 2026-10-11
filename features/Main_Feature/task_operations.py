"""Centralized task management operations for OrbitTask.

Add, update, complete, and delete behavior is kept in this module
rather than implemented inside the GUI view.
"""

from PyQt6.QtWidgets import QDialog, QMessageBox


class TaskOperations:
    """Handles task actions initiated by the TaskView interface."""

    def __init__(self, view, dialog_class):
        self.view = view
        self.service = view.service
        self.dialog_class = dialog_class

    def _categories(self):
        defaults = self.view.CATEGORIES
        saved = self.service.get_categories()
        return sorted(set(defaults + saved), key=str.casefold)

    def add_task(self):
        dialog = self.dialog_class(self.view, categories=self._categories())
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return

        data = dialog.data()
        try:
            self.service.add_task(
                data["title"], data["category"],
                data["created_date"], data["due_date"]
            )
        except ValueError as error:
            QMessageBox.warning(self.view, "Invalid Task", str(error))
            return
        self.view.load_tasks()

    def update_task(self):
        task_id = self.view.selected_task_id()
        if task_id is None:
            self.view.show_select_message()
            return

        task = self.view.get_task(task_id)
        if task is None:
            return

        dialog = self.dialog_class(
            self.view, task, self._categories()
        )
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return

        data = dialog.data()
        try:
            self.service.update_task(
                task_id, data["title"], data["category"],
                data["created_date"], data["due_date"]
            )
        except ValueError as error:
            QMessageBox.warning(self.view, "Invalid Task", str(error))
            return
        self.view.load_tasks()

    def complete_task(self):
        task_id = self.view.selected_task_id()
        if task_id is None:
            self.view.show_select_message()
            return

        task = self.view.get_task(task_id)
        if task and not task.is_completed:
            self.service.complete_task(task_id)
            self.view.load_tasks()

    def delete_task(self):
        task_id = self.view.selected_task_id()
        if task_id is None:
            self.view.show_select_message()
            return

        task = self.view.get_task(task_id)
        if task is None:
            return

        answer = QMessageBox.question(
            self.view, "Delete Task", f"Delete '{task.title}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if answer == QMessageBox.StandardButton.Yes:
            self.service.delete_task(task_id)
            self.view.load_tasks()
