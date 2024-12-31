import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7670645750:AAHkdB1bpFv8E4vD93ft9Ab_s74IhNqEpus")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "26929088"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "dd10ed29ede84d1704f2f419fb376392")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "26929088"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://mohamedfoda9919:@cluster0.glpzm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
