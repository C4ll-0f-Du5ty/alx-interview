#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size> (if the format is not this one, the line
must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size>
(see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer,
don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order

line list = [<IP Address>, -, [<date>], "GET /projects/260 HTTP/1.1",
<status code>, <file size>]
"""

import sys

counter = 0
size = 0
statusCode = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0,
}


try:
    for line in sys.stdin:

        lineComp = line.split(" ")
        if len(lineComp) > 4:
            if lineComp[-2] in statusCode.keys():
                statusCode[lineComp[-2]] += 1
            size += int(lineComp[-1])
            counter += 1
        if counter == 10:
            counter = 0
            print("File size: {}".format(size))
            for key, value in sorted(statusCode.items()):
                if value != 0:
                    print("{}: {}".format(key, value))

except Exception as err:
    pass

finally:
    print("File size: {}".format(size))
    for key, value in sorted(statusCode.items()):
        if value != 0:
            print("{}: {}".format(key, value))
