
import os
import time

# Important variables

old_path = "..\res\pokemon"

# Functions

def their_political_opinion():
    was_answered = False
    for i in range(1, 7):
        side = input("Who are you going to purge then? ('the old ones'/'the copy cat younglings'/'both')\n")
        if side == "the old ones":
            was_answered = True
            time.sleep(1)
            return 1
        elif side == "the copy cat younglings":
            was_answered = True
            time.sleep(1)
            return 2
        elif side == 'both':
            was_answered = True
            time.sleep(1)
            return 3
        else:
            if i <= 4:
                print("I don't think that I heard that correctly... \n")
            elif i == 5:
                print("Now im pretty shure your just messing with me! Strike 1!\n")
            elif i == 6:
                side = input("Are you messing with me or do you just not want to kill any of them? ('I am messing with you, I just do not wish to kill them!'/'I am not messing with you, i just want you to keep them alive''the old ones'/'the younglings'/'both') : ")
                if side == "I am not messing with you, i just want you to keep them alive":
                    print("Okay, i am not here to judge.")
                    time.sleep(1)
                    return 4
    if was_answered == False:
        print("We don't want your kind here!")
        exit()


def opperation_keep_the_old_ones_alive(old_path, new_path):
    # Deletes all the newer pokemons that have the original version with them 
    el_original = []
    el_gen_alpha = []
    os.chdir(old_path)
    for name in os.listdir():
        el_original.append(name)
    os.chdir(new_path)
    for name in os.listdir():
        el_gen_alpha.append(name)
        for potential_copycateds in el_original:
            if name == potential_copycateds:
                el_gen_alpha.remove(name)
                os.rmdir(name)
                print("Die! ")
    return el_gen_alpha
    # Takes care of every mention of the pokemons in the code


def opperation_keep_the_old_ones_dead(old_path, new_path):
    # Deletes all the original pokemons that have a newer version
    el_original = []
    el_gen_alpha = []
    os.chdir(new_path)
    for name in os.listdir():
        el_gen_alpha.append(name)
    os.chdir(old_path)
    for name in os.listdir():
        el_original.append(name)
        for potential_copycat in el_original:
            if name == potential_copycateds:
                el_copycats.append(potential_copycateds)
    # Takes care of every mention of the pokemons in the code

def god_is_dead(old_path, new_path):
    # Deletes all of them!
    all = []
    os.chdir(new_path)
    for name in os.listdir():
        os.rmdir(name)
        all.append(name)
    os.chdir(old_path)
    for name in os.listdir():
        os.rmdir(name)
        all.append(name)
    # Takes care of every mention of the pokemons in the code

def rainbow(old_path, new_path):
    # Lists all of them
    all = []
    os.chdir(new_path)
    for name in os.listdir():
        all.append(name)
    os.chdir(old_path)
    for name in os.listdir():
        all.append(name)
    return all
    # Takes care of every mention of the pokemons in the code

            
# Main code

# Start Dialogue

print("Welcome to the Setup Wizard!\n")
time.sleep(1)
print("Pyromaniac Setup Wizard (PSW for short) : Thank you for welcoming me. I am the pyromaniac setup wizard")
input("So... You wanna make up a pertext to commit genocide on weird digital creatures huuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu? (Y/N) : ")
print("That was a rethorical question... Of course you do!")
time.sleep(1)

new_path = "0"
ans = True
while ans:
    new_path = input("What is the path to the new peoples vilage? : ")
    if os.path.isdir(new_path):
        ans = False

# The pokemons they will keep

their_political_opinions = their_political_opinion()
if their_political_opinions == 1:
    opperation_keep_the_old_ones_dead(old_path, new_path)
if their_political_opinions == 2:
    opperation_keep_the_old_ones_alive(old_path, new_path)
if their_political_opinions == 3:
    god_is_dead(old_path, new_path)
if their_political_opinions == 4:
    print(rainbow(old_path, new_path))