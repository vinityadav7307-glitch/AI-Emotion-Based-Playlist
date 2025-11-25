# Q9.py
# Program: Classify 10 intelligent features as AI or ML

def classify_feature(feature):
    """Classify a single intelligent feature as AI or ML."""
    ai_keywords = ["reasoning", "planning", "decision", "vision", "speech", "language", "image", "robot"]
    ml_keywords = ["prediction", "classification", "training", "model", "clustering", "regression", "data"]

    f = feature.lower()

    if any(word in f for word in ai_keywords):
        return "AI"
    elif any(word in f for word in ml_keywords):
        return "ML"
    else:
        return "Unknown"


def main():
    print("Enter 10 intelligent features (e.g., prediction, planning, image detection):\n")

    results = {}

    for i in range(10):
        feature = input(f"Enter feature {i+1}: ").strip()
        category = classify_feature(feature)
        results[feature] = category

    # Display results
    print("\n=== Classification Results ===")
    for feature, category in results.items():
        print(f"{feature:<30} → {category}")

    # Summary
    ai_count = sum(1 for v in results.values() if v == "AI")
    ml_count = sum(1 for v in results.values() if v == "ML")
    unknown_count = sum(1 for v in results.values() if v == "Unknown")

    print("\n=== Summary ===")
    print(f"AI Features: {ai_count}")
    print(f"ML Features: {ml_count}")
    print(f"Unknown Features: {unknown_count}")


if __name__ == "__main__":
    main()
