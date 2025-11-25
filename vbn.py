# Simple Intelligent System Classifier

history = []

print("Enter intelligent systems (e.g., Fraud Detection, Chatbot, Translator)")
print("Type 'exit' to stop.\n")

while True:
    name = input("Enter system name: ").strip()
    if name.lower() == "exit":
        break

    n = name.lower()
    if any(k in n for k in ["detect", "predict", "classify"]):
        kind = "ML"
    elif any(k in n for k in ["chatbot", "translate", "language", "reason"]):
        kind = "AI"
    else:
        kind = "Unknown"

    history.append((name, kind))
    print(f"→ {name} is classified as {kind}\n")

print("\n--- History ---")
for h in history:
    print(f"{h[0]} → {h[1]}")

