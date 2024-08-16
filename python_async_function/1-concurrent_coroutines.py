#!/usr/bin/env python3
import asyncio
from typing import List
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously wait for a random delay between 0 and
    max_delay (inclusive) seconds.

    Args:
     max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
    float: The delay time in seconds.
    """
    # Generate a random float between 0 and max_delay
    delay = random.uniform(0, max_delay)
    # Asynchronously wait for the generated delay
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn n coroutines that each wait for a random delay
    between 0 and max_delay seconds,
    and return a list of these delays in ascending order.

    Args:
        n (int): The number of coroutines to spawn.
        max_delay (int): The maximum delay for each coroutine in seconds.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    # Create a list of coroutine tasks
    tasks = [wait_random(max_delay) for _ in range(n)]

    delays = []
    # Gather results as they complete and store them in delays
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
