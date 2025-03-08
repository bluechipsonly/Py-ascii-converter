import time as t
import sys as s
from colorama import Fore, Back, Style


def sys_param():
    for i in range(0, 21):
        percentage = (i / 20) * 100
        t.sleep(0.1)

        s.stdout.write(
            f"\r{Back.GREEN}{Fore.BLACK} Progress: {percentage:.0f}% [{'#' * i}{'.' * (20 - i)}] {Style.RESET_ALL}"
            )

        s.stdout.flush()
    s.stdout.write(" \n")
