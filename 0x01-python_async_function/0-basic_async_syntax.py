#!/usr/bin/env python3
"""
Module - 0-basic_async_syntax
"""

import asyncio
import random


async def wait_random(wait_random=10):
    """simple async"""
    delay = random.uniform(0, wait_random)
    await asyncio.sleep(delay)
    return delay
