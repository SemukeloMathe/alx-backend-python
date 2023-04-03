#!/usr/bin/env python3
"""This module defines a coroutine"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returns a random float value."""

    res = random.uniform(0, max_delay)
    await asyncio.sleep(res)
    return res
