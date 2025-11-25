# Q5.py
# Program: Display 8 AI/ML applications using a dictionary in table format

def main():
    # Dictionary with keys and list of examples
    applications = {
        "Application Name": [
            "ChatGPT",
            "Google Assistant",
            "TensorFlow",
            "Midjourney",
            "Scikit-learn",
            "Fraud Detection System",
            "Language Translator",
            "Face Recognition"
        ],
        "Intelligent Feature": [
            "Natural language understanding & response",
            "Voice recognition and task automation",
            "Machine learning model building",
            "AI-based image generation",
            "Data analysis and prediction",
            "Detecting fraudulent activities",
            "Automatic text translation",
            "Identifying people from images"
        ],
        "Category (AI/ML)": [
            "AI",
            "AI",
            "ML",
            "AI",
            "ML",
            "ML",
            "AI",
            "AI"
        ]
    }

    # Print formatted table header
    print("=" * 90)
    print(f"{'Application Name':<25} {'Intelligent Feature':<45} {'Category (AI/ML)':<15}")
    print("=" * 90)

    # Loop through all 8 entries
    for i in range(8):
        print(f"{applications['Application Name'][i]:<25} {applications['Intelligent Feature'][i]:<45} {applications['Category (AI/ML)'][i]:<15}")

    print("=" * 90)


# Run program
if __name__ == "__main__":
    main()
