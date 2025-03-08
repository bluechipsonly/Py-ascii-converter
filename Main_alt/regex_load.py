import time as t
import sys


def regex_param(duration=1):
    animation = ["|", "/", "-", "\\"]
    end_time = t.time() + duration
    while t.time() < end_time:
        for char in animation:
            sys.stdout.write(f"\rloading {char}")
            sys.stdout.flush()
            t.sleep(0.1)
    sys.stdout.write("\rDone!   \n")
    sys.stdout.flush()