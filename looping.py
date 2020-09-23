#!/usr/bin/env python3


farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
{"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

#EASY
for animals in farms[0]['agriculture']:
    print(animals)

#MEDIUM
user_choice = input("Choose to see agriculture from 'NE Farm', 'SE Farm' or 'W Farm'")

for items in farms:
    if items['name']== user_choice:
        # add second for loop
