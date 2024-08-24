#!/usr/bin/env python3

"""async generator"""


import random
from typing import Generator
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """random number from 0 through 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
