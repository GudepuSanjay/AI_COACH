import os
from dotenv import load_dotenv
from flask import Flask
import asyncio

from bot import run_bot
from scheduler import start_scheduler

load_dotenv()

# =========================
# FLASK (FOR RENDER PORT)
# =========================
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "IBPS AI Bot is Running 🚀"

# =========================
# MAIN ASYNC FUNCTION
# =========================
async def main():
    app = run_bot(os.getenv("TELEGRAM_BOT_TOKEN"))
    start_scheduler(app)

    # 🔥 run flask in background (non-blocking)
    loop = asyncio.get_event_loop()
    port = int(os.environ.get("PORT", 10000))

    loop.run_in_executor(
        None,
        lambda: flask_app.run(host="0.0.0.0", port=port)
    )

    # ✅ run bot in MAIN thread (important)
    await app.run_polling()

# =========================
# ENTRY POINT
# =========================
if __name__ == "__main__":
    asyncio.run(main())