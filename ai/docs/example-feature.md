# Feature: Task Management System

## Overview
This document provides implementation details for a **Task Management System** feature, built using Python 3.14, following TDD principles, and adhering to project best practices. It serves as a reference for both developers and AI assistants.

## Related Documentation
- **Requirements**: See @file(ai/prd.md) for feature requirements
- **Implementation Plan**: See @file(ai/plan.md) for development phases

## Implementation Details

### Data Models
The feature uses the following data models (defined in `src/models/task.py`):

```python
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional


class TaskStatus(Enum):
    """Task status enumeration."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class TaskPriority(Enum):
    """Task priority enumeration."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


@dataclass(frozen=True)
class Task:
    """Task model representing a single task.

    Attributes:
        id: Unique identifier for the task.
        title: Task title.
        description: Detailed task description.
        status: Current task status.
        priority: Task priority level.
        created_at: Task creation timestamp.
        updated_at: Last update timestamp.
        due_date: Optional due date for the task.
    """
    id: str
    title: str
    description: str
    status: TaskStatus
    priority: TaskPriority
    created_at: datetime
    updated_at: datetime
    due_date: Optional[datetime] = None

    def is_overdue(self) -> bool:
        """Check if task is overdue."""
        if self.due_date is None:
            return False
        return datetime.now() > self.due_date and self.status != TaskStatus.COMPLETED
```

### Repository Layer
Data access is handled through a repository pattern (located in `src/repositories/task_repository.py`):

```python
from abc import ABC, abstractmethod
from typing import List, Optional

from src.models.task import Task, TaskStatus


class TaskRepository(ABC):
    """Abstract base class for task data persistence."""

    @abstractmethod
    async def save(self, task: Task) -> Task:
        """Save a task to the data store."""
        pass

    @abstractmethod
    async def find_by_id(self, task_id: str) -> Optional[Task]:
        """Find a task by its ID."""
        pass

    @abstractmethod
    async def find_all(self, status: Optional[TaskStatus] = None) -> List[Task]:
        """Find all tasks, optionally filtered by status."""
        pass

    @abstractmethod
    async def delete(self, task_id: str) -> bool:
        """Delete a task by its ID."""
        pass


class InMemoryTaskRepository(TaskRepository):
    """In-memory implementation of TaskRepository for development/testing."""

    def __init__(self) -> None:
        """Initialize the repository with empty storage."""
        self._tasks: dict[str, Task] = {}

    async def save(self, task: Task) -> Task:
        """Save a task to memory."""
        self._tasks[task.id] = task
        return task

    async def find_by_id(self, task_id: str) -> Optional[Task]:
        """Find a task by ID in memory."""
        return self._tasks.get(task_id)

    async def find_all(self, status: Optional[TaskStatus] = None) -> List[Task]:
        """Find all tasks in memory, optionally filtered by status."""
        tasks = list(self._tasks.values())
        if status:
            tasks = [t for t in tasks if t.status == status]
        return tasks

    async def delete(self, task_id: str) -> bool:
        """Delete a task from memory."""
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False
```

### Service Layer
Business logic is implemented in the service layer (located in `src/services/task_service.py`):

```python
from datetime import datetime
from typing import List, Optional
from uuid import uuid4

from src.exceptions import TaskNotFoundError, ValidationError
from src.models.task import Task, TaskPriority, TaskStatus
from src.repositories.task_repository import TaskRepository


class TaskService:
    """Service for managing task operations."""

    def __init__(self, repository: TaskRepository) -> None:
        """Initialize the service with a repository.

        Args:
            repository: Task repository for data persistence.
        """
        self._repository = repository

    async def create_task(
        self,
        title: str,
        description: str,
        priority: TaskPriority = TaskPriority.MEDIUM,
        due_date: Optional[datetime] = None,
    ) -> Task:
        """Create a new task.

        Args:
            title: Task title.
            description: Task description.
            priority: Task priority level.
            due_date: Optional due date.

        Returns:
            The created task.

        Raises:
            ValidationError: If title or description is empty.
        """
        if not title.strip():
            raise ValidationError("Task title cannot be empty")
        if not description.strip():
            raise ValidationError("Task description cannot be empty")

        now = datetime.now()
        task = Task(
            id=str(uuid4()),
            title=title,
            description=description,
            status=TaskStatus.PENDING,
            priority=priority,
            created_at=now,
            updated_at=now,
            due_date=due_date,
        )

        return await self._repository.save(task)

    async def get_task(self, task_id: str) -> Task:
        """Get a task by ID.

        Args:
            task_id: The task ID.

        Returns:
            The requested task.

        Raises:
            TaskNotFoundError: If task doesn't exist.
        """
        task = await self._repository.find_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(f"Task with ID {task_id} not found")
        return task

    async def list_tasks(
        self, status: Optional[TaskStatus] = None
    ) -> List[Task]:
        """List all tasks, optionally filtered by status.

        Args:
            status: Optional status filter.

        Returns:
            List of tasks.
        """
        return await self._repository.find_all(status)

    async def update_task_status(
        self, task_id: str, new_status: TaskStatus
    ) -> Task:
        """Update a task's status.

        Args:
            task_id: The task ID.
            new_status: The new status.

        Returns:
            The updated task.

        Raises:
            TaskNotFoundError: If task doesn't exist.
        """
        task = await self.get_task(task_id)
        # Since Task is frozen, create a new instance with updated values
        updated_task = Task(
            id=task.id,
            title=task.title,
            description=task.description,
            status=new_status,
            priority=task.priority,
            created_at=task.created_at,
            updated_at=datetime.now(),
            due_date=task.due_date,
        )
        return await self._repository.save(updated_task)
```

