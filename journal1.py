# simple_interest.py

import sys

if len(sys.argv) == 4:
    script_name=sys.argv[0]
    p = float(sys.argv[1])  # Principal
    r = float(sys.argv[2])  # Rate
    t = float(sys.argv[3])  # Time
        
else:
    script_name=sys.argv[0]
    p=10000
    r=10
    t=3


si = (p * r * t) / 100
print(f"Simple Interest: {si}")
