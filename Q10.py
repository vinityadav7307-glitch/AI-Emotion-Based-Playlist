# Q10.py
# Program: Read a CSV file, classify applications as AI or ML, and save results to a new CSV

import csv

def classify_app(description):
    """Classify app based on keywords in its description."""
    ai_keywords = ["chat", "assistant", "voice", "vision", "language", "speech", "reasoning", "planning"]
    ml_keywords = ["prediction", "classification", "clustering", "regression", "model", "training", "data"]

    text = description.lower()

    if any(word in text for word in ai_keywords):
        return "AI"
    elif any(word in text for word in ml_keywords):
        return "ML"
    else:
        return "Unknown"


def main():
    input_file = "applications.csv"
    output_file = "classified_applications.csv"

    try:
        with open(input_file, "r", newline='', encoding="utf-8") as infile, \
             open(output_file, "w", newline='', encoding="utf-8") as outfile:

            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames + ["Category"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            writer.writeheader()

            for row in reader:
                app_name = row.get("Application Name", "")
                description = row.get("Description", "")
                category = classify_app(description)
                row["Category"] = category
                writer.writerow(row)

        print(f"✅ Classification complete! Results saved to '{output_file}'")

    except FileNotFoundError:
        print(f"❌ Error: '{input_file}' not found. Please make sure the file exists in the same folder.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")


if __name__ == "__main__":
    main()
