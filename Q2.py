# Q4.py
# Program: Classify 5 applications as AI or ML using functions

# Function to take 5 user inputs
def get_applications():
    apps = []
    print("Enter names of 5 intelligent systems/applications:")
    for i in range(5):
        app = input(f"Enter application {i+1}: ")
        apps.append(app)
    return apps


# Function to classify each application
def classify(app):
    ai_keywords = ['chat', 'assistant', 'voice', 'translator', 'gpt', 'ai', 'image', 'vision']
    ml_keywords = ['predict', 'train', 'detect', 'model', 'tensorflow', 'pytorch', 'scikit']

    name = app.lower()

    if any(word in name for word in ai_keywords):
        return "AI"
    elif any(word in name for word in ml_keywords):
        return "ML"
    else:
        return "Unknown"


# Function to display classification results
def display(results):
    print("\n=== Classification Results ===")
    for app, category in results.items():
        print(f"{app} → {category}")


# Main program flow
def main():
    apps = get_applications()  # get user input
    results = {}               # dictionary to store classifications

    for app in apps:
        results[app] = classify(app)

    display(results)           # show results


# Run program
if __name__ == "__main__":
    main()
