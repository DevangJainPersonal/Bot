import os


class Config:

    BOT_TOKEN = os.environ.get("BOT_TOKEN")

    SESSION_NAME = os.environ.get("SESSION_NAME", ":memory:")

    API_ID = int(os.environ.get("API_ID"))

    API_HASH = os.environ.get("API_HASH")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")
