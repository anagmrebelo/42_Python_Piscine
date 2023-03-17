import time
import math


def ft_progress(lst):
    start = time.time()
    i = 0
    size = len(lst)
    while i < size:
        current = time.time() - start
        i += 1
        interval = current / i
        eta = (size - i) * interval
        pct = round(i/size * 100)
        prog = math.floor(pct/10) * "=" + ">"
        print(f"\rETA: {eta:.2f}s [{pct:3d}%] [{prog.ljust(11)}]", end='')
        print(f" {i:3d}/{len(lst)} | elapsed time: {current:.2f}s", end='')
        yield lst[i - 1]
