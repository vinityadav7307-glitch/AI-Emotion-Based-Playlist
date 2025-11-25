
from collections import Counter

def classify_system(text: str) -> str:
    """Classify the system as AI, ML, or Unknown using simple keyword rules."""
    t = text.lower()

    ai_keywords = [
        "chat", "assistant", "bot", "translator", "translate",
        "nlp", "language", "speech", "voice", "vision", "image",
        "summariz", "qa ", "question answering", "recommendation engine"
    ]
    ml_keywords = [
        "detect", "classification", "regression", "predict", "forecast",
        "anomaly", "recommend", "clustering", "recognition",
        "fraud", "spam", "risk", "pricing", "churn"
    ]

    if any(k in t for k in ai_keywords):
        return "AI"
    if any(k in t for k in ml_keywords):
        return "ML"
    return "Unknown"

def main():
    history = []  # list of dicts: {"name": str, "category": str}

    print("Intelligent System Classifier")
    print("Type system names (e.g., 'Fraud Detection', 'Chatbot').")
    print("Type 'exit' to finish.\n")

    try:
        while True:
            user_input = input("Enter intelligent system (or 'exit'): ").strip()
            if not user_input:
                continue
            if user_input.lower() in {"exit", "quit", "q"}:
                break

            category = classify_system(user_input)
            history.append({"name": user_input, "category": category})
            print(f" → Classified as: {category}\n")

    except KeyboardInterrupt:
        print("\n\n(Interrupted) Exiting and printing history...")

    # Print history
    if history:
        print("\n==== Classification History ====")
        for i, item in enumerate(history, start=1):
            print(f"{i}. {item['name']} — {item['category']}")

        # Optional summary
        counts = Counter(h["category"] for h in history)
        print("\nSummary:")
        for label in ("AI", "ML", "Unknown"):
            print(f"  {label}: {counts.get(label, 0)}")
    else:
        print("\nNo entries were classified.")

if __name__ == "__main__":
    main()
