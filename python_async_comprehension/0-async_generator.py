#!/usr/bin/env python3
"""random generator"""

import random
import asyncio
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """function async_generator"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
