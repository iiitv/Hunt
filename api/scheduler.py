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
        now = datetime.datetime(2021, 2, 19, 18, 0, 0, 0) + datetime.timedelta(seconds = 3601)
        print(str(now))
        scheduler.add_job(level.score_decay, 'interval', start_date = str(now), minutes=60)
        i+=1
    scheduler.start()
