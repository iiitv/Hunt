from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from api.models import Level
import datetime

def start_job():
    scheduler = BackgroundScheduler()
    levels = Level.objects.all().order_by('level_number')
    print("Number of jobs = ", len(levels))
    i = 0
    for level in levels:
        now = datetime.datetime.now() + datetime.timedelta(seconds = 3601)
        scheduler.add_job(level.score_decay, 'interval', start_date = str(now)[:-7], minutes=60)
        i+=1
    scheduler.start()
