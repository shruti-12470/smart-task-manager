import re
from datetime import datetime

CATEGORY_KEYWORDS = {
    "scheduling": ["meeting", "schedule", "call", "appointment", "deadline"],
    "finance": ["payment", "invoice", "bill", "budget", "expense", "cost"],
    "technical": ["bug", "fix", "error", "install", "repair", "maintain"],
    "safety": ["safety", "hazard", "inspection", "compliance", "ppe"],
}

PRIORITY_KEYWORDS = {
    "high": ["urgent", "asap", "immediately", "today", "critical", "emergency"],
    "medium": ["soon", "this week", "important"],
}

SUGGESTED_ACTIONS = {
    "scheduling": ["Block calendar", "Send invite", "Prepare agenda", "Set reminder"],
    "finance": ["Check budget", "Get approval", "Generate invoice", "Update records"],
    "technical": ["Diagnose issue", "Assign technician", "Document fix"],
    "safety": ["Conduct inspection", "File report", "Notify supervisor"],
    "general": ["Review task", "Assign owner", "Set due date"],
}


def detect_category(text: str) -> str:
    text = text.lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(word in text for word in keywords):
            return category
    return "general"


def detect_priority(text: str) -> str:
    text = text.lower()
    for priority, keywords in PRIORITY_KEYWORDS.items():
        if any(word in text for word in keywords):
            return priority
    return "low"


def extract_entities(text: str) -> dict:
    entities = {}

    # Date extraction (simple)
    date_match = re.search(r"\b(today|tomorrow|\d{1,2}/\d{1,2}/\d{4})\b", text.lower())
    if date_match:
        entities["date"] = date_match.group()

    # Person extraction
    person_match = re.search(r"(with|assign to|by)\s([A-Za-z ]+)", text)
    if person_match:
        entities["person"] = person_match.group(2).strip()

    return entities


def classify_task(title: str, description: str | None):
    combined_text = f"{title} {description or ''}"

    category = detect_category(combined_text)
    priority = detect_priority(combined_text)
    entities = extract_entities(combined_text)
    actions = SUGGESTED_ACTIONS.get(category, [])

    return {
        "category": category,
        "priority": priority,
        "extracted_entities": entities,
        "suggested_actions": actions,
    }