#!/usr/bin/env python3

"""coroutine that run 4 times in parallel"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """returns the runtime of the async_comprehension function"""
    start_time = time.perf_counter()

    await asyncio.gather(*(async_comprehension() for i in range(4)))

    end_time = time.perf_counter()

    return end_time - start_time
