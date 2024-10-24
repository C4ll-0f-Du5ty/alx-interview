#!/usr/bin/python3

import signal
import re
import sys

patt = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "(.*?)" (\d+) (\d+)'
counter = 0
size = 0
statusCode = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}


def signal_handler(sig, frame):
    print(f"File size: {size}")
    for key, value in statusCode.items():
        if value > 0:
            print(f"{key}: {value}")


signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    try:
        match = re.match(patt, line)
        if match:
            size += int(match.group(5))
            statusCode[int(match.group(4))] += 1
            counter += 1
            if counter % 10 == 0:
                print(f"File size: ", size)
                for key, value in statusCode.items():
                    if value > 0:
                        print(f"{key}: {value}")
    except KeyboardInterrupt:
        pass
