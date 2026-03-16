# Task_Management

# Task Management System

A full-stack Task Management System to create, organize, update, and track tasks with secure authentication and role-aware access controls.

## 1. Project Overview

The **Task Management System** is designed to help users manage daily work efficiently through a structured CRUD workflow.  
It provides APIs and/or UI flows for task lifecycle management: **Create → Read → Update → Delete**.

### Key Goals
- Simple and clean task tracking
- Secure access with authentication/authorization
- Reliable and testable CRUD operations
- Maintainable project structure for team collaboration



## 2. Features

- User authentication and protected routes
- Task CRUD operations:
  - Create task
  - View task list/details
  - Update task
  - Delete task
- Validation and structured error handling
- Modular architecture (models, serializers, views, routes)
- Contribution-friendly Git workflow



## 3. Tech Stack

> Update this section with your exact versions.

- **Backend:** Django / Django REST Framework
- **Database:** SQLite (dev) 
- **Frontend:** HTML/CSS/JS and Django Templates
- **Version Control:** Git + GitHub



## 4. Project Structure

```text
Task_Management/
├── core/
├── tasks/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
├── users/
├── web/
├── templates/
├── static/
├── manage.py
└── README.md

## 5. Setup and Installation

### Prerequisites
- Python 3.10+ (or your project version)
- pip
- Git

### Steps

```bash
# 1. Clone repository
git clone https://github.com/aaditya01-oss/Task_Management.git
cd Task_Management

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# 4) Install dependencies
pip install -r requirements.txt

# 5) Run migrations
python manage.py migrate

# 6) Start server
python manage.py runserver
```

Application runs at: `http://127.0.0.1:8000/`

---



## 6. API Documentation (Sample)

> Adjust endpoints to match your implementation.

### Base URL
`/api/tasks/`

### Endpoints

#### Create Task
- **Method:** `POST`
- **URL:** `/api/tasks/`
- **Body:**
```json
{
  "title": "Prepare project report",
  "description": "Finalize documentation and submit",
  "status": "pending"
}
```

#### Get All Tasks
- **Method:** `GET`
- **URL:** `/api/tasks/`

#### Get Task by ID
- **Method:** `GET`
- **URL:** `/api/tasks/{id}/`

#### Update Task
- **Method:** `PUT` / `PATCH`
- **URL:** `/api/tasks/{id}/`



---

## 7. Authentication & Authorization

- Auth mechanism: JWT (update with actual)
- Protected endpoints require authenticated user
- Permission checks applied on sensitive operations

---

## 8. Validation and Error Handling

- Required field validation
- Type and format validation
- Standardized API error responses
- Proper HTTP status codes (`200`, `201`, `400`, `401`, `404`, `500`)

---

## 9. Testing

### Manual/API Testing
- Tested all CRUD endpoints locally
- Verified auth-protected routes
- Verified expected error responses



## 10. Git Workflow Followed

1. Create feature branch from `main`
2. Implement scoped changes
3. Commit with meaningful messages
4. Push branch and open Pull Request
5. Resolve conflicts (if any)
6. Merge after review/checks
7. Sync local `main`

---

## 11. Team Contributions

| Contributor | Role | Key Contributions |
|------------|------|-------------------|
| @aaditya01-oss | Project Lead / Developer | Architecture, reviews, merge management,improvement and testing |
| @ravi-ally-lab | Developer/Contributor | UI/docs a11y updates, cleanup, PR contributions |
| @mishrabishal2003-ship-it | Contributor | Documentation notes and merge activity |



---

## 12. Known Issues / Improvements

- Add pagination/filter/search for tasks
- Add due dates and priority levels
- Add unit/integration test coverage expansion
- Add Docker-based deployment
- Add CI pipeline for lint/test checks

---

##  Contact

For queries, reach out via project maintainer: **@aaditya01-oss**