import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24068416"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "28a2547994e9a64f046eabbd87dcc09d")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://sadulanita536:R7K10VSNV9CBik3j@cluster0.g4ptofo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
