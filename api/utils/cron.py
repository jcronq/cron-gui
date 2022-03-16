from crontab import CronTab

def get_crontab(user: str):
  cron = CronTab(user=user)
  return [
    str(job)
    for job in cron
  ]