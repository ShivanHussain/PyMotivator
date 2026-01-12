import time
from apscheduler.schedulers.background import BackgroundScheduler # type: ignore
from send import send_daily_quote

scheduler = BackgroundScheduler(timezone="Asia/Kolkata")
scheduler.start()

scheduler.add_job(
    send_daily_quote,
    trigger="cron",
    hour=9,
    minute=0
)

print("Scheduler started...")

try:
    while True:
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
    print("Scheduler stopped")
