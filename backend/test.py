from app.services.classifier import classify_task

print(
    classify_task(
        "Schedule urgent meeting with team today",
        "Discuss budget allocation"
    )
)