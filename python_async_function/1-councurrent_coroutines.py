#!/usr/bin/env python3
import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute wait_random n times and return list of delays
    in ascending order."""

    # Create a list of coroutine tasks
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    # Gather all results as they complete
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
