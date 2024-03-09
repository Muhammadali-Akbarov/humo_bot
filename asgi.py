"""
deployment configuration
"""
from multiprocessing import cpu_count

# Socket Path
bind = 'unix:/run/humo_bot.sock'

# Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'
