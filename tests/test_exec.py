import time
import asyncio
import pytest
from exectime.exec import exec_time


@exec_time
async def async_function():
    # Simulate a time-consuming task asynchronously
    await asyncio.sleep(2)


def test_execution_time():
    @exec_time
    def time_consuming_function():
        # Simulate a time-consuming task
        time.sleep(2)

    # Call the decorated function
    time_consuming_function()

    # Assert that the execution time is within an acceptable range
    assert time_consuming_function.execution_time >= 1.9
    assert time_consuming_function.execution_time <= 2.1


@pytest.mark.asyncio
async def test_async_execution_time():
    # Call the decorated async function
    await async_function()

    # Assert that the execution time is within an acceptable range
    assert async_function.execution_time >= 1.9
    assert async_function.execution_time <= 2.1
