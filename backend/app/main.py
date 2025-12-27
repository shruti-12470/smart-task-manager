from fastapi import FastAPI
from app.routers import tasks

app = FastAPI(title="Smart Task Manager")

app.include_router(tasks.router, prefix="/api/tasks", tags=["Tasks"])

@app.get("/")
def health():
    return {"status": "ok"}