#!/usr/bin/env python3

import requests


    ## create r, which is our request object
r = requests.get('http://api.open-notify.org/astros.json').json()

print(f"People in space: {r['number']} ")

for output in r["people"]:
    print(f"{output['name']} on {output['craft']}")


