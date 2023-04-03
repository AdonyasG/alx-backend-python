#!/usr/bin/env python3
"""
Module - tasks
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    returns a Task object that represents the coroutine,
    which you can then use to monitor the status of
    the coroutine and potentially cancel it
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
