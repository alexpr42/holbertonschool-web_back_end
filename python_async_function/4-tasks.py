#!/usr/bin/env python3
"""take a code and alter it into a new function"""


import asyncio
from typing import List


async def wait_random(max_delay: int) -> float:
    """
    Asynchronous function that waits for a random delay
    between 0 and max_delay.

    Args:
        max_delay (int): The maximum delay to be used.

    Returns:
        float: The delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio Task that runs wait_random
    with the given max_delay.

    Args:
        max_delay (int): The maximum delay to be used by wait_random.

    Returns:
        asyncio.Task: The asyncio Task object.
    """
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create a list of tasks that run wait_random and return their
    results in ascending order.

    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay to be used by wait_random.

    Returns:
        List[float]: The list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return delays
