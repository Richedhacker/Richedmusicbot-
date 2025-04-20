import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 25359040
API_HASH = "27b1988b1b6a6a600db4ee7607d36946"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7533599560:AAHk2Jl4_XX75-GwN1nrgcRHfct1iRz4RZA"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://MAHAVIRKUMAR123:MAHAVIRKUMAR123@cluster0.afaopoh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002657124059

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 7557581984

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/+-z4BzmO6R5BlYzI9"
SUPPORT_GROUP = "https://t.me/+ROUNPC4Y8QQzYjZl"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQAf70YAoR2loOOlE_Qd8L6UPHaTi2YbO3btAxqKoPS4v1rgsV97A13U8vGxoJ45Vll5aGMjAKNK7K8K54KPqyXGkEj0w5hLew2s7-48-k7kqOCIualbO5915iGXYnoEclaVmejPeTV-M2d3wf9xU9tC3PNRXfv_00KKwrn8KNhvemk4NChSFP7padrYbUT8VWvL2yXt4OEs7i-zzn28AweOQDsz1kLMBXQKCtXB38z8Nyu2Fz98iPvtU90GUrjYwluHVZfpPtvUmdYhRW_ZtKXA0bhiXqW8Gg28px1WxQU100aQ_4OkSTkNW16Yxs0XNIdVtBQHiKurFPdbMt-Xav-TYM0FdgAAAAFQpeskAA"
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


START_IMG_URL = "https://graph.org/file/f586172fe40a0b5d0b0df.jpg"

PING_IMG_URL = "https://graph.org/file/f586172fe40a0b5d0b0df.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/2acd841333e96fa2dc455-3527e6c8716b60838d.jpg"
STATS_IMG_URL = "https://graph.org/file/2acd841333e96fa2dc455-3527e6c8716b60838d.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/2acd841333e96fa2dc455-3527e6c8716b60838d.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/2acd841333e96fa2dc455-3527e6c8716b60838d.jpg"
STREAM_IMG_URL = "https://graph.org/file/2acd841333e96fa2dc455-3527e6c8716b60838d.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/2acd841333e96fa2dc455-3527e6c8716b60838d.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/2acd841333e96fa2dc455-3527e6c8716b60838d.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/2acd841333e96fa2dc455-3527e6c8716b60838d.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/2acd841333e96fa2dc455-3527e6c8716b60838d.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/2acd841333e96fa2dc455-3527e6c8716b60838d.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
