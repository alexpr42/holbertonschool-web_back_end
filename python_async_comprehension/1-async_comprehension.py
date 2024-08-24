#!/usr/bin/env python3
""" a coroutine that takes no arguments"""


import asyncio
from 0-async_generator import async_generator

async def async_comprehension():
    return [i async for i in async_generator()]
