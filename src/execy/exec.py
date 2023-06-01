import time
import asyncio
from functools import wraps


def exec_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if asyncio.iscoroutinefunction(func):
            return measure_execution_time_async(func, *args, **kwargs)
        else:
            return measure_execution_time_sync(func, *args, **kwargs)

    def measure_execution_time_sync(func, *args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        wrapper.execution_time = execution_time  # type: ignore
        print(f"Function '{func.__name__}' executed in {execution_time} seconds.")
        return result

    async def measure_execution_time_async(func, *args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        wrapper.execution_time = execution_time  # type: ignore
        print(f"Function '{func.__name__}' executed in {execution_time} seconds.")
        return result

    return wrapper
