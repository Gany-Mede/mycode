#!/usr/bin/python3

#~~~~WHAT I DID~~~~
#Created a room with a dragon
#In order to escape the room, you need a magic shield
#To get the shield, you need to find a riddle room, get 3/5 riddles right and then get the magic shield
#If you don't have a magic shield when you enter the dragon room, you are now dinner for the dragon
#Happy riddling! 

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'east' : 'Dragon Room',
                  'item' : 'potion',
                  'north' : 'Pantry',
               },
            'Garden' : {
                  'north' : 'Dining Room'
               },
            'Pantry' : {
                  'east' : 'Riddle Room',
                  'south' : 'Dining Room',
                  'item' : 'cookie',
            },
            'Riddle Room' : {
                  'west': 'Pantry',
                  'south' : 'Dragon Room',
                },
            'Dragon Room' : {
                  'north': 'Riddle Room',
                  'west' : 'Dining Room',

                }
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#Riddle function
def riddles():
    global inventory
    score = 0
    print("WELCOME TO THE RIDDLE ROOM!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Get at least 3 questions right and you will win a prize, get less than 3 questions right and you will lose one of the items in your inventory!")
    answer1 = int(input("\nHow many months of the year have 28 days? "))
    if answer1 == 12:
        print("That is correct! ")
        score +=1
    else: 
        print("You got this one wrong! ")
        print("The answer is 12. All months have 28 days in them")
        score -= 1
    print(f"You current score is: {score}")
    answer2 = int(input("\nWhen Grant was 8, his brother was half his age. Now, Grant is 14. How old is his brother? "))
    if answer2 == 10:
        print("You are right!")
        score +=1
    else: 
        print("Wrong! Better learn how to count")
        print("His brother is 10. Half of 8 is 4, so Grant’s brother is 4 years younger. This means when Grant is 14, his brother is still 4 years younger, so he’s 10.")
        score -=1
    print(f"Your current score is {score}")
    answer3 = int(input("\nYou’re running a race and at the very end, you pass the person in 2nd place. What place did you finish the race in? Type just a number.  "))
    if answer3 == 2:
        print("Good Job!!")
        score +=1
    else: 
        print("Got this one wrong!")
        print("If you pass a person in 2nd place, you are now in 2nd place")
        score -=1
    print(f"Your curent score is {score}")
    answer4 = int(input("\nIf two is company and three is a crowd, what are four and five? "))
    if answer4 == 9:
        print("You are absolutely right!")
        score +=1
    else:
        print("Got you! The Answer is 9")
        score -=1
    print(f"Your current score is {score}")
    answer5 = int(input("\nI am an odd number; take away an alphabet and I become even. What number am I ?"))
    if answer5 == 7:
        print("Yes! You are right!")
        score += 1
    else:
        print("This is elementary!")
        print("The answer is: 7 (SEVEN-S=EVEN)")
    print(f"\nYour final score is {score}")
    if score >= 3:
        print("Congratulations! Your prize is a magic riddle  shield!!!")
        inventory.append('shield')
    else: 
        if not inventory:
            print("You bum, you have nothing to take!")
        else:
            print(f"You lost: {inventory[-1]}")
            inventory.pop()

#Dragon Room
def dragon():
    if 'shield' in inventory:
        print("\nYou enter the room, there is a dragon looking at you, you are looking at the dragon. \nThe dragon doesn't like when people stare at him... \nIt breathes FIRE... and.... YOU BLOCKED IT WITH YOUR MAGIC SHIELD!!! \nThe dragon was not ready for that, got confused and flew away.")
    else:
        print("\nDragon: 'Well, would you look at that, dinner just came in. \nYou are a little early. \nI just recently ate, but don't let that fool you... \nI'll fry you anyway and just eat you later.' \nDragon breathes fire... AND YOU ARE FRIED!!! \nGame over!  ")
        exit()


#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
  
  ## Start riddles
  if currentRoom == 'Riddle Room':
      riddles()
  
  ##Dragon Room
  if currentRoom == 'Dragon Room':
      dragon()
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break
  
  ## If a player enters a room with a monster BUT HAS A COOKIE
  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'cookie' in inventory:
    print('The monster takes your cookie and runs away! Whew!')
    del rooms[currentRoom]['item']
    inventory.remove('cookie')

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break
