#!/usr/bin/env python3
"""
Module - async_generator
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """async generator"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10