#!/usr/bin/env python3
"""
Module - measure_runtime
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measures runtime of a coroutine"""
    start_time = time.time()

    loop = asyncio.get_event_loop()
    delay = await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    
    end_time = time.time()

    return end_time - start_time
