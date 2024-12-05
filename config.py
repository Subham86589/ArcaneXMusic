import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = "20927981"
API_HASH = "a17ee98cbe699823b441f2f2dae29439"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7241166244:7542474131:AAE8KLtvuoYovRIuwGvXlNgXIflbXEhPdRk"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 170000))

# Chat id of a group for logging bot's activities
LOGGER_ID = "-1002285159960"

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = "7218905176"

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Subham86589/ArcaneXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Bengali_Chatting_Hubb")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Bengali_Chatting_Hubb")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = "BQE_Ve0ApdAngrqmcADcCfUb0UwfyAPnwYrFdnCU8-aztwrEILoi1wPWAD0_iFWXBUMRVKbuP6t2v0lprfqI1iCGjOv6my9UG4qpkBx4c0KnKtdBqHSFwcHH1LjOFMRztKEjOlT0dZ34uS7AURCeLC78Y3HybsCrN8iAQhMVo7rM9NCae_Rv4FHUj956CzfOIBWlnH0hYS_4HU5hjEUXe4-FDfa4Hqj5JEXStjtGv9mHgWHRDOYpi-19dUXMz6enn6gl1oRgl0WgWXRbb4-NNggF0DdHjZrCFbH725Jjum1TcFhW9K5QW3sCNXGucruuW194pC_yJs9Sx2Vy78sH46310e80SwAAAAGbhjzeAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/cf684dc4363f8e73170c0.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/6b9896175ba9c88516b0d.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/f4a09619435575b8c7ae6.jpg"
STATS_IMG_URL = "https://graph.org/file/46c5cf7a128cce4e08894.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/45bf5808ed711cd527d0b.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/45bf5808ed711cd527d0b.jpg"
STREAM_IMG_URL = "https://graph.org/file/1c4267989df6a772a6e11.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/c3f922d37ddb4ee494d52.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/0cbddf2119a267cad60d7.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/b81e9dcb80caf963dedac.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/83eb7a8aefeb5e02c1a0b.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/fc9cfabd574b8b6e81fc5.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
