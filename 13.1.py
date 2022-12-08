from datetime import date, datetime
import time

now = date.today()

now_str = now.isoformat()

with open('today.txt', 'wt') as output:
    output.write(now_str)

with open('today.txt', 'rt') as input:
    today_string = input.read()

fmt = "%Y-%m-%d"

datetime.strptime(today_string, fmt)

