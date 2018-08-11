import time

import os
import sys
import logging

current = os.path.dirname(os.path.abspath(__file__))
parent = os.path.abspath(os.path.join(current, os.pardir))
sys.path.append(parent)

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def make_timer():
    last_time = None

    def elapsed():
        nonlocal last_time
        now = time.time()
        if not last_time:
            last_time = now
            return None
        result = now - last_time
        last_time = now
        return result
    return elapsed


t = make_timer()
print(t())
print(t())
print(t())
print(t())