### Custom Exceptions
Domain-specific exceptions (defined in `src/exceptions.py`):

```python
class TaskManagementError(Exception):
    """Base exception for task management errors."""
    pass


class TaskNotFoundError(TaskManagementError):
    """Raised when a task is not found."""
    pass


class ValidationError(TaskManagementError):
    """Raised when validation fails."""
    pass
```

### Testing Strategy
Tests follow TDD principles and are located in `tests/`:

**Test Files:**
- `tests/models/test_task.py` - Tests for Task model
- `tests/repositories/test_task_repository.py` - Tests for repository implementations
- `tests/services/test_task_service.py` - Tests for business logic

**Example Test (tests/services/test_task_service.py):**

```python
import pytest
from datetime import datetime, timedelta

from src.exceptions import TaskNotFoundError, ValidationError
from src.models.task import TaskPriority, TaskStatus
from src.repositories.task_repository import InMemoryTaskRepository
from src.services.task_service import TaskService


@pytest.fixture
def task_service() -> TaskService:
    """Provide a TaskService instance with in-memory repository."""
    repository = InMemoryTaskRepository()
    return TaskService(repository)


class TestTaskService:
    """Tests for TaskService."""

    @pytest.mark.asyncio
    async def test_create_task_success(self, task_service: TaskService) -> None:
        """Test successful task creation."""
        # Arrange
        title = "Test Task"
        description = "Test Description"
        priority = TaskPriority.HIGH

        # Act
        task = await task_service.create_task(title, description, priority)

        # Assert
        assert task.title == title
        assert task.description == description
        assert task.priority == priority
        assert task.status == TaskStatus.PENDING

    @pytest.mark.asyncio
    async def test_create_task_with_empty_title_raises_error(
        self, task_service: TaskService
    ) -> None:
        """Test that empty title raises ValidationError."""
        with pytest.raises(ValidationError, match="title cannot be empty"):
            await task_service.create_task("", "Description")

    @pytest.mark.asyncio
    async def test_get_nonexistent_task_raises_error(
        self, task_service: TaskService
    ) -> None:
        """Test that getting nonexistent task raises TaskNotFoundError."""
        with pytest.raises(TaskNotFoundError):
            await task_service.get_task("nonexistent-id")

    @pytest.mark.asyncio
    async def test_update_task_status(self, task_service: TaskService) -> None:
        """Test updating task status."""
        # Arrange
        task = await task_service.create_task("Title", "Description")

        # Act
        updated = await task_service.update_task_status(
            task.id, TaskStatus.COMPLETED
        )

        # Assert
        assert updated.status == TaskStatus.COMPLETED
        assert updated.id == task.id
```

### Usage Example

```python
import asyncio
from datetime import datetime, timedelta

from src.models.task import TaskPriority, TaskStatus
from src.repositories.task_repository import InMemoryTaskRepository
from src.services.task_service import TaskService


async def main() -> None:
    """Demonstrate task management functionality."""
    # Initialize service with repository
    repository = InMemoryTaskRepository()
    service = TaskService(repository)

    # Create a new task
    task = await service.create_task(
        title="Implement authentication",
        description="Add JWT-based authentication to the API",
        priority=TaskPriority.HIGH,
        due_date=datetime.now() + timedelta(days=7),
    )
    print(f"Created task: {task.title} (ID: {task.id})")

    # List all tasks
    tasks = await service.list_tasks()
    print(f"Total tasks: {len(tasks)}")

    # Update task status
    updated_task = await service.update_task_status(
        task.id, TaskStatus.IN_PROGRESS
    )
    print(f"Task status updated to: {updated_task.status.value}")

    # List tasks by status
    in_progress_tasks = await service.list_tasks(TaskStatus.IN_PROGRESS)
    print(f"In-progress tasks: {len(in_progress_tasks)}")


if __name__ == "__main__":
    asyncio.run(main())
```

## Architecture Decisions

### Why Repository Pattern?
- Separates data access from business logic
- Makes testing easier with mock/in-memory implementations
- Allows switching data sources without changing business logic

### Why Frozen Dataclasses?
- Ensures immutability of domain models
- Prevents accidental state mutations
- Makes code more predictable and testable

### Why Async/Await?
- Better I/O performance for database operations
- Enables concurrent task processing
- Aligns with modern Python web frameworks (FastAPI, etc.)

## Performance Considerations
- Use async operations for all I/O
- Implement caching for frequently accessed tasks
- Add pagination for task lists
- Consider indexing on status and due_date for filtering

## Future Improvements
- Add task assignment to users
- Implement task dependencies
- Add task comments/notes
- Implement task history/audit log
- Add task tags/labels for better organization
- Implement recurring tasks