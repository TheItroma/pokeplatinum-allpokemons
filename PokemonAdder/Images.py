
import os
import time

# Important variables

old_path = "..\\res\\pokemon"

female_back = "a"
female_front = "a"
male_back = "a"
male_front = "a"

# Main code
def their_political_opinion():
    was_answered = False
    for i in range(1, 6):
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
            if i <= 3:
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
        os._exit()


def opperation_keep_the_old_ones_alive(old_path, new_path):
    el_original = []
    el_gen_alpha = []
    el_copycats = []
    os.chdir(old_path)
    for name in os.listdir():
        el_original.append(name)
    os.chdir(new_path)
    for name in os.listdir():
        el_gen_alpha.append(name)
        for potential_copycateds in el_original:
            if name == potential_copycateds:
                 
                print("Die! ")


def opperation_keep_the_old_ones_dead(old_path, new_path):
    el_original = []
    el_gen_alpha = []
    el_copycats = []
    os.chdir(new_path)
    for name in os.listdir():
        el_gen_alpha.append(name)
    os.chdir(old_path)
    for name in os.listdir():
        el_original.append(name)
        for potential_copycat in el_original:
            if name == potential_copycateds:
                el_copycats.append(potential_copycateds)
            

# Start Dialogue

print("Welcome to the Setup Wizard!\n")
time.sleep(1)
print("Setup Wizard (SW for short) : Thank you for welcoming me. I am the Image Setup Wizard(64 by 64 images only (them being next to each other is accepted))!")
time.sleep(2)
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
if their_political_opinions == 2:
    opperation_keep_the_old_ones_alive(old_path, new_path)

# Functions

