#!/usr/bin/env python3
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random delay and returns it.

    Args:
        max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The actual delay that was waited.
    """
    random.seed(42)  # Seed for reproducibility
    delay = random.uniform(0, max_delay)  # Generate a random delay
    await asyncio.sleep(delay)            # Wait for the delay
    return delay                           # Return the delay

# Testing the function
if __name__ == "__main__":
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
