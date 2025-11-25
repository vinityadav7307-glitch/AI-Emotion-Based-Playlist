# Q7.py
# Program: Classify an online app based on its intelligent feature and give an explanation

def classify_app(app_name):
    """Classify app and give explanation."""
    app = app_name.lower()

    if "youtube" in app:
        return ("AI", "YouTube uses Artificial Intelligence to recommend\n videos based on your watch history and preferences.")
    elif "netflix" in app:
        return ("AI", "Netflix uses AI to suggest shows and movies you might like using recommendation algorithms.")
    elif "myntra" in app or "amazon" in app or "flipkart" in app:
        return ("ML", "This app uses Machine Learning for personalized product recommendations and demand forecasting.")
    elif "uber" in app or "ola" in app:
        return ("Hybrid AI", "Uber uses ML for fare prediction and AI for route optimization and demand management.")
    elif "instagram" in app or "facebook" in app:
        return ("AI", "This app uses AI to recognize faces, filter content, and personalize your feed.")
    elif "zomato" in app or "swiggy" in app:
        return ("ML", "Uses ML to predict food delivery time and suggest restaurants based on your order history.")
    else:
        return ("Unknown", "This app's intelligent features are not clearly identifiable from the given input.")


def main():
    app_name = input("Enter any online app you use daily: ")

    category, explanation = classify_app(app_name)

    print("\n=== Classification Result ===")
    print(f"App Name: {app_name}")
    print(f"Category: {category}")
    print(f"Explanation: {explanation}")


if __name__ == "__main__":
    main()
