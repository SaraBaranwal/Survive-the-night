import sys
inventory = []
steps = 0
MAX_STEPS = 15
print ('================================')
print ('Survive the night')
print ('================================')
print ('You wake up on a beach. You see a forest to the north and the sea behind you. You can also hear running water. The last thing you remember is being on a boat with your friends. You look around and see that the boat is gone. You are alone on the beach. \nYou look around. The island appears to be deserted.')
print ('You need to survive the nightfall by finding food, shelter and a way to stay warm during the night. The nightfall will come after 10 steps.')
input ("Lets start the game. Press Enter to continue.")
print ()
def chapter1():
    if inventory != []:
        print ('Inventory: ' + ', '.join(inventory))
    print ('You are on the beach. What do you do?')
    print ('1. Go to the forest \n2. Go to the sea \n3. Search the beach \n4. Follow the sound of running water')
    choice = input ("Enter your choice: ")
    match choice:
        case '1': take_step(); return chapter2
        case '2': take_step(); return chapter3
        case '3': take_step(); return chapter4
        case '4': take_step(); return chapter5
        case _: print ("Invalid choice. Please try again."); return chapter1

def chapter2():
    if inventory != []:
        print ('Inventory: ' + ', '.join(inventory))
    print ('You walk into the forest. The trees are blocking the little sunlight you can see.')
    if 'Torch' in inventory:
        print ('You use your torch to see better. You see a bear. You cannot continue without fighting it.')
        print ('1. Fight the bear \n2. Go back to the beach')
        choice = input ("Enter your choice: ")
        match choice:
            case '1': 
                take_step()
                if 'Knife' in inventory:
                    print ('You successfully defeated the bear using the knife. You found firewood as you continued through the forest. You go back to the beach.')
                    if 'Firewood' not in inventory:
                        inventory.append('Firewood')
                    return chapter1
                else:
                    print ('You do not have a weapon to fight the bear. You are killed by the bear. Game Over.')
                    print ('Do you wish to restart the game?')
                    choice = input ("Enter your choice (Yes/No): ")
                    if choice == 'Yes':
                        inventory.clear()
                        steps = 0
                        return chapter1
                    else:
                        sys.exit()
            case '2': take_step(); return chapter1
            case _: print ("Invalid choice. Please try again."); return chapter2    
    else: 
        print ('You get lost in the forest. Do you wish to continue?')
        print ('1. Yes \n2. No')
        choice = input ("Enter your choice: ")
        match choice:
            case '1': 
                take_step()
                print ('You continue on even though you cannot see well. You see a shadow and are attacked by a bear. You could not defend yourself. You are killed by the bear. Game Over.')
                print ('Do you wish to restart the game?')
                choice = input ("Enter your choice (Yes/No): ")
                if choice == 'Yes':
                    inventory.clear()
                    steps = 0
                    return chapter1
                else:
                    sys.exit()
            case '2': take_step(); return chapter1
            case _: print ("Invalid choice. Please try again."); return chapter2

def chapter3():
    if inventory != []:
        print ('Inventory: ' + ', '.join(inventory))
    print ('You go into the sea. It is very dark and you cannot see anything.')
    if 'Torch' in inventory:
        print ('You use your torch to see better. You see a shark. You cannot continue without trapping it.')
        print ('1. Trap the shark \n2. Go back to the beach')
        choice = input ("Enter your choice: ")
        match choice:
            case '1':
                take_step()
                if 'Fishnet' in inventory:
                    print ('You successfully trapped the shark using the fishnet. You managed to catch some fish for food. You go back to the beach.')
                    if 'Fish' not in inventory:
                        inventory.append('Fish')
                    return chapter1
                else:
                    print ('You do not have anything to trap the shark. You are killed by the shark. Game Over.')
                    print ('Do you wish to restart the game?')
                    choice = input ("Enter your choice (Yes/No): ")
                    if choice == 'Yes':
                        inventory.clear()
                        steps = 0
                        return chapter1
                    else:
                        sys.exit()
            case '2': take_step(); return chapter1
            case _: print ("Invalid choice. Please try again."); return chapter3
    else: 
        print ('You get lost in the sea. Do you wish to continue?')
        print ('1. Yes \n2. No')
        choice = input ("Enter your choice: ")
        match choice:
            case '1':
                take_step()
                print ('You continue on even though you cannot see well. You see a shadow and are attacked by a shark. You could not defend yourself. You are killed by the shark. Game Over.')
                print ('Do you wish to restart the game?')
                choice = input ("Enter your choice (Yes/No): ")
                if choice == 'Yes':
                    inventory.clear()
                    steps = 0
                    return chapter1
                else:
                    sys.exit()
            case '2': take_step(); return chapter1
            case _: print ("Invalid choice. Please try again."); return chapter3

def chapter4():
    if inventory != []:
        print ('Inventory: ' + ', '.join(inventory))
    print ('You search the beach. You find a torch, a knife and a cave you can use for shelter. You also found footsteps leading towards the river.')
    if 'Torch' not in inventory:
        inventory.append('Torch')
    if 'Knife' not in inventory:
        inventory.append('Knife')
    if 'Shelter' not in inventory:
        inventory.append('Shelter')
    print ('What do you want to do next?')
    print ('1. Go to the forest \n2. Go to the sea \n3. Follow the footsteps towards the river')
    choice = input ("Enter your choice: ")
    match choice:
        case '1': take_step(); return chapter2
        case '2': take_step(); return chapter3
        case '3': take_step(); return chapter5
        case _: print ("Invalid choice. Please try again."); return chapter4

