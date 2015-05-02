from apscheduler.scheduler import Scheduler
sched = Scheduler()
sched.daemonic=False
def job_function(text):
    print text

from datetime import datetime
job=sched.add_date_job(job_function, datetime(2015, 4, 14, 21, 52, 00, 0),['hello world'])
sched.start()
