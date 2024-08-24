#!/usr/bin/env python3
"""Coroutine that will execute four times in parallel"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime():
    start_time = time.perf_counter()

    # Run async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.perf_counter()
    return end_time - start_time
