# Task Management API

The Task Management API is a robust solution designed to streamline and organize tasks efficiently. It provides a centralized platform for creating, updating, and managing tasks, enhancing collaboration and productivity. With features such as task assignment, due dates, and priority settings, this API empowers users to seamlessly integrate task management into their applications, facilitating a more organized and structured workflow. Easy-to-use endpoints make integration straightforward.

## Endpoints

The Task Management API provides endpoints for listing, filtering tasks by priority, status, or tags, user authentication, and performing operations like creating, updating, deleting tasks. Additionally, users can search for tasks by titles or descriptions, offering a comprehensive and streamlined task management experience.

### Tasks Endpoints

| Endpoint                        | Method   | Description                                           |
|---------------------------------|----------|-------------------------------------------------------|
| `/api/tasks/`                   | GET      | List all tasks                                        |
| `/api/tasks/?priority=high`      | GET      | Filter tasks by high priority                         |
| `/api/tasks/?completed=true` | GET      | Filter tasks by completed status                    |
| `/api/tasks/?tag=tag_name`       | GET      | Filter tasks by specific tag                          |
| `/auth/`                    | POST     | User Authentication (Login, Reset Password)                                  |
| `/auth/registration`                    | POST     | User Registration                               |
| `/api/tasks/<task_id>/`      | GET      | View a single intance of a task                  |
| `/api/tasks/`                   | POST     | Create a new task                                     |
| `/api/tasks/<task_id>/`         | PUT      | Update an existing task                               |
| `/api/tasks/<task_id>/`         | DELETE   | Delete an existing task                               |
| `/api/tasks/?search=query`      | GET      | Search tasks by title or description                  |

