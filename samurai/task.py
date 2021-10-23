from huey import RedisHuey, crontab

huey = RedisHuey('base_app', host='127.0.0.1')


@huey.periodic_task(crontab(minute='*'))
def print_time():
    print("lalala")
