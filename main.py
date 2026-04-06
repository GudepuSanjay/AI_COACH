import os
import asyncio
from dotenv import load_dotenv
from flask import Flask

from bot import run_bot
from scheduler import start_scheduler

load_dotenv()

# =========================
# FLASK (Render requirement)
# =========================
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "IBPS AI Bot is Running 🚀"

# =========================
# MAIN
# =========================
async def main():
    print("🚀 BOT STARTING...")

    app = run_bot(os.getenv("TELEGRAM_BOT_TOKEN"))

    # start scheduler
    start_scheduler(app)

    # run flask in background
    loop = asyncio.get_running_loop()
    port = int(os.environ.get("PORT", 10000))

    loop.run_in_executor(
        None,
        lambda: flask_app.run(host="0.0.0.0", port=port)
    )

    print("✅ BOT RUNNING...")

    # START BOT PROPERLY
    await app.initialize()
    await app.start()
    await app.bot.initialize()
    await app.updater.start_polling()

    await asyncio.Event().wait()   # keep alive

# =========================
# ENTRY
# =========================
if __name__ == "__main__":
    asyncio.run(main())