def chapter5():
    if inventory != []:
        print ('Inventory: ' + ', '.join(inventory))
    print ('You follow the sound of running water and find a river. You can see the footsteps leading further down the river. You also see a fishnet floating on the water, tangled to a rock.')
    print ('What do you want to do next?')
    print ('1. Follow the footsteps \n2. Get the fishnet \n3. Go back to the beach')
    choice = input ("Enter your choice: ")
    match choice:
        case '1': take_step(); return chapter6
        case '2':
            print ('You see that the river is filled with Piranhas. You cannot get the fishnet without scaring the Piranhas away.')
            print ('1. Try to scare the Piranhas away \n2. Go back to the beach')
            choice = input ("Enter your choice: ")
            match choice:
                case '1':
                    take_step()
                    if 'Firewood' in inventory:
                        print ('You successfully scared the Piranhas away using your firewood. You got the fishnet.')
                        if 'Fishnet' not in inventory:
                            inventory.append('Fishnet')
                        print("What do you want to do next?")
                        print("1. Follow the footsteps \n2. Go back to the beach")
                        choice = input("Enter your choice: ")
                        match choice:
                            case '1': take_step(); return chapter6
                            case '2': take_step(); return chapter1
                            case _: print("Invalid choice. Please try again."); return chapter5
                    else:
                        print ('You do not have anything to scare the Piranhas away. You are killed by the Piranhas. Game Over.')
                        print ('Do you wish to restart the game?')
                        choice = input ("Enter your choice (Yes/No): ")
                        if choice == 'Yes':
                            inventory.clear()
                            steps = 0
                            return chapter1
                        else:
                            sys.exit()
                case '2': take_step(); return chapter1
                case _: print ("Invalid choice. Please try again."); return chapter5
        case '3': take_step(); return chapter1
        case _: print ("Invalid choice. Please try again."); return chapter5

def chapter6():
    if inventory != []:
            print ('Inventory: ' + ', '.join(inventory))
    print ('You followed the footsteps into the forest. It is very dark and you cannot see anything.')
    if 'Torch' in inventory:
        print ('You use your torch to see better. You see a bear. You cannot continue without fighting it.')
        print ('1. Fight the bear \n2. Go back to the river')
        choice = input ("Enter your choice: ")
        match choice:
            case '1':
                take_step()
                if 'Knife' in inventory:
                    print ('You successfully defeated the bear using the knife. You found firewood as you continued through the forest.')
                    if 'Firewood' not in inventory:
                        inventory.append('Firewood')
                    print ('Do you wish to continue following the footsteps or go back to the river?')
                    print ('1. Continue following the footsteps \n2. Go back to the river')
                    choice = input ("Enter your choice: ")
                    match choice:
                        case '1': take_step(); return chapter7
                        case '2': take_step(); return chapter5
                        case _: print ("Invalid choice. Please try again."); return chapter6
                else:
                    print ('You do not have a weapon to fight the bear. You are killed by the bear. Game Over.')
                    print ('Do you wish to restart the game?')
                    choice = input ("Enter your choice (Yes/No): ")
                    if choice == 'Yes':
                        inventory.clear()
                        steps = 0
                        return chapter1
                    else:
                        sys.exit()
            case '2': take_step(); return chapter5
            case _: print ("Invalid choice. Please try again."); return chapter6
    else: 
        print ('You get lost in the forest. Do you wish to continue?')
        print ('1. Yes \n2. No')
        choice = input ("Enter your choice: ")
        match choice:
            case '1': 
                take_step()
                print ('You continue on even though you cannot see well. You see a shadow and are attacked by a bear. You could not defend yourself. You are killed by the bear. Game Over.')
                print ('Do you wish to restart the game?')
                choice = input ("Enter your choice (Yes/No): ")
                if choice == 'Yes':
                    inventory.clear()
                    steps = 0
                    return chapter1
                else:
                    sys.exit()
            case '2': take_step(); return chapter5
            case _: print ("Invalid choice. Please try again."); return chapter6

def chapter7():
    if inventory != []:
        print ('Inventory: ' + ', '.join(inventory))
    print ('You continue following the footsteps and found a small village. You are safe. You survived the night. Congratulations!')
    print ('Do you wish to restart the game?')
    choice = input ("Enter your choice (Yes/No): ")
    if choice == 'Yes':
        inventory.clear()
        steps = 0
        return chapter1
    else:
        sys.exit()

def take_step():
    global steps
    steps += 1
    print(f"\nSteps: {steps}/{MAX_STEPS}")
    if steps >= MAX_STEPS:
        if 'Shelter' in inventory and 'Firewood' in inventory and 'Fish' in inventory:
            print("\nNight has fallen.")
            print("You have found food, shelter, and firewood. You survived the night. Congratulations!")
            print ('Do you wish to restart the game?')
            choice = input ("Enter your choice (Yes/No): ")
            if choice == 'Yes':
                inventory.clear()
                steps = 0
                return chapter1
            else:
                sys.exit()
        else: 
            print("\nNight has fallen.")
            print("You were unable to prepare for the night.")
            print("You died from the cold. Game Over.")
            print ('Do you wish to restart the game?')
            choice = input ("Enter your choice (Yes/No): ")
            if choice == 'Yes':
                inventory.clear()
                steps = 0
                return chapter1
            else:
                sys.exit()

current = chapter1
while current is not None:
    current = current()