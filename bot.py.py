import tweepy
import time
import datetime
import random

# Twitter API credentials 
API_KEY = "AEkPNToofiDmFg4iavud0t7RU"
API_SECRET = "QDzKuGYQoGZmXyqA9z5z6QRPeCSMBko5zKb17QKajvVFHsRvrl"
ACCESS_TOKEN = "1250758816280399876-3MfWxdG3D4lJYDNuBKcPsZo6mChdXm"
ACCESS_SECRET = "LBC11AUWSMMspC27ByCmlZSrenz3skh0MVoiMHsYDxj75"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAKU50QEAAAAAZCgDunpM1gBnsaf7WnK99rm0yNE%3Du2mDyt5QSil3ayFDz0MqqjsqsLLtmj3B78saD9zMHowU6Hdr28" 

# 🔑 Authenticate with Twitter API v2
client = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAKU50QEAAAAAZCgDunpM1gBnsaf7WnK99rm0yNE%3Du2mDyt5QSil3ayFDz0MqqjsqsLLtmj3B78saD9zMHowU6Hdr28", 
                       consumer_key="AEkPNToofiDmFg4iavud0t7RU", 
                       consumer_secret="QDzKuGYQoGZmXyqA9z5z6QRPeCSMBko5zKb17QKajvVFHsRvrl",
                       access_token= "1250758816280399876-3MfWxdG3D4lJYDNuBKcPsZo6mChdXm",
                       access_token_secret="LBC11AUWSMMspC27ByCmlZSrenz3skh0MVoiMHsYDxj75")

# === Astrology Content Pool ===
astrology_messages = [
    "♈ Aries – Today’s energy is all about action. Take the lead, but don’t rush. 💪",
    "♉ Taurus – Ground yourself. Your intuition is your best guide today. 🌱",
    "♊ Gemini – Communication will open new doors. Speak up! 🗣️",
    "♋ Cancer – Feel deeply, but don’t drown. Self-care is a must. 💧",
    "♌ Leo – Step into the spotlight. Shine without fear. 🌟",
    "♍ Virgo – Details matter, but don’t forget the bigger picture. 🧠",
    "♎ Libra – Harmony can be found if you choose peace over perfection. ⚖️",
    "♏ Scorpio – Intensity is your strength. Use it wisely. 🔥",
    "♐ Sagittarius – Adventure is calling. Trust the journey. 🏹",
    "♑ Capricorn – Your hard work is about to pay off. Stay focused. 🧗",
    "♒ Aquarius – Embrace the weird. Your uniqueness is your power. 🧬",
    "♓ Pisces – Dream big, but act grounded. Magic is real. ✨",
    "🌌 Today’s cosmic vibe: Trust what your soul whispers, not what your fears shout.",
    "🌠 Let the stars remind you: Your path is written in magic, not logic.",
    "🪐 Astrological tip: Mercury may be in retrograde, but your mind doesn’t have to be!"
]

# === Tweet Function ===
def post_astrology_tweet():
    today = datetime.datetime.now().strftime("%A, %B %d")
    message = random.choice(astrology_messages)
    tweet_text = f"{message} \n\n🌙 {today} #Astrology #Horoscope"

    try:
        client.create_tweet(text=tweet_text)
        print(f"[{today}] Tweet posted: {tweet_text}")

        with open("tweet_log.txt", "a", encoding="utf-8") as log:
            log.write(f"{datetime.datetime.now()} - {tweet_text}\n")
    except tweepy.TweepyException as e:
        print("Error posting tweet:", e)

# === Main Loop: 500 tweets/month ≈ every 87 minutes (525,600 min/year ÷ 12 ÷ 500) ===
interval_minutes = 87
while True:
    post_astrology_tweet()
    time.sleep(interval_minutes * 60)  # Convert minutes to seconds