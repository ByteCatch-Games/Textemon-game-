import time
import random2

# intro message & disclaimer
print('In a land far far away...')
print("is the land of Textemon. A world were text based monsters roamed.")
print('This idea and all names are from the Nintendo company and Game Freak.')
print("Pokémon is a trademark of Nintendo. This project is not affiliated with or endorsed by Nintendo.")
print("Copyright © ByteCatch Games 2023")
print(
    "All rights reserved. This project and its contents are protected by copyright law. No part of this project may be reproduced, distributed, or transmitted in any form or by any means, without the prior written permission of the copyright owner.")
print("\n\n\n\n")
time.sleep(5)


# core engine
class Pokemon:
    def __init__(self, name, element, max_hp, max_energy, ):
        self.name = name
        self.element = element
        self.max_hp = max_hp
        self.hp = max_hp
        self.max_energy = max_energy
        self.energy = max_energy
        self.offensive_moves1 = []
        self.offensive_moves2 = []
        self.offensive_moves3 = []
        self.defensive_moves1 = []
        self.defensive_moves2 = []

    # noinspection PyArgumentList
    def add_offensive_move1(self, move_name, damage, damage2):
        # Add an offensive move to the list of moves
        self.offensive_moves1.append([move_name, damage, damage2, self.energy])

    def add_offensive_move2(self, move_name, damage, damage2):
        # Add an offensive move to the list of moves
        self.offensive_moves2.append([move_name, damage, damage2, self.energy])

    def add_offensive_move3(self, move_name, damage, damage2):
        # Add an offensive move to the list of moves
        self.offensive_moves3.append([move_name, damage, damage2, self.energy])

    def add_defensive_move1(self, move_name, reduce_damage, heal, ):
        # Add a defensive move to the list of moves
        self.defensive_moves1.append([move_name, reduce_damage, heal])

    def add_defensive_move2(self, move_name, reduce_damage, heal, ):
        # Add a defensive move to the list of moves
        self.defensive_moves2.append([move_name, reduce_damage, heal])


# create a Pikachu instance with moves
pikachu = Pokemon("Pikachu", ["Electric"], 400, 70, )
pikachu.add_offensive_move1("Thunderbolt", 35, 35, )
pikachu.add_offensive_move2("Iron Tail", 20, 20, )
pikachu.add_offensive_move3("Quick Attack", 15, 15, )
pikachu.add_defensive_move1("Agility", 0.5, 0, )
pikachu.add_defensive_move2("Double Team", 0.3, 0, )

# create a Charizard instance with moves
charizard = Pokemon("Charizard", ["Fire", "Flying"], 520, 40, )
charizard.add_offensive_move1("Flamethrower", 30, 30, )
charizard.add_offensive_move2("Dragon Claw", 25, 25, )
charizard.add_offensive_move3("Air Slash", 20, 20, )
charizard.add_defensive_move1("Dragon Dance", 0.5, 0, )
charizard.add_defensive_move2("Roost", 0, 60, )

# create a Blastoise instance with moves
blastoise = Pokemon("Blastoise", ["Water"], 520, 40, )
blastoise.add_offensive_move1("Hydro Pump", 30, 30, )
blastoise.add_offensive_move2("Ice Beam", 25, 25, )
blastoise.add_offensive_move3("Earthquake", 20, 20, )
blastoise.add_defensive_move1("Protect", 0.7, 0, )
blastoise.add_defensive_move2("Withdraw", 0, 40, )

# create a Venusaur instance with moves
venusaur = Pokemon("Venusaur", ["Grass", "Poison"], 520, 40, )
venusaur.add_offensive_move1("Solar Beam", 30, 30, )
venusaur.add_offensive_move2("Sludge Bomb", 25, 25, )
venusaur.add_offensive_move3("Earthquake", 20, 20, )
venusaur.add_defensive_move1("Leech Seed", 0.4, 10, )
venusaur.add_defensive_move2("Sleep Powder", 0.3, 0, )

# create a Lycanroc instance with moves
lycanroc = Pokemon("Lycanroc", ["Rock"], 480, 45, )
lycanroc.add_offensive_move1("Stone Edge", 35, 35, )
lycanroc.add_offensive_move2("Accelerock", 25, 25, )
lycanroc.add_offensive_move3("Crunch", 20, 20, )
lycanroc.add_defensive_move1("Swords Dance", 0.5, 0, )
lycanroc.add_defensive_move2("Stealth Rock", 0.3, 0, )

# create a Beedrill instance with types Bug and Poison
beedrill = Pokemon("Beedrill", ["Bug", "Poison"], 400, 70, )
beedrill.add_offensive_move1("Twineedle", 30, 30, )
beedrill.add_offensive_move2("Poison Jab", 20, 20, )
beedrill.add_offensive_move3("U-turn", 30, 30, )
beedrill.add_defensive_move1("Harden", 0.5, 0, )
beedrill.add_defensive_move2("Protect", 0.3, 0, )

# create a Crobat instance with types Poison and Flying
crobat = Pokemon("Crobat", ["Poison", "Flying"], 400, 70, )
crobat.add_offensive_move1("Cross Poison", 30, 30, )
crobat.add_offensive_move2("Air Slash", 25, 25, )
crobat.add_offensive_move3("Brave Bird", 40, 40, )
crobat.add_defensive_move1("Roost", 0, 60, )
crobat.add_defensive_move2("Toxic", 0.4, 10, )

# create a Gengar instance with types Ghost and Poison
gengar = Pokemon("Gengar", ["Ghost", "Poison"], 440, 60, )
gengar.add_offensive_move1("Shadow Ball", 30, 30, )
gengar.add_offensive_move2("Sludge Bomb", 25, 25, )
gengar.add_offensive_move3("Venom Drench", 20, 20, )
gengar.add_defensive_move1("Hypnosis", 0.5, 0, )
gengar.add_defensive_move2("Destiny Bond", 0.3, 10, )

