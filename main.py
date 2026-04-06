import os
import asyncio
import threading
from dotenv import load_dotenv

from bot import run_bot
from scheduler import start_scheduler

from flask import Flask

load_dotenv()

# =========================
# TELEGRAM BOT (ASYNC FIXED)
# =========================
async def start_bot_async():
    app = run_bot(os.getenv("TELEGRAM_BOT_TOKEN"))
    start_scheduler(app)
    await app.run_polling()

def start_bot():
    asyncio.run(start_bot_async())   # ✅ FIXED event loop issue

# =========================
# FLASK WEB SERVER
# =========================
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "IBPS AI Bot is Running 🚀"

# =========================
# MAIN
# =========================
if __name__ == "__main__":

    # 🔥 Run bot in background thread
    bot_thread = threading.Thread(target=start_bot)
    bot_thread.start()

    # 🔥 Required for Render Web Service
    port = int(os.environ.get("PORT", 10000))
    flask_app.run(host="0.0.0.0", port=port)