#!/usr/bin/env python3
"""
Module - measure_runtime
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures time of the eventloop"""
    start_time = time.time()

    loop = asyncio.get_event_loop()
    delays = loop.run_until_complete(wait_n(n, max_delay))
    end_time = time.time()
    return end_time - start_time / n
