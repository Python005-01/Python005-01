import functools
import time


loop = asyncio.get_event_loop()
def Time(func):
    @functools.wraps(func)
    def time_wraps(*args, **kwargs):
        print(f'{func.__name__} --start--')
        start_time = time.time()
        ret = func(*args, **kwargs)
        end_time = time.time()-start_time
        print(f"执行时间{end_time}")
        print(f'{func.__name__} --end--')
        return ret

    return time_wraps
@Time
def sleep_time(n):
        time.sleep(n)
    #return n

sleep_time(3)



