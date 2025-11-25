import sys
import random

# --- Sentiment (VADER) ---
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def ensure_vader():
    try:
        nltk.data.find("sentiment/vader_lexicon.zip")
    except LookupError:
        nltk.download("vader_lexicon")

def get_sentiment_score(text: str) -> float:
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)["compound"]

# --- Mood mapping ---
def score_to_mood(score: float) -> str:
    if score <= -0.6:
        return "angry"
    elif score <= -0.2:
        return "sad"
    elif score <= 0.2:
        return "chill"
    elif score <= 0.6:
        return "happy"
    else:
        return "energetic"

# --- Demo playlists (replace with your own taste) ---
MOOD_PLAYLISTS = {
    "angry": {
        "title": "Cool Off & Focus",
        "tracks": [
            "Lo-Fi Study Beats – Various",
            "Weightless – Marconi Union",
            "Thinking – Anevo",
            "Sunset Lover – Petit Biscuit",
        ],
        "tags": ["calm", "instrumental", "low-BPM"]
    },
    "sad": {
        "title": "Warm & Uplifting",
        "tracks": [
            "River Flows in You – Yiruma",
            "Holocene – Bon Iver",
            "Fix You – Coldplay",
            "Skinny Love – Birdy",
        ],
        "tags": ["gentle", "acoustic", "warm"]
    },
    "chill": {
        "title": "Coffeehouse Chill",
        "tracks": [
            "Lost in Paris – Tom Misch",
            "Night Owl – Galimatias",
            "Breezeblocks – alt-J",
            "Riptide – Vance Joy",
        ],
        "tags": ["indie", "lo-fi", "mellow"]
    },
    "happy": {
        "title": "Feel-Good Pop",
        "tracks": [
            "Levitating – Dua Lipa",
            "Shut Up and Dance – WALK THE MOON",
            "Uptown Funk – Mark Ronson ft. Bruno Mars",
            "Can’t Stop the Feeling! – Justin Timberlake",
        ],
        "tags": ["pop", "dance", "upbeat"]
    },
    "energetic": {
        "title": "Hype & Pump",
        "tracks": [
            "Believer – Imagine Dragons",
            "Stronger – Kanye West",
            "Titanium – David Guetta ft. Sia",
            "Power – Hardwell",
        ],
        "tags": ["edm", "high-BPM", "bangers"]
    },
}

def suggest_playlist(mood: str) -> dict:
    pl = MOOD_PLAYLISTS[mood]
    # Shuffle a little for variety
    picks = random.sample(pl["tracks"], k=min(4, len(pl["tracks"])))
    return {"mood": mood, "title": pl["title"], "tracks": picks, "tags": pl["tags"]}

def main():
    ensure_vader()
    user_text = " ".join(sys.argv[1:]).strip()
    if not user_text:
        user_text = input("Describe your mood or type a message: ").strip()

    if not user_text:
        print("No input provided.")
        return

    score = get_sentiment_score(user_text)
    mood = score_to_mood(score)
    rec = suggest_playlist(mood)

    print("\n=== Emotion-Based Playlist Suggestion ===")
    print(f"Input text: {user_text}")
    print(f"Sentiment score (compound): {score:.3f}")
    print(f"Detected mood: {mood}")
    print(f"Playlist: {rec['title']}  |  tags: {', '.join(rec['tags'])}")
    print("Tracks:")
    for i, t in enumerate(rec["tracks"], 1):
        print(f"  {i}. {t}")

if __name__ == "__main__":
    main()