# create a Metagross instance with types Steel and Psychic
metagross = Pokemon("Metagross", ["Steel", "Psychic"], 520, 35, )
metagross.add_offensive_move1("Meteor Mash", 35, 35, )
metagross.add_offensive_move2("Zen Headbutt", 25, 25, )
metagross.add_offensive_move3("Zen Headbutt", 40, 40, )
metagross.add_defensive_move1("Agility", 0.5, 0, )
metagross.add_defensive_move2("Light Screen", 0.3, 10)

# create a Noivern instance with types Flying and Dragon
noivern = Pokemon("Noivern", ["Flying", "Dragon"], 480, 50, )
noivern.add_offensive_move1("Dragon Pulse", 30, 30, )
noivern.add_offensive_move2("Air Slash", 25, 25, )
noivern.add_offensive_move3("Hurricane", 35, 35, )
noivern.add_defensive_move1("Roost", 0, 60, )
noivern.add_defensive_move2("U-turn", 0.4, 0, )

# create a Garchomp instance with types Dragon and Ground
garchomp = Pokemon("Garchomp", ["Dragon", "Ground"], 560, 30.)
garchomp.add_offensive_move1("Dragon Claw", 35, 35, )
garchomp.add_offensive_move2("Earthquake", 30, 30, )
garchomp.add_offensive_move3("Stone Edge", 40, 40, )
garchomp.add_defensive_move1("Swords Dance", 0.5, 0, )
garchomp.add_defensive_move2("Sandstorm", 0.3, 5, )

# create a Krookodile instance with types Ground and Dark
krookodile = Pokemon("Krookodile", ["Ground", "Dark"], 440, 45, )
krookodile.add_offensive_move1("Earthquake", 30, 30, )
krookodile.add_offensive_move2("Stone Edge", 40, 40, )
krookodile.add_offensive_move3("Crunch", 35, 35, )
krookodile.add_defensive_move1("Sandstorm", 0.3, 5, )
krookodile.add_defensive_move2("Swagger", 0.3, 7, )

# Create a Tyranitar instance
tyranitar = Pokemon("Tyranitar", ["Dark", "Rock"], 480, 30, )
tyranitar.add_offensive_move1("Crunch", 25, 25, )
tyranitar.add_offensive_move2("Stone Edge", 30, 30, )
tyranitar.add_offensive_move3("Earthquake", 35, 35, )
tyranitar.add_defensive_move1("Protect", 0.7, 0, )
tyranitar.add_defensive_move2("Sandstorm", 0.3, 5, )

# Create a Machamp instance
machamp = Pokemon("Machamp", ["Fighting"], 440, 45, )
machamp.add_offensive_move1("Cross Chop", 25, 25, )
machamp.add_offensive_move2("Submission", 30, 30, )
machamp.add_offensive_move3("Dynamic Punch", 35, 35, )
machamp.add_defensive_move1("Bulk Up", 0.5, 5, )
machamp.add_defensive_move2("Detect", 0.75, 0, )

# Create a Gardevoir instance
gardevoir = Pokemon("Gardevoir", ["Psychic", "Fairy"], 400, 60, )
gardevoir.add_offensive_move1("Psychic", 25, 25, )
gardevoir.add_offensive_move2("Moonblast", 30, 30, )
gardevoir.add_offensive_move3("Dazzling Gleam", 20, 20, )
gardevoir.add_defensive_move1("Calm Mind", 0.5, 0, )
gardevoir.add_defensive_move2("Will-O-Wisp", 0.25, 5, )

# Create a Mimikyu instance
mimikyu = Pokemon("Mimikyu", ["Ghost", "Fairy"], 360, 70, )
mimikyu.add_offensive_move1("Shadow Claw", 25, 25, )
mimikyu.add_offensive_move2("Play Rough", 30, 30, )
mimikyu.add_offensive_move3("Phantom Force", 35, 35, )
mimikyu.add_defensive_move1("Protect", 0.5, 0, )
mimikyu.add_defensive_move2("Substitute", 1, -25, )

# Create a Silvally instance
silvally = Pokemon("Silvally", ["Normal"], 480, 45, )
silvally.add_offensive_move1("Multi-Attack", 35, 35, )
silvally.add_offensive_move2("Crunch", 25, 25, )
silvally.add_offensive_move3("X-Scissor", 30, 30, )
silvally.add_defensive_move1("Iron Defense", 0.5, 0, )
silvally.add_defensive_move2("Roar", 0.25, 0, )

# Create a Cryogonal instance
cryogonal = Pokemon("Cryogonal", ["Ice"], 400, 60, )
cryogonal.add_offensive_move1("Ice Beam", 25, 25, )
cryogonal.add_offensive_move2("Blizzard", 35, 35, )
cryogonal.add_offensive_move3("Freeze-Dry", 35, 35, )
cryogonal.add_defensive_move1("Reflect", 0.5, 0, )
cryogonal.add_defensive_move2("Light Screen", 0.5, 0, )

print("Available Pokemons:")
print("""Example: 
pokemon name, pokemon type
Offensive moves: ['Thunderbolt', 'Iron Tail', 'Quick Attack']
Defensive moves: ['Agility', 'Double Team']""")
print()
for pokemon in [pikachu, charizard, blastoise, venusaur, lycanroc, beedrill, crobat, gengar, metagross, noivern,
                garchomp, krookodile, tyranitar, machamp, gardevoir, mimikyu, silvally, cryogonal]:
    print(f"{pokemon.name},hp:{pokemon.hp},energy:{pokemon.energy},type:{pokemon.element}")
    print(
        f"  Offensive moves: {pokemon.offensive_moves1[0][0]},{pokemon.offensive_moves2[0][0]},{pokemon.offensive_moves3[0][0]}")
    print(f"  Defensive moves: {pokemon.defensive_moves1[0][0]},{pokemon.defensive_moves2[0][0]}\n")
    time.sleep(1)
elemental_chart = {}

types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic",
         "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]

