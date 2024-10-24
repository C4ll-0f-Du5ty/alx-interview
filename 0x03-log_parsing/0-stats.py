#!/usr/bin/python3

import re
import sys

pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "(.*?)" (\d+) (\d+)'

for line in sys.stdin:
    match = re.match(pattern, line)
    if match:
        print(match)
