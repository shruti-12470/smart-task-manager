# Smart Task Manager

A backend-driven task management system that automatically classifies and prioritizes tasks based on content.

## Tech Stack
- Backend: FastAPI (Python)
- Database: PostgreSQL (Supabase)
- ORM: SQLAlchemy
- API Docs: Swagger (FastAPI)

## Features
- Create, list, update, delete tasks
- Auto-classification (category & priority)
- Entity extraction (date, person)
- Suggested actions per task
- REST APIs with clean architecture

## API Endpoints
- POST /api/tasks
- GET /api/tasks

## Auto-Classification Logic
- Category & priority detected using keyword-based rules
- Entities extracted using simple regex
- Suggested actions mapped per category

## Setup Instructions
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload