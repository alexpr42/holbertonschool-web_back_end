#!/usr/bin/env python3
import asyncio
import time
from typing import List
import random


async def wait_random(max_delay: int) -> float:
    """Async function that waits for a random delay and returns it."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Async function that spawns n wait_random coroutine
    s and returns the list of delays."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return delays


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for the wait_n function and returns
    the average time per coroutine.

    Args:
        n (int): The number of coroutines to spawn.
        max_delay (int): The maximum delay in seconds for each coroutine.

    Returns:
        float: The average time per coroutine.
    """
    start_time = time.time()  # Record the start time
    asyncio.run(wait_n(n, max_delay))  # Execute wait_n and wait
    end_time = time.time()  # Record the end time

    total_time = end_time - start_time  # Calculate total execution time
    return total_time / n  # Return the average time per coroutine
