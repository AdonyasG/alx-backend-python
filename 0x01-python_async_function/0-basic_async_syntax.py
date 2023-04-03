#!/usr/bin/env python3
"""
Module - 0-basic_async_syntax
"""

import asyncio
import random


async def wait_random(wait_random: float =10) -> float:
    """simple async"""
    delay: float = random.uniform(0, wait_random)
    await asyncio.sleep(delay)
    return delay
