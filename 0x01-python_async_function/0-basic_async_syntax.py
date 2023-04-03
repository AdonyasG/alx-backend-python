#!/usr/bin/env python3
"""
Module - 0-basic_async_syntax
"""

import asyncio
import random


async def wait_random(max_delay=10):
    """simple async"""
    await asyncio.sleep(random.uniform(0, max_delay))
    return (random.uniform(0, max_delay))
