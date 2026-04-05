import os
from dotenv import load_dotenv
from bot import run_bot
from scheduler import start_scheduler

load_dotenv()

if __name__ == "__main__":
    app = run_bot(os.getenv("TELEGRAM_BOT_TOKEN"))

    # attach scheduler AFTER app created
    start_scheduler(app)

    app.run_polling()