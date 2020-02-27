from apscheduler.schedulers.blocking import BlockingScheduler
import tweet

twische = BlockingScheduler()

@twische.scheduled_job('interval',minutes=3)
def timed_job():
    tweet.timeline_favo()

if __name__ == "__main__":
    twische.start()