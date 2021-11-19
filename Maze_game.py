from datetime import date
today = date.today()
now = today.strftime("%B %d, %Y")


def intro():
    print(f"""
    It's a chilly day on {now}. 
    Your best friends think it's a good idea to go to a maze today.
    They found a new maze online and want to go check it out. 
    They ask you if you want to go too...  """)
    while True:
        main_menu =input("""
        A. You choose to stay home and catch up on your coding homework
        B. You want to go see the new maze! """) 
        if main_menu== "A" or main_menu == "a":
            print("""
            You tell your friends that you need to study and wave goodbye. 
            The next day you learn about a tragic accident that occurred at a new maze.
            You hope your friends are okay...""")
            Try_again = input("Would you like to try again? yes or no ")
            if Try_again == "yes" or Try_again == "Yes":
                main_menu
            elif Try_again =="no" or Try_again == "No":
                print("You'll be back")
                break
            else:
                print("Input invalid, try again")
                Try_again = input("Would you like to try again? yes or no ")
        if main_menu == "B" or main_menu == "b":
            print("""
            You put on your jacket and head out with your friends.
            Once you get there...""") 
            item_choices()
        else:
            print("Input invalid, try again")
            main_menu
            

def item_choices():
    print(""" 
    you and your group of friends have a choice of three items:
    rock, sword, shield, emerald, stick, torch """)
    while True:    
        options= "rock, sword, shield, emerald, stick, torch"
        items_list= ""
        item1= input("What is the first item you choose? ")
        if item1 in options:
            print(f"You chose {item1}")
        else:
            print("Input invalid, try again. ")
            item1 = input("What is the first item you choose? ")
        items_list += item1 + ", "
        item2  = input("What is the second item you choose? ")
        if item2 in options and item2 not in items_list:
            print(f"You chose {item2}")
        else:
            print("Input invalid, try again")
            item2 = input("What is the second item you choose? ")
        items_list += item2 + ", "
        item3 = input("What is the third item you choose? ")
        if item3 in options and item3 not in items_list:
            print(f"You chose {item3}")
        else:
            print("Input invalid, try again")
            item3 = input("What is the third item you choose? ")
        items_list+= item3 
        print(f"You chose these items: {items_list}. Time to enter the maze!")
        return items_list and maze1(items_list)
        

def maze1(items_list): 
    print("""
    You enter the maze and head down a narrow passageway.
    The passageway then splits into a fork. Now it's time to make a decision...""")
    while True:
        first_turn = input("Do you go right or left? ")
        if first_turn == "right" or first_turn == "Right":
            print(""" 
            You and your friends turn right.... 
            As you keep walking, the passageway gets narrower and narrower every few feet.
            You finally come to a dead end.  """)
            first_turn_question = input("Would you like to try again? yes or no ")
            if first_turn_question == "yes" or first_turn_question == "Yes":
                maze1(items_list)
            elif first_turn_question == "no" or first_turn_question == "No":
                print("""You'll be back""")
                quit()
            else:
                print("Input invalid, try again")
                first_turn_question = input("Would you like to try again? ")
        elif first_turn == "left" or first_turn == "Left":
            print(f"""
            You make a left turn!
            As you walk along the passageway you approach a tunnel 
            with a sign that says "Can only enter with a torch".
            You and your friends look at the items you chose and see {items_list}""")
            if "torch" not in items_list:
                print ("OH NO! You don't have a torch!")
                choose_items = input("Would you like to start over? yes or no? ")
                if choose_items == "yes" or choose_items == "Yes":
                    item_choices()
                elif choose_items == "no" or choose_items == "No":
                    quit()
            else:
                print("Great! You have a torch!")
                items_list2= items_list.replace("torch", "")
                print("""


                Your friend Jason lights the torch and you continue your journey through the tunnel.
                After going through the tunnel, your passageway comes to end with 
                a door on the right side, a door in the middle
                and a door on the left side...
                
                """)
                maze2(items_list2)
        else:
            print("Input invalid, try again")

