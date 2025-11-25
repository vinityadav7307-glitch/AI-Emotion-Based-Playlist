import random
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from flask import Flask, render_template, request

app = Flask(__name__)

# --- Sentiment setup ---
def ensure_vader():
    try:
        nltk.data.find("sentiment/vader_lexicon.zip")
    except LookupError:
        nltk.download("vader_lexicon")

ensure_vader()
sia = SentimentIntensityAnalyzer()


def get_sentiment_score(text: str) -> float:
    return sia.polarity_scores(text)["compound"]


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


# ✅ LEVEL-1 PLAYLISTS WITH LINKS
MOOD_PLAYLISTS = {
    "happy": {
        "title": "Feel-Good Pop",
        "tracks": [
            {
                "name": "Levitating – Dua Lipa",
                "spotify": "https://open.spotify.com/track/463CkQjx2Zk1yXoBuierM9",
                "youtube": "https://www.youtube.com/watch?v=TUVcZfQe-Kw"
            },
            {
                "name": "Uptown Funk – Mark Ronson ft. Bruno Mars",
                "spotify": "https://open.spotify.com/track/32OlwWuMpZ6b0aN2RZOeMS",
                "youtube": "https://www.youtube.com/watch?v=OPf0YbXqDm0"
            },
            {
                "name": "Can't Stop The Feeling – Justin Timberlake",
                "spotify": "https://open.spotify.com/track/6JV2JOEocMgcZxYSZelKcc",
                "youtube": "https://www.youtube.com/watch?v=ru0K8uYEZWw"
            },
            {
                "name": "Shut Up and Dance – WALK THE MOON",
                "spotify": "https://open.spotify.com/track/3w3y8KPTfNeOKPiqUTakBh",
                "youtube": "https://www.youtube.com/watch?v=6JCLY0Rlx6Q"
            },
        ],
        "tags": ["pop", "dance", "upbeat"]
    },

    "sad": {
        "title": "Warm & Comfort",
        "tracks": [
            {
                "name": "Fix You – Coldplay",
                "spotify": "https://open.spotify.com/track/7LVHVU3tWFCXkVA2zL7u4d",
                "youtube": "https://www.youtube.com/watch?v=k4V3Mo61fJM"
            },
            {
                "name": "Skinny Love – Birdy",
                "spotify": "https://open.spotify.com/track/7oFBrCe9jGZABdTWltfLlm",
                "youtube": "https://www.youtube.com/watch?v=aNzCDt2eidg"
            },
            {
                "name": "River Flows In You – Yiruma",
                "spotify": "https://open.spotify.com/track/45Egmo7icyopuzJN0oPjZR",
                "youtube": "https://www.youtube.com/watch?v=7maJOI3QMu0"
            },
            {
                "name": "Holocene – Bon Iver",
                "spotify": "https://open.spotify.com/track/4mVtZdwO5UZkEQqG8TfXYM",
                "youtube": "https://www.youtube.com/watch?v=TWcyIpul8OE"
            },
        ],
        "tags": ["acoustic", "calm", "warm"]
    },

    "chill": {
        "title": "Coffeehouse Chill",
        "tracks": [
            {
                "name": "Lost in Paris – Tom Misch",
                "spotify": "https://open.spotify.com/track/6bLZPMgR0TjHoltgnTj2EJ",
                "youtube": "https://www.youtube.com/watch?v=5CFRVnqGCGc"
            },
            {
                "name": "Night Owl – Galimatias",
                "spotify": "https://open.spotify.com/track/49r84UTv48PdZcHQg4GkA0",
                "youtube": "https://www.youtube.com/watch?v=K_yBUfMGvzc"
            },
            {
                "name": "Breezeblocks – alt-J",
                "spotify": "https://open.spotify.com/track/3Fy7gAztGt6l7LNRdE9kP4",
                "youtube": "https://www.youtube.com/watch?v=Qg6BwvDcANg"
            },
            {
                "name": "Riptide – Vance Joy",
                "spotify": "https://open.spotify.com/track/7wGoVu4Dady5GV0Sv4UIsx",
                "youtube": "https://www.youtube.com/watch?v=uJ_1HMAGb4k"
            },
        ],
        "tags": ["indie", "lo-fi", "mellow"]
    }
}


def suggest_playlist(mood: str) -> dict:
    pl = MOOD_PLAYLISTS[mood]
    tracks = random.sample(pl["tracks"], k=min(4, len(pl["tracks"])))
    return {"mood": mood, "title": pl["title"], "tracks": tracks, "tags": pl["tags"]}


@app.route("/", methods=["GET", "POST"])
def index():
    suggestion = None
    user_text = ""
    score = None

    if request.method == "POST":
        user_text = (request.form.get("mood_text") or "").strip()

        if user_text:
            score = get_sentiment_score(user_text)
            mood = score_to_mood(score)
            suggestion = suggest_playlist(mood)

    return render_template("index.html", suggestion=suggestion, user_text=user_text, score=score)


if __name__ == "__main__":
    app.run(debug=True)
# Virtual environment
venv/

# Python cache
__pycache__/
*.pyc

# IDE files
.idea/
*.iml

# Jupyter
*.ipynb

# Data/output files
*.csv
*.png
*.txt
