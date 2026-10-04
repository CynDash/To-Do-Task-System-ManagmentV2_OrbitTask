from datetime import date, timedelta

from PyQt6.QtCore import QDate, Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (
    QComboBox,
    QDateEdit,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QScrollArea,
    QStackedWidget,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget
)


class TaskDialog(QDialog):

    def __init__(self, parent=None, task=None, categories=None):
        super().__init__(parent)

        self.setWindowTitle(
            "Update Task" if task else "Add Task"
        )

        self.setMinimumWidth(420)

        self.title = QLineEdit()
        self.title.setPlaceholderText(
            "Enter task description..."
        )

        self.category = QComboBox()
        self.category.addItems(categories or [])

        self.due_date = QDateEdit()
        self.due_date.setCalendarPopup(True)
        self.due_date.setDisplayFormat("yyyy-MM-dd")
        self.due_date.setDate(QDate.currentDate())

        form = QFormLayout()
        form.setSpacing(14)

        form.addRow("Task:", self.title)
        form.addRow("Category:", self.category)
        form.addRow("Due Date:", self.due_date)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save |
            QDialogButtonBox.StandardButton.Cancel
        )

        buttons.accepted.connect(self.validate)
        buttons.rejected.connect(self.reject)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            28,
            28,
            28,
            28
        )

        layout.setSpacing(18)

        layout.addLayout(form)
        layout.addWidget(buttons)

        if task:
            self.title.setText(task.title)
            self.category.setCurrentText(task.category)

            d = QDate.fromString(
                task.due_date,
                "yyyy-MM-dd"
            )

            if d.isValid():
                self.due_date.setDate(d)

    def validate(self):
        if not self.title.text().strip():
            QMessageBox.warning(
                self,
                "Invalid Task",
                "Task description cannot be empty."
            )
            return

        self.accept()

    def data(self):
        return {
            "title": self.title.text().strip(),
            "category": self.category.currentText(),
            "due_date": self.due_date.date().toString(
                "yyyy-MM-dd"
            )
        }


