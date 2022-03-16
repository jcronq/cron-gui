# from pathlib import Path
# import subprocess

# etc = Path('/etc')
# daily_cron   = etc / 'cron.daily'
# weekly_cron  = etc / 'cron.weekly'
# monthly_cron = etc / 'cron.monthly'

# supported_job_class = ['daily', 'monthly', 'weekly']

# def list_jobs(job_class: str):
#   if job_class == 'all':
#     return [{
#         "name": path.name,
#         "jobClass": str(path.parent).split('.')[1],
#       }
#       for path in etc.glob('cron.*/*')
#     ]
#   if job_class in supported_job_class:
#     return [{
#         "name": path.name,
#         "jobClass": job_class,
#       }
#       for path in (etc / f"cron.{job_class}").glob('*')
#     ]

# def get_job_code(job_class: str, job_name: str):
#   if job_class in supported_job_class:
#     with (etc / f"cron.{job_class}" / job_name).open('r') as _f:
#       return _f.read()
