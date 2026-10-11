from dataclasses import dataclass
from typing import Optional
from datetime import date


@dataclass
class Task:
    id: Optional[int]
    title: str
    category: str
    created_date: str
    due_date: str
    is_completed: bool = False

    @property
    def status(self) -> str:
        if self.is_completed:
            return "Completed"

        if self.due_date:
            try:
                if date.fromisoformat(self.due_date) < date.today():
                    return "Overdue"
            except ValueError:
                pass

        return "In Progress"