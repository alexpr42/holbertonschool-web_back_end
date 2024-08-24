#!/usr/bin/env python3
"""coroutine that takes no arguments"""


import asyncio
import random


async def async_generator():
    """async generator with range"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
