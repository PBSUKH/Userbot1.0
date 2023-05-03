from os import getenv

API_ID = int(getenv("API_ID", "13335263"))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", ""))
LOG_GROUP = getenv("LOG_GROUP", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5392070730").split()))

ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/a62b9c7d9848afde0569e.jpg")
REPO_URL = getenv("REPO_URL", "https://github.com/Romeo-RJ/cloner")
BRANCH = getenv("BRANCH", "main")


STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
