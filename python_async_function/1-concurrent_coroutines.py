#!/usr/bin/env python3
import asyncio
from typing import List
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay
    (inclusive) seconds."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute wait_random n times and return list of delays
    in ascending order."""
    # Create a list of coroutine tasks
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Gather all results as they complete
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
