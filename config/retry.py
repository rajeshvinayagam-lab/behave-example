from time import sleep


def retry(func, retries=3, delay=1):
    for _ in range(retries):
        try:
            return func()
        except Exception as e:
            sleep(delay)
    raise e
