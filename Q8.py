# Q8.py
# Program: Compare AI and ML features based on user input keywords

def classify_feature(feature):
    """Classify a single feature as AI or ML using keywords."""
    ai_keywords = ["reasoning", "planning", "decision", "language", "vision", "speech", "understanding"]
    ml_keywords = ["prediction", "classification", "clustering", "regression", "training", "model", "data"]

    f = feature.lower()

    if any(word in f for word in ai_keywords):
        return "AI"
    elif any(word in f for word in ml_keywords):
        return "ML"
    else:
        return "Unknown"


def main():
    print("Enter 5 features of intelligent systems:")
    ai_features = []
    ml_features = []
    unknown_features = []

    for i in range(5):
        feature = input(f"Enter feature {i+1}: ")
        category = classify_feature(feature)

        if category == "AI":
            ai_features.append(feature)
        elif category == "ML":
            ml_features.append(feature)
        else:
            unknown_features.append(feature)

    # Display results
    print("\n=== Classification Results ===")
    print("\nAI Features:")
    if ai_features:
        for f in ai_features:
            print(f" - {f}")
    else:
        print(" (None)")

    print("\nML Features:")
    if ml_features:
        for f in ml_features:
            print(f" - {f}")
    else:
        print(" (None)")

    if unknown_features:
        print("\nUnclassified Features:")
        for f in unknown_features:
            print(f" - {f}")


if __name__ == "__main__":
    main()
