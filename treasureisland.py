print("""
.-. .-. .-. .-. .-. . . .-. .-.   .-. .-. .   .-. . . .-.   
 |  |(  |-  |-| `-. | | |(  |-     |  `-. |   |-| |\| |  )  
 '  ' ' `-' ` ' `-' `-' ' ' `-'   `-' `-' `-' ` ' ' ` `-' """)
print("""
  ooo,    .---.
 o`  o   /    |\________________
o`   'oooo()  | ________   _   _)
`oo   o` \    |/        | | | |
  `ooo'   `---'         "-" |_|""")

# 1. Welcomes player and initializes game
print("\nWelcome to Treasure Island.\nYour mission is to find the treasure.\n")

print("Your boat is wrecked behind you and you are on the shore facing a jungle of trees.")
print("Which way do you go? - Type 'L' or 'R'")
first_stop = input("> ")

# 2. Determines game sequence depending on user's choice 1.
if (first_stop == "L"):
    print("You've reached the Magic Rainbow Coconut Tree..") 
    print("There are three coconut colors to choose from: Red, Blue, Green.")
    print("Which Magic Coconut will you choose? - Type R, B, or G.")
elif (first_stop == 'R'):
    print("You've fallen through a trap and into the Jungle Beast's lair.\n")
    print("---Game Over---")
    print("Press CTRL C (^C) to move on to the afterlife.")
else:
    print("Your indecision has angered the Rainbow Gods. You're hit with a lightening bolt.\n")
    print("---Game Over---")
    print("Press CTRL C (^C) to move on to the afterlife.")
    
# 3. Determines game sequence depending on user's choice 2.
magic_coconut = input("> ")
print("Do you wish to break open this Magic Coconut or drop it? - Type 'O' or 'D")
coconut_prompt = input("> ")
    
if (coconut_prompt == 'O'):
    if (magic_coconut == "B"):
        print("You've found the Magic Turquoise Gem!")
        print("The Rainbow Gods have granted you a way off of the island.\n")
        print("---You Win---")
    elif (magic_coconut == "R"):
        print("Uh Oh. You've unleashed a swarm of potent killer scorpions..\n")
        print("---Game Over---")
    else:
        print("You've released a noxious fog.")
        print("You're getting.... sleepy......\n")
        print("---Game Over---")
else:
    print("It isn't safe to camp here. Choose to go left or right. - Type 'L' or 'R'")
    answer2 = input("> ")
    if (answer2 == "R"):
        print("You've reached a white door. Nothing around it, just a door.")
        print("Do you wish to go through this door? - Y or N")
        
    else:
        print("Didn't you hear the Jungle Beast creep up on you?\n")
        print("---Game Over---")
        print("Press CTRL C (^C) to move on to the afterlife.")
           
# 4. Determines game sequence depending on user's choice 3.
    in_or_out_of_door = input("> ")
    if (in_or_out_of_door == "Y"):
        print("Oh no! Walking through this door has instantly turned you to stone..")
        print("Random doors should not be trusted.\n")
        print("---Game Over---")
    else: 
        print("You've arrived at the Doom Lagoon. There is something shiny on the other side.")
        print("Do you wish to swim across the lagoon or use the abandoned canoe? - Type 'S' or 'C'\n")
        swim_or_sail = input("> ")
            
# 5. Determines game sequence depending on user's choice 4.  
        if (swim_or_sail == "S"):
            print("Unwise choice.. It is called 'Doom Lagoon', afterall.\n")
            print("---Game Over---")
        else: 
            print("Safe bet, but there's no treasure here..\n")
            print("---Game Over---")

            
    
    
