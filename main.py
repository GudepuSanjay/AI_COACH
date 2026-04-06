import os
from dotenv import load_dotenv
from bot import run_bot
from scheduler import start_scheduler

from flask import Flask
import threading

load_dotenv()

# =========================
# TELEGRAM BOT
# =========================
def start_bot():
    app = run_bot(os.getenv("TELEGRAM_BOT_TOKEN"))
    start_scheduler(app)
    app.run_polling()

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

    # run bot in background thread
    t = threading.Thread(target=start_bot)
    t.start()

    # Render requires this
    port = int(os.environ.get("PORT", 10000))
    flask_app.run(host="0.0.0.0", port=port)