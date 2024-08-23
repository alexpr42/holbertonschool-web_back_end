#!/usr/bin/env python3
"""write a function that takes an integer with max delay
and return asyncio"""


import asyncio
import random


async def wait_random(max_delay: int) -> float:
    """
    Asynchronous function that waits for a random dela
    y between 0 and max_delay.

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
