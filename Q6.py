# Q6.py
# Program: Classify applications as ML, AI, or Hybrid AI based on their features

def classify_application(features):
    """Classify based on given rules."""
    features = features.lower()

    has_ml = any(word in features for word in ["prediction", "classify", "classification"])
    has_ai = any(word in features for word in ["reasoning", "planning", "decision"])

    if has_ml and has_ai:
        return "Hybrid AI"
    elif has_ml:
        return "ML"
    elif has_ai:
        return "AI"
    else:
        return "Unknown"


def main():
    print("Enter details of applications to classify (type 'exit' to stop):\n")
    while True:
        app_name = input("Enter application name: ").strip()
        if app_name.lower() == "exit":
            break

        features = input("Enter main intelligent features (e.g., prediction, planning, reasoning): ")
        category = classify_application(features)

        print(f"→ {app_name} is classified as: {category}\n")


if __name__ == "__main__":
    main()
