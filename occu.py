#!/usr/bin/env python
from UCB import occupy_cal
from Oakland import port

for member in occupy_cal:
    member.march_to(port)
