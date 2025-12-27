from app.services.classifier import classify_task

def test_classify_scheduling_high_priority():
    result = classify_task(
        "Schedule urgent meeting today",
        "Discuss budget with team"
    )

    assert result["category"] == "scheduling"
    assert result["priority"] == "high"
    assert "Block calendar" in result["suggested_actions"]