def maze2(items_list2):
    while True:
        second_turn = input("Which door would you like to open, the left, middle, or right one? ")
        if second_turn == "left" or second_turn == "Left":
            print("""


            A loud screech comes from inside the door! 
            Your friend Cindy immediately shuts the door. 
            "That's definitely the wrong door", she says.
            
            """)
            screech = input("Try again? yes or no  ")
            if screech == "Yes" or screech == "yes":
                maze2(items_list2)
            elif screech == "No" or screech =="no":
                print("""You'll be back""")
                exit()
            else:
                print("Input invalid, try again")
                screech = input("Try again? yes or no  ")
        elif second_turn == "middle" or second_turn == "Middle":
            print("""


            A blazing fire shoots out from the door!
            Your friend Eduardo shuts the door.
            "That ain't the right one", he says.
            
            """)
            fire = input("Try again? yes or no  ")
            if fire == "yes" or fire == "Yes":
                maze2(items_list2)
            elif fire == "No" or fire == "no":
                print("""You'll be back""")
                exit()
            else:
                print("Input invalid, try again")
                fire = input("Try again? yes or no  ")
        elif second_turn == "right" or second_turn == "Right":
            print(f"""


            You open the door and your friends rush through the doorway with excitement.
            after walking a few yards in the passageway it makes a sharp left and then you see it.....
            the dragon....  the words, "SLAY THE DRAGON WITH YOUR SWORD" are scribbled on the wall. 
            
            Your friend, Keisha, looks to see if you have a sword...you have: {items_list2}.
            """)
            if "sword" not in items_list2:
                print("""
                "DANG IT! we don't have a sword!", she says. 
                Everyone panics and runs the opposite way.  """)
                pregunta = input("Would you like to try again? yes or no  ")
                if pregunta == "yes" or pregunta == "Yes":
                    item_choices()
                elif pregunta == "no" or pregunta =="No":
                    print("""You'll be back""") 
                    exit()
                else:
                    print("Invalid input. Try again")
                    pregunta = input("Would you like to try again? yes or no  ")
            elif "sword" in items_list2:
                print("""


                Bob has a sword! Keisha grabs the sword and "HI-YA!", she yells as she slays the dragon.
                You didn't know she could do that, "You go girl" you think to yourself as you and your group
                of friends scurry past the dead dragon.
                
                """)
                items_list3 = items_list2.replace("sword", "")
                maze3(items_list3)
            
        else:
            print("Input invalid, try again")

def maze3(items_list3):
    print("""
    You and your friends stop to catch your breath after that huge adrenaline rush.
    "They didn't tell us this place is dangerous!" Daphne yelled. 
    You start wondering if you made a mistake by coming to the maze...
    Jason says,"Let's get outta here" and now your group is remotivated to finish the maze and go home.
    You walk down the hallway and reach another fork in the path.
    There's a hallway on the left and one on the right......
    
    
    """)
    while True:
        third_turn = input("Which hallway do you choose? left or right?  ")
        if third_turn == "left" or third_turn == "Left":
            print("""
            Yall go down the hallway on the left side. 
            You walk a few yards and stop as the floor in front of you drops off into a cliff.
            You look over the cliff to see if you can see anything,
            but all you see is darkness. "We chose the wrong hallway," 
            you say as everyone turns around to go back.  
            
            """)
            keep_trying = input("Do you want to try again? yes or no  ")
            if keep_trying == "yes" or keep_trying == "Yes":
                third_turn = input("Which hallway do you choose? left or right?  ")
            elif keep_trying == "no" or keep_trying == "No":
                exit()
            else:
                print("Input invald. Try again")
                keep_trying = input("Do you want to try again? yes or no  ")
        elif third_turn == "right" or third_turn == "Right":
            print(f"""


            Yall go down the hallway on the right side.
            You walk a few yards and see the exit sign,
            the light at the end of the tunnel.
            Everyone gets excited and starts to run towards the exit....
            
            """)
            print(f"""Then a witch appears right in front of you out of thin air! 
            "I'll only let you pass if you give me something precious....like an emerald.
            Everyone looks to see the last item you have: {items_list3}.""" )
            if "emerald" not in items_list3:
                print("""


                OH NO! you don't have an emerald. 
                The witch turns you and your friends into mice and you're stuck 
                in the maze forever!
                
                """)
                last_time = input("Would you like to try again? yes or no ")
                if last_time == "yes" or last_time == "Yes":
                    item_choices()
                elif last_time == "no" or last_time == "No":
                    exit()
                else:
                    print("Input invalid. Try again")
                    last_time = input("Would you like to try again? yes or no ")
            elif "emerald" in items_list3:
                print("""


                You're holding an emerald! 
                You give it to the witch and she disappears.
                "YES!" everyone shouts as you run to the exit 
                and out the exit door. You made it, you survived the maze.
                
                """)
                print("THE END, hope you had fun. ")
                exit()
        else:
            print("Invalid input. Try Again")

intro()
