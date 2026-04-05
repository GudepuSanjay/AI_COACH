from apscheduler.schedulers.asyncio import AsyncIOScheduler
from db import Session, User
from bot import send_question
from pytz import timezone

def start_scheduler(application):

    ist = timezone("Asia/Kolkata")
    scheduler = AsyncIOScheduler(timezone=ist)

    async def daily_test():
        db = Session()
        users = db.query(User).all()

        for user in users:
            for _ in range(25):
                await send_question(application.bot, user.user_id)

    scheduler.add_job(
        daily_test,
        "cron",
        hour=10,
        minute= 0
    )

    # ✅ FIX: async wrapper
    async def start_sched(context):
        scheduler.start()

    application.job_queue.run_once(start_sched, when=1)