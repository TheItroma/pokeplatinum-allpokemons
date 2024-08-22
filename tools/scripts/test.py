import os

mew_path = os.getcwd() + ".."

el_new = 0
os.chdir(mew_path)
mew_path = os.getcwd() + "\\PokemonAdder\\pokemon"
os.chdir(mew_path)
for name in os.listdir():
    el_new += 1

NUM_POKEMON = 494 + el_new