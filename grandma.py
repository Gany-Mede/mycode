#!/usr/bin/env python3

#For every [broccoli] I find on your [plate] I'm going to [slap you].
plate = ["potato","broccoli", "carrots", "broccoli", "broccoli", "lettuce" ]
number =0
print("Grandma takes broccoli seriously and you should too!")
for food in plate:
    if food == "broccoli":
        number = number + 1
        print(f"Oh no you didn't, that's broccoli number {number} SLAP!!!")

#For every [light] I find on in an empty [room] I'm going to [take a dollar]!
room = ["light_on", "light_off", "light_on", "light_off", "light_off"]
dollars = 10
print(f"\nGrandma is about to start her rounds, you have ${dollars} so fair, she'll be taking one dollar for every light that is turned on.")
for light in room:
    if light=="light_on":
        dollars = dollars -1
        print(f"That's another light, You now have ${dollars}! ")

#For every [F] I find in your [report card] I'm going to put another [snake] in your {bed}.
report_card = ["A", "C", "B", "F", "F", "F", "C", "A","A", "A"]
snakes = 0; 
print(f"\nSo far there are {snakes} snakes in your bed, let's see how that changes once grandma looks at your report card!")
for grade in report_card:
    if grade =="F":
        snakes = snakes + 1
        print(f"Well, here is an F, you now have {snakes} snakes in your bed")