class TaskView(QMainWindow):

    CATEGORIES = [
        "General",
        "School",
        "House Chores",
        "Work",
        "Personal"
    ]

    def __init__(self, service):
        super().__init__()

        self.service = service

        self.setWindowTitle(
            "OrbitTask - To-Do Task Management System"
        )

        self.setMinimumSize(900, 600)

        screen = self.screen().availableGeometry()

        width = min(
            1200,
            screen.width() - 40
        )

        height = min(
            750,
            screen.height() - 40
        )

        self.resize(width, height)

        self.move(
            screen.center() - self.rect().center()
        )

        self.build_ui()
        self.load_tasks()

    def build_ui(self):
        main = QWidget()
        self.setCentralWidget(main)

        root = QHBoxLayout(main)

        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        root.addWidget(
            self.create_sidebar()
        )

        scroll = QScrollArea()

        scroll.setWidgetResizable(True)

        scroll.setFrameShape(
            QScrollArea.Shape.NoFrame
        )

        scroll.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        scroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        scroll.setSizeAdjustPolicy(
            QScrollArea.SizeAdjustPolicy.AdjustToContents
        )

        content = QWidget()

        content.setMinimumWidth(700)

        layout = QVBoxLayout(content)

        layout.setContentsMargins(
            28,
            24,
            28,
            24
        )

        layout.setSpacing(16)

        header = QHBoxLayout()

        titles = QVBoxLayout()

        self.page_title = QLabel(
            "Dashboard"
        )

        self.page_title.setObjectName(
            "pageTitle"
        )

        subtitle = QLabel(
            "Manage your tasks and stay productive."
        )

        subtitle.setObjectName(
            "subtitle"
        )

        titles.addWidget(
            self.page_title
        )

        titles.addWidget(
            subtitle
        )

        header.addLayout(
            titles
        )

        header.addStretch()

        today = QLabel(
            date.today().strftime(
                "%A, %B %d, %Y"
            )
        )

        today.setObjectName(
            "todayLabel"
        )

        header.addWidget(
            today
        )

        layout.addLayout(header)

        layout.addWidget(
            self.create_filter_bar()
        )

        self.action_bar = (
            self.create_action_buttons()
        )

        layout.addWidget(
            self.action_bar
        )

        self.pages = QStackedWidget()

        pages = [
            self.create_dashboard(),
            self.create_task_page("In Progress"),
            self.create_task_page("Completed"),
            self.create_task_page("All Tasks")
        ]

        for page in pages:
            self.pages.addWidget(page)

        layout.addWidget(
            self.pages,
            1
        )

        scroll.setWidget(
            content
        )

        root.addWidget(
            scroll,
            1
        )

    def create_sidebar(self):
        sidebar = QWidget()

        sidebar.setObjectName(
            "sidebar"
        )

        sidebar.setMinimumWidth(170)
        sidebar.setMaximumWidth(220)

        layout = QVBoxLayout(sidebar)

        layout.setContentsMargins(
            18,
            24,
            18,
            24
        )

        logo = QLabel(
            "OrbitTask"
        )

        logo.setObjectName(
            "logo"
        )

        subtitle = QLabel(
            "TASK MANAGEMENT"
        )

        subtitle.setObjectName(
            "logoSubtitle"
        )

        layout.addWidget(logo)
        layout.addWidget(subtitle)

        layout.addSpacing(28)

        self.sidebar_buttons = []

        for text, index in [
            ("Dashboard", 0),
            ("In Progress", 1),
            ("Completed", 2),
            ("All Tasks", 3)
        ]:
            button = self.sidebar_button(
                text,
                index
            )

            self.sidebar_buttons.append(
                button
            )

            layout.addWidget(
                button
            )

        layout.addStretch()

        info = QLabel(
            "Stay organized.\n"
            "Stay productive."
        )

        info.setObjectName(
            "sidebarInfo"
        )

        layout.addWidget(info)

        self.sidebar_buttons[0].setProperty(
            "active",
            True
        )

        return sidebar

    def sidebar_button(self, text, index):
        button = QPushButton(text)

        button.setObjectName(
            "sidebarButton"
        )

        button.setFocusPolicy(
            Qt.FocusPolicy.NoFocus
        )

        button.clicked.connect(
            lambda: self.change_page(index)
        )

        return button

    def change_page(self, index):
        self.pages.setCurrentIndex(index)

        names = [
            "Dashboard",
            "In Progress",
            "Completed",
            "All Tasks"
        ]

        self.page_title.setText(
            names[index]
        )

        for button in self.sidebar_buttons:
            button.setProperty(
                "active",
                False
            )

            button.style().unpolish(button)
            button.style().polish(button)

        button = self.sidebar_buttons[index]

        button.setProperty(
            "active",
            True
        )

        button.style().unpolish(button)
        button.style().polish(button)

        self.action_bar.setVisible(
            index == 1
        )

    def create_filter_bar(self):
        widget = QWidget()

        widget.setObjectName(
            "filterBar"
        )

        layout = QHBoxLayout(widget)

        layout.setContentsMargins(
            16,
            10,
            16,
            10
        )

        layout.addWidget(
            QLabel("Date")
        )

        self.date_filter = QComboBox()

        self.date_filter.addItems([
            "Today",
            "Yesterday",
            "This Week",
            "This Month",
            "All Dates",
            "Custom Date"
        ])

        self.date_filter.setCurrentText(
            "All Dates"
        )

        self.date_filter.setMinimumWidth(120)

        layout.addWidget(
            self.date_filter
        )

        self.custom_date = QDateEdit()

        self.custom_date.setCalendarPopup(True)

        self.custom_date.setDisplayFormat(
            "MMM dd, yyyy"
        )

        self.custom_date.setDate(
            QDate.currentDate()
        )

        self.custom_date.hide()

        layout.addWidget(
            self.custom_date
        )

        layout.addWidget(
            QLabel("Category")
        )

        self.category_filter = QComboBox()

        self.category_filter.addItem(
            "All Categories"
        )

        self.category_filter.addItems(
            self.CATEGORIES
        )

        self.category_filter.setMinimumWidth(120)

        layout.addWidget(
            self.category_filter
        )

        layout.addStretch()

        self.date_filter.currentTextChanged.connect(
            self.date_filter_changed
        )

        self.custom_date.dateChanged.connect(
            self.load_tasks
        )

        self.category_filter.currentTextChanged.connect(
            self.load_tasks
        )

        return widget

    def date_filter_changed(self, value):
        self.custom_date.setVisible(
            value == "Custom Date"
        )

        self.load_tasks()

    def create_action_buttons(self):
        widget = QWidget()

        layout = QHBoxLayout(widget)

        layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        for text, name, function in [
            (
                "+ Add Task",
                "addButton",
                self.add_task
            ),
            (
                "Update",
                "updateButton",
                self.update_task
            ),
            (
                "Complete",
                "completeButton",
                self.complete_task
            ),
            (
                "Delete",
                "deleteButton",
                self.delete_task
            )
        ]:
            button = QPushButton(text)

            button.setObjectName(name)

            button.clicked.connect(function)

            layout.addWidget(button)

        layout.addStretch()

        return widget

    def create_dashboard(self):
        page = QWidget()

        layout = QVBoxLayout(page)

        layout.setSpacing(12)

        title = QLabel(
            "Overview"
        )

        title.setObjectName(
            "sectionTitle"
        )

        layout.addWidget(title)

        cards = QHBoxLayout()

        self.total = self.create_stat_card(
            "TOTAL TASKS",
            "0",
            "totalCard"
        )

        self.pending_count = self.create_stat_card(
            "IN PROGRESS",
            "0",
            "pendingCard"
        )

        self.overdue_count = self.create_stat_card(
            "OVERDUE",
            "0",
            "overdueCard"
        )

        self.completed_count = self.create_stat_card(
            "COMPLETED",
            "0",
            "completedCard"
        )

        for card in (
            self.total,
            self.pending_count,
            self.overdue_count,
            self.completed_count
        ):
            cards.addWidget(
                card,
                1
            )

        layout.addLayout(cards)

        title = QLabel(
            "Completion Progress"
        )

        title.setObjectName(
            "sectionTitle"
        )

        layout.addWidget(title)

        progress_box = QWidget()

        progress_box.setObjectName(
            "progressBox"
        )

        progress_layout = QVBoxLayout(
            progress_box
        )

        self.progress = QProgressBar()

        self.progress.setRange(
            0,
            100
        )

        self.progress.setFormat(
            "%p%"
        )

        progress_layout.addWidget(
            self.progress
        )

        layout.addWidget(
            progress_box
        )

        title = QLabel(
            "Pending Tasks"
        )

        title.setObjectName(
            "sectionTitle"
        )

        layout.addWidget(title)

        self.dashboard_pending = (
            self.create_dashboard_table()
        )

        layout.addWidget(
            self.dashboard_pending
        )

        title = QLabel(
            "Completed Tasks"
        )

        title.setObjectName(
            "sectionTitle"
        )

        layout.addWidget(title)

        self.dashboard_completed = (
            self.create_dashboard_table()
        )

        layout.addWidget(
            self.dashboard_completed
        )

        return page

    def create_stat_card(
        self,
        title,
        value,
        name
    ):
        card = QLabel(
            f"{title}\n\n{value}"
        )

        card.setObjectName(name)

        card.setMinimumHeight(105)

        return card

    def create_dashboard_table(self):
        table = QTableWidget(0, 5)

        table.setHorizontalHeaderLabels([
            "Task",
            "Category",
            "Created Date",
            "Due Date",
            "Status"
        ])

        table.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )

        table.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )

        table.setFocusPolicy(
            Qt.FocusPolicy.NoFocus
        )

        table.verticalHeader().hide()

        table.setAlternatingRowColors(True)
        table.setShowGrid(False)

        table.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        table.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        header = table.horizontalHeader()

        for column in range(5):
            header.setSectionResizeMode(
                column,
                QHeaderView.ResizeMode.Stretch
            )

        header.setFixedHeight(38)

        table.verticalHeader().setDefaultSectionSize(32)

        table.setMinimumHeight(120)
        table.setMaximumHeight(220)

        return table

    def create_task_page(self, name):
        page = QWidget()

        layout = QVBoxLayout(page)

        title = QLabel(name)

        title.setObjectName(
            "sectionTitle"
        )

        layout.addWidget(title)

        table = self.create_table()

        layout.addWidget(
            table,
            1
        )

        if name == "In Progress":
            self.pending = table

        elif name == "Completed":
            self.completed = table

        else:
            self.all_tasks = table

        return page

    def create_table(self):
        table = QTableWidget(0, 6)

        table.setHorizontalHeaderLabels([
            "ID",
            "Task",
            "Category",
            "Created Date",
            "Due Date",
            "Status"
        ])

        table.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )

        table.setSelectionMode(
            QTableWidget.SelectionMode.SingleSelection
        )

        table.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )

        table.setFocusPolicy(
            Qt.FocusPolicy.NoFocus
        )

        table.verticalHeader().hide()

        table.setAlternatingRowColors(True)
        table.setShowGrid(False)

        header = table.horizontalHeader()

        header.setSectionResizeMode(
            0,
            QHeaderView.ResizeMode.ResizeToContents
        )

        header.setSectionResizeMode(
            1,
            QHeaderView.ResizeMode.Stretch
        )

        for column in range(2, 6):
            header.setSectionResizeMode(
                column,
                QHeaderView.ResizeMode.ResizeToContents
            )

        return table

    def get_filtered_tasks(self):
        tasks = self.service.get_all_tasks()

        today = date.today()

        option = self.date_filter.currentText()

        if option == "Today":
            tasks = [
                t for t in tasks
                if t.created_date == today.isoformat()
            ]

        elif option == "Yesterday":
            d = today - timedelta(days=1)

            tasks = [
                t for t in tasks
                if t.created_date == d.isoformat()
            ]

        elif option == "This Week":
            start = today - timedelta(
                days=today.weekday()
            )

            end = start + timedelta(days=6)

            filtered = []

            for t in tasks:
                try:
                    created = date.fromisoformat(
                        t.created_date
                    )

                    if start <= created <= end:
                        filtered.append(t)

                except ValueError:
                    pass

            tasks = filtered

        elif option == "This Month":
            filtered = []

            for t in tasks:
                try:
                    created = date.fromisoformat(
                        t.created_date
                    )

                    if (
                        created.year == today.year
                        and created.month == today.month
                    ):
                        filtered.append(t)

                except ValueError:
                    pass

            tasks = filtered

        elif option == "Custom Date":
            selected = (
                self.custom_date
                .date()
                .toString("yyyy-MM-dd")
            )

            tasks = [
                t for t in tasks
                if t.created_date == selected
            ]

        category = (
            self.category_filter.currentText()
        )

        if category != "All Categories":
            tasks = [
                t for t in tasks
                if t.category == category
            ]

        return tasks

    def fill_table(
        self,
        table,
        tasks
    ):
        table.setRowCount(0)

        for task in tasks:
            row = table.rowCount()

            table.insertRow(row)

            values = [
                task.id,
                task.title,
                task.category,
                task.created_date,
                task.due_date,
                task.status
            ]

            for col, value in enumerate(values):
                item = QTableWidgetItem(
                    str(value)
                )

                if col == 0:
                    item.setData(
                        Qt.ItemDataRole.UserRole,
                        task.id
                    )

                if col == 5:
                    if task.status == "Overdue":
                        item.setForeground(
                            QColor("#ef4444")
                        )

                    elif task.status == "Completed":
                        item.setForeground(
                            QColor("#10b981")
                        )

                table.setItem(
                    row,
                    col,
                    item
                )

    def fill_dashboard_table(
        self,
        table,
        tasks
    ):
        table.setRowCount(0)

        for task in tasks:
            row = table.rowCount()

            table.insertRow(row)

            values = [
                task.title,
                task.category,
                task.created_date,
                task.due_date,
                task.status
            ]

            for col, value in enumerate(values):
                item = QTableWidgetItem(
                    str(value)
                )

                if col == 4:
                    if task.status == "Overdue":
                        item.setForeground(
                            QColor("#ef4444")
                        )

                    elif task.status == "Completed":
                        item.setForeground(
                            QColor("#10b981")
                        )

                table.setItem(
                    row,
                    col,
                    item
                )

            table.setRowHeight(
                row,
                32
            )

    def load_tasks(self):
        tasks = self.get_filtered_tasks()

        pending = [
            t for t in tasks
            if not t.is_completed
        ]

        completed = [
            t for t in tasks
            if t.is_completed
        ]

        self.fill_table(
            self.pending,
            pending
        )

        self.fill_table(
            self.completed,
            completed
        )

        self.fill_table(
            self.all_tasks,
            tasks
        )

        all_tasks = self.service.get_all_tasks()

        pending_all = [
            t for t in all_tasks
            if not t.is_completed
        ]

        completed_all = [
            t for t in all_tasks
            if t.is_completed
        ]

        overdue = [
            t for t in all_tasks
            if not t.is_completed
            and t.status == "Overdue"
        ]

        self.fill_dashboard_table(
            self.dashboard_pending,
            pending_all
        )

        self.fill_dashboard_table(
            self.dashboard_completed,
            completed_all
        )

        total = len(tasks)

        done = len(completed)

        self.total.setText(
            f"TOTAL TASKS\n\n{total}"
        )

        self.pending_count.setText(
            f"IN PROGRESS\n\n{len(pending)}"
        )

        self.overdue_count.setText(
            f"OVERDUE\n\n{len(overdue)}"
        )

        self.completed_count.setText(
            f"COMPLETED\n\n{done}"
        )

        self.progress.setValue(
            int(done / total * 100)
            if total
            else 0
        )

    def selected_task_id(self):
        if self.pages.currentIndex() != 1:
            return None

        table = self.pending

        if table.currentRow() < 0:
            return None

        item = table.item(
            table.currentRow(),
            0
        )

        return (
            item.data(
                Qt.ItemDataRole.UserRole
            )
            if item
            else None
        )

    def get_task(self, task_id):
        return next(
            (
                task
                for task
                in self.service.get_all_tasks()
                if task.id == task_id
            ),
            None
        )

    def add_task(self):
        dialog = TaskDialog(
            self,
            categories=self.CATEGORIES
        )

        if (
            dialog.exec()
            != QDialog.DialogCode.Accepted
        ):
            return

        data = dialog.data()

        self.service.add_task(
            data["title"],
            data["category"],
            date.today().isoformat(),
            data["due_date"]
        )

        self.load_tasks()

    def update_task(self):
        task_id = self.selected_task_id()

        if task_id is None:
            QMessageBox.information(
                self,
                "Select Task",
                "Please select a task first."
            )
            return

        task = self.get_task(task_id)

        if not task:
            return

        dialog = TaskDialog(
            self,
            task,
            self.CATEGORIES
        )

        if (
            dialog.exec()
            != QDialog.DialogCode.Accepted
        ):
            return

        data = dialog.data()

        self.service.update_task(
            task_id,
            data["title"],
            data["category"],
            data["due_date"]
        )

        self.load_tasks()

    def complete_task(self):
        task_id = self.selected_task_id()

        if task_id is None:
            QMessageBox.information(
                self,
                "Select Task",
                "Please select a task first."
            )
            return

        task = self.get_task(task_id)

        if task and not task.is_completed:
            self.service.complete_task(
                task_id
            )

            self.load_tasks()

    def delete_task(self):
        task_id = self.selected_task_id()

        if task_id is None:
            QMessageBox.information(
                self,
                "Select Task",
                "Please select a task first."
            )
            return

        task = self.get_task(task_id)

        if not task:
            return

        answer = QMessageBox.question(
            self,
            "Delete Task",
            f"Delete '{task.title}'?",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )

        if (
            answer ==
            QMessageBox.StandardButton.Yes
        ):
            self.service.delete_task(
                task_id
            )

            self.load_tasks()