for t in types:
    weaknesses = []
    strengths = []

    if t == "Normal":
        weaknesses = ["Fighting"]

    elif t == "Fire":
        weaknesses = ["Water", "Ground", "Rock"]
        strengths = ["Grass", "Ice", "Bug", "Steel"]

    elif t == "Water":
        weaknesses = ["Grass", "Electric"]
        strengths = ["Fire", "Ground", "Rock"]

    elif t == "Electric":
        weaknesses = ["Ground"]
        strengths = ["Water", "Flying"]

    elif t == "Grass":
        weaknesses = ["Fire", "Ice", "Poison", "Flying", "Bug"]
        strengths = ["Water", "Ground", "Rock"]

    elif t == "Ice":
        weaknesses = ["Fire", "Fighting", "Rock", "Steel"]
        strengths = ["Grass", "Ground", "Flying", "Dragon"]

    elif t == "Fighting":
        weaknesses = ["Flying", "Psychic", "Fairy"]
        strengths = ["Normal", "Ice", "Rock", "Dark", "Steel"]

    elif t == "Poison":
        weaknesses = ["Ground", "Psychic"]
        strengths = ["Grass", "Fairy"]

    elif t == "Ground":
        weaknesses = ["Water", "Grass", "Ice"]
        strengths = ["Fire", "Electric", "Poison", "Rock", "Steel"]

    elif t == "Flying":
        weaknesses = ["Electric", "Ice", "Rock"]
        strengths = ["Grass", "Fighting", "Bug"]

    elif t == "Psychic":
        weaknesses = ["Bug", "Ghost", "Dark"]
        strengths = ["Fighting", "Poison"]

    elif t == "Bug":
        weaknesses = ["Fire", "Flying", "Rock"]
        strengths = ["Grass", "Psychic", "Dark"]

    elif t == "Rock":
        weaknesses = ["Water", "Grass", "Fighting", "Ground", "Steel"]
        strengths = ["Fire", "Ice", "Flying", "Bug"]

    elif t == "Ghost":
        weaknesses = ["Ghost", "Dark"]
        strengths = ["Psychic", "Ghost"]

    elif t == "Dragon":
        weaknesses = ["Ice", "Dragon", "Fairy"]
        strengths = ["Dragon"]

    elif t == "Dark":
        weaknesses = ["Fighting", "Bug", "Fairy"]
        strengths = ["Psychic", "Ghost"]

    elif t == "Steel":
        weaknesses = ["Fire", "Fighting", "Ground"]
        strengths = ["Ice", "Rock", "Fairy"]

    elif t == "Fairy":
        weaknesses = ["Poison", "Steel"]
        strengths = ["Fighting", "Dragon", "Dark"]

    elemental_chart[t] = {
        "weaknesses": weaknesses,
        "strengths": strengths
    }

# pokemon picking
chosen_one = input("Which pokemon would you want to have?")
if chosen_one == "Pikachu" or chosen_one == "pikachu":
    chosen_one = pikachu
elif chosen_one == "Charizard" or chosen_one == "charizard":
    chosen_one = charizard
elif chosen_one == "Blastoise" or chosen_one == "blastoise":
    chosen_one = blastoise
elif chosen_one == "Venusaur" or chosen_one == "venusaur":
    chosen_one = venusaur
elif chosen_one == "Lycanroc" or chosen_one == "lycanroc":
    chosen_one = lycanroc
elif chosen_one == "Beedrill" or chosen_one == "beedrill":
    chosen_one = beedrill
elif chosen_one == "Crobat" or chosen_one == "crobat":
    chosen_one = crobat
elif chosen_one == "Gengar" or chosen_one == "gengar":
    chosen_one = gengar
elif chosen_one == "Metagross" or chosen_one == "metagross":
    chosen_one = metagross
elif chosen_one == "Garchomp" or chosen_one == "garchomp":
    chosen_one = garchomp
elif chosen_one == "Krookodile" or chosen_one == "krookodile":
    chosen_one = krookodile
elif chosen_one == "Cryogonal" or chosen_one == "cryogonal":
    chosen_one = cryogonal
elif chosen_one == "Tyranitar" or chosen_one == "tyranitar":
    chosen_one = tyranitar
elif chosen_one == "Machamp" or chosen_one == "machamp":
    chosen_one = machamp
elif chosen_one == "noivern" or chosen_one == "Noivern":
    chosen_one = noivern
elif chosen_one == "Gardevoir" or chosen_one == "gardevoir":
    chosen_one = gardevoir
elif chosen_one == "Mimikyu" or chosen_one == "mimikyu":
    chosen_one = mimikyu
else:
    chosen_one = silvally
# pokemon check
print()
print(" {}: {}".format(chosen_one.name, chosen_one.element))

# weakness and strength of chosen one
chosen_one_weakness = []
chosen_one_strength = []
for i in range(len(chosen_one.element)):
    chosen_one_type_chart = elemental_chart[chosen_one.element[i]]
    chosen_one_weakness += [chosen_one_type_chart["weaknesses"]]
    chosen_one_strength += [chosen_one_type_chart["strengths"]]

# AI pokemon
pokemons = [pikachu, charizard, blastoise, venusaur, lycanroc, beedrill, crobat, gengar, noivern, metagross, garchomp,
            krookodile, tyranitar, machamp, gardevoir, mimikyu, silvally, cryogonal]
random_pokemon = pokemons[random2.randint(0, 17)]
print("The AI has selected", random_pokemon.name)

# weakness and strength of chosen one
random_pokemon_weakness = []
random_pokemon_strength = []
for i in range(len(random_pokemon.element)):
    random_pokemon_type_chart = elemental_chart[random_pokemon.element[i]]
    random_pokemon_weakness += [random_pokemon_type_chart["weaknesses"]]
    random_pokemon_strength += [random_pokemon_type_chart["strengths"]]

# type effectiveness
damage_multiplier = 1
for i in range(len(chosen_one_weakness)):
    for n in range(len(random_pokemon.element)):
        if random_pokemon.element[n] in chosen_one_weakness[i]:
            damage_multiplier = damage_multiplier * 2

for i in range(len(chosen_one_strength)):
    for n in range(len(random_pokemon.element)):
        if random_pokemon.element[n] in chosen_one_strength[i]:
            damage_multiplier = damage_multiplier * 0.5
random_pokemon_damage = damage_multiplier
damage_multiplier = 1
for i in range(len(random_pokemon_weakness)):
    for n in range(len(chosen_one.element)):
        if chosen_one.element[n] in random_pokemon_weakness[i]:
            damage_multiplier = damage_multiplier * 2

for i in range(len(random_pokemon_strength)):
    for n in range(len(chosen_one.element)):
        if chosen_one.element[n] in random_pokemon_strength[i]:
            damage_multiplier = damage_multiplier * 0.5
chosen_one_damage = damage_multiplier
# Who starts first code
user_choice = input("Pick heads or tails: ")
if user_choice == "head" or user_choice == "heads" or user_choice == "Head" or user_choice == "Heads":
    user_choice = "heads"
elif user_choice == "tails" or user_choice == "tail" or user_choice == "Tail" or user_choice == "Tails":
    user_choice = "tails"
coin = ["", "heads", "tails"]
flip = coin[random2.randint(1, 2)]
print()
print("The coin landed on ", flip, "!")
if user_choice == flip:
    print("You start first!")
    start = 1
else:
    print("Your opponent starts first!")
    start = 2
print()

# Battle part
round1 = 0
round2 = 0
round4 = 0
round5 = 0
chosen_one.hp = int(chosen_one.hp)
random_pokemon.hp = int(random_pokemon.hp)
while chosen_one.hp > 0 and random_pokemon.hp > 0:
    if start == 1:
        round3 = round1 - round2
        if round3 == 2:
            # prevents the defensive moves from being too OP
            (random_pokemon.offensive_moves1[0])[1] = (random_pokemon.offensive_moves1[0])[2]
            (random_pokemon.offensive_moves2[0])[1] = (random_pokemon.offensive_moves2[0])[2]
            (random_pokemon.offensive_moves3[0])[1] = (random_pokemon.offensive_moves3[0])[2]
        if chosen_one.energy <= 0:
            print(f"""{chosen_one.name}   hp:{chosen_one.hp}   energy:{chosen_one.energy}
{random_pokemon.name}   hp:{random_pokemon.hp}   energy:{random_pokemon.energy}""")
            print(f"""{chosen_one.name} has no more energy
{chosen_one.name} used struggle""")
            chosen_one.hp = 3 / 4 * chosen_one.hp
            random_pokemon.hp = random_pokemon.hp - ((chosen_one.offensive_moves1[0][1] +
                                                      chosen_one.offensive_moves2[0][1] +
                                                      chosen_one.offensive_moves3[0][1]) / 3)
        # Player's turn
        elif chosen_one.energy > 0:
            print(f"""{chosen_one.name}   hp:{chosen_one.hp}   energy:{chosen_one.energy}
{random_pokemon.name}   hp:{random_pokemon.hp}   energy:{random_pokemon.energy}
{chosen_one.name}'s moves:
Offensive moves: {chosen_one.offensive_moves1[0][0]}(uses 1 energy),{chosen_one.offensive_moves2[0][0]}(uses 1 energy),{chosen_one.offensive_moves3[0][0]}(uses 1 energy)
Defensive moves: {chosen_one.defensive_moves1[0][0]}(uses 3 energy),{chosen_one.defensive_moves2[0][0]}(uses 3 energy)""")

            choice = int(input(
                "What is your move? Note:Do your moves in order from 1 to 5. 1 being the first offensive move and 5 being the last defensive move."))
            if choice == 1:
                random_pokemon.hp = random_pokemon.hp - ((chosen_one.offensive_moves1[0][1]) * chosen_one_damage)
                chosen_one.energy = chosen_one.energy - 1
                print(f"{chosen_one.name} used {chosen_one.offensive_moves1[0][0]}")
            elif choice == 2:
                random_pokemon.hp = random_pokemon.hp - ((chosen_one.offensive_moves2[0][1]) * chosen_one_damage)
                chosen_one.energy = chosen_one.energy - 1
                print(f"{chosen_one.name} used {chosen_one.offensive_moves2[0][0]}")
            elif choice == 3:
                random_pokemon.hp = random_pokemon.hp - ((chosen_one.offensive_moves3[0][1]) * chosen_one_damage)
                chosen_one.energy = chosen_one.energy - 1
                print(f"{chosen_one.name} used {chosen_one.offensive_moves3[0][0]}")
            elif choice == 4:
                random_pokemon.offensive_moves1[0][1] = (1 - chosen_one.defensive_moves1[0][1]) * \
                                                        random_pokemon.offensive_moves1[0][1]
                random_pokemon.offensive_moves2[0][1] = (1 - chosen_one.defensive_moves1[0][1]) * \
                                                        random_pokemon.offensive_moves2[0][1]
                random_pokemon.offensive_moves3[0][1] = (1 - chosen_one.defensive_moves1[0][1]) * \
                                                        random_pokemon.offensive_moves3[0][1]
                chosen_one_hp = chosen_one.hp
                chosen_one.hp = (chosen_one.defensive_moves1[0][2] / 100 * chosen_one.hp) + chosen_one.hp
                if chosen_one.hp > chosen_one.max_hp:
                    chosen_one.hp = chosen_one.hp - (chosen_one.max_hp - chosen_one.hp)
                    chosen_one.energy = chosen_one.energy - 3
                print(f"{chosen_one.name} used {chosen_one.defensive_moves1[0][0]}")
                if random_pokemon.offensive_moves1[0][1] < random_pokemon.offensive_moves1[0][2] and \
                        random_pokemon.offensive_moves2[0][1] < random_pokemon.offensive_moves2[0][2] and \
                        random_pokemon.offensive_moves3[0][1] < random_pokemon.offensive_moves3[0][2]:
                    print(f"{chosen_one.name}'s defence increased")
                if chosen_one.hp > chosen_one_hp:
                    print(f"{chosen_one.name}'s hp increased")
                round1 = round2
            else:
                random_pokemon.offensive_moves1[0][1] = (1 - chosen_one.defensive_moves2[0][1]) * \
                                                        random_pokemon.offensive_moves1[0][1]
                random_pokemon.offensive_moves2[0][1] = (1 - chosen_one.defensive_moves2[0][1]) * \
                                                        random_pokemon.offensive_moves2[0][1]
                random_pokemon.offensive_moves3[0][1] = (1 - chosen_one.defensive_moves2[0][1]) * \
                                                        random_pokemon.offensive_moves3[0][1]
                chosen_one_hp = chosen_one.hp
                chosen_one.hp = (chosen_one.defensive_moves2[0][2] / 100 * chosen_one.hp) + chosen_one.hp
                if chosen_one.hp > chosen_one.max_hp:
                    chosen_one.hp = chosen_one.hp - (chosen_one.max_hp - chosen_one.hp)
                    chosen_one.energy = chosen_one.energy - 3
                    print(f"{chosen_one.name} used {chosen_one.defensive_moves2[0][0]}")
                if random_pokemon.offensive_moves1[0][1] < random_pokemon.offensive_moves1[0][2] and \
                        random_pokemon.offensive_moves2[0][1] < random_pokemon.offensive_moves2[0][2] and \
                        random_pokemon.offensive_moves3[0][1] < random_pokemon.offensive_moves3[0][2]:
                    print(f"{chosen_one.name}'s defence increased")
                if chosen_one.hp > chosen_one_hp:
                    print(f"{chosen_one.name}'s hp increased")
                round1 = round2
        round1 += 1
        round4 += 1
        print(f"""{chosen_one.name}   hp:{chosen_one.hp}   energy:{chosen_one.energy}
{random_pokemon.name}   hp:{random_pokemon.hp}   energy:{random_pokemon.energy}""")

        # AI's turn
        round6 = round4 - round5
        if round6 == 2:
            chosen_one.offensive_moves1[0][1] = chosen_one.offensive_moves1[0][2]
            chosen_one.offensive_moves2[0][1] = chosen_one.offensive_moves2[0][2]
            chosen_one.offensive_moves3[0][1] = chosen_one.offensive_moves3[0][2]
        if random_pokemon.energy <= 0:
            print(f"{random_pokemon.name} used struggle")
            random_pokemon.hp = 3 / 4 * random_pokemon.hp
            chosen_one.hp = chosen_one.hp - ((random_pokemon.offensive_moves1[0][1] +
                                              random_pokemon.offensive_moves2[0][1] +
                                              random_pokemon.offensive_moves3[0][1]) / 3)
        elif random_pokemon.energy >= 0:
            if random_pokemon.hp <= random_pokemon.max_hp / 4:
                if random_pokemon.defensive_moves1[0][2] > 0:
                    random_pokemon.hp = random_pokemon.hp
                    random_pokemon.defensive_moves1[0][2] = (random_pokemon.defensive_moves1[0][
                                                                 2] / 100 * random_pokemon.hp) + random_pokemon.hp
                    chosen_one.offensive_moves1[0][1] = (1 - random_pokemon.defensive_moves1[0][1]) * \
                                                        chosen_one.offensive_moves1[0][1]
                    chosen_one.offensive_moves2[0][1] = (1 - random_pokemon.defensive_moves1[0][1]) * \
                                                        chosen_one.offensive_moves2[0][1]
                    chosen_one.offensive_moves3[0][1] = (1 - random_pokemon.defensive_moves1[0][1]) * \
                                                        chosen_one.offensive_moves3[0][1]
                    print(f"{random_pokemon.name} used {random_pokemon.defensive_moves1[0][0]}")
                    if random_pokemon.hp > random_pokemon.max_hp:
                        random_pokemon.hp = random_pokemon.max_hp
                    if random_pokemon.hp < random_pokemon.hp:
                        print(f"{random_pokemon.name} healed")
                    if chosen_one.offensive_moves3[0][2] > chosen_one.offensive_moves3[0][1]:
                        print(f"{random_pokemon.name}'s defence increased")
                    random_pokemon.energy -= 3
                    round4 = round5
                elif random_pokemon.defensive_moves2[0][2] > 0:
                    random_pokemon_hp = random_pokemon.hp
                    random_pokemon.defensive_moves1[0][2] = (random_pokemon.defensive_moves2[0][
                                                                 2] / 100 * random_pokemon.hp) + random_pokemon.hp
                    chosen_one.offensive_moves1[0][1] = (1 - random_pokemon.defensive_moves2[0][1]) * \
                                                        chosen_one.offensive_moves1[0][1]
                    chosen_one.offensive_moves2[0][1] = (1 - random_pokemon.defensive_moves2[0][1]) * \
                                                        chosen_one.offensive_moves2[0][1]
                    chosen_one.offensive_moves3[0][1] = (1 - random_pokemon.defensive_moves2[0][1]) * \
                                                        chosen_one.offensive_moves3[0][1]
                    print(f"{random_pokemon.name} used {random_pokemon.defensive_moves2[0][0]}")
                    if random_pokemon.hp > random_pokemon.max_hp:
                        random_pokemon.hp = random_pokemon.max_hp
                    if random_pokemon_hp < random_pokemon.hp:
                        print(f"{random_pokemon.name} healed")
                    if chosen_one.offensive_moves3[0][2] > chosen_one.offensive_moves3[0][1]:
                        print(f"{random_pokemon.name}'s defence increased")
                    random_pokemon.energy -= 3
                    round4 = round5
                else:
                    AI_choice = random2.randint(1, 3)
                    if AI_choice == 1:
                        chosen_one.hp = chosen_one.hp - (random_pokemon.offensive_moves1[0][1] * random_pokemon_damage)
                        random_pokemon.energy -= 1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                    elif AI_choice == 2:
                        chosen_one.hp = chosen_one.hp - (random_pokemon.offensive_moves2[0][1] * random_pokemon_damage)
                        random_pokemon.energy -= 1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                    else:
                        chosen_one.hp = chosen_one.hp - (random_pokemon.offensive_moves3[0][1] * random_pokemon_damage)
                        random_pokemon.energy -= 1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
            elif random_pokemon.hp <= random_pokemon.max_hp / 2:
                if round3 >= 2:
                    if random_pokemon.defensive_moves1[0][1] > 0:
                        chosen_one.offensive_moves1[0][1] = (1 - random_pokemon.defensive_moves1[0][1]) * \
                                                            chosen_one.offensive_moves1[0][1]
                        chosen_one.offensive_moves2[0][1] = (1 - random_pokemon.defensive_moves1[0][1]) * \
                                                            chosen_one.offensive_moves2[0][1]
                        chosen_one.offensive_moves3[0][1] = (1 - random_pokemon.defensive_moves1[0][1]) * \
                                                            chosen_one.offensive_moves3[0][1]
                        random_pokemon.defensive_moves1[0][2] = (chosen_one.defensive_moves1[0][
                                                                     2] / 100 * random_pokemon.hp) + random_pokemon.hp
                        print(f"{random_pokemon.name} used {random_pokemon.defensive_moves1[0]}")
                        if random_pokemon.hp > random_pokemon.max_hp:
                            random_pokemon.hp = random_pokemon.max_hp
                        if random_pokemon.hp < random_pokemon.hp:
                            print(f"{random_pokemon.name} healed")
                        if chosen_one.offensive_moves3[0][2] > chosen_one.offensive_moves3[0][1]:
                            print(f"{random_pokemon.name}'s defence increased")
                        random_pokemon.energy -= 3
                        round4 = round5
                    elif random_pokemon.defensive_moves2[0][1] > 0:
                        chosen_one.offensive_moves1[0][1] = (1 - random_pokemon.defensive_moves2[0][1]) * \
                                                            chosen_one.offensive_moves1[0][1]
                        chosen_one.offensive_moves2[0][1] = (1 - random_pokemon.defensive_moves2[0][1]) * \
                                                            chosen_one.offensive_moves2[0][1]
                        chosen_one.offensive_moves3[0][1] = (1 - random_pokemon.defensive_moves2[0][1]) * \
                                                            chosen_one.offensive_moves3[0][1]
                        random_pokemon.defensive_moves1[0][2] = (chosen_one.defensive_moves1[0][
                                                                     2] / 100 * random_pokemon.hp) + random_pokemon.hp
                        print(f"{random_pokemon.name} used {random_pokemon.defensive_moves1[0]}")
                        if random_pokemon.hp > random_pokemon.max_hp:
                            random_pokemon.hp = random_pokemon.max_hp
                        if random_pokemon.hp < random_pokemon.hp:
                            print(f"{random_pokemon.name} healed")
                        if chosen_one.offensive_moves3[0][2] > chosen_one.offensive_moves3[0][1]:
                            print(f"{random_pokemon.name}'s defence increased")
                        random_pokemon.energy -= 3
                        round4 = round5
                else:
                    AI_choice = random2.randint(1, 3)
                    if AI_choice == 1:
                        chosen_one.hp = chosen_one.hp - (random_pokemon.offensive_moves1[0][1] * random_pokemon_damage)
                        random_pokemon.energy -= 1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                    elif AI_choice == 2:
                        chosen_one.hp = chosen_one.hp - (random_pokemon.offensive_moves2[0][1] * random_pokemon_damage)
                        random_pokemon.energy -= 1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                    else:
                        chosen_one.hp = chosen_one.hp - (random_pokemon.offensive_moves3[0][1] * random_pokemon_damage)
                        random_pokemon.energy -= 1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
            else:
                AI_choice = random2.randint(1, 3)
                if AI_choice == 1:
                    chosen_one.hp = chosen_one.hp - (random_pokemon.offensive_moves1[0][1] * random_pokemon_damage)
                    random_pokemon.energy -= 1
                    print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                elif AI_choice == 2:
                    chosen_one.hp = chosen_one.hp - (random_pokemon.offensive_moves2[0][1] * random_pokemon_damage)
                    random_pokemon.energy -= 1
                    print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                else:
                    chosen_one.hp = chosen_one.hp - (random_pokemon.offensive_moves3[0][1] * random_pokemon_damage)
                    random_pokemon.energy -= 1
                    print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
        round1 += 1
        round2 += 1
        round4 += 1
        round5 += 1

    if start == 2:
        # AI's turn
        print(f"""{chosen_one.name}   hp:{chosen_one.hp}   energy:{chosen_one.energy}
{random_pokemon.name}   hp:{random_pokemon.hp}   energy:{random_pokemon.energy}""")
        round6 = round4 - round5
        if round6 == 2:
            chosen_one.offensive_moves1[0][1] = chosen_one.offensive_moves1[0][2]
            chosen_one.offensive_moves2[0][1] = chosen_one.offensive_moves2[0][2]
            chosen_one.offensive_moves3[0][1] = chosen_one.offensive_moves3[0][2]
        if random_pokemon.energy <= 0:
            print(f"{random_pokemon.name} used struggle")
            random_pokemon.hp = 3 / 4 * random_pokemon.hp
            chosen_one.hp = chosen_one.hp - ((random_pokemon.offensive_moves1[0][1] +
                                              random_pokemon.offensive_moves2[0][1] +
                                              random_pokemon.offensive_moves3[0][1]) / 3)
        elif random_pokemon.energy >= 0:
            if random_pokemon.hp <= random_pokemon.max_hp / 4:
                if random_pokemon.defensive_moves1[0][2] > 0:
                    random_pokemon.defensive_moves1[0][2] = (random_pokemon.defensive_moves1[0][
                                                                 2] / 100 * random_pokemon.hp) + random_pokemon.hp
                    chosen_one.offensive_moves1[0][1] = (1 - random_pokemon.defensive_moves1[0][1]) * \
                                                        chosen_one.offensive_moves1[0][1]
                    chosen_one.offensive_moves2[0][1] = (1 - random_pokemon.defensive_moves1[0][1]) * \
                                                        chosen_one.offensive_moves2[0][1]
                    chosen_one.offensive_moves3[0][1] = (1 - random_pokemon.defensive_moves1[0][1]) * \
                                                        chosen_one.offensive_moves3[0][1]
                    print(f"{random_pokemon.name} used {random_pokemon.defensive_moves1[0][0]}")
                    if random_pokemon.hp > random_pokemon.max_hp:
                        random_pokemon.hp = random_pokemon.max_hp
                    print(f"{random_pokemon.name} healed")
                    if chosen_one.offensive_moves3[0][2] > chosen_one.offensive_moves3[0][1]:
                        print(f"{random_pokemon.name}'s defence increased")
                    random_pokemon.energy -= 3
                    round4 = round5
                elif random_pokemon.defensive_moves2[0][2] > 0:
                    random_pokemon.defensive_moves2[0][2] = (random_pokemon.defensive_moves2[0][
                                                                 2] / 100 * random_pokemon.hp) + random_pokemon.hp
                    chosen_one.offensive_moves1[0][1] = (1 - random_pokemon.defensive_moves2[0][1]) * \
                                                        chosen_one.offensive_moves1[0][1]
                    chosen_one.offensive_moves2[0][1] = (1 - random_pokemon.defensive_moves2[0][1]) * \
                                                        chosen_one.offensive_moves2[0][1]
                    chosen_one.offensive_moves3[0][1] = (1 - random_pokemon.defensive_moves2[0][1]) * \
                                                        chosen_one.offensive_moves3[0][1]
                    print(f"{random_pokemon.name} used {random_pokemon.defensive_moves2[0][0]}")
                    random_pokemon.energy -= 3
                    round4 = round5
                else:
                    AI_choice = random2.randint(1, 3)
                    if AI_choice == 1:
                        chosen_one.hp = chosen_one.hp - (random_pokemon.offensive_moves1[0][1] * random_pokemon_damage)
                        random_pokemon.energy -= 1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                    elif AI_choice == 2:
                        chosen_one.hp = chosen_one.hp - (random_pokemon.offensive_moves2[0][1] * random_pokemon_damage)
                        random_pokemon.energy -= 1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                    else:
                        chosen_one.hp = chosen_one.hp - (random_pokemon.offensive_moves3[0][1] * random_pokemon_damage)
                        random_pokemon.energy -= 1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
            elif random_pokemon.hp <= random_pokemon.max_hp / 2:
                if round3 >= 2:
                    if random_pokemon.defensive_moves1[0][1] > 0:
                        chosen_one.offensive_moves1[0][1] = (1 - random_pokemon.defensive_moves1[0][1]) * \
                                                            chosen_one.offensive_moves1[0][1]
                        chosen_one.offensive_moves2[0][1] = (1 - random_pokemon.defensive_moves1[0][1]) * \
                                                            chosen_one.offensive_moves2[0][1]
                        chosen_one.offensive_moves3[0][1] = (1 - random_pokemon.defensive_moves1[0][1]) * \
                                                            chosen_one.offensive_moves3[0][1]
                        random_pokemon.defensive_moves1[0][2] = (chosen_one.defensive_moves1[0][
                                                                     2] / 100 * random_pokemon.hp) + random_pokemon.hp
                        print(f"{random_pokemon.name} used {random_pokemon.defensive_moves1[0]}")
                        if random_pokemon.hp > random_pokemon.max_hp:
                            random_pokemon.hp = random_pokemon.max_hp
                        if random_pokemon.hp < random_pokemon.hp:
                            print(f"{random_pokemon.name} healed")
                        if chosen_one.offensive_moves3[0][2] > chosen_one.offensive_moves3[0][1]:
                            print(f"{random_pokemon.name}'s defence increased")
                        random_pokemon.energy -= 3
                        round4 = round5
                    elif random_pokemon.defensive_moves2[0][1] > 0:
                        chosen_one.offensive_moves1[0][1] = (1 - random_pokemon.defensive_moves2[0][1]) * \
                                                            chosen_one.offensive_moves1[0][1]
                        chosen_one.offensive_moves2[0][1] = (1 - random_pokemon.defensive_moves2[0][1]) * \
                                                            chosen_one.offensive_moves2[0][1]
                        chosen_one.offensive_moves3[0][1] = (1 - random_pokemon.defensive_moves2[0][1]) * \
                                                            chosen_one.offensive_moves3[0][1]
                        random_pokemon.defensive_moves1[0][2] = (chosen_one.defensive_moves1[0][
                                                                     2] / 100 * random_pokemon.hp) + random_pokemon.hp
                        print(f"{random_pokemon.name} used {random_pokemon.defensive_moves1[0]}")
                        if random_pokemon.hp > random_pokemon.max_hp:
                            random_pokemon.hp = random_pokemon.max_hp
                        if random_pokemon.hp < random_pokemon.hp:
                            print(f"{random_pokemon.name} healed")
                        if chosen_one.offensive_moves3[0][2] > chosen_one.offensive_moves3[0][1]:
                            print(f"{random_pokemon.name}'s defence increased")
                        random_pokemon.energy -= 3
                        round4 = round5
                    else:
                        AI_choice = random2.randint(1, 3)
                    if AI_choice == 1:
                        chosen_one.hp = chosen_one.hp - (random_pokemon.offensive_moves1[0][1] * random_pokemon_damage)
                        random_pokemon.energy -= 1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                    elif AI_choice == 2:
                        chosen_one.hp = chosen_one.hp - (random_pokemon.offensive_moves2[0][1] * random_pokemon_damage)
                        random_pokemon.energy -= 1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                    else:
                        chosen_one.hp = chosen_one.hp - (random_pokemon.offensive_moves3[0][1] * random_pokemon_damage)
                        random_pokemon.energy -= 1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
            else:
                AI_choice = random2.randint(1, 3)
                if AI_choice == 1:
                    chosen_one.hp = chosen_one.hp - (random_pokemon.offensive_moves1[0][1] * random_pokemon_damage)
                    random_pokemon.energy -= 1
                    print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                elif AI_choice == 2:
                    chosen_one.hp = chosen_one.hp - (random_pokemon.offensive_moves2[0][1] * random_pokemon_damage)
                    random_pokemon.energy -= 1
                    print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                else:
                    chosen_one.hp = chosen_one.hp - (random_pokemon.offensive_moves3[0][1] * random_pokemon_damage)
                    random_pokemon.energy -= 1
                    print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
        round1 += 1
        round4 += 1
        if chosen_one.hp<=0:
            print("You lost")
            break
        if random_pokemon.hp<=0:
            print("You won")
            break

        # Player's turn
        round3 = round1 - round2
        if round3 == 2:
            # prevents the defensive moves from being too OP
            (random_pokemon.offensive_moves1[0])[1] = (random_pokemon.offensive_moves1[0])[2]
            (random_pokemon.offensive_moves2[0])[1] = (random_pokemon.offensive_moves2[0])[2]
            (random_pokemon.offensive_moves3[0])[1] = (random_pokemon.offensive_moves3[0])[2]
        if chosen_one.energy <= 0:
            print(f"""{chosen_one.name}   hp:{chosen_one.hp}   energy:{chosen_one.energy}
{random_pokemon.name}   hp:{random_pokemon.hp}   energy:{random_pokemon.energy}""")
            print(f"""{chosen_one.name} has no more energy
{chosen_one.name} used struggle""")
            chosen_one.hp = 3 / 4 * chosen_one.hp
            random_pokemon.hp = random_pokemon.hp - ((chosen_one.offensive_moves1[0][1] +
                                                      chosen_one.offensive_moves2[0][1] +
                                                      chosen_one.offensive_moves3[0][1]) / 3)
        elif chosen_one.energy > 0:
            print(f"""{chosen_one.name}   hp:{chosen_one.hp}   energy:{chosen_one.energy}
{random_pokemon.name}   hp:{random_pokemon.hp}   energy:{random_pokemon.energy}
{chosen_one.name}'s moves:
Offensive moves: {chosen_one.offensive_moves1[0][0]}(uses 1 energy),{chosen_one.offensive_moves2[0][0]}(uses 1 energy),{chosen_one.offensive_moves3[0][0]}(uses 1 energy)
Defensive moves: {chosen_one.defensive_moves1[0][0]}(uses 3 energy),{chosen_one.defensive_moves2[0][0]}(uses 3 energy)""")

            choice = int(input(
                "What is your move? Note:Do your moves in order from 1 to 5. 1 being the first offensive move and 5 being the last defensive move."))
            if choice == 1:
                random_pokemon.hp = random_pokemon.hp - ((chosen_one.offensive_moves1[0][1]) * chosen_one_damage)
                chosen_one.energy = chosen_one.energy - 1
                print(f"{chosen_one.name} used {chosen_one.offensive_moves1[0][0]}")
            elif choice == 2:
                random_pokemon.hp = random_pokemon.hp - ((chosen_one.offensive_moves2[0][1]) * chosen_one_damage)
                chosen_one.energy = chosen_one.energy - 1
                print(f"{chosen_one.name} used {chosen_one.offensive_moves2[0][0]}")
            elif choice == 3:
                random_pokemon.hp = random_pokemon.hp - ((chosen_one.offensive_moves3[0][1]) * chosen_one_damage)
                chosen_one.energy = chosen_one.energy - 1
                print(f"{chosen_one.name} used {chosen_one.offensive_moves3[0][0]}")
            elif choice == 4:
                random_pokemon.offensive_moves1[0][1] = (1 - chosen_one.defensive_moves1[0][1]) * \
                                                        random_pokemon.offensive_moves1[0][1]
                random_pokemon.offensive_moves2[0][1] = (1 - chosen_one.defensive_moves1[0][1]) * \
                                                        random_pokemon.offensive_moves2[0][1]
                random_pokemon.offensive_moves3[0][1] = (1 - chosen_one.defensive_moves1[0][1]) * \
                                                        random_pokemon.offensive_moves3[0][1]
                chosen_one_hp = chosen_one.hp
                chosen_one.hp = (chosen_one.defensive_moves1[0][2] / 100 * chosen_one.hp) + chosen_one.hp
                if chosen_one.hp > chosen_one.max_hp:
                    chosen_one.hp = chosen_one.hp - (chosen_one.max_hp - chosen_one.hp)
                    chosen_one.energy = chosen_one.energy - 3
                print(f"{chosen_one.name} used {chosen_one.defensive_moves1[0][0]}")
                if random_pokemon.offensive_moves1[0][1] < random_pokemon.offensive_moves1[0][2] and \
                        random_pokemon.offensive_moves2[0][1] < random_pokemon.offensive_moves2[0][2] and \
                        random_pokemon.offensive_moves3[0][1] < random_pokemon.offensive_moves3[0][2]:
                    print(f"{chosen_one.name}'s defence increased")
                if chosen_one.hp > chosen_one_hp:
                    print(f"{chosen_one.name}'s hp increased")
                round1 = round2
            else:
                random_pokemon.offensive_moves1[0][1] = (1 - chosen_one.defensive_moves2[0][1]) * \
                                                        random_pokemon.offensive_moves1[0][1]
                random_pokemon.offensive_moves2[0][1] = (1 - chosen_one.defensive_moves2[0][1]) * \
                                                        random_pokemon.offensive_moves2[0][1]
                random_pokemon.offensive_moves3[0][1] = (1 - chosen_one.defensive_moves2[0][1]) * \
                                                        random_pokemon.offensive_moves3[0][1]
                chosen_one_hp = chosen_one.hp
                chosen_one.hp = (chosen_one.defensive_moves2[0][2] / 100 * chosen_one.hp) + chosen_one.hp
                if chosen_one.hp > chosen_one.max_hp:
                    chosen_one.hp = chosen_one.hp - (chosen_one.max_hp - chosen_one.hp)
                    chosen_one.energy = chosen_one.energy - 3
                    print(f"{chosen_one.name} used {chosen_one.defensive_moves2[0][0]}")
                if random_pokemon.offensive_moves1[0][1] < random_pokemon.offensive_moves1[0][2] and \
                        random_pokemon.offensive_moves2[0][1] < random_pokemon.offensive_moves2[0][2] and \
                        random_pokemon.offensive_moves3[0][1] < random_pokemon.offensive_moves3[0][2]:
                    print(f"{chosen_one.name}'s defence increased")
                if chosen_one.hp > chosen_one_hp:
                    print(f"{chosen_one.name}'s hp increased")
                round1 = round2
        chosen_one.hp = int(chosen_one.hp)
        random_pokemon.hp = int(random_pokemon.hp)
        print(f"""{chosen_one.name}   hp:{chosen_one.hp}   energy:{chosen_one.energy}
        {random_pokemon.name}   hp:{random_pokemon.hp}   energy:{random_pokemon.energy}""")
        round1 += 1
        round2 += 1
        round4 += 1
        round5 += 1

# round end like boost of energy regen
chosen_one.energy = chosen_one.energy + 30
if chosen_one.energy > chosen_one.max_energy:
    chosen_one.energy = chosen_one.max_energy
 