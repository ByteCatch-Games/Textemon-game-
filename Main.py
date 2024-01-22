#Test and debugging
import time
import random

#intro message & disclaimer
print('In a land far far away...')
print("is the land of textemon. A world were text based monsters roamed.")
print('This idea and all names are from the Nintendo company and Game Freak.')
print("Pokémon is a trademark of Nintendo. This project is not affiliated with or endorsed by Nintendo.")
print("Copyright © ByteCatch Games 2023")
print("All rights reserved. This project and its contents are protected by copyright law. No part of this project may be reproduced, distributed, or transmitted in any form or by any means, without the prior written permission of the copyright owner.")
time.sleep(5)
print("\n\n\n\n")

#core engine
class Pokemon:
    def __init__(self, name, element, max_hp, max_energy,speed, attack,heal):
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
        self.speed=speed
        self.heal=heal
        self.attack=attack

    # noinspection PyArgumentList
    def add_offensive_move1(self, move_name,damage, damage2,move_element, paralyzing,burn, freeze,confusion,poison,badly_poison):
        # Add an offensive move to the list of moves
        self.offensive_moves1.append([move_name,damage,damage2,move_element, paralyzing, burn, freeze,confusion,poison, self.energy])
    
    def add_offensive_move2(self, move_name,damage, damage2, move_element, paralyzing,burn, freeze,confusion,poison,badly_poison):
        # Add an offensive move to the list of moves
        self.offensive_moves2.append([move_name,damage,damage2, move_element, paralyzing,burn, freeze,confusion,poison,badly_poison, self.energy])

    def add_offensive_move3(self, move_name,damage, damage2, move_element, paralyzing,burn, freeze,confusion,poison,badly_poison):
        # Add an offensive move to the list of moves
        self.offensive_moves3.append([move_name,damage,damage2, move_element,paralyzing,burn, freeze,confusion,poison,badly_poison, self.energy])

    def add_defensive_move1(self, move_name, reduce_damage, heal, increase_damage,turns,speed_increase, paralyzing ,burn, freeze,confusion,sleep,poison,badly_poison):
        # Add a defensive move to the list of moves
        self.defensive_moves1.append([move_name, reduce_damage, heal, increase_damage,turns,speed_increase, paralyzing,burn, freeze,confusion,sleep,poison,badly_poison])

    def add_defensive_move2(self, move_name, reduce_damage, heal, increase_damage,turns,speed_increase, paralyzing,burn, freeze,confusion,sleep,poison,badly_poison):
        # Add a defensive move to the list of moves
        self.defensive_moves2.append([move_name, reduce_damage, heal, increase_damage,turns,speed_increase, paralyzing,burn, freeze,confusion,sleep,poison,badly_poison])

# create a Pikachu instance with moves
pikachu = Pokemon("Pikachu", ["Electric"], 400, 60,90,53,20)
pikachu.add_offensive_move1("Thunderbolt", 70,70, "Electric",10,0,0,0,0,0,)
pikachu.add_offensive_move2("Iron Tail", 40,40, "Steel",0,0,0,0,0,0,)
pikachu.add_offensive_move3("Quick Attack", 30,30, "Normal",0,0,0,0,0,0,)
pikachu.add_defensive_move1("Agility", 0, 0,0,None,1,0,0,0,0,0,0,0,)
pikachu.add_defensive_move2("Double Team", 0, 0,0,None,0.5,0,0,0,0,0,0,0,)

# create a Charizard instance with moves
charizard = Pokemon("Charizard", ["Fire", "Flying"], 520, 50,100,97,5)
charizard.add_offensive_move1("Flamethrower", 60,60, "Fire",0,10,0,0,0,0,)
charizard.add_offensive_move2("Dragon Claw", 50,50,"Dragon",0,0,0,0,0,0,)
charizard.add_offensive_move3("Air Slash", 40,40,"Flying",0,0,0,0,0,0,)
charizard.add_defensive_move1("Dragon Dance",0.3, 0, 0.3,None,0,0,0,0,0,0,0,0,)
charizard.add_defensive_move2("Roost", 0, 60,0,None,0,0,0,0,0,0,0,0,)

# create a Blastoise instance with moves
blastoise = Pokemon("Blastoise", ["Water"], 520, 50,78,84,15)
blastoise.add_offensive_move1("Hydro Pump", 60,60,"Water",0,0,0,0,0,0,)
blastoise.add_offensive_move2("Ice Beam", 50,50,"Ice",0,0,10,0,0,0,)
blastoise.add_offensive_move3("Earthquake", 40,40,"Ground",0,0,0,0,0,0,)
blastoise.add_defensive_move1("Protect", 1,0,0,1,0,0,0,0,0,0,0,0,)
blastoise.add_defensive_move2("Withdraw", 0.5,0,0,None,0,0,0,0,0,0,0,0,)

# create a Venusaur instance with moves
venusaur = Pokemon("Venusaur", ["Grass", "Poison"], 520, 50,80,91,10)
venusaur.add_offensive_move1("Solar Beam", 60,60,"Grass",0,0,0,0,0,0,)
venusaur.add_offensive_move2("Sludge Bomb", 50,50,"Poison",0,0,0,0,30,0,)
venusaur.add_offensive_move3("Earthquake", 40,40,"Ground",0,0,0,0,0,0,)
venusaur.add_defensive_move1("Leech Seed", 0, 20,0,None,0,0,0,0,0,0,0,0,)
venusaur.add_defensive_move2("Sleep Powder", 0,0,0,None,0,0,0,0,0,100,0,0,)

# create a Lycanroc instance with moves
lycanroc = Pokemon("Lycanroc", ["Rock"], 480, 45,112,85,10)
lycanroc.add_offensive_move1("Stone Edge", 70,70,"Rock",0,0,0,0,0,0,)
lycanroc.add_offensive_move2("Accelerock", 50,50,"Rock",0,0,0,0,0,0,)
lycanroc.add_offensive_move3("Crunch", 40,40,"Dark",0,0,0,0,0,0,)
lycanroc.add_defensive_move1("Swords Dance", 0,0,0.3,None,0,0,0,0,0,0,0,0,)
lycanroc.add_defensive_move2("Stealth Rock", 0.3,0,0.3,None,0.3,0,0,0,0,0,0,0,)

# create a Beedrill instance with types Bug and Poison
beedrill = Pokemon("Beedrill", ["Bug", "Poison"], 400, 60,75,68,10)
beedrill.add_offensive_move1("Twineedle", 60,60,"Bug",0,0,0,0,0,0,)
beedrill.add_offensive_move2("Poison Jab", 40,40,"Poison",0,0,0,0,30,0,)
beedrill.add_offensive_move3("U-turn", 60,60,"Bug",0,0,0,0,0,0,)
beedrill.add_defensive_move1("Harden", 0.5,0,0,None,0,0,0,0,0,0,0,0,)
beedrill.add_defensive_move2("Protect", 1,0,0,1,0,0,0,0,0,0,0,0,)

# create a Crobat instance with types Poison and Flying
crobat = Pokemon("Crobat", ["Poison", "Flying"], 400, 60,130,80,5)
crobat.add_offensive_move1("Cross Poison", 60,60,"Poison",0,0,0,0,10,0,)
crobat.add_offensive_move2("Air Slash", 50,50,"Flying",0,0,0,0,0,0,)
crobat.add_offensive_move3("Brave Bird", 80,80,"Flying",0,0,0,0,0,0,)
crobat.add_defensive_move1("Roost", 0,60,0,None,0,0,0,0,0,0,0,0,)
crobat.add_defensive_move2("Toxic", 0.4,10,0,None,0,0,0,0,0,0,0,100)

# create a Gengar instance with types Ghost and Poison
gengar = Pokemon("Gengar", ["Ghost", "Poison"], 440, 60,110,118,10)
gengar.add_offensive_move1("Shadow Ball", 60,60,"Ghost",0,0,0,0,0,0,)
gengar.add_offensive_move2("Sludge Bomb", 50,50,"Poison",0,0,0,0,30,0,)
gengar.add_offensive_move3("Venom Drench", 40,40,"Poison",0,0,0,0,0,0,)
gengar.add_defensive_move1("Hypnosis", 0,0,0,None,0,0,0,0,0,100,0,0,)
gengar.add_defensive_move2("Destiny Bond", 0.3,10,0,None,0.3,0,0,0,0,0,0,0,)

# create a Metagross instance with types Steel and Psychic
metagross = Pokemon("Metagross", ["Steel", "Psychic"], 520, 45,70,115,5)
metagross.add_offensive_move1("Meteor Mash", 70,70,"Steel",0,0,0,0,0,0,)
metagross.add_offensive_move2("Zen Headbutt", 50,50,"Psychic",0,0,0,0,0,0,)
metagross.add_offensive_move3("Psychic", 80,80,"Psychic",0,0,0,0,0,0,)
metagross.add_defensive_move1("Agility", 0,0,0,None,1,0,0,0,0,0,0,0,)
metagross.add_defensive_move2("Light Screen", 0.3,10,0,None,0,0,0,0,0,0,0,0,)

# create a Noivern instance with types Flying and Dragon
noivern = Pokemon("Noivern", ["Flying", "Dragon"], 480, 50,123,84,5)
noivern.add_offensive_move1("Dragon Pulse", 60,60,"Dragon",0,0,0,0,0,0,)
noivern.add_offensive_move2("Air Slash", 50,50,"Flying",0,0,0,0,0,0,)
noivern.add_offensive_move3("Hurricane", 70,70,"Flying",0,0,0,0,0,0,)
noivern.add_defensive_move1("Roost",0,60,0,None,0,0,0,0,0,0,0,0,)
noivern.add_defensive_move2("Protect", 1,0,0,1,0,0,0,0,0,0,0,0,)

# create a Garchomp instance with types Dragon and Ground
garchomp = Pokemon("Garchomp", ["Dragon", "Ground"], 560, 40,102,145,5)
garchomp.add_offensive_move1("Dragon Claw", 70,70,"Dragon",0,0,0,0,0,0,)
garchomp.add_offensive_move2("Earthquake", 60,60,"Ground",0,0,0,0,0,0,)
garchomp.add_offensive_move3("Stone Edge", 80,80,"Rock",0,0,0,0,0,0,)
garchomp.add_defensive_move1("Swords Dance", 0,0,0.2,None,0,0,0,0,0,0,0,0,)
garchomp.add_defensive_move2("Sandstorm", 0,0,0.2,None,0,0,0,0,0,0,0,0,)

# create a Krookodile instance with types Ground and Dark
krookodile = Pokemon("Krookodile", ["Ground", "Dark"], 440, 55,92,91,10)
krookodile.add_offensive_move1("Earthquake", 60,60,"Ground",0,0,0,0,0,0,)
krookodile.add_offensive_move2("Stone Edge", 80,80,"Rock",0,0,0,0,0,0,)
krookodile.add_offensive_move3("Crunch", 70,70,"Dark",0,0,0,0,0,0,)
krookodile.add_defensive_move1("Sandstorm", 0,0,0.5,None,0,0,0,0,0,0,0,0,)
krookodile.add_defensive_move2("Swagger", -0.4,0,0,None,0,0,0,0,100,0,0,0,)


# Create a Tyranitar instance
tyranitar = Pokemon("Tyranitar", ["Dark", "Rock"], 480, 40,61,130,5)
tyranitar.add_offensive_move1("Crunch", 50,50,"Dark",0,0,0,0,0,0,)
tyranitar.add_offensive_move2("Stone Edge", 60,60,"Rock",0,0,0,0,0,0,)
tyranitar.add_offensive_move3("Earthquake", 70,70,"Ground",0,0,0,0,0,0,)
tyranitar.add_defensive_move1("Protect", 1,0,0,1,0,0,0,0,0,0,0,0,)
tyranitar.add_defensive_move2("Sandstorm", 0,0,0.5,None,0,0,0,0,0,0,0,0,)

# Create a Machamp instance
machamp = Pokemon("Machamp", ["Fighting"], 440, 55,55,98,10)
machamp.add_offensive_move1("Cross Chop", 50,50,"Fighting",0,0,0,0,0,0,)
machamp.add_offensive_move2("Submission", 60,60,"Fighting",0,0,0,0,0,0,)
machamp.add_offensive_move3("Dynamic Punch", 70,70,"Fighting",0,0,0,0,0,0,)
machamp.add_defensive_move1("Bulk Up", 0.2,0,0.2,None,0,0,0,0,0,0,0,0,)
machamp.add_defensive_move2("Detect", 0,0,0,None,0.2,0,0,0,0,0,0,0,) 

# Create a Gardevoir instance
gardevoir = Pokemon("Gardevoir", ["Psychic", "Fairy"], 440, 60,80,95,20)
gardevoir.add_offensive_move1("Psychic", 50,50,"Psychic",0,0,0,0,0,0,)
gardevoir.add_offensive_move2("Moonblast", 60,60,"Fairy",0,0,0,0,0,0,)
gardevoir.add_offensive_move3("Dazzling Gleam", 40,40,"Fairy",0,0,0,0,0,0,)
gardevoir.add_defensive_move1("Calm Mind", 0.2,0,0.2,None,0,0,0,0,0,0,0,0,)
gardevoir.add_defensive_move2("Will-O-Wisp", 0,0,0,None,0,0,100,0,0,0,0,0,)


# Create a Mimikyu instance
mimikyu = Pokemon("Mimikyu", ["Ghost", "Fairy"], 440, 60,96,70,15)
mimikyu.add_offensive_move1("Shadow Claw", 50,50,"Ghost",0,0,0,0,0,0,)
mimikyu.add_offensive_move2("Play Rough", 60,60,"Fairy",0,0,0,0,0,0,)
mimikyu.add_offensive_move3("Phantom Force", 70,70,"Ghost",0,0,0,0,0,0,)
mimikyu.add_defensive_move1("Protect", 1, 0, 0,1,0,0,0,0,0,0,0,0,)
mimikyu.add_defensive_move2("Substitute", 1,-25,0,2,0,0,0,0,0,0,0,0,)

# Create a Silvally instance
silvally = Pokemon("Silvally", ["Normal"], 480, 55,95,95,15)
silvally.add_offensive_move1("Multi-Attack", 70,70,"Normal",0,0,0,0,0,0,)
silvally.add_offensive_move2("Crunch", 50,50,"Dark",0,0,0,0,0,0,)
silvally.add_offensive_move3("X-Scissor", 60,60,"Bug",0,0,0,0,0,0,)
silvally.add_defensive_move1("Iron Defense", 0.4,0,0,None,0,0,0,0,0,0,0,0,)
silvally.add_defensive_move2("Roar", 0.25,0,0,None,0,0,0,0,0,0,0,0,) 

# Create a Cryogonal instance
cryogonal = Pokemon("Cryogonal", ["Ice"], 400, 55,105,73,20)
cryogonal.add_offensive_move1("Ice Beam", 50,50,"Ice",0,0,10,0,0,0,)
cryogonal.add_offensive_move2("Blizzard", 70,70,"Ice",0,0,10,0,0,0,)
cryogonal.add_offensive_move3("Freeze-Dry", 70,70,"Ice",0,0,10,0,0,0,)
cryogonal.add_defensive_move1("Reflect", 0.5,0,0,None,0,0,0,0,0,0,0,0,)
cryogonal.add_defensive_move2("Light Screen", 0.5,0,0,None,0,0,0,0,0,0,0,0,)

print("Available Pokemons:")
print("""Example: 
pokemon name, pokemon type
Offensive moves: ['Thunderbolt', 'Iron Tail', 'Quick Attack']
Defensive moves: ['Agility', 'Double Team']""")
time.sleep(1)
print()
for pokemon in [pikachu, charizard, blastoise, venusaur, lycanroc, beedrill, crobat, gengar, metagross, noivern, garchomp, krookodile, tyranitar, machamp, gardevoir, mimikyu, silvally, cryogonal ]:
    print(f"{pokemon.name},hp:{pokemon.hp},energy:{pokemon.energy},type:{pokemon.element}")
    print(f"Offensive moves: {pokemon.offensive_moves1[0][0]},{pokemon.offensive_moves2[0][0]},{pokemon.offensive_moves3[0][0]}")
    print(f"Defensive moves: {pokemon.defensive_moves1[0][0]},{pokemon.defensive_moves2[0][0]}")
    print(f"Heals:{pokemon.heal}")
    time.sleep(1)
    print()
    
elemental_chart = {}

types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]

for t in types:
    weaknesses = []
    strengths = []
    immune=[]
    
    if t == "Normal":
        weaknesses = ["Fighting"]
        immune=["Ghost"]
        
    elif t == "Fire":
        weaknesses = ["Water", "Ground", "Rock"]
        strengths = ["Grass", "Ice", "Bug", "Steel","Fairy","Fire"]
        
    elif t == "Water":
        weaknesses = ["Grass", "Electric"]
        strengths = ["Fire", "Steel","Water","Ice"]
        
    elif t == "Electric":
        weaknesses = ["Ground"]
        strengths = ["Steel", "Flying","Electric"]
        
    elif t == "Grass":
        weaknesses = ["Fire", "Ice", "Poison", "Flying", "Bug"]
        strengths = ["Water", "Ground", "Grass","Electric"]
        
    elif t == "Ice":
        weaknesses = ["Fire", "Fighting", "Rock", "Steel"]
        strengths = ["Ice"]
        
    elif t == "Fighting":
        weaknesses = ["Flying", "Psychic", "Fairy"]
        strengths = ["Dark", "Bug", "Rock"]
        
    elif t == "Poison":
        weaknesses = ["Ground", "Psychic"]
        strengths = ["Grass","Fighting", "Poison","Bug", "Fairy"]
        
    elif t == "Ground":
        weaknesses = ["Water", "Grass", "Ice"]
        strengths = ["Poison", "Rock"]
        immune=["Electric"]
        
    elif t == "Flying":
        weaknesses = ["Electric", "Ice", "Rock"]
        strengths = ["Grass", "Fighting", "Bug"]
        immune=["Ground"]
        
    elif t == "Psychic":
        weaknesses = ["Bug", "Ghost", "Dark"]
        strengths = ["Fighting", "Psychic"]
        
    elif t == "Bug":
        weaknesses = ["Fire", "Flying", "Rock"]
        strengths = ["Grass", "Fighting", "Ground"]
        
    elif t == "Rock":
        weaknesses = ["Water", "Grass", "Fighting", "Ground", "Steel"]
        strengths = ["Fire", "Poison", "Flying","Normal"]
        
    elif t == "Ghost":
        weaknesses = ["Ghost", "Dark"]
        strengths = ["Poison","Bug"]
        immune=["Normal", "Fighting"]
        
    elif t == "Dragon":
        weaknesses = ["Ice", "Dragon", "Fairy"]
        strengths = ["Fire","Water","Electric","Grass"]
        
    elif t == "Dark":
        weaknesses = ["Fighting", "Bug", "Fairy"]
        strengths = ["Ghost","Dark"]
        immune=["Psychic"]
        
    elif t == "Steel":
        weaknesses = ["Fire", "Fighting", "Ground"]
        strengths = ["Normal", "Grass", "Ice", "Flying","Psychic","Bug","Rock","Dragon","Steel","Fairy"]
        immune=["Poison"]
        
    elif t == "Fairy":
        weaknesses = ["Poison", "Steel"]
        strengths = ["Fighting", "Dark","Bug"]
        immune=["Dragon"]
    
    elemental_chart[t] = {
        "weaknesses": weaknesses,
        "strengths": strengths,
        "immune": immune
    }

#pokemon picking
pokemons = [pikachu,charizard,blastoise,venusaur,lycanroc,beedrill,crobat,gengar,noivern,metagross,garchomp,krookodile,tyranitar,machamp,gardevoir,mimikyu,silvally,cryogonal]
chosen_one=input("Pick which pokemon you want by typing its name or type random to choose a random pokemon?")
while chosen_one==chosen_one:
    if chosen_one=="Pikachu" or chosen_one=="pikachu" or chosen_one=="PIKACHU":
        chosen_one=pikachu
        del pokemons[0]
        break
    elif chosen_one=="Charizard" or chosen_one=="charizard" or chosen_one=="CHARIZARD":
        chosen_one=charizard
        del pokemons[1]
        break
    elif chosen_one == "Blastoise" or chosen_one == "blastoise" or chosen_one=="BLASTOISE":
        chosen_one = blastoise
        del pokemons[2]
        break
    elif chosen_one == "Venusaur" or chosen_one == "venusaur" or chosen_one=="VENUSAUR":
        chosen_one = venusaur
        del pokemons[3]
        break
    elif chosen_one == "Lycanroc" or chosen_one == "lycanroc" or chosen_one=="LYCANROC":
        chosen_one = lycanroc
        del pokemons[4]
        break
    elif chosen_one == "Beedrill" or chosen_one == "beedrill" or chosen_one=="BEEDRILL":
        chosen_one = beedrill
        del pokemons[5]
        break
    elif chosen_one == "Crobat" or chosen_one == "crobat" or chosen_one=="CROBAT":
        chosen_one = crobat
        del pokemons[6]
        break
    elif chosen_one == "Gengar" or chosen_one == "gengar" or chosen_one=="GENGAR":
        chosen_one = gengar
        del pokemons[7]
        break
    elif chosen_one == "Metagross" or chosen_one == "metagross" or chosen_one=="METAGROSS":
        chosen_one = metagross
        del pokemons[9]
        break
    elif chosen_one == "Garchomp" or chosen_one == "garchomp" or chosen_one=="GARCHOMP":
        chosen_one = garchomp
        del pokemons[10]
        break
    elif chosen_one == "Krookodile" or chosen_one == "krookodile" or chosen_one=="KROOKODILE":
        chosen_one = krookodile
        del pokemons[11]
        break
    elif chosen_one == "Cryogonal" or chosen_one == "cryogonal" or chosen_one=="CRYOGONAL":
        chosen_one = cryogonal
        del pokemons[17]
        break
    elif chosen_one == "Tyranitar" or chosen_one == "tyranitar" or chosen_one=="TYRANITAR":
        chosen_one = tyranitar
        del pokemons[12]
        break
    elif chosen_one == "Machamp" or chosen_one == "machamp" or chosen_one=="MACHAMP":
        chosen_one = machamp
        del pokemons[13]
        break
    elif chosen_one == "noivern" or chosen_one == "Noivern" or chosen_one=="NOIVERN":
        chosen_one = noivern
        del pokemons[8]
        break
    elif chosen_one == "Gardevoir" or chosen_one == "gardevoir" or chosen_one=="GARDEVOIR":
        chosen_one = gardevoir
        del pokemons[14]
        break
    elif chosen_one == "Mimikyu" or chosen_one == "mimikyu" or chosen_one=="MIMIKYU":
        chosen_one = mimikyu
        del pokemons[15]
        break
    elif chosen_one == "Silvally" or chosen_one == "silvally" or chosen_one=="SILVALLY":
        chosen_one = silvally
        del pokemons[16]
        break
    elif chosen_one=="Random" or chosen_one=="random" or chosen_one=="RANDOM":
        random_chosen_one=random2.randint(0,17)
        chosen_one=pokemons[random_chosen_one]
        del pokemons[random_chosen_one]
        break
    else:
        print("That is not a pokemon. Please read the list again and choose your pokemon\n")
        chosen_one=input("Pick which pokemon you want by typing its name or type random to choose a random pokemon?")

#pokemon check
print()
print(f"You picked {chosen_one.name}")

#weakness and strength of chosen one
chosen_one_weakness=[]
chosen_one_strength=[]
chosen_one_immune=[]
for i in range(len(chosen_one.element)):
    chosen_one_type_chart = elemental_chart[chosen_one.element[i]]
    chosen_one_weakness += chosen_one_type_chart["weaknesses"]
    chosen_one_strength += chosen_one_type_chart["strengths"]
    chosen_one_immune += chosen_one_type_chart["immune"]
#AI pokemon
random_pokemon = pokemons[random2.randint(0,16)]
print("The AI has selected", random_pokemon.name)
print()
print("{}: {}".format(chosen_one.name, chosen_one.element))
print("{}: {}".format(random_pokemon.name, random_pokemon.element))
time.sleep(1)
print()
# weakness and strength of chosen one
random_pokemon_weakness=[]
random_pokemon_strength=[]
random_pokemon_immune=[]
for i in range(len(random_pokemon.element)):
    random_pokemon_type_chart = elemental_chart[random_pokemon.element[i]]
    random_pokemon_weakness += random_pokemon_type_chart["weaknesses"]
    random_pokemon_strength += random_pokemon_type_chart["strengths"]
    random_pokemon_immune += random_pokemon_type_chart["immune"]


#type effectiveness
chosen_one_damage1=1
chosen_one_damage2=1
chosen_one_damage3=1
random_pokemon_damage1=1
random_pokemon_damage2=1
random_pokemon_damage3=1

#Move type effectiveness
for i in range(len(random_pokemon_weakness)):
    if chosen_one.offensive_moves1[0][3] in random_pokemon_weakness[i]:
        chosen_one_damage1=chosen_one_damage1* 2
for i in range(len(random_pokemon_weakness)):
    if chosen_one.offensive_moves2[0][3] in random_pokemon_weakness[i]:
        chosen_one_damage2=chosen_one_damage2* 2
for i in range(len(random_pokemon_weakness)):
    if chosen_one.offensive_moves3[0][3] in random_pokemon_weakness[i]:
        chosen_one_damage3=chosen_one_damage3* 2

for i in range(len(random_pokemon_strength)):
    if chosen_one.offensive_moves1[0][3] in random_pokemon_strength[i]:
        chosen_one_damage1=chosen_one_damage1* 0.5
for i in range(len(random_pokemon_strength)):
    if chosen_one.offensive_moves2[0][3] in random_pokemon_strength[i]:
        chosen_one_damage2=chosen_one_damage2* 0.5
for i in range(len(random_pokemon_strength)):
    if chosen_one.offensive_moves3[0][3] in random_pokemon_strength[i]:
        chosen_one_damage3=chosen_one_damage3* 0.5

for i in range(len(random_pokemon_immune)):
    if chosen_one.offensive_moves1[0][3] in random_pokemon_immune[i]:
        chosen_one_damage1=chosen_one_damage1* 0
for i in range(len(random_pokemon_immune)):
    if chosen_one.offensive_moves2[0][3] in random_pokemon_immune[i]:
        chosen_one_damage2=chosen_one_damage2* 0
for i in range(len(random_pokemon_immune)):
    if chosen_one.offensive_moves3[0][3] in random_pokemon_immune[i]:
        chosen_one_damage3=chosen_one_damage3* 0



for i in range(len(chosen_one_weakness)):
    if random_pokemon.offensive_moves1[0][3] in chosen_one_weakness[i]:
        random_pokemon_damage1=random_pokemon_damage1* 2
                            
    if random_pokemon.offensive_moves2[0][3] in chosen_one_weakness[i]:
        random_pokemon_damage2=random_pokemon_damage2* 2
                            
    if random_pokemon.offensive_moves3[0][3] in chosen_one_weakness[i]:
        random_pokemon_damage3=random_pokemon_damage3* 2

for i in range(len(chosen_one_strength)):
    if random_pokemon.offensive_moves1[0][3] in chosen_one_strength[i]:
        random_pokemon_damage1=random_pokemon_damage1*0.5
                            
    if random_pokemon.offensive_moves2[0][3] in chosen_one_strength[i]:
        random_pokemon_damage2=random_pokemon_damage2*0.5
                            
    if random_pokemon.offensive_moves3[0][3] in chosen_one_strength[i]:
        random_pokemon_damage3=random_pokemon_damage3*0.5

for i in range(len(chosen_one_immune)):
    if random_pokemon.offensive_moves1[0][3] in chosen_one_immune[i]:
        random_pokemon_damage1=random_pokemon_damage1*0
                            
    if random_pokemon.offensive_moves2[0][3] in chosen_one_immune[i]:
        random_pokemon_damage2=random_pokemon_damage2*0
                            
    if random_pokemon.offensive_moves3[0][3] in chosen_one_immune[i]:
        random_pokemon_damage3=random_pokemon_damage3*0




random_pokemon_damage_1=random_pokemon_damage1
random_pokemon_damage_2=random_pokemon_damage2
random_pokemon_damage_3=random_pokemon_damage3
chosen_one_damage_1=chosen_one_damage1
chosen_one_damage_2=chosen_one_damage2
chosen_one_damage_3=chosen_one_damage3

#Same type attack bonus
if random_pokemon.offensive_moves1[0][3] in random_pokemon.element:
    random_pokemon_damage_1=random_pokemon_damage1*1.5
                            
if random_pokemon.offensive_moves2[0][3] in random_pokemon.element:
    random_pokemon_damage_2=random_pokemon_damage2*1.5
                            
if random_pokemon.offensive_moves3[0][3] in random_pokemon.element:
    random_pokemon_damage_3=random_pokemon_damage3*1.5

if chosen_one.offensive_moves1[0][3] in chosen_one.element:
    chosen_one_damage_1=chosen_one_damage1* 1.5

if chosen_one.offensive_moves2[0][3] in chosen_one.element:
    chosen_one_damage_2=chosen_one_damage2* 1.5

if chosen_one.offensive_moves3[0][3] in chosen_one.element:
    chosen_one_damage_3=chosen_one_damage3* 1.5
#Who starts first code
start=0
#Battle part
round1=0
round2=0
round3=0
round4=0
round5=0
round6=0
chosen_one.hp=int(chosen_one.hp)
random_pokemon.hp=int(random_pokemon.hp)

#Paralasys
chosen_one_paralasys_mode=False
chosen_one_paralasys_number=0
random_pokemon_paralasys_mode=False
random_pokemon_paralasys_number=0

#burn
chosen_one_burn_mode=False
chosen_one_burn_number=0
random_pokemon_burn_mode=False
random_pokemon_burn_number=0

#freeze
chosen_one_freeze_mode=False
chosen_one_freeze_number=0
random_pokemon_freeze_mode=False
random_pokemon_freeze_number=0
#confusion
chosen_one_confusion_number=0
random_pokemon_confusion_number=0
chosen_one_confusion_mode=[False]
random_pokemon_confusion_mode=[False]

def chosen_one_confusion_effect(pokemon, move):
    chosen_one_confusion=random2.randint(1,100)
    if chosen_one_confusion<=move:
        print(f"{chosen_one.name} confused {random_pokemon.name}")
        chosen_one_confusion_mode.append(True)
    elif chosen_one_confusion_number>4:
        chosen_one_confusion_number.append(False)
        chosen_one_confusion_number=0
        
def random_pokemon_confusion_effect(pokemon, move):
    random_pokemon_confusion=random2.randint(1,100)
    if random_pokemon_confusion<=move:
        print(f"{random_pokemon.name} confused {chosen_one.name}")
        random_pokemon_confusion_mode.append(True)
    elif random_pokemon_confusion_number>4:
        chosen_one_confusion_mode.append(False)
        random_pokemon_confusion_number=0

#sleep
chosen_one_sleep_number=0
random_pokemon_sleep_number=0
chosen_one_sleep_mode=[False]
random_pokemon_sleep_mode=[False]

def chosen_one_sleep_effect(move):
    chosen_one_sleep=random2.randint(1,100)
    if chosen_one_sleep<=move:
        print(f"{random_pokemon.name} went to sleep")
        chosen_one_sleep_mode.append(True)
    elif chosen_one_sleep_number>5:
        chosen_one_sleep_mode.append(False)
        chosen_one_sleep_number=0

def random_pokemon_sleep_effect(move):
    random_pokemon_sleep=random2.randint(1,100)
    if random_pokemon_sleep<=move:
        print(f"{chosen_one.name} went to sleep")
        random_pokemon_sleep_mode.append(True)
    elif random_pokemon_sleep_number>5:
        random_pokemon_sleep_mode.append(False)
        random_pokemon_sleep_number=0

#poison
chosen_one_poison_number=0
random_pokemon_poison_number=0
chosen_one_poison_mode=[False]
random_pokemon_poison_mode=[False]

def chosen_one_poison_effect(move):
    chosen_one_poison=random2.randint(1,100)
    if chosen_one_poison<=move:
        print(f"{chosen_one.name} poisoned {random_pokemon.name}")
        chosen_one_poison_mode.append(True)
    elif random_pokemon_poison_number>20:
        chosen_one_poison_mode.append(False)
        
def random_pokemon_poison_effect(number):
    if number==1:
        random_pokemon_poison=random2.randint(1,100)
        if random_pokemon_poison<=random_pokemon.offensive_moves1[0][8]:
            print(f"{random_pokemon.name} poisoned {chosen_one.name}")
            random_pokemon_poison_mode.append(True)
        elif random_pokemon_poison_number>20:
            random_pokemon_poison_mode.append(False)
    elif number==2:
        random_pokemon_poison=random2.randint(1,100)
        if random_pokemon_poison<=random_pokemon.offensive_moves2[0][8]:
            print(f"{random_pokemon.name} poisoned {chosen_one.name}")
            random_pokemon_poison_mode.append(True)
        elif random_pokemon_poison_number>20:
            random_pokemon_poison_mode.append(False)
    elif number==3:
        random_pokemon_poison=random2.randint(1,100)
        if random_pokemon_poison<=random_pokemon.offensive_moves3[0][8]:
            print(f"{random_pokemon.name} poisoned {chosen_one.name}")
            random_pokemon_poison_mode.append(True)
        elif random_pokemon_poison_number>20:
            random_pokemon_poison_mode.append(False)
    elif number==4:
        random_pokemon_poison=random2.randint(1,100)
        if random_pokemon_poison<=random_pokemon.defensive_moves1[0][11]:
            print(f"{random_pokemon.name} poisoned {chosen_one.name}")
            random_pokemon_poison_mode.append(True)
        elif random_pokemon_poison_number>20:
            random_pokemon_poison_mode.append(False)
    elif number==5:
        random_pokemon_poison=random2.randint(1,100)
        if random_pokemon_poison<=random_pokemon.defensive_moves2[0][11]:
            print(f"{random_pokemon.name} poisoned {chosen_one.name}")
            random_pokemon_poison_mode.append(True)
        elif random_pokemon_poison_number>20:
            random_pokemon_poison_mode.append(False)
        
#badly poison
chosen_one_badly_poison_number=0
random_pokemon_badly_poison_number=0
chosen_one_badly_poison_mode=[False]
random_pokemon_badly_poison_mode=[False]

def chosen_one_badly_poison_effect(move):
    chosen_one_badly_poison=random2.randint(1,100)
    if chosen_one_badly_poison<=move:
        print(f"{chosen_one.name} badly poisoned {random_pokemon.name}")
        chosen_one_badly_poison_mode.append(True)
    elif random_pokemon_badly_poison_number>5:
        chosen_one_badly_poison_mode.append(False)
        
def random_pokemon_badly_poison_effect(number):
    if number==1:
        random_pokemon_badly_poison=random2.randint(1,100)
        if random_pokemon_badly_poison<=random_pokemon.offensive_moves1[0][9]:
            print(f"{random_pokemon.name} badly poisoned {chosen_one.name}")
            random_pokemon_badly_poison_mode.append(True)
        elif random_pokemon_badly_poison_number>5:
            random_pokemon_badly_poison_mode.append(False)
    elif number==2:
        random_pokemon_badly_poison=random2.randint(1,100)
        if random_pokemon_badly_poison<=random_pokemon.offensive_moves2[0][9]:
            print(f"{random_pokemon.name} badly poisoned {chosen_one.name}")
            random_pokemon_badly_poison_mode.append(True)
        elif random_pokemon_badly_poison_number>5:
            random_pokemon_badly_poison_mode.append(False)
    elif number==3:
        random_pokemon_badly_poison=random2.randint(1,100)
        if random_pokemon_badly_poison<=random_pokemon.offensive_moves3[0][9]:
            print(f"{random_pokemon.name} badly poisoned {chosen_one.name}")
            random_pokemon_badly_poison_mode.append(True)
        elif random_pokemon_badly_poison_number>5:
            random_pokemon_badly_poison_mode.append(False)
    elif number==4:
        random_pokemon_badly_poison=random2.randint(1,100)
        if random_pokemon_badly_poison<=random_pokemon.defensive_moves1[0][12]:
            print(f"{random_pokemon.name} badly poisoned {chosen_one.name}")
            random_pokemon_badly_poison_mode.append(True)
        elif random_pokemon_badly_poison_number>5:
            random_pokemon_badly_poison_mode.append(False)
    elif number==5:
        random_pokemon_badly_poison=random2.randint(1,100)
        if random_pokemon_badly_poison<=random_pokemon.defensive_moves2[0][12]:
            print(f"{random_pokemon.name} badly poisoned {chosen_one.name}")
            random_pokemon_badly_poison_mode.append(True)
        elif random_pokemon_badly_poison_number>5:
            random_pokemon_badly_poison_mode.append(False)

while chosen_one.hp>0 and random_pokemon.hp>0:

    if chosen_one.speed>random_pokemon.speed or start==1:
        chosen_one.hp=int(chosen_one.hp)
        random_pokemon.hp=int(random_pokemon.hp)
        random_pokemon_damage_check=random_pokemon.offensive_moves1[0][1]
        chosen_one_damage_check=chosen_one.offensive_moves1[0][1]
        round3=round1-round2
        if round6==chosen_one.defensive_moves2[0][4] and chosen_one.defensive_moves2[0][4]!=None:
            #prevents the defensive moves from being too OP
            random_pokemon.offensive_moves1[0][1]=random_pokemon.offensive_moves1[0][2]
            random_pokemon.offensive_moves2[0][1]=random_pokemon.offensive_moves2[0][2]
            random_pokemon.offensive_moves3[0][1]=random_pokemon.offensive_moves3[0][2]

        if round6==chosen_one.defensive_moves1[0][4] and chosen_one.defensive_moves1[0][4]!=None:
            #prevents the defensive moves from being too OP
            random_pokemon.offensive_moves1[0][1]=random_pokemon.offensive_moves1[0][2]
            random_pokemon.offensive_moves2[0][1]=random_pokemon.offensive_moves1[0][2]
            random_pokemon.offensive_moves3[0][1]=random_pokemon.offensive_moves1[0][2]

        if random_pokemon_paralasys_number>3:
            random_pokemon_paralasys_mode=False
            random_pokemon_paralasys_number=0
        if random_pokemon_paralasys_mode==True and random_pokemon_paralasys_number<=3:
            random_pokemon_paralasys_number+=1
            print(f"{chosen_one.name} is paralyzed")
        if random_pokemon_freeze_mode==True:
            freeze_chance=random2.randint(1,256)
            if freeze_chance<=25:
                random_pokemon_freeze_mode==False
                print(f"{chosen_one.name} escaped the ice")
            else:
                print(f"{chosen_one.name} is frozen")
        if random_pokemon_sleep_mode[-1]==True:
            if random_pokemon_sleep_number==0:
                print(f"{chosen_one.name} is fast sleep")
                random_pokemon_sleep_number+=1
            else:
                wake_up=random2.randint(1, 5-random_pokemon_sleep_number)
                if wake_up==1:
                    print(f"{chosen_one.name} woke up")
                    random_pokemon_sleep_number=0
                    random_pokemon_sleep_mode.append(False)
                else:
                    print(f"{chosen_one.name} is fast sleep")
                    random_pokemon_sleep_number+=1
        if random_pokemon_paralasys_mode==False and random_pokemon_freeze_mode==False and random_pokemon_sleep_mode[-1]==False:
            if chosen_one.energy<=0:
                chosen_one.energy=0
                print(f"""{chosen_one.name}   hp:{chosen_one.hp}   energy:{chosen_one.energy} heals:{chosen_one.heal}
{random_pokemon.name}   hp:{random_pokemon.hp}   energy:{random_pokemon.energy} heals:{random_pokemon.heal}""")
                print(f"""{chosen_one.name} has no more energy
{chosen_one.name} used struggle""")
                print()
                chosen_one.hp=3/4*chosen_one.hp
                random_pokemon.hp=random_pokemon.hp-((chosen_one.offensive_moves1[0][1]+chosen_one.offensive_moves2[0][1]+chosen_one.offensive_moves3[0][1])*chosen_one.attack/100/3)
            #Player's turn
            elif chosen_one.energy>0:
                print(f"""{chosen_one.name}   hp:{chosen_one.hp}   energy:{chosen_one.energy} heals:{chosen_one.heal}
{random_pokemon.name}   hp:{random_pokemon.hp}   energy:{random_pokemon.energy} heals:{random_pokemon.heal}
{chosen_one.name}'s moves:
Offensive moves: {chosen_one.offensive_moves1[0][0]}(uses 1 energy),{chosen_one.offensive_moves2[0][0]}(uses 1 energy),{chosen_one.offensive_moves3[0][0]}(uses 1 energy)
Defensive moves: {chosen_one.defensive_moves1[0][0]}(uses 3 energy),{chosen_one.defensive_moves2[0][0]}(uses 3 energy)
Heal:{chosen_one.heal}""")
                print()
                random_pokemon_damage_check=random_pokemon.offensive_moves1[0][1]
                chosen_one_damage_check=chosen_one.offensive_moves1[0][1]
                choice=input("What is your move? Note:Do your moves in order from 1 to 6. 1 being the first offensive move and 6 being a heal." )
                while choice==choice:
                    if choice=="6":
                        if chosen_one.heal>0:
                            chosen_one.hp+=100
                            print(f"You used a heal on {chosen_one.name}")
                            chosen_one.heal-=1
                            if chosen_one.hp>chosen_one.max_hp:
                                chosen_one.hp=chosen_one.max_hp
                        elif chosen_one.heal<=0:
                            print("You don't have any heals")
                        break
                    elif random_pokemon_confusion_mode[-1]==True and random_pokemon_confusion_number<=4:
                        spin_the_wheel=random2.randint(1,2)
                        if spin_the_wheel==1:
                            print(f"{chosen_one.name} is confused")
                            chosen_one.hp-=((chosen_one.offensive_moves1[0][1]+chosen_one.offensive_moves2[0][1]+chosen_one.offensive_moves3[0][1])*chosen_one.attack/100/3)
                            random_pokemon_confusion_number+=1
                            break
                        if spin_the_wheel==2:
                            random_pokemon_confusion_number+=1
                    elif choice=="1":
                        random_pokemon.hp= random_pokemon.hp - ((chosen_one.offensive_moves1[0][1])*chosen_one_damage_1*chosen_one.attack/100)
                        chosen_one.energy=chosen_one.energy-1
                        print(f"{chosen_one.name} used {chosen_one.offensive_moves1[0][0]}")
                        if chosen_one_damage1>1:
                            print("It's super effective")
                        elif chosen_one_damage1==0:
                            print("It's immune to it")
                        elif chosen_one_damage1<1:
                            print("It's not effective")
                        chosen_one_paralasys=random2.randint(1,100)
                        if chosen_one_paralasys<=chosen_one.offensive_moves1[0][4]:
                            print(f"{chosen_one.name} paralyzed {random_pokemon.name}")
                            chosen_one_paralasys_mode=True
                        chosen_one_burn=random2.randint(1,100)
                        if chosen_one_burn<=chosen_one.offensive_moves1[0][5]:
                            print(f"{chosen_one.name} burned {random_pokemon.name}")
                            chosen_one_burn_mode=True
                        chosen_one_freeze=random2.randint(1,100)
                        if chosen_one_freeze<=chosen_one.offensive_moves1[0][6]:
                            print(f"{chosen_one.name} froze {random_pokemon.name}")
                            chosen_one_freeze_mode=True
                        chosen_one_confusion_effect(chosen_one, chosen_one.offensive_moves1[0][7])
                        chosen_one_poison_effect(chosen_one.offensive_moves1[0][8])
                        chosen_one_badly_poison_effect(chosen_one.offensive_moves1[0][9])
                        break
                    elif choice=="2":
                        random_pokemon.hp= random_pokemon.hp - ((chosen_one.offensive_moves2[0][1])*chosen_one_damage_2*chosen_one.attack/100)
                        chosen_one.energy=chosen_one.energy-1
                        print(f"{chosen_one.name} used {chosen_one.offensive_moves2[0][0]}")
                        if chosen_one_damage2>1:
                            print("It's super effective")
                        elif chosen_one_damage2==0:
                            print("It's immune to it")
                        elif chosen_one_damage2<1:
                            print("It's not effective")
                        chosen_one_paralasys=random2.randint(1,100)
                        if chosen_one_paralasys<=chosen_one.offensive_moves2[0][4]:
                            print(f"{chosen_one.name} paralyzed {random_pokemon.name}")
                            chosen_one_paralasys_mode=True
                        chosen_one_burn=random2.randint(1,100)
                        if chosen_one_burn<=chosen_one.offensive_moves2[0][5]:
                            print(f"{chosen_one.name} burned {random_pokemon.name}")
                            chosen_one_burn_mode=True
                        chosen_one_freeze=random2.randint(1,100)
                        if chosen_one_freeze<=chosen_one.offensive_moves2[0][6]:
                            print(f"{chosen_one.name} froze {random_pokemon.name}")
                            chosen_one_freeze_mode=True
                        chosen_one_confusion_effect(chosen_one, chosen_one.offensive_moves2[0][7])
                        chosen_one_poison_effect(chosen_one.offensive_moves2[0][8])
                        chosen_one_badly_poison_effect(chosen_one.offensive_moves2[0][9])
                        break
                    elif choice=="3":
                        random_pokemon.hp= random_pokemon.hp - ((chosen_one.offensive_moves3[0][1])*chosen_one_damage_3*chosen_one.attack/100)
                        chosen_one.energy=chosen_one.energy-1
                        print(f"{chosen_one.name} used {chosen_one.offensive_moves3[0][0]}")
                        if chosen_one_damage3>1:
                            print("It's super effective")
                        elif chosen_one_damage3==0:
                            print("It's immune to it")
                        elif chosen_one_damage3<1:
                            print("It's not effective")
                        chosen_one_paralasys=random2.randint(1,100)
                        if chosen_one_paralasys<=chosen_one.offensive_moves3[0][4]:
                            print(f"{chosen_one.name} paralyzed {random_pokemon.name}")
                            chosen_one_paralasys_mode=True
                        chosen_one_burn=random2.randint(1,100)
                        if chosen_one_burn<=chosen_one.offensive_moves3[0][5]:
                            print(f"{chosen_one.name} burned {random_pokemon.name}")
                            chosen_one_burn_mode=True
                        chosen_one_freeze=random2.randint(1,100)
                        if chosen_one_freeze<=chosen_one.offensive_moves3[0][6]:
                            print(f"{chosen_one.name} froze {random_pokemon.name}")
                            chosen_one_freeze_mode=True
                        chosen_one_confusion_effect(chosen_one, chosen_one.offensive_moves3[0][7])
                        chosen_one_poison_effect(chosen_one.offensive_moves3[0][8])
                        chosen_one_badly_poison_effect(chosen_one.offensive_moves3[0][9])
                        break
                    elif choice=="4":
                        chosen_one_check=chosen_one.offensive_moves1[0][1]
                        random_pokemon.offensive_moves1[0][1]= (1 - chosen_one.defensive_moves1[0][1]) * random_pokemon.offensive_moves1[0][1]
                        random_pokemon.offensive_moves2[0][1]= (1 - chosen_one.defensive_moves1[0][1]) * random_pokemon.offensive_moves2[0][1]
                        random_pokemon.offensive_moves3[0][1]= (1 - chosen_one.defensive_moves1[0][1]) * random_pokemon.offensive_moves3[0][1]
                        chosen_one.offensive_moves1[0][1]=(1+chosen_one.defensive_moves1[0][3])*chosen_one.offensive_moves1[0][1]
                        chosen_one.offensive_moves2[0][1]=(1+chosen_one.defensive_moves1[0][3])*chosen_one.offensive_moves2[0][1]
                        chosen_one.offensive_moves3[0][1]=(1+chosen_one.defensive_moves1[0][3])*chosen_one.offensive_moves3[0][1]
                        chosen_one.offensive_moves1[0][2]=(1+chosen_one.defensive_moves1[0][3])*chosen_one.offensive_moves1[0][2]
                        chosen_one.offensive_moves2[0][2]=(1+chosen_one.defensive_moves1[0][3])*chosen_one.offensive_moves2[0][2]
                        chosen_one.offensive_moves3[0][2]=(1+chosen_one.defensive_moves1[0][3])*chosen_one.offensive_moves3[0][2]
                        chosen_one_hp=chosen_one.hp
                        chosen_one.hp= (chosen_one.defensive_moves1[0][2] / 100 * chosen_one.max_hp) + chosen_one.hp
                        chosen_one_speed=chosen_one.speed
                        chosen_one.speed=(1+chosen_one.defensive_moves1[0][5])*chosen_one.speed
                        print(f"{chosen_one.name} used {chosen_one.defensive_moves1[0][0]}")
                        if chosen_one_speed<chosen_one.speed:
                            print(f"{chosen_one.name}'s speed increased")
                        if chosen_one.defensive_moves1[0][3]==None:
                            random_pokemon.offensive_moves1[0][2]=(1-chosen_one.defensive_moves1[0][1])*random_pokemon.offensive_moves1[0][2]
                            random_pokemon.offensive_moves2[0][2]=(1-chosen_one.defensive_moves1[0][1])*random_pokemon.offensive_moves2[0][2]
                            random_pokemon.offensive_moves3[0][2]=(1-chosen_one.defensive_moves1[0][1])*random_pokemon.offensive_moves3[0][2]
                        if chosen_one_check<chosen_one.offensive_moves1[0][1]:
                            print(f"{chosen_one.name}'s attack increased")
                        if chosen_one.hp>chosen_one.max_hp:
                            chosen_one.hp=chosen_one.max_hp
                        chosen_one.energy=chosen_one.energy-3
                
                        if random_pokemon_damage_check>random_pokemon.offensive_moves1[0][1]:
                            print(f"{chosen_one.name}'s defence increased")
                        if chosen_one.hp>chosen_one_hp:
                            print(f"{chosen_one.name}'s hp increased")
                        
                        chosen_one_paralasys=random2.randint(1,100)
                        if chosen_one_paralasys<=chosen_one.defensive_moves1[0][6]:
                            print(f"{chosen_one.name} paralyzed {random_pokemon.name}")
                            chosen_one_paralasys_mode=True
                        chosen_one_burn=random2.randint(1,100)
                        if chosen_one_burn<=chosen_one.defensive_moves1[0][7]:
                            print(f"{chosen_one.name} burned {random_pokemon.name}")
                            chosen_one_burn_mode=True
                        chosen_one_freeze=random2.randint(1,100)
                        if chosen_one_freeze<=chosen_one.defensive_moves1[0][8]:
                            print(f"{chosen_one.name} froze {random_pokemon.name}")
                            chosen_one_freeze_mode=True
                        chosen_one_confusion_effect(chosen_one, chosen_one.defensive_moves1[0][9])
                        chosen_one_sleep_effect(chosen_one.defensive_moves1[0][10])
                        chosen_one_poison_effect(chosen_one.defensive_moves1[0][11])
                        chosen_one_badly_poison_effect(chosen_one.defensive_moves1[0][12])
                        round1=0
                        round2=0
                        round3=0
                        break
                    elif choice=="5":
                        chosen_one_check=chosen_one.offensive_moves2[0][1]
                        random_pokemon.offensive_moves1[0][1]= (1 - chosen_one.defensive_moves2[0][1]) * random_pokemon.offensive_moves1[0][1]
                        random_pokemon.offensive_moves2[0][1]= (1 - chosen_one.defensive_moves2[0][1]) * random_pokemon.offensive_moves2[0][1]
                        random_pokemon.offensive_moves3[0][1]= (1 - chosen_one.defensive_moves2[0][1]) * random_pokemon.offensive_moves3[0][1]
                        chosen_one.offensive_moves1[0][1]=(1+chosen_one.defensive_moves2[0][3])*chosen_one.offensive_moves1[0][1]
                        chosen_one.offensive_moves2[0][1]=(1+chosen_one.defensive_moves2[0][3])*chosen_one.offensive_moves2[0][1]
                        chosen_one.offensive_moves3[0][1]=(1+chosen_one.defensive_moves2[0][3])*chosen_one.offensive_moves3[0][1]
                        chosen_one.offensive_moves1[0][2]=(1+chosen_one.defensive_moves2[0][3])*chosen_one.offensive_moves1[0][2]
                        chosen_one.offensive_moves2[0][2]=(1+chosen_one.defensive_moves2[0][3])*chosen_one.offensive_moves2[0][2]
                        chosen_one.offensive_moves3[0][2]=(1+chosen_one.defensive_moves2[0][3])*chosen_one.offensive_moves3[0][2]
                        chosen_one_hp=chosen_one.hp
                        chosen_one.hp= (chosen_one.defensive_moves2[0][2] / 100 * chosen_one.max_hp) + chosen_one.hp
                        chosen_one_speed=chosen_one.speed
                        chosen_one.speed=(1+chosen_one.defensive_moves1[0][5])*chosen_one.speed
                        if chosen_one_speed<chosen_one.speed:
                            print(f"{chosen_one.name}'s speed increased")
                        if chosen_one.defensive_moves2[0][3]==None:
                            random_pokemon.offensive_moves1[0][2]=(1-chosen_one.defensive_moves2[0][1])*random_pokemon.offensive_moves1[0][2]
                            random_pokemon.offensive_moves2[0][2]=(1-chosen_one.defensive_moves2[0][1])*random_pokemon.offensive_moves2[0][2]
                            random_pokemon.offensive_moves3[0][2]=(1-chosen_one.defensive_moves2[0][1])*random_pokemon.offensive_moves3[0][2]
                        print(f"{chosen_one.name} used {chosen_one.defensive_moves2[0][0]}")                                     
                        if chosen_one.hp>chosen_one.max_hp:
                            chosen_one.hp=chosen_one.max_hp
                        if chosen_one_check<chosen_one.offensive_moves2[0][1]:
                            print(f"{chosen_one.name}'s attack increased")
                        chosen_one.energy=chosen_one.energy-3
                        if random_pokemon_damage_check>random_pokemon.offensive_moves1[0][1]:
                            print(f"{chosen_one.name}'s defence increased")
                        if chosen_one.hp>chosen_one_hp:
                            print(f"{chosen_one.name}'s hp increased")
                        
                        chosen_one_paralasys=random2.randint(1,100)
                        if chosen_one_paralasys<=chosen_one.defensive_moves2[0][6]:
                            print(f"{chosen_one.name} paralyzed {random_pokemon.name}")
                            chosen_one_paralasys_mode=True
                        chosen_one_burn=random2.randint(1,100)
                        if chosen_one_burn<=chosen_one.defensive_moves2[0][7]:
                            print(f"{chosen_one.name} burned {random_pokemon.name}")
                            chosen_one_burn_mode=True
                        chosen_one_freeze=random2.randint(1,100)
                        if chosen_one_freeze<=chosen_one.defensive_moves2[0][8]:
                            print(f"{chosen_one.name} froze {random_pokemon.name}")
                            chosen_one_freeze_mode=True
                        chosen_one_confusion_effect(chosen_one, chosen_one.defensive_moves2[0][9]) 
                        chosen_one_sleep_effect(chosen_one.defensive_moves2[0][10])
                        chosen_one_poison_effect(chosen_one.defensive_moves2[0][11])
                        chosen_one_badly_poison_effect(chosen_one.defensive_moves2[0][12])
                        round1=0
                        round2=0
                        round3=0
                        break
                    else:
                        print("You gave an invalid move try again\n")
                        choice=input("What is your move? Note:Do your moves in order from 1 to 6. 1 being the first offensive move and 6 being a heal." )
        #burn type check
        for i in range(len(random_pokemon.element)):
            if random_pokemon.element[i]=="Fire" and chosen_one_burn_mode==True:
                chosen_one_burn_mode==False
                print(f"{random_pokemon.name} isn't affected by burn")
        for i in range(len(chosen_one.element)):
            if chosen_one.element[i]=="Fire" and random_pokemon_burn_mode==True:
                random_pokemon_burn_mode==False
                print(f"{chosen_one.name} isn't affected by burn")
        
        if chosen_one.hp<=0:
            print("You lost")
            break
        elif random_pokemon.hp<=0:
            print("You won")
            break
        chosen_one.hp=int(chosen_one.hp)
        random_pokemon.hp=int(random_pokemon.hp)
        round1+=1
        round4+=1
        time.sleep(1)
        #AI's turn
        chosen_one.hp=int(chosen_one.hp)
        random_pokemon.hp=int(random_pokemon.hp)
        random_pokemon_damage_check=random_pokemon.offensive_moves1[0][1]
        chosen_one_damage_check=chosen_one.offensive_moves1[0][1]
        if random_pokemon.energy<=0:
            random_pokemon.energy=0
        print(f"""{chosen_one.name}   hp:{chosen_one.hp}   energy:{chosen_one.energy} heals:{chosen_one.heal}
{random_pokemon.name}   hp:{random_pokemon.hp}   energy:{random_pokemon.energy} heals:{random_pokemon.heal}""")
        print()
        round6=round4-round5
        if round3==random_pokemon.defensive_moves2[0][4] and random_pokemon.defensive_moves2[0][4]!=None:
            #prevents the defensive moves from being too OP
            chosen_one.offensive_moves1[0][1]=chosen_one.offensive_moves1[0][2]
            chosen_one.offensive_moves2[0][1]=chosen_one.offensive_moves2[0][2]
            chosen_one.offensive_moves3[0][1]=chosen_one.offensive_moves3[0][2]
        if round3==random_pokemon.defensive_moves1[0][4] and random_pokemon.defensive_moves1[0][4]!=None:
            #prevents the defensive moves from being too OP
            chosen_one.offensive_moves1[0][1]=chosen_one.offensive_moves1[0][2]
            chosen_one.offensive_moves2[0][1]=chosen_one.offensive_moves2[0][2]
            chosen_one.offensive_moves3[0][1]=chosen_one.offensive_moves3[0][2]
        if chosen_one_paralasys_number==5:
            chosen_one_paralasys_mode=False
            chosen_one_paralasys_number=0
        if chosen_one_paralasys_mode==True and chosen_one_paralasys_number<=5:
            chosen_one_paralasys_number+=1
            print(f"{random_pokemon.name} is paralyzed")
        if chosen_one_freeze_mode==True:
            freeze_chance=random2.randint(1,256)
            if freeze_chance<=25:
                chosen_one_freeze_mode==False
                print(f"{random_pokemon.name} escaped the ice")
            else:
                print(f"{random_pokemon.name} is frozen")
        if chosen_one_sleep_mode[-1]==True:
            if chosen_one_sleep_number==0:
                print(f"{random_pokemon.name} is fast sleep")
                chosen_one_sleep_number+=1
            else:
                wake_up=random2.randint(1, 5-chosen_one_sleep_number)
                if wake_up==1:
                    print(f"{random_pokemon.name} woke up")
                    chosen_one_sleep_number=0
                    chosen_one_sleep_mode.append(False)
                else:
                    print(f"{random_pokemon.name} is fast sleep")
                    chosen_one_sleep_number+=1
        if chosen_one_paralasys_mode==False and chosen_one_freeze_mode==False and chosen_one_sleep_mode[-1]==False:
            if chosen_one_confusion_mode[-1]==True and chosen_one_confusion_number<=4:
                spin_the_wheel=random2.randint(1,2)
                if spin_the_wheel==1:
                    print(f"{random_pokemon.name} is confused")
                    random_pokemon.hp-=((random_pokemon.offensive_moves1[0][1]+random_pokemon.offensive_moves2[0][1]+random_pokemon.offensive_moves3[0][1])*random_pokemon.attack/100/3)
                    chosen_one_confusion_number+=1
                if spin_the_wheel==2:
                    chosen_one_confusion_number+=1
                    AI_choice=random2.randint(1,3)
                    if AI_choice==1:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage_1*random_pokemon.attack/100)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                        if random_pokemon_damage1>1:
                            print("It's super effective")
                        elif random_pokemon_damage1==0:
                            print("It's immune to it")
                        elif random_pokemon_damage1<1:
                            print("It's not effective")
                        random_pokemon_paralasys=random2.randint(1,100)
                        if random_pokemon_paralasys<=random_pokemon.offensive_moves1[0][4]:
                            print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                            random_pokemon_paralasys_mode=True
                        random_pokemon_burn=random2.randint(1,100)
                        if random_pokemon_burn<=random_pokemon.offensive_moves1[0][5]:
                            print(f"{random_pokemon.name} burned {chosen_one.name}")
                            random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                        if random_pokemon_freeze<=random_pokemon.offensive_moves1[0][6]:
                            print(f"{random_pokemon.name} froze {chosen_one.name}")
                            random_pokemon_freeze_mode=True
                        random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves1[0][7])
                        random_pokemon_poison_effect(1)
                        random_pokemon_badly_poison_effect(1)
                        print()
                    elif AI_choice==2:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage_2*random_pokemon.attack/100 )
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                        if random_pokemon_damage2>1:
                            print("It's super effective")
                        elif random_pokemon_damage2==0:
                                print("It's immune to it")
                        elif random_pokemon_damage2<1:
                            print("It's not effective")
                        random_pokemon_paralasys=random2.randint(1,100)
                        if random_pokemon_paralasys<=random_pokemon.offensive_moves2[0][4]:
                            print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                            random_pokemon_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                        if random_pokemon_burn<=random_pokemon.offensive_moves2[0][5]:
                            print(f"{random_pokemon.name} burned {chosen_one.name}")
                            random_pokemon_burn_mode=True
                        random_pokemon_freeze=random2.randint(1,100)
                        if random_pokemon_freeze<=random_pokemon.offensive_moves2[0][6]:
                            print(f"{random_pokemon.name} froze {chosen_one.name}")
                            random_pokemon_freeze_mode=True
                        random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves2[0][7])
                        random_pokemon_poison_effect(2)
                        random_pokemon_badly_poison_effect(2)
                        print()
                    else:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage_3*random_pokemon.attack/100)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                        if random_pokemon_damage3>1:
                            print("It's super effective")
                        elif random_pokemon_damage3==0:
                            print("It's immune to it")
                        elif random_pokemon_damage3<1:
                            print("It's not effective")
                        random_pokemon_paralasys=random2.randint(1,100)
                        if random_pokemon_paralasys<=random_pokemon.offensive_moves3[0][4]:
                            print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                            random_pokemon_paralasys_mode=True 
                        random_pokemon_burn=random2.randint(1,100)
                        if random_pokemon_burn<=random_pokemon.offensive_moves3[0][5]:
                            print(f"{random_pokemon.name} burned {chosen_one.name}")
                            random_pokemon_burn_mode=True
                        random_pokemon_freeze=random2.randint(1,100)
                        if random_pokemon_freeze<=random_pokemon.offensive_moves3[0][6]:
                            print(f"{random_pokemon.name} froze {chosen_one.name}")
                            random_pokemon_freeze_mode=True
                        random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves3[0][7])
                        random_pokemon_poison_effect(3)
                        random_pokemon_badly_poison_effect(3)
                        print()
            elif random_pokemon.energy<=0:
                print(f"{random_pokemon.name} used struggle")
                print()
                random_pokemon.hp=3/4*random_pokemon.hp
                chosen_one.hp=chosen_one.hp-((random_pokemon.offensive_moves1[0][1]+random_pokemon.offensive_moves2[0][1]+random_pokemon.offensive_moves3[0][1])*random_pokemon.attack/100/3)
            elif random_pokemon.energy>=0:
                random_pokemon_hp=random_pokemon.hp
                random_pokemon_damage_check=random_pokemon.offensive_moves1[0][1]
                chosen_one_damage_check=chosen_one.offensive_moves1[0][1]
                random_pokemon_speed=random_pokemon.speed
                if chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage_1)<=0:
                    chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage_1*random_pokemon.attack/100)
                    random_pokemon.energy-=1
                    print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                    if random_pokemon_damage1>1:
                        print("It's super effective")
                    elif random_pokemon_damage1==0:
                        print("It's immune to it")
                    elif random_pokemon_damage1<1:
                        print("It's not effective")
                    random_pokemon_paralasys=random2.randint(1,100)
                    if random_pokemon_paralasys<=random_pokemon.offensive_moves1[0][4]:
                        print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                        random_pokemon_paralasys_mode=True

                    random_pokemon_burn=random2.randint(1,100)
                    if random_pokemon_burn<=random_pokemon.offensive_moves1[0][5]:
                        print(f"{random_pokemon.name} burned {chosen_one.name}")
                        random_pokemon_burn_mode=True
                    random_pokemon_freeze=random2.randint(1,100)
                    if random_pokemon_freeze<=random_pokemon.offensive_moves1[0][6]:
                        print(f"{random_pokemon.name} froze {chosen_one.name}")
                        random_pokemon_freeze_mode=True
                    random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves1[0][7])
                    random_pokemon_poison_effect(1)
                    random_pokemon_badly_poison_effect(1)
                    print()
                elif chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage_2)<=0:
                    chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage_2*random_pokemon.attack/100)
                    random_pokemon.energy-=1
                    print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                    if random_pokemon_damage2>1:
                        print("It's super effective")
                    elif random_pokemon_damage2==0:
                        print("It's immune to it")
                    elif random_pokemon_damage2<1:
                        print("It's not effective")
                    random_pokemon_paralasys=random2.randint(1,100)
                    if random_pokemon_paralasys<=random_pokemon.offensive_moves2[0][4]:
                        print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                        random_pokemon_paralasys_mode=True
                    random_pokemon_burn=random2.randint(1,100)
                    if random_pokemon_burn<=random_pokemon.offensive_moves2[0][5]:
                        print(f"{random_pokemon.name} burned {chosen_one.name}")
                        random_pokemon_burn_mode=True
                    random_pokemon_freeze=random2.randint(1,100)
                    if random_pokemon_freeze<=random_pokemon.offensive_moves2[0][6]:
                        print(f"{random_pokemon.name} froze {chosen_one.name}")
                        random_pokemon_freeze_mode=True
                    random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves2[0][7])
                    random_pokemon_poison_effect(2)
                    random_pokemon_badly_poison_effect(2)
                    print()
                elif chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage3)<=0:
                    chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage_3*random_pokemon.attack/100)
                    random_pokemon.energy-=1
                    print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                    if random_pokemon_damage3>1:
                        print("It's super effective")
                    elif random_pokemon_damage3==0:
                        print("It's immune to it")
                    elif random_pokemon_damage3<1:
                        print("It's not effective") 
                    random_pokemon_paralasys=random2.randint(1,100)
                    if random_pokemon_paralasys<=random_pokemon.offensive_moves3[0][4]:
                        print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                        random_pokemon_paralasys_mode=True 
                    random_pokemon_burn=random2.randint(1,100)
                    if random_pokemon_burn<=random_pokemon.offensive_moves3[0][5]:
                        print(f"{random_pokemon.name} burned {chosen_one.name}")
                        random_pokemon_burn_mode=True
                    random_pokemon_freeze=random2.randint(1,100)
                    if random_pokemon_freeze<=random_pokemon.offensive_moves3[0][6]:
                        print(f"{random_pokemon.name} froze {chosen_one.name}")
                        random_pokemon_freeze_mode=True
                    random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves3[0][7])
                    random_pokemon_poison_effect(3)
                    random_pokemon_badly_poison_effect(3)
                    print()
                elif random_pokemon.hp<=random_pokemon.max_hp/4:
                    if random_pokemon.hp-chosen_one.offensive_moves1[0][2]<=0 and random_pokemon.heal>0:
                        random_pokemon.hp+=100
                        print(f"AI used a heal on {random_pokemon.name}")
                        if random_pokemon.hp>random_pokemon.max_hp:
                            random_pokemon.hp=random_pokemon.max_hp
                        random_pokemon.heal-=1
                    elif random_pokemon.hp-chosen_one.offensive_moves1[0][2]<=0 and random_pokemon.defensive_moves2[0][2]>0 or random_pokemon.hp-chosen_one.offensive_moves1[0][2]<=0 and random_pokemon.defensive_moves2[0][2]>0 or random_pokemon.hp-chosen_one.offensive_moves1[0][2]<=0 and random_pokemon.defensive_moves2[0][2]>0 or random_pokemon.defensive_moves2[0][2]>0 and (random_pokemon.defensive_moves2[0][2] / 100 * random_pokemon.max_hp)>((chosen_one.offensive_moves1[0][1]*chosen_one_damage1+chosen_one.offensive_moves2[0][1]*chosen_one_damage2+chosen_one.offensive_moves3[0][1]*chosen_one_damage3)/3):
                        random_pokemon_speed=random_pokemon.speed
                        random_pokemon.speed=(1+random_pokemon.defensive_moves1[0][5])*random_pokemon.speed
                        random_pokemon_hp=random_pokemon.hp
                        random_pokemon_check=random_pokemon.offensive_moves1[0][1]
                        random_pokemon.hp=(random_pokemon.defensive_moves1[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                        chosen_one.offensive_moves1[0][1]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][1]
                        chosen_one.offensive_moves2[0][1]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][1]
                        chosen_one.offensive_moves3[0][1]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][1]
                        random_pokemon.offensive_moves1[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves1[0][1]
                        random_pokemon.offensive_moves2[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves2[0][1]
                        random_pokemon.offensive_moves3[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves3[0][1]
                        random_pokemon.offensive_moves1[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves1[0][1]
                        random_pokemon.offensive_moves2[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves2[0][1]
                        random_pokemon.offensive_moves3[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves3[0][1]
                        print(f"{random_pokemon.name} used {random_pokemon.defensive_moves1[0][0]}")
                        if random_pokemon_speed<random_pokemon.speed:
                            print(f"{random_pokemon.name}'s speed increased")
                        if random_pokemon.hp>random_pokemon.max_hp:
                            random_pokemon.hp=random_pokemon.max_hp
                        if random_pokemon_check<random_pokemon.offensive_moves1[0][1]:
                            print(f"{random_pokemon.name}'s attack increased")
                        if random_pokemon_hp<random_pokemon.hp:
                            print(f"{random_pokemon.name} healed")
                        if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                            print(f"{random_pokemon.name}'s defence increased")
                        random_pokemon_paralasys=random2.randint(1,100)
                        if random_pokemon_paralasys<=random_pokemon.defensive_moves1[0][6]:
                            print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                            chosen_one_paralasys_mode=True
                        random_pokemon_burn=random2.randint(1,100)
                        if random_pokemon_burn<=random_pokemon.defensive_moves1[0][7]:
                            print(f"{random_pokemon.name} burned {chosen_one.name}")
                            random_pokemon_burn_mode=True
                        random_pokemon_freeze=random2.randint(1,100)
                        if random_pokemon_freeze<=random_pokemon.defensive_moves1[0][8]:
                            print(f"{random_pokemon.name} froze {chosen_one.name}")
                            random_pokemon_freeze_mode=True
                        random_pokemon_confusion_effect(random_pokemon, random_pokemon.defensive_moves1[0][9])
                        random_pokemon_sleep_effect(random_pokemon.defensive_moves1[0][10])
                        random_pokemon_poison_effect(4)
                        random_pokemon_badly_poison_effect(4)
                        print()
                        if random_pokemon.defensive_moves1[0][4]==None:
                            chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][2]
                            chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][2]
                            chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][2]
                        random_pokemon.energy-=3
                        round4=0
                        round5=0
                        round6=0
                    elif random_pokemon.hp-chosen_one.offensive_moves1[0][2]<=0 and random_pokemon.defensive_moves2[0][2]>0 or random_pokemon.hp-chosen_one.offensive_moves1[0][2]<=0 and random_pokemon.defensive_moves2[0][2]>0 or random_pokemon.hp-chosen_one.offensive_moves3[0][2]<=0 and random_pokemon.defensive_moves2[0][2]>0 or random_pokemon.defensive_moves2[0][2]>0 and (random_pokemon.defensive_moves2[0][2] / 100 * random_pokemon.max_hp)>((chosen_one.offensive_moves1[0][1]*chosen_one_damage1+chosen_one.offensive_moves2[0][1]*chosen_one_damage2+chosen_one.offensive_moves3[0][1]*chosen_one_damage3)/3):
                        random_pokemon_speed=random_pokemon.speed
                        random_pokemon.speed=(1+random_pokemon.defensive_moves2[0][5])*random_pokemon.speed
                        random_pokemon_hp=random_pokemon.hp
                        random_pokemon_check=random_pokemon.offensive_moves2[0][1]
                        random_pokemon.hp=(random_pokemon.defensive_moves2[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                        chosen_one.offensive_moves1[0][1]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves1[0][1]
                        chosen_one.offensive_moves2[0][1]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves2[0][1]
                        chosen_one.offensive_moves3[0][1]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves3[0][1]
                        random_pokemon.offensive_moves1[0][1]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves1[0][1]
                        random_pokemon.offensive_moves2[0][1]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves2[0][1]
                        random_pokemon.offensive_moves3[0][1]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves3[0][1]
                        random_pokemon.offensive_moves1[0][2]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves1[0][2]
                        random_pokemon.offensive_moves2[0][2]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves2[0][2]
                        random_pokemon.offensive_moves3[0][2]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves3[0][2]
                        print(f"{random_pokemon.name} used {random_pokemon.defensive_moves2[0][0]}")
                        if random_pokemon_speed<random_pokemon.speed:
                            print(f"{random_pokemon.name}'s speed increased")
                        if random_pokemon_check<random_pokemon.offensive_moves2[0][1]:
                            print(f"{random_pokemon.name}'s attack increased")
                        if random_pokemon.hp>random_pokemon.max_hp:
                            random_pokemon.hp=random_pokemon.max_hp
                        if random_pokemon_hp<random_pokemon.hp:
                            print(f"{random_pokemon.name} healed")
                        if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                            print(f"{random_pokemon.name}'s defence increased")
                        random_pokemon_paralasys=random2.randint(1,100)
                        if random_pokemon_paralasys<=random_pokemon.defensive_moves2[0][6]:
                            print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                            chosen_one_paralasys_mode=True
                        random_pokemon_burn=random2.randint(1,100)
                        if random_pokemon_burn<=random_pokemon.defensive_moves2[0][7]:
                            print(f"{random_pokemon.name} burned {chosen_one.name}")
                            random_pokemon_burn_mode=True
                        random_pokemon_freeze=random2.randint(1,100)
                        if random_pokemon_freeze<=random_pokemon.defensive_moves2[0][8]:
                            print(f"{random_pokemon.name} froze {chosen_one.name}")
                            random_pokemon_freeze_mode=True
                        random_pokemon_confusion_effect(random_pokemon, random_pokemon.defensive_moves2[0][9])
                        random_pokemon_sleep_effect(random_pokemon.defensive_moves2[0][10])
                        random_pokemon_poison_effect(5)
                        random_pokemon_badly_poison_effect(5)
                        print()
                        if random_pokemon.defensive_moves1[0][4]==None:
                            chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves1[0][2]
                            chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves2[0][2]
                            chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves3[0][2]
                        
                        random_pokemon.energy-=3
                        round4=0
                        round5=0
                        round6=0
                    else:
                        AI_choice=random2.randint(1,3)
                        if AI_choice==1:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage_1*random_pokemon.attack/100)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                            if random_pokemon_damage1>1:
                                print("It's super effective")
                            elif random_pokemon_damage1==0:
                                print("It's immune to it")
                            elif random_pokemon_damage1<1:
                                print("It's not effective")
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.offensive_moves1[0][4]:
                                print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                random_pokemon_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.offensive_moves1[0][5]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.offensive_moves1[0][6]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves1[0][7])
                            random_pokemon_poison_effect(1)
                            random_pokemon_badly_poison_effect(1)
                            print()
                        elif AI_choice==2:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage_2*random_pokemon.attack/100 )
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                            if random_pokemon_damage2>1:
                                print("It's super effective")
                            elif random_pokemon_damage2==0:
                                print("It's immune to it")
                            elif random_pokemon_damage2<1:
                                print("It's not effective")
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.offensive_moves2[0][4]:
                                print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                random_pokemon_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.offensive_moves2[0][5]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.offensive_moves2[0][6]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves2[0][7])
                            random_pokemon_poison_effect(2)
                            random_pokemon_badly_poison_effect(2)
                            print()
                        else:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage_3*random_pokemon.attack/100)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                            if random_pokemon_damage3>1:
                                print("It's super effective")
                            elif random_pokemon_damage3==0:
                                print("It's immune to it")
                            elif random_pokemon_damage3<1:
                                print("It's not effective")
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.offensive_moves3[0][4]:
                                print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                random_pokemon_paralasys_mode=True 
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.offensive_moves3[0][5]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.offensive_moves3[0][6]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves3[0][7])
                            random_pokemon_poison_effect(3)
                            random_pokemon_badly_poison_effect(3)
                            print()
                elif random_pokemon.hp<=random_pokemon.max_hp/2:
                    if round6>=2:
                        random_pokemon_hp=random_pokemon.hp
                        if random_pokemon.defensive_moves1[0][1]>0:
                            random_pokemon.speed=(1+random_pokemon.defensive_moves1[0][5])*random_pokemon.speed
                            random_pokemon_check=random_pokemon.offensive_moves1[0][1]
                            chosen_one.offensive_moves1[0][1]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][1]
                            chosen_one.offensive_moves2[0][1]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][1]
                            chosen_one.offensive_moves3[0][1]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][1]
                            random_pokemon.offensive_moves1[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves1[0][1]
                            random_pokemon.offensive_moves2[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves2[0][1]
                            random_pokemon.offensive_moves3[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves3[0][1]
                            random_pokemon.offensive_moves1[0][2]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves1[0][2]
                            random_pokemon.offensive_moves2[0][2]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves2[0][2]
                            random_pokemon.offensive_moves3[0][2]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves3[0][2]
                            print(f"{random_pokemon.name} used {random_pokemon.defensive_moves1[0][0]}")
                            if random_pokemon_speed<random_pokemon.speed:
                                print(f"{random_pokemon.name}'s speed increased")
                            if random_pokemon.defensive_moves1[0][2]>0:
                                random_pokemon.hp=(random_pokemon.defensive_moves1[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                            if random_pokemon_check<random_pokemon.offensive_moves1[0][1]:
                                print(f"{random_pokemon.name}'s attack increased")
                            if random_pokemon.hp>random_pokemon.max_hp:
                                random_pokemon.hp=random_pokemon.max_hp
                            if random_pokemon_hp<random_pokemon.hp:
                                print(f"{random_pokemon.name} healed")
                            if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                                print(f"{random_pokemon.name}'s defence increased")
                            if random_pokemon.defensive_moves1[0][4]==None:
                                chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][2]
                                chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][2]
                                chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][2]
                            
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.defensive_moves1[0][6]:
                                print(f"{chosen_one.name} paralyzed {random_pokemon.name}")
                                chosen_one_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.defensive_moves1[0][7]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.defensive_moves1[0][8]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.defensive_moves1[0][9])
                            random_pokemon_sleep_effect(random_pokemon.defensive_moves1[0][10])
                            random_pokemon_poison_effect(4)
                            random_pokemon_badly_poison_effect(4)
                            random_pokemon.energy-=3
                            round4=0
                            round5=0
                            round6=0
                        elif random_pokemon.defensive_moves2[0][1]>0:
                            random_pokemon.speed=(1+random_pokemon.defensive_moves2[0][5])*random_pokemon.speed
                            random_pokemon_check=random_pokemon.offensive_moves1[0][1]
                            chosen_one.offensive_moves1[0][1]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves1[0][1]
                            chosen_one.offensive_moves2[0][1]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves2[0][1]
                            chosen_one.offensive_moves3[0][1]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves3[0][1]
                            random_pokemon.offensive_moves1[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves1[0][1]
                            random_pokemon.offensive_moves2[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves2[0][1]
                            random_pokemon.offensive_moves3[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves3[0][1]
                            random_pokemon.offensive_moves1[0][2]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves1[0][2]
                            random_pokemon.offensive_moves2[0][2]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves2[0][2]
                            random_pokemon.offensive_moves3[0][2]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves3[0][2]
                            print(f"{random_pokemon.name} used {random_pokemon.defensive_moves2[0][0]}")
                            if random_pokemon_speed<random_pokemon.speed:
                                print(f"{random_pokemon.name}'s speed increased")
                            if random_pokemon.defensive_moves1[0][2]>0:
                                random_pokemon.hp=(random_pokemon.defensive_moves2[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                            if random_pokemon.hp>random_pokemon.max_hp:
                                random_pokemon.hp=random_pokemon.max_hp
                            if random_pokemon_hp<random_pokemon.hp:
                                print(f"{random_pokemon.name} healed")
                            if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                                print(f"{random_pokemon.name}'s defence increased")
                            if random_pokemon_check<random_pokemon.offensive_moves1[0][1]:
                                print(f"{random_pokemon.name}'s attack increased")
                            if random_pokemon.defensive_moves2[0][4]==None:
                                chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][2]
                                chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][2]
                                chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][2]
                            
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.defensive_moves2[0][6]:
                                print(f"{chosen_one.name} paralyzed {random_pokemon.name}")
                                chosen_one_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.defensive_moves2[0][7]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.defensive_moves2[0][8]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.defensive_moves2[0][9])
                            random_pokemon_sleep_effect(random_pokemon.defensive_moves2[0][10])
                            random_pokemon_poison_effect(5)
                            random_pokemon_badly_poison_effect(5)
                            random_pokemon.energy-=3
                            round4=0
                            round5=0
                            round6=0
                        else:
                            AI_choice=random2.randint(1,3)
                            if AI_choice==1:
                                chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage_1*random_pokemon.attack/100)
                                random_pokemon.energy-=1
                                print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                                if random_pokemon_damage1>1:
                                    print("It's super effective")
                                elif random_pokemon_damage1==0:
                                    print("It's immune to it")
                                elif random_pokemon_damage1<1:
                                    print("It's not effective")
                                random_pokemon_paralasys=random2.randint(1,100)
                                if random_pokemon_paralasys<=random_pokemon.offensive_moves1[0][4]:
                                    print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                    random_pokemon_paralasys_mode=True
                                random_pokemon_burn=random2.randint(1,100)
                                if random_pokemon_burn<=random_pokemon.offensive_moves1[0][5]:
                                    print(f"{random_pokemon.name} burned {chosen_one.name}")
                                    random_pokemon_burn_mode=True
                                random_pokemon_freeze=random2.randint(1,100)
                                if random_pokemon_freeze<=random_pokemon.offensive_moves1[0][6]:
                                    print(f"{random_pokemon.name} froze {chosen_one.name}")
                                    random_pokemon_freeze_mode=True
                                random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves1[0][7])
                                random_pokemon_poison_effect(1)
                                random_pokemon_badly_poison_effect(1)
                            elif AI_choice==2:
                                chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage_2*random_pokemon.attack/100)
                                random_pokemon.energy-=1
                                print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                                if random_pokemon_damage2>1:
                                    print("It's super effective")
                                elif random_pokemon_damage2==0:
                                    print("It's immune to it")
                                elif random_pokemon_damage2<1:
                                    print("It's not effective")
                                random_pokemon_paralasys=random2.randint(1,100)
                                if random_pokemon_paralasys<=random_pokemon.offensive_moves2[0][4]:
                                    print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                    random_pokemon_paralasys_mode=True
                                random_pokemon_burn=random2.randint(1,100)
                                if random_pokemon_burn<=random_pokemon.offensive_moves2[0][5]:
                                    print(f"{random_pokemon.name} burned {chosen_one.name}")
                                    random_pokemon_burn_mode=True
                                random_pokemon_freeze=random2.randint(1,100)
                                if random_pokemon_freeze<=random_pokemon.offensive_moves2[0][6]:
                                    print(f"{random_pokemon.name} froze {chosen_one.name}")
                                    random_pokemon_freeze_mode=True
                                random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves2[0][7])
                                random_pokemon_poison_effect(2)
                                random_pokemon_badly_poison_effect(2)
                            else:
                                chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage_3*random_pokemon.attack/100)
                                random_pokemon.energy-=1
                                print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                                if random_pokemon_damage3>1:
                                    print("It's super effective")
                                elif random_pokemon_damage3==0:
                                    print("It's immune to it")
                                elif random_pokemon_damage3<1:
                                    print("It's not effective")
                                random_pokemon_paralasys=random2.randint(1,100)
                                if random_pokemon_paralasys<=random_pokemon.offensive_moves3[0][4]:
                                    print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                    random_pokemon_paralasys_mode=True
                                random_pokemon_burn=random2.randint(1,100)
                                if random_pokemon_burn<=random_pokemon.offensive_moves3[0][5]:
                                    print(f"{random_pokemon.name} burned {chosen_one.name}")
                                    random_pokemon_burn_mode=True
                                random_pokemon_freeze=random2.randint(1,100)
                                if random_pokemon_freeze<=random_pokemon.offensive_moves3[0][6]:
                                    print(f"{random_pokemon.name} froze {chosen_one.name}")
                                    random_pokemon_freeze_mode=True
                                random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves3[0][7])
                                random_pokemon_poison_effect(3)
                                random_pokemon_badly_poison_effect(3)
                    else:
                        AI_choice=random2.randint(1,3)
                        if AI_choice==1:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage_1*random_pokemon.attack/100)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                            if random_pokemon_damage1>1:
                                print("It's super effective")
                            elif random_pokemon_damage1==0:
                                print("It's immune to it")
                            elif random_pokemon_damage1<1:
                                print("It's not effective")
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.offensive_moves1[0][4]:
                                print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                random_pokemon_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.offensive_moves1[0][5]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.offensive_moves1[0][6]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves1[0][7])
                            random_pokemon_poison_effect(1)
                            random_pokemon_badly_poison_effect(1)
                        elif AI_choice==2:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage_2*random_pokemon.attack/100)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                            if random_pokemon_damage2>1:
                                print("It's super effective")
                            elif random_pokemon_damage2==0:
                                print("It's immune to it")
                            elif random_pokemon_damage2<1:
                                print("It's not effective")
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.offensive_moves2[0][4]:
                                print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                random_pokemon_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.offensive_moves2[0][5]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.offensive_moves2[0][6]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves2[0][7])
                            random_pokemon_poison_effect(2)
                            random_pokemon_badly_poison_effect(2)
                        else:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage_3*random_pokemon.attack/100)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                            if random_pokemon_damage3>1:
                                print("It's super effective")
                            elif random_pokemon_damage3==0:
                                print("It's immune to it")
                            elif random_pokemon_damage3<1:
                                print("It's not effective")
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.offensive_moves3[0][4]:
                                print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                random_pokemon_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.offensive_moves3[0][5]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.offensive_moves3[0][6]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves3[0][7])
                            random_pokemon_poison_effect(3)
                            random_pokemon_badly_poison_effect(3)
                    print()
                elif random_pokemon.max_hp/8*7<random_pokemon.hp:
                    random_pokemon_hp=random_pokemon.hp
                    if random_pokemon.defensive_moves1[0][3]>0:
                        random_pokemon.speed=(1+random_pokemon.defensive_moves1[0][5])*random_pokemon.speed
                        random_pokemon_check=random_pokemon.offensive_moves1[0][1]
                        chosen_one.offensive_moves1[0][1]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][1]
                        chosen_one.offensive_moves2[0][1]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][1]
                        chosen_one.offensive_moves3[0][1]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][1]
                        random_pokemon.offensive_moves1[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves1[0][1]
                        random_pokemon.offensive_moves2[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves2[0][1]
                        random_pokemon.offensive_moves3[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves3[0][1]
                        random_pokemon.offensive_moves1[0][2]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves1[0][2]
                        random_pokemon.offensive_moves2[0][2]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves2[0][2]
                        random_pokemon.offensive_moves3[0][2]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves3[0][2]
                        print(f"{random_pokemon.name} used {random_pokemon.defensive_moves1[0][0]}")
                        if random_pokemon_speed<random_pokemon.speed:
                            print(f"{random_pokemon.name}'s speed increased")
                        if random_pokemon.defensive_moves1[0][4]==None:
                            chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][2]
                            chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][2]
                            chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][2]
                        if random_pokemon.defensive_moves1[0][2]>0:
                            random_pokemon.hp=(chosen_one.defensive_moves1[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                        if random_pokemon_check<random_pokemon.offensive_moves1[0][1]:
                            print(f"{random_pokemon.name}'s attack increased")
                        if random_pokemon_hp<random_pokemon.hp:
                            print(f"{random_pokemon.name} healed")
                        if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                            print(f"{random_pokemon.name}'s defence increased")
                        random_pokemon_paralasys=random2.randint(1,100)
                        if random_pokemon_paralasys<=random_pokemon.defensive_moves1[0][6]:
                            print(f"{chosen_one.name} paralyzed {random_pokemon.name}")
                            chosen_one_paralasys_mode=True
                        random_pokemon_burn=random2.randint(1,100)
                        if random_pokemon_burn<=random_pokemon.defensive_moves1[0][7]:
                            print(f"{random_pokemon.name} burned {chosen_one.name}")
                            random_pokemon_burn_mode=True
                        random_pokemon_freeze=random2.randint(1,100)
                        if random_pokemon_freeze<=random_pokemon.defensive_moves1[0][8]:
                            print(f"{random_pokemon.name} froze {chosen_one.name}")
                            random_pokemon_freeze_mode=True
                        random_pokemon_confusion_effect(random_pokemon, random_pokemon.defensive_moves1[0][9])
                        random_pokemon_sleep_effect(random_pokemon.defensive_moves1[0][10])
                        random_pokemon_poison_effect(4)
                        random_pokemon_badly_poison_effect(4)
                        print()
                        random_pokemon.energy-=3
                        round4=0
                        round5=0
                        round6=0
                    elif random_pokemon.defensive_moves2[0][3]>0:
                        random_pokemon.speed=(1+random_pokemon.defensive_moves2[0][5])*random_pokemon.speed
                        random_pokemon_check=random_pokemon.offensive_moves2[0][1]
                        chosen_one.offensive_moves1[0][1]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves1[0][1]
                        chosen_one.offensive_moves2[0][1]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves2[0][1]
                        chosen_one.offensive_moves3[0][1]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves3[0][1]
                        random_pokemon.offensive_moves1[0][1]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves1[0][1]
                        random_pokemon.offensive_moves2[0][1]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves2[0][1]
                        random_pokemon.offensive_moves3[0][1]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves3[0][1]
                        random_pokemon.offensive_moves1[0][2]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves1[0][2]
                        random_pokemon.offensive_moves2[0][2]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves2[0][2]
                        random_pokemon.offensive_moves3[0][2]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves3[0][2]
                        print(f"{random_pokemon.name} used {random_pokemon.defensive_moves2[0][0]}")
                        if random_pokemon_speed<random_pokemon.speed:
                            print(f"{random_pokemon.name}'s speed increased")
                        if random_pokemon.defensive_moves2[0][4]==None:
                            chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][2]
                            chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][2]
                            chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][2]                    
                        if random_pokemon.defensive_moves2[0][2]>0:
                            random_pokemon.hp=(chosen_one.defensive_moves2[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                        if random_pokemon_check<random_pokemon.offensive_moves2[0][1]:
                            print(f"{random_pokemon.name}'s attack increased")
                        if random_pokemon_hp<random_pokemon.hp:
                            print(f"{random_pokemon.name} healed")
                        if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                            print(f"{random_pokemon.name}'s defence increased")
                        random_pokemon_paralasys=random2.randint(1,100)
                        if random_pokemon_paralasys<=random_pokemon.defensive_moves2[0][6]:
                            print(f"{chosen_one.name} paralyzed {random_pokemon.name}")
                            chosen_one_paralasys_mode=True
                        random_pokemon_burn=random2.randint(1,100)
                        if random_pokemon_burn<=random_pokemon.defensive_moves2[0][7]:
                            print(f"{random_pokemon.name} burned {chosen_one.name}")
                            random_pokemon_burn_mode=True
                        random_pokemon_freeze=random2.randint(1,100)
                        if random_pokemon_freeze<=random_pokemon.defensive_moves2[0][8]:
                            print(f"{random_pokemon.name} froze {chosen_one.name}")
                            random_pokemon_freeze_mode=True
                        random_pokemon_confusion_effect(random_pokemon, random_pokemon.defensive_moves2[0][9])
                        random_pokemon_sleep_effect(random_pokemon.defensive_moves2[0][10])
                        random_pokemon_poison_effect(5)
                        random_pokemon_badly_poison_effect(5)
                        print()
                        random_pokemon.energy-=3
                        round4=0
                        round5=0
                        round6=0
                    else:
                        AI_choice=random2.randint(1,3)
                        if AI_choice==1:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage_1*random_pokemon.attack/100)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                            if random_pokemon_damage1>1:
                                print("It's super effective")
                            elif random_pokemon_damage1==0:
                                print("It's immune to it")
                            elif random_pokemon_damage1<1:
                                print("It's not effective")
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.offensive_moves1[0][4]:
                                print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                random_pokemon_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.offensive_moves1[0][5]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.offensive_moves1[0][6]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves1[0][7])
                            random_pokemon_poison_effect(1)
                            random_pokemon_badly_poison_effect(1)
                            print()
                        elif AI_choice==2:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage_2*random_pokemon.attack/100)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                            if random_pokemon_damage2>1:
                                print("It's super effective")
                            elif random_pokemon_damage2==0:
                                print("It's immune to it")
                            elif random_pokemon_damage2<1:
                                print("It's not effective")
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.offensive_moves2[0][4]:
                                print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                random_pokemon_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.offensive_moves2[0][5]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.offensive_moves2[0][6]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves2[0][7])
                            random_pokemon_poison_effect(2)
                            random_pokemon_badly_poison_effect(2)
                            print()
                        else:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage_3*random_pokemon.attack/100)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                            if random_pokemon_damage3>1:
                                print("It's super effective")
                            elif random_pokemon_damage3==0:
                                print("It's immune to it")
                            elif random_pokemon_damage3<1:
                                print("It's not effective")
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.offensive_moves3[0][4]:
                                print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                random_pokemon_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.offensive_moves3[0][5]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.offensive_moves3[0][6]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves3[0][7])
                            random_pokemon_poison_effect(3)
                            random_pokemon_badly_poison_effect(3)
                            print()
                elif random_pokemon.speed<chosen_one.speed:
                    if (1+random_pokemon.defensive_moves1[0][5])*random_pokemon.speed>chosen_one.speed:
                        random_pokemon_speed=random_pokemon.speed
                        random_pokemon.speed=(1+random_pokemon.defensive_moves1[0][5])*random_pokemon.speed
                        random_pokemon_check=random_pokemon.offensive_moves1[0][1]
                        chosen_one.offensive_moves1[0][1]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][1]
                        chosen_one.offensive_moves2[0][1]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][1]
                        chosen_one.offensive_moves3[0][1]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][1]
                        random_pokemon.offensive_moves1[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves1[0][1]
                        random_pokemon.offensive_moves2[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves2[0][1]
                        random_pokemon.offensive_moves3[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves3[0][1]
                        random_pokemon.offensive_moves1[0][2]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves1[0][2]
                        random_pokemon.offensive_moves2[0][2]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves2[0][2]
                        random_pokemon.offensive_moves3[0][2]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves3[0][2]
                        print(f"{random_pokemon.name} used {random_pokemon.defensive_moves1[0][0]}")
                        if random_pokemon_speed<random_pokemon.speed:
                            print(f"{random_pokemon.name}'s speed increased")
                        if random_pokemon.defensive_moves1[0][2]>0:
                            random_pokemon.hp=(chosen_one.defensive_moves1[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                        if random_pokemon_check<random_pokemon.offensive_moves1[0][1]:
                            print(f"{random_pokemon.name}'s attack increased")
                        if random_pokemon_hp<random_pokemon.hp:
                            print(f"{random_pokemon.name} healed")
                        if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                            print(f"{random_pokemon.name}'s defence increased")
                        random_pokemon_paralasys=random2.randint(1,100)
                        if random_pokemon_paralasys<=random_pokemon.defensive_moves1[0][6]:
                            print(f"{chosen_one.name} paralyzed {random_pokemon.name}")
                            chosen_one_paralasys_mode=True
                        random_pokemon_burn=random2.randint(1,100)
                        if random_pokemon_burn<=random_pokemon.defensive_moves1[0][7]:
                            print(f"{random_pokemon.name} burned {chosen_one.name}")
                            random_pokemon_burn_mode=True
                        random_pokemon_freeze=random2.randint(1,100)
                        if random_pokemon_freeze<=random_pokemon.defensive_moves1[0][8]:
                            print(f"{random_pokemon.name} froze {chosen_one.name}")
                            random_pokemon_freeze_mode=True
                        random_pokemon_confusion_effect(random_pokemon, random_pokemon.defensive_moves1[0][9])
                        random_pokemon_sleep_effect(random_pokemon.defensive_moves1[0][10])
                        random_pokemon_poison_effect(4)
                        random_pokemon_badly_poison_effect(4)
                        print()
                        if random_pokemon.defensive_moves1[0][4]==None:
                            chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][2]
                            chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][2]
                            chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][2]
                    
                        random_pokemon.energy-=3
                        round4=0
                        round5=0
                        round6=0
                    elif (1+random_pokemon.defensive_moves2[0][5])*random_pokemon.speed>chosen_one.speed:
                        random_pokemon_speed=random_pokemon.speed
                        random_pokemon.speed=(1+random_pokemon.defensive_moves2[0][5])*random_pokemon.speed
                        random_pokemon_check=random_pokemon.offensive_moves1[0][1]
                        chosen_one.offensive_moves1[0][1]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves1[0][1]
                        chosen_one.offensive_moves2[0][1]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves2[0][1]
                        chosen_one.offensive_moves3[0][1]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves3[0][1]
                        random_pokemon.offensive_moves1[0][1]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves1[0][1]
                        random_pokemon.offensive_moves2[0][1]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves2[0][1]
                        random_pokemon.offensive_moves3[0][1]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves3[0][1]
                        random_pokemon.offensive_moves1[0][2]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves1[0][2]
                        random_pokemon.offensive_moves2[0][2]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves2[0][2]
                        random_pokemon.offensive_moves3[0][2]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves3[0][2]
                        print(f"{random_pokemon.name} used {random_pokemon.defensive_moves1[0][0]}")
                        if random_pokemon_speed<random_pokemon.speed:
                            print(f"{random_pokemon.name}'s speed increased")
                        if random_pokemon.defensive_moves1[0][2]>0:
                            random_pokemon.hp=(chosen_one.defensive_moves1[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                        if random_pokemon_check<random_pokemon.offensive_moves1[0][1]:
                            print(f"{random_pokemon.name}'s attack increased")
                        if random_pokemon_hp<random_pokemon.hp:
                            print(f"{random_pokemon.name} healed")
                        if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                            print(f"{random_pokemon.name}'s defence increased")
                        random_pokemon_paralasys=random2.randint(1,100)
                        if random_pokemon_paralasys<=random_pokemon.defensive_moves2[0][6]:
                            print(f"{chosen_one.name} paralyzed {random_pokemon.name}")
                            chosen_one_paralasys_mode=True
                        random_pokemon_burn=random2.randint(1,100)
                        if random_pokemon_burn<=random_pokemon.defensive_moves2[0][7]:
                            print(f"{random_pokemon.name} burned {chosen_one.name}")
                            random_pokemon_burn_mode=True
                        random_pokemon_freeze=random2.randint(1,100)
                        if random_pokemon_freeze<=random_pokemon.defensive_moves2[0][8]:
                            print(f"{random_pokemon.name} froze {chosen_one.name}")
                            random_pokemon_freeze_mode=True
                        random_pokemon_confusion_effect(random_pokemon, random_pokemon.defensive_moves2[0][9])
                        random_pokemon_sleep_effect(random_pokemon.defensive_moves2[0][10])
                        random_pokemon_poison_effect(5)
                        random_pokemon_badly_poison_effect(5)
                        print()
                        if random_pokemon.defensive_moves1[0][4]==None:
                           chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves1[0][2]
                           chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves2[0][2]
                           chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves3[0][2] 
                        random_pokemon.energy-=3
                        round4=0
                        round5=0
                        round6=0
                    else:
                        AI_choice=random2.randint(1,3)
                        if AI_choice==1:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage_1*random_pokemon.attack/100)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                            if random_pokemon_damage1>1:
                                print("It's super effective")
                            elif random_pokemon_damage1==0:
                                print("It's immune to it")
                            elif random_pokemon_damage1<1:
                                print("It's not effective")
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.offensive_moves1[0][4]:
                                print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                random_pokemon_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.offensive_moves1[0][5]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.offensive_moves1[0][6]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves1[0][7])
                            random_pokemon_poison_effect(1)
                            random_pokemon_badly_poison_effect(1)
                            print()
                        elif AI_choice==2:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage_2*random_pokemon.attack/100)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                            if random_pokemon_damage2>1:
                                print("It's super effective")
                            elif random_pokemon_damage2==0:
                                print("It's immune to it")
                            elif random_pokemon_damage2<1:
                                print("It's not effective")
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.offensive_moves2[0][4]:
                                print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                random_pokemon_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.offensive_moves2[0][5]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.offensive_moves2[0][6]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves2[0][7])
                            random_pokemon_poison_effect(2)
                            random_pokemon_badly_poison_effect(2)
                            print()
                        else:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage_3*random_pokemon.attack/100)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                            if random_pokemon_damage3>1:
                                print("It's super effective")
                            elif random_pokemon_damage3==0:
                                print("It's immune to it")
                            elif random_pokemon_damage3<1:
                                print("It's not effective")
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.offensive_moves3[0][4]:
                                print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                random_pokemon_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.offensive_moves3[0][5]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.offensive_moves3[0][6]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves3[0][7])
                            random_pokemon_poison_effect(3)
                            random_pokemon_badly_poison_effect(3) 
                            print()
                else:
                    AI_choice=random2.randint(1,3)
                    if AI_choice==1:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage_1*random_pokemon.attack/100)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                        if random_pokemon_damage1>1:
                            print("It's super effective")
                        elif random_pokemon_damage1==0:
                            print("It's immune to it")
                        elif random_pokemon_damage1<1:
                            print("It's not effective")
                        random_pokemon_paralasys=random2.randint(1,100)
                        if random_pokemon_paralasys<=random_pokemon.offensive_moves1[0][4]:
                            print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                            random_pokemon_paralasys_mode=True
                        random_pokemon_burn=random2.randint(1,100)
                        if random_pokemon_burn<=random_pokemon.offensive_moves1[0][5]:
                            print(f"{random_pokemon.name} burned {chosen_one.name}")
                            random_pokemon_burn_mode=True
                        random_pokemon_freeze=random2.randint(1,100)
                        if random_pokemon_freeze<=random_pokemon.offensive_moves1[0][6]:
                            print(f"{random_pokemon.name} froze {chosen_one.name}")
                            random_pokemon_freeze_mode=True
                        random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves1[0][7])
                        random_pokemon_poison_effect(1)
                        random_pokemon_badly_poison_effect(1)
                    elif AI_choice==2:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage_2*random_pokemon.attack/100)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                        if random_pokemon_damage2>1:
                            print("It's super effective")
                        elif random_pokemon_damage2==0:
                            print("It's immune to it")
                        elif random_pokemon_damage2<1:
                            print("It's not effective")
                        random_pokemon_paralasys=random2.randint(1,100)
                        if random_pokemon_paralasys<=random_pokemon.offensive_moves2[0][4]:
                            print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                            random_pokemon_paralasys_mode=True
                        random_pokemon_burn=random2.randint(1,100)
                        if random_pokemon_burn<=random_pokemon.offensive_moves2[0][5]:
                            print(f"{random_pokemon.name} burned {chosen_one.name}")
                            random_pokemon_burn_mode=True
                        chosen_one_freeze=random2.randint(1,100)
                        if chosen_one_freeze<=chosen_one.offensive_moves2[0][6]:
                            print(f"{chosen_one.name} froze {random_pokemon.name}")
                            chosen_one_freeze_mode=True
                        random_pokemon_freeze=random2.randint(1,100)
                        if random_pokemon_freeze<=random_pokemon.offensive_moves2[0][6]:
                            print(f"{random_pokemon.name} froze {chosen_one.name}")
                            random_pokemon_freeze_mode=True
                        random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves2[0][7])
                        random_pokemon_poison_effect(2)
                        random_pokemon_badly_poison_effect(2)
                    else:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage_3*random_pokemon.attack/100)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                        if random_pokemon_damage3>1:
                            print("It's super effective")
                        elif random_pokemon_damage3==0:
                            print("It's immune to it")
                        elif random_pokemon_damage3<1:
                            print("It's not effective")
                        random_pokemon_paralasys=random2.randint(1,100)
                        if random_pokemon_paralasys<=random_pokemon.offensive_moves3[0][4]:
                            print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                            random_pokemon_paralasys_mode=True
                        random_pokemon_burn=random2.randint(1,100)
                        if random_pokemon_burn<=random_pokemon.offensive_moves3[0][5]:
                            print(f"{random_pokemon.name} burned {chosen_one.name}")
                            random_pokemon_burn_mode=True
                        random_pokemon_freeze=random2.randint(1,100)
                        if random_pokemon_freeze<=random_pokemon.offensive_moves3[0][6]:
                            print(f"{random_pokemon.name} froze {chosen_one.name}")
                            random_pokemon_freeze_mode=True
                        random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves3[0][7])
                        random_pokemon_poison_effect(3)
                        random_pokemon_badly_poison_effect(3)
                    print()
            
            #burn check
            for i in range(len(random_pokemon.element)):
                if random_pokemon.element[i]=="Fire" and chosen_one_burn_mode==True:
                    chosen_one_burn_mode=False
                    print(f"{random_pokemon.name} isn't affected by burn")
            for i in range(len(chosen_one.element)):
                if chosen_one.element[i]=="Fire" and random_pokemon_burn_mode==True:
                    random_pokemon_burn_mode=False
                    print(f"{chosen_one.name} isn't affected by burn")

            if random_pokemon_burn_number==10:
                random_pokemon_burn_number=0
                chosen_one.offensive_moves2[0][1]=chosen_one.offensive_moves2[0][1]*2
                chosen_one.offensive_moves2[0][2]=chosen_one.offensive_moves2[0][2]*2
                chosen_one.offensive_moves1[0][1]=chosen_one.offensive_moves1[0][1]*2
                chosen_one.offensive_moves1[0][2]=chosen_one.offensive_moves1[0][2]*2
                chosen_one.offensive_moves3[0][1]=chosen_one.offensive_moves3[0][1]*2
                chosen_one.offensive_moves3[0][2]=chosen_one.offensive_moves3[0][2]*2
                random_pokemon_burn_mode=False
            if random_pokemon_burn_mode== True:
                print(f"{chosen_one.name} is burned")
                chosen_one.hp-=chosen_one.max_hp/8
                random_pokemon_burn_number+=1
            if random_pokemon_burn_number==1:
                chosen_one.offensive_moves2[0][1]=chosen_one.offensive_moves2[0][1]/2
                chosen_one.offensive_moves2[0][2]=chosen_one.offensive_moves2[0][2]/2
                chosen_one.offensive_moves1[0][1]=chosen_one.offensive_moves1[0][1]/2
                chosen_one.offensive_moves1[0][2]=chosen_one.offensive_moves1[0][2]/2
                chosen_one.offensive_moves3[0][1]=chosen_one.offensive_moves3[0][1]/2
                chosen_one.offensive_moves3[0][2]=chosen_one.offensive_moves3[0][2]/2

            if chosen_one_burn_number==10:
                chosen_one_burn_number=0
                random_pokemon.offensive_moves2[0][1]=random_pokemon.offensive_moves2[0][1]*2
                random_pokemon.offensive_moves2[0][2]=random_pokemon.offensive_moves2[0][2]*2
                random_pokemon.offensive_moves1[0][1]=random_pokemon.offensive_moves1[0][1]*2
                random_pokemon.offensive_moves1[0][2]=random_pokemon.offensive_moves1[0][2]*2
                random_pokemon.offensive_moves3[0][1]=random_pokemon.offensive_moves3[0][1]*2
                random_pokemon.offensive_moves3[0][2]=random_pokemon.offensive_moves3[0][2]*2
                chosen_one_burn_mode=False
            if chosen_one_burn_mode==True:
                print(f"{random_pokemon.name} is burned")
                random_pokemon.hp-=random_pokemon.max_hp/8
                chosen_one_burn_number+=1
            if chosen_one_burn_number==1:
                random_pokemon.offensive_moves2[0][1]=random_pokemon.offensive_moves2[0][1]/2
                random_pokemon.offensive_moves2[0][2]=random_pokemon.offensive_moves2[0][2]/2
                random_pokemon.offensive_moves1[0][1]=random_pokemon.offensive_moves1[0][1]/2
                random_pokemon.offensive_moves1[0][2]=random_pokemon.offensive_moves1[0][2]/2
                random_pokemon.offensive_moves3[0][1]=random_pokemon.offensive_moves3[0][1]/2
                random_pokemon.offensive_moves3[0][2]=random_pokemon.offensive_moves3[0][2]/2
            if chosen_one_confusion_number>4:
                chosen_one_confusion_number=0
            if random_pokemon_confusion_number>4:
                random_pokemon_confusion_number=0
            

            if random_pokemon_poison_mode[-1]== True:
                print(f"{chosen_one.name} is poisoned")
                chosen_one.hp-=chosen_one.max_hp/16
                random_pokemon_poison_number+=1
            if random_pokemon_poison_number==20:
                random_pokemon_poison_number=0
                random_pokemon_poison_mode.append(False)


            if chosen_one_poison_mode[-1]== True:
                print(f"{random_pokemon.name} is poisoned")
                random_pokemon.hp-=chosen_one.max_hp/16
                chosen_one_poison_number+=1
            if chosen_one_poison_number==20:
                chosen_one_poison_number=0
                chosen_one_poison_mode.append(False)          
            
            
            if random_pokemon_badly_poison_mode[-1]== True:
                print(f"{chosen_one.name} is poisoned")
                chosen_one.hp-=chosen_one.max_hp/16*(random_pokemon_badly_poison_number+1)
                random_pokemon_badly_poison_number+=1
            if random_pokemon_badly_poison_number==20:
                random_pokemon_badly_poison_number=0
                random_pokemon_badly_poison_mode.append(False)
            

            if chosen_one_badly_poison_mode[-1]== True:
                print(f"{random_pokemon.name} is poisoned")
                random_pokemon.hp-=chosen_one.max_hp/16*(chosen_one_badly_poison_number+1)
                chosen_one_badly_poison_number+=1
            if chosen_one_badly_poison_number==20:
                chosen_one_badly_poison_number=0
                chosen_one_badly_poison_mode.append(False) 
            
            round1+=1
            round4+=1
            if chosen_one.hp<=0:
                print("You lost")
                break
            elif random_pokemon.hp<=0:
                print("You won")
                break
            time.sleep(1)

    elif chosen_one.speed<random_pokemon.speed or start==2:
        chosen_one.hp=int(chosen_one.hp)
        random_pokemon.hp=int(random_pokemon.hp)
        random_pokemon_damage_check=random_pokemon.offensive_moves1[0][1]
        chosen_one_damage_check=chosen_one.offensive_moves1[0][1]
        if chosen_one.energy>0:
            print(f"""{chosen_one.name}   hp:{chosen_one.hp}   energy:{chosen_one.energy} heals:{chosen_one.heal}
{random_pokemon.name}   hp:{random_pokemon.hp}   energy:{random_pokemon.energy} heals:{random_pokemon.heal}
{chosen_one.name}'s moves:
Offensive moves: {chosen_one.offensive_moves1[0][0]}(uses 1 energy),{chosen_one.offensive_moves2[0][0]}(uses 1 energy),{chosen_one.offensive_moves3[0][0]}(uses 1 energy)
Defensive moves: {chosen_one.defensive_moves1[0][0]}(uses 3 energy),{chosen_one.defensive_moves2[0][0]}(uses 3 energy)
Heal:{chosen_one.heal}""")
            print()
            choice=input("What is your move? Note:Do your moves in order from 1 to 6. 1 being the first offensive move and 6 being a heal." )
        #AI's turn
        chosen_one.hp=int(chosen_one.hp)
        random_pokemon.hp=int(random_pokemon.hp)
        random_pokemon_damage_check=random_pokemon.offensive_moves1[0][1]
        chosen_one_damage_check=chosen_one.offensive_moves1[0][1]
        if random_pokemon.energy<=0:
            random_pokemon.energy=0
        print(f"""{chosen_one.name}   hp:{chosen_one.hp}   energy:{chosen_one.energy} heals:{chosen_one.heal}
{random_pokemon.name}   hp:{random_pokemon.hp}   energy:{random_pokemon.energy} heals:{random_pokemon.heal}""")
        print()
        round6=round4-round5
        if round3==random_pokemon.defensive_moves2[0][4] and random_pokemon.defensive_moves2[0][4]!=None:
            #prevents the defensive moves from being too OP
            chosen_one.offensive_moves1[0][1]=chosen_one.offensive_moves1[0][2]
            chosen_one.offensive_moves2[0][1]=chosen_one.offensive_moves2[0][2]
            chosen_one.offensive_moves3[0][1]=chosen_one.offensive_moves3[0][2]
        if round3==random_pokemon.defensive_moves1[0][4] and random_pokemon.defensive_moves1[0][4]!=None:
            #prevents the defensive moves from being too OP
            chosen_one.offensive_moves1[0][1]=chosen_one.offensive_moves1[0][2]
            chosen_one.offensive_moves2[0][1]=chosen_one.offensive_moves2[0][2]
            chosen_one.offensive_moves3[0][1]=chosen_one.offensive_moves3[0][2]
        if chosen_one_paralasys_number==5:
            chosen_one_paralasys_mode=False
            chosen_one_paralasys_number=0
        if chosen_one_paralasys_mode==True and chosen_one_paralasys_number<=5:
            chosen_one_paralasys_number+=1
            print(f"{random_pokemon.name} is paralyzed")
        if chosen_one_freeze_mode==True:
            freeze_chance=random2.randint(1,256)
            if freeze_chance<=25:
                chosen_one_freeze_mode==False
                print(f"{random_pokemon.name} escaped the ice")
            else:
                print(f"{random_pokemon.name} is frozen")
        if chosen_one_sleep_mode[-1]==True:
            if chosen_one_sleep_number==0:
                print(f"{random_pokemon.name} is fast sleep")
                chosen_one_sleep_number+=1
            else:
                wake_up=random2.randint(1, 5-chosen_one_sleep_number)
                if wake_up==1:
                    print(f"{random_pokemon.name} woke up")
                    chosen_one_sleep_number=0
                    chosen_one_sleep_mode.append(False)
                else:
                    print(f"{random_pokemon.name} is fast sleep")
                    chosen_one_sleep_number+=1
        if chosen_one_paralasys_mode==False and chosen_one_freeze_mode==False and chosen_one_sleep_mode[-1]==False:
            if chosen_one_confusion_mode[-1]==True and chosen_one_confusion_number<=4:
                spin_the_wheel=random2.randint(1,2)
                if spin_the_wheel==1:
                    print(f"{random_pokemon.name} is confused")
                    random_pokemon.hp-=((random_pokemon.offensive_moves1[0][1]+random_pokemon.offensive_moves2[0][1]+random_pokemon.offensive_moves3[0][1])*random_pokemon.attack/100/3)
                    chosen_one_confusion_number+=1
                if spin_the_wheel==2:
                    chosen_one_confusion_number+=1
                    AI_choice=random2.randint(1,3)
                    if AI_choice==1:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage_1*random_pokemon.attack/100)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                        if random_pokemon_damage1>1:
                            print("It's super effective")
                        elif random_pokemon_damage1==0:
                            print("It's immune to it")
                        elif random_pokemon_damage1<1:
                            print("It's not effective")
                        random_pokemon_paralasys=random2.randint(1,100)
                        if random_pokemon_paralasys<=random_pokemon.offensive_moves1[0][4]:
                            print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                            random_pokemon_paralasys_mode=True
                        random_pokemon_burn=random2.randint(1,100)
                        if random_pokemon_burn<=random_pokemon.offensive_moves1[0][5]:
                            print(f"{random_pokemon.name} burned {chosen_one.name}")
                            random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                        if random_pokemon_freeze<=random_pokemon.offensive_moves1[0][6]:
                            print(f"{random_pokemon.name} froze {chosen_one.name}")
                            random_pokemon_freeze_mode=True
                        random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves1[0][7])
                        random_pokemon_poison_effect(1)
                        random_pokemon_badly_poison_effect(1)
                        print()
                    elif AI_choice==2:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage_2*random_pokemon.attack/100 )
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                        if random_pokemon_damage2>1:
                            print("It's super effective")
                        elif random_pokemon_damage2==0:
                                print("It's immune to it")
                        elif random_pokemon_damage2<1:
                            print("It's not effective")
                        random_pokemon_paralasys=random2.randint(1,100)
                        if random_pokemon_paralasys<=random_pokemon.offensive_moves2[0][4]:
                            print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                            random_pokemon_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                        if random_pokemon_burn<=random_pokemon.offensive_moves2[0][5]:
                            print(f"{random_pokemon.name} burned {chosen_one.name}")
                            random_pokemon_burn_mode=True
                        random_pokemon_freeze=random2.randint(1,100)
                        if random_pokemon_freeze<=random_pokemon.offensive_moves2[0][6]:
                            print(f"{random_pokemon.name} froze {chosen_one.name}")
                            random_pokemon_freeze_mode=True
                        random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves2[0][7])
                        random_pokemon_poison_effect(2)
                        random_pokemon_badly_poison_effect(2)
                        print()
                    else:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage_3*random_pokemon.attack/100)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                        if random_pokemon_damage3>1:
                            print("It's super effective")
                        elif random_pokemon_damage3==0:
                            print("It's immune to it")
                        elif random_pokemon_damage3<1:
                            print("It's not effective")
                        random_pokemon_paralasys=random2.randint(1,100)
                        if random_pokemon_paralasys<=random_pokemon.offensive_moves3[0][4]:
                            print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                            random_pokemon_paralasys_mode=True 
                        random_pokemon_burn=random2.randint(1,100)
                        if random_pokemon_burn<=random_pokemon.offensive_moves3[0][5]:
                            print(f"{random_pokemon.name} burned {chosen_one.name}")
                            random_pokemon_burn_mode=True
                        random_pokemon_freeze=random2.randint(1,100)
                        if random_pokemon_freeze<=random_pokemon.offensive_moves3[0][6]:
                            print(f"{random_pokemon.name} froze {chosen_one.name}")
                            random_pokemon_freeze_mode=True
                        random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves3[0][7])
                        random_pokemon_poison_effect(3)
                        random_pokemon_badly_poison_effect(3)
                        print()
            elif random_pokemon.energy<=0:
                print(f"{random_pokemon.name} used struggle")
                print()
                random_pokemon.hp=3/4*random_pokemon.hp
                chosen_one.hp=chosen_one.hp-((random_pokemon.offensive_moves1[0][1]+random_pokemon.offensive_moves2[0][1]+random_pokemon.offensive_moves3[0][1])*random_pokemon.attack/100/3)
            elif random_pokemon.energy>=0:
                random_pokemon_hp=random_pokemon.hp
                random_pokemon_damage_check=random_pokemon.offensive_moves1[0][1]
                chosen_one_damage_check=chosen_one.offensive_moves1[0][1]
                random_pokemon_speed=random_pokemon.speed
                if chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage_1)<=0:
                    chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage_1*random_pokemon.attack/100)
                    random_pokemon.energy-=1
                    print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                    if random_pokemon_damage1>1:
                        print("It's super effective")
                    elif random_pokemon_damage1==0:
                        print("It's immune to it")
                    elif random_pokemon_damage1<1:
                        print("It's not effective")
                    random_pokemon_paralasys=random2.randint(1,100)
                    if random_pokemon_paralasys<=random_pokemon.offensive_moves1[0][4]:
                        print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                        random_pokemon_paralasys_mode=True

                    random_pokemon_burn=random2.randint(1,100)
                    if random_pokemon_burn<=random_pokemon.offensive_moves1[0][5]:
                        print(f"{random_pokemon.name} burned {chosen_one.name}")
                        random_pokemon_burn_mode=True
                    random_pokemon_freeze=random2.randint(1,100)
                    if random_pokemon_freeze<=random_pokemon.offensive_moves1[0][6]:
                        print(f"{random_pokemon.name} froze {chosen_one.name}")
                        random_pokemon_freeze_mode=True
                    random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves1[0][7])
                    random_pokemon_poison_effect(1)
                    random_pokemon_badly_poison_effect(1)
                    print()
                elif chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage_2)<=0:
                    chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage_2*random_pokemon.attack/100)
                    random_pokemon.energy-=1
                    print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                    if random_pokemon_damage2>1:
                        print("It's super effective")
                    elif random_pokemon_damage2==0:
                        print("It's immune to it")
                    elif random_pokemon_damage2<1:
                        print("It's not effective")
                    random_pokemon_paralasys=random2.randint(1,100)
                    if random_pokemon_paralasys<=random_pokemon.offensive_moves2[0][4]:
                        print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                        random_pokemon_paralasys_mode=True
                    random_pokemon_burn=random2.randint(1,100)
                    if random_pokemon_burn<=random_pokemon.offensive_moves2[0][5]:
                        print(f"{random_pokemon.name} burned {chosen_one.name}")
                        random_pokemon_burn_mode=True
                    random_pokemon_freeze=random2.randint(1,100)
                    if random_pokemon_freeze<=random_pokemon.offensive_moves2[0][6]:
                        print(f"{random_pokemon.name} froze {chosen_one.name}")
                        random_pokemon_freeze_mode=True
                    random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves2[0][7])
                    random_pokemon_poison_effect(2)
                    random_pokemon_badly_poison_effect(2)
                    print()
                elif chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage3)<=0:
                    chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage_3*random_pokemon.attack/100)
                    random_pokemon.energy-=1
                    print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                    if random_pokemon_damage3>1:
                        print("It's super effective")
                    elif random_pokemon_damage3==0:
                        print("It's immune to it")
                    elif random_pokemon_damage3<1:
                        print("It's not effective") 
                    random_pokemon_paralasys=random2.randint(1,100)
                    if random_pokemon_paralasys<=random_pokemon.offensive_moves3[0][4]:
                        print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                        random_pokemon_paralasys_mode=True 
                    random_pokemon_burn=random2.randint(1,100)
                    if random_pokemon_burn<=random_pokemon.offensive_moves3[0][5]:
                        print(f"{random_pokemon.name} burned {chosen_one.name}")
                        random_pokemon_burn_mode=True
                    random_pokemon_freeze=random2.randint(1,100)
                    if random_pokemon_freeze<=random_pokemon.offensive_moves3[0][6]:
                        print(f"{random_pokemon.name} froze {chosen_one.name}")
                        random_pokemon_freeze_mode=True
                    random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves3[0][7])
                    random_pokemon_poison_effect(3)
                    random_pokemon_badly_poison_effect(3)
                    print()
                elif random_pokemon.hp<=random_pokemon.max_hp/4:
                    if random_pokemon.hp-chosen_one.offensive_moves1[0][2]<=0 and random_pokemon.heal>0:
                        random_pokemon.hp+=100
                        print(f"AI used a heal on {random_pokemon.name}")
                        if random_pokemon.hp>random_pokemon.max_hp:
                            random_pokemon.hp=random_pokemon.max_hp
                        random_pokemon.heal-=1
                    elif random_pokemon.hp-chosen_one.offensive_moves1[0][2]<=0 and random_pokemon.defensive_moves2[0][2]>0 or random_pokemon.hp-chosen_one.offensive_moves1[0][2]<=0 and random_pokemon.defensive_moves2[0][2]>0 or random_pokemon.hp-chosen_one.offensive_moves1[0][2]<=0 and random_pokemon.defensive_moves2[0][2]>0 or random_pokemon.defensive_moves2[0][2]>0 and (random_pokemon.defensive_moves2[0][2] / 100 * random_pokemon.max_hp)>((chosen_one.offensive_moves1[0][1]*chosen_one_damage1+chosen_one.offensive_moves2[0][1]*chosen_one_damage2+chosen_one.offensive_moves3[0][1]*chosen_one_damage3)/3):
                        random_pokemon_speed=random_pokemon.speed
                        random_pokemon.speed=(1+random_pokemon.defensive_moves1[0][5])*random_pokemon.speed
                        random_pokemon_hp=random_pokemon.hp
                        random_pokemon_check=random_pokemon.offensive_moves1[0][1]
                        random_pokemon.hp=(random_pokemon.defensive_moves1[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                        chosen_one.offensive_moves1[0][1]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][1]
                        chosen_one.offensive_moves2[0][1]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][1]
                        chosen_one.offensive_moves3[0][1]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][1]
                        random_pokemon.offensive_moves1[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves1[0][1]
                        random_pokemon.offensive_moves2[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves2[0][1]
                        random_pokemon.offensive_moves3[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves3[0][1]
                        random_pokemon.offensive_moves1[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves1[0][1]
                        random_pokemon.offensive_moves2[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves2[0][1]
                        random_pokemon.offensive_moves3[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves3[0][1]
                        print(f"{random_pokemon.name} used {random_pokemon.defensive_moves1[0][0]}")
                        if random_pokemon_speed<random_pokemon.speed:
                            print(f"{random_pokemon.name}'s speed increased")
                        if random_pokemon.hp>random_pokemon.max_hp:
                            random_pokemon.hp=random_pokemon.max_hp
                        if random_pokemon_check<random_pokemon.offensive_moves1[0][1]:
                            print(f"{random_pokemon.name}'s attack increased")
                        if random_pokemon_hp<random_pokemon.hp:
                            print(f"{random_pokemon.name} healed")
                        if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                            print(f"{random_pokemon.name}'s defence increased")
                        random_pokemon_paralasys=random2.randint(1,100)
                        if random_pokemon_paralasys<=random_pokemon.defensive_moves1[0][6]:
                            print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                            chosen_one_paralasys_mode=True
                        random_pokemon_burn=random2.randint(1,100)
                        if random_pokemon_burn<=random_pokemon.defensive_moves1[0][7]:
                            print(f"{random_pokemon.name} burned {chosen_one.name}")
                            random_pokemon_burn_mode=True
                        random_pokemon_freeze=random2.randint(1,100)
                        if random_pokemon_freeze<=random_pokemon.defensive_moves1[0][8]:
                            print(f"{random_pokemon.name} froze {chosen_one.name}")
                            random_pokemon_freeze_mode=True
                        random_pokemon_confusion_effect(random_pokemon, random_pokemon.defensive_moves1[0][9])
                        random_pokemon_sleep_effect(random_pokemon.defensive_moves1[0][10])
                        random_pokemon_poison_effect(4)
                        random_pokemon_badly_poison_effect(4)
                        print()
                        if random_pokemon.defensive_moves1[0][4]==None:
                            chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][2]
                            chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][2]
                            chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][2]
                        random_pokemon.energy-=3
                        round4=0
                        round5=0
                        round6=0
                    elif random_pokemon.hp-chosen_one.offensive_moves1[0][2]<=0 and random_pokemon.defensive_moves2[0][2]>0 or random_pokemon.hp-chosen_one.offensive_moves1[0][2]<=0 and random_pokemon.defensive_moves2[0][2]>0 or random_pokemon.hp-chosen_one.offensive_moves3[0][2]<=0 and random_pokemon.defensive_moves2[0][2]>0 or random_pokemon.defensive_moves2[0][2]>0 and (random_pokemon.defensive_moves2[0][2] / 100 * random_pokemon.max_hp)>((chosen_one.offensive_moves1[0][1]*chosen_one_damage1+chosen_one.offensive_moves2[0][1]*chosen_one_damage2+chosen_one.offensive_moves3[0][1]*chosen_one_damage3)/3):
                        random_pokemon_speed=random_pokemon.speed
                        random_pokemon.speed=(1+random_pokemon.defensive_moves2[0][5])*random_pokemon.speed
                        random_pokemon_hp=random_pokemon.hp
                        random_pokemon_check=random_pokemon.offensive_moves2[0][1]
                        random_pokemon.hp=(random_pokemon.defensive_moves2[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                        chosen_one.offensive_moves1[0][1]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves1[0][1]
                        chosen_one.offensive_moves2[0][1]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves2[0][1]
                        chosen_one.offensive_moves3[0][1]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves3[0][1]
                        random_pokemon.offensive_moves1[0][1]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves1[0][1]
                        random_pokemon.offensive_moves2[0][1]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves2[0][1]
                        random_pokemon.offensive_moves3[0][1]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves3[0][1]
                        random_pokemon.offensive_moves1[0][2]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves1[0][2]
                        random_pokemon.offensive_moves2[0][2]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves2[0][2]
                        random_pokemon.offensive_moves3[0][2]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves3[0][2]
                        print(f"{random_pokemon.name} used {random_pokemon.defensive_moves2[0][0]}")
                        if random_pokemon_speed<random_pokemon.speed:
                            print(f"{random_pokemon.name}'s speed increased")
                        if random_pokemon_check<random_pokemon.offensive_moves2[0][1]:
                            print(f"{random_pokemon.name}'s attack increased")
                        if random_pokemon.hp>random_pokemon.max_hp:
                            random_pokemon.hp=random_pokemon.max_hp
                        if random_pokemon_hp<random_pokemon.hp:
                            print(f"{random_pokemon.name} healed")
                        if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                            print(f"{random_pokemon.name}'s defence increased")
                        random_pokemon_paralasys=random2.randint(1,100)
                        if random_pokemon_paralasys<=random_pokemon.defensive_moves2[0][6]:
                            print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                            chosen_one_paralasys_mode=True
                        random_pokemon_burn=random2.randint(1,100)
                        if random_pokemon_burn<=random_pokemon.defensive_moves2[0][7]:
                            print(f"{random_pokemon.name} burned {chosen_one.name}")
                            random_pokemon_burn_mode=True
                        random_pokemon_freeze=random2.randint(1,100)
                        if random_pokemon_freeze<=random_pokemon.defensive_moves2[0][8]:
                            print(f"{random_pokemon.name} froze {chosen_one.name}")
                            random_pokemon_freeze_mode=True
                        random_pokemon_confusion_effect(random_pokemon, random_pokemon.defensive_moves2[0][9])
                        random_pokemon_sleep_effect(random_pokemon.defensive_moves2[0][10])
                        random_pokemon_poison_effect(5)
                        random_pokemon_badly_poison_effect(5)
                        print()
                        if random_pokemon.defensive_moves1[0][4]==None:
                            chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves1[0][2]
                            chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves2[0][2]
                            chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves3[0][2]
                        random_pokemon.energy-=3
                        round4=0
                        round5=0
                        round6=0
                    else:
                        AI_choice=random2.randint(1,3)
                        if AI_choice==1:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage_1*random_pokemon.attack/100)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                            if random_pokemon_damage1>1:
                                print("It's super effective")
                            elif random_pokemon_damage1==0:
                                print("It's immune to it")
                            elif random_pokemon_damage1<1:
                                print("It's not effective")
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.offensive_moves1[0][4]:
                                print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                random_pokemon_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.offensive_moves1[0][5]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.offensive_moves1[0][6]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves1[0][7])
                            random_pokemon_poison_effect(1)
                            random_pokemon_badly_poison_effect(1)
                            print()
                        elif AI_choice==2:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage_2*random_pokemon.attack/100 )
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                            if random_pokemon_damage2>1:
                                print("It's super effective")
                            elif random_pokemon_damage2==0:
                                print("It's immune to it")
                            elif random_pokemon_damage2<1:
                                print("It's not effective")
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.offensive_moves2[0][4]:
                                print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                random_pokemon_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.offensive_moves2[0][5]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.offensive_moves2[0][6]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves2[0][7])
                            random_pokemon_poison_effect(2)
                            random_pokemon_badly_poison_effect(2)
                            print()
                        else:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage_3*random_pokemon.attack/100)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                            if random_pokemon_damage3>1:
                                print("It's super effective")
                            elif random_pokemon_damage3==0:
                                print("It's immune to it")
                            elif random_pokemon_damage3<1:
                                print("It's not effective")
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.offensive_moves3[0][4]:
                                print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                random_pokemon_paralasys_mode=True 
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.offensive_moves3[0][5]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.offensive_moves3[0][6]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves3[0][7])
                            random_pokemon_poison_effect(3)
                            random_pokemon_badly_poison_effect(3)
                            print()
                elif random_pokemon.hp<=random_pokemon.max_hp/2:
                    if round6>=2:
                        random_pokemon_hp=random_pokemon.hp
                        if random_pokemon.defensive_moves1[0][1]>0:
                            random_pokemon.speed=(1+random_pokemon.defensive_moves1[0][5])*random_pokemon.speed
                            random_pokemon_check=random_pokemon.offensive_moves1[0][1]
                            chosen_one.offensive_moves1[0][1]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][1]
                            chosen_one.offensive_moves2[0][1]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][1]
                            chosen_one.offensive_moves3[0][1]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][1]
                            random_pokemon.offensive_moves1[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves1[0][1]
                            random_pokemon.offensive_moves2[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves2[0][1]
                            random_pokemon.offensive_moves3[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves3[0][1]
                            random_pokemon.offensive_moves1[0][2]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves1[0][2]
                            random_pokemon.offensive_moves2[0][2]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves2[0][2]
                            random_pokemon.offensive_moves3[0][2]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves3[0][2]
                            print(f"{random_pokemon.name} used {random_pokemon.defensive_moves1[0][0]}")
                            if random_pokemon_speed<random_pokemon.speed:
                                print(f"{random_pokemon.name}'s speed increased")
                            if random_pokemon.defensive_moves1[0][2]>0:
                                random_pokemon.hp=(random_pokemon.defensive_moves1[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                            if random_pokemon_check<random_pokemon.offensive_moves1[0][1]:
                                print(f"{random_pokemon.name}'s attack increased")
                            if random_pokemon.hp>random_pokemon.max_hp:
                                random_pokemon.hp=random_pokemon.max_hp
                            if random_pokemon_hp<random_pokemon.hp:
                                print(f"{random_pokemon.name} healed")
                            if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                                print(f"{random_pokemon.name}'s defence increased")
                            if random_pokemon.defensive_moves1[0][4]==None:
                                chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][2]
                                chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][2]
                                chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][2]
                            
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.defensive_moves1[0][6]:
                                print(f"{chosen_one.name} paralyzed {random_pokemon.name}")
                                chosen_one_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.defensive_moves1[0][7]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.defensive_moves1[0][8]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.defensive_moves1[0][9])
                            random_pokemon_sleep_effect(random_pokemon.defensive_moves1[0][10])
                            random_pokemon_poison_effect(4)
                            random_pokemon_badly_poison_effect(4)
                            random_pokemon.energy-=3
                            round4=0
                            round5=0
                            round6=0
                        elif random_pokemon.defensive_moves2[0][1]>0:
                            random_pokemon.speed=(1+random_pokemon.defensive_moves2[0][5])*random_pokemon.speed
                            random_pokemon_check=random_pokemon.offensive_moves1[0][1]
                            chosen_one.offensive_moves1[0][1]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves1[0][1]
                            chosen_one.offensive_moves2[0][1]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves2[0][1]
                            chosen_one.offensive_moves3[0][1]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves3[0][1]
                            random_pokemon.offensive_moves1[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves1[0][1]
                            random_pokemon.offensive_moves2[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves2[0][1]
                            random_pokemon.offensive_moves3[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves3[0][1]
                            random_pokemon.offensive_moves1[0][2]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves1[0][2]
                            random_pokemon.offensive_moves2[0][2]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves2[0][2]
                            random_pokemon.offensive_moves3[0][2]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves3[0][2]
                            print(f"{random_pokemon.name} used {random_pokemon.defensive_moves2[0][0]}")
                            if random_pokemon_speed<random_pokemon.speed:
                                print(f"{random_pokemon.name}'s speed increased")
                            if random_pokemon.defensive_moves1[0][2]>0:
                                random_pokemon.hp=(random_pokemon.defensive_moves2[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                            if random_pokemon.hp>random_pokemon.max_hp:
                                random_pokemon.hp=random_pokemon.max_hp
                            if random_pokemon_hp<random_pokemon.hp:
                                print(f"{random_pokemon.name} healed")
                            if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                                print(f"{random_pokemon.name}'s defence increased")
                            if random_pokemon_check<random_pokemon.offensive_moves1[0][1]:
                                print(f"{random_pokemon.name}'s attack increased")
                            if random_pokemon.defensive_moves2[0][4]==None:
                                chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][2]
                                chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][2]
                                chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][2]
                            
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.defensive_moves2[0][6]:
                                print(f"{chosen_one.name} paralyzed {random_pokemon.name}")
                                chosen_one_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.defensive_moves2[0][7]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.defensive_moves2[0][8]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.defensive_moves2[0][9])
                            random_pokemon_sleep_effect(random_pokemon.defensive_moves2[0][10])
                            random_pokemon_poison_effect(5)
                            random_pokemon_badly_poison_effect(5)
                            random_pokemon.energy-=3
                            round4=0
                            round5=0
                            round6=0
                        else:
                            AI_choice=random2.randint(1,3)
                            if AI_choice==1:
                                chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage_1*random_pokemon.attack/100)
                                random_pokemon.energy-=1
                                print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                                if random_pokemon_damage1>1:
                                    print("It's super effective")
                                elif random_pokemon_damage1==0:
                                    print("It's immune to it")
                                elif random_pokemon_damage1<1:
                                    print("It's not effective")
                                random_pokemon_paralasys=random2.randint(1,100)
                                if random_pokemon_paralasys<=random_pokemon.offensive_moves1[0][4]:
                                    print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                    random_pokemon_paralasys_mode=True
                                random_pokemon_burn=random2.randint(1,100)
                                if random_pokemon_burn<=random_pokemon.offensive_moves1[0][5]:
                                    print(f"{random_pokemon.name} burned {chosen_one.name}")
                                    random_pokemon_burn_mode=True
                                random_pokemon_freeze=random2.randint(1,100)
                                if random_pokemon_freeze<=random_pokemon.offensive_moves1[0][6]:
                                    print(f"{random_pokemon.name} froze {chosen_one.name}")
                                    random_pokemon_freeze_mode=True
                                random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves1[0][7])
                                random_pokemon_poison_effect(1)
                                random_pokemon_badly_poison_effect(1)
                            elif AI_choice==2:
                                chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage_2*random_pokemon.attack/100)
                                random_pokemon.energy-=1
                                print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                                if random_pokemon_damage2>1:
                                    print("It's super effective")
                                elif random_pokemon_damage2==0:
                                    print("It's immune to it")
                                elif random_pokemon_damage2<1:
                                    print("It's not effective")
                                random_pokemon_paralasys=random2.randint(1,100)
                                if random_pokemon_paralasys<=random_pokemon.offensive_moves2[0][4]:
                                    print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                    random_pokemon_paralasys_mode=True
                                random_pokemon_burn=random2.randint(1,100)
                                if random_pokemon_burn<=random_pokemon.offensive_moves2[0][5]:
                                    print(f"{random_pokemon.name} burned {chosen_one.name}")
                                    random_pokemon_burn_mode=True
                                random_pokemon_freeze=random2.randint(1,100)
                                if random_pokemon_freeze<=random_pokemon.offensive_moves2[0][6]:
                                    print(f"{random_pokemon.name} froze {chosen_one.name}")
                                    random_pokemon_freeze_mode=True
                                random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves2[0][7])
                                random_pokemon_poison_effect(2)
                                random_pokemon_badly_poison_effect(2)
                            else:
                                chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage_3*random_pokemon.attack/100)
                                random_pokemon.energy-=1
                                print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                                if random_pokemon_damage3>1:
                                    print("It's super effective")
                                elif random_pokemon_damage3==0:
                                    print("It's immune to it")
                                elif random_pokemon_damage3<1:
                                    print("It's not effective")
                                random_pokemon_paralasys=random2.randint(1,100)
                                if random_pokemon_paralasys<=random_pokemon.offensive_moves3[0][4]:
                                    print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                    random_pokemon_paralasys_mode=True
                                random_pokemon_burn=random2.randint(1,100)
                                if random_pokemon_burn<=random_pokemon.offensive_moves3[0][5]:
                                    print(f"{random_pokemon.name} burned {chosen_one.name}")
                                    random_pokemon_burn_mode=True
                                random_pokemon_freeze=random2.randint(1,100)
                                if random_pokemon_freeze<=random_pokemon.offensive_moves3[0][6]:
                                    print(f"{random_pokemon.name} froze {chosen_one.name}")
                                    random_pokemon_freeze_mode=True
                                random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves3[0][7])
                                random_pokemon_poison_effect(3)
                                random_pokemon_badly_poison_effect(3)
                    else:
                        AI_choice=random2.randint(1,3)
                        if AI_choice==1:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage_1*random_pokemon.attack/100)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                            if random_pokemon_damage1>1:
                                print("It's super effective")
                            elif random_pokemon_damage1==0:
                                print("It's immune to it")
                            elif random_pokemon_damage1<1:
                                print("It's not effective")
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.offensive_moves1[0][4]:
                                print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                random_pokemon_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.offensive_moves1[0][5]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.offensive_moves1[0][6]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves1[0][7])
                            random_pokemon_poison_effect(1)
                            random_pokemon_badly_poison_effect(1)
                        elif AI_choice==2:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage_2*random_pokemon.attack/100)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                            if random_pokemon_damage2>1:
                                print("It's super effective")
                            elif random_pokemon_damage2==0:
                                print("It's immune to it")
                            elif random_pokemon_damage2<1:
                                print("It's not effective")
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.offensive_moves2[0][4]:
                                print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                random_pokemon_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.offensive_moves2[0][5]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.offensive_moves2[0][6]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves2[0][7])
                            random_pokemon_poison_effect(2)
                            random_pokemon_badly_poison_effect(2)
                        else:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage_3*random_pokemon.attack/100)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                            if random_pokemon_damage3>1:
                                print("It's super effective")
                            elif random_pokemon_damage3==0:
                                print("It's immune to it")
                            elif random_pokemon_damage3<1:
                                print("It's not effective")
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.offensive_moves3[0][4]:
                                print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                random_pokemon_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.offensive_moves3[0][5]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.offensive_moves3[0][6]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves3[0][7])
                            random_pokemon_poison_effect(3)
                            random_pokemon_badly_poison_effect(3)
                    print()
                elif random_pokemon.max_hp/8*7<random_pokemon.hp:
                    random_pokemon_hp=random_pokemon.hp
                    if random_pokemon.defensive_moves1[0][3]>0:
                        random_pokemon.speed=(1+random_pokemon.defensive_moves1[0][5])*random_pokemon.speed
                        random_pokemon_check=random_pokemon.offensive_moves1[0][1]
                        chosen_one.offensive_moves1[0][1]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][1]
                        chosen_one.offensive_moves2[0][1]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][1]
                        chosen_one.offensive_moves3[0][1]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][1]
                        random_pokemon.offensive_moves1[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves1[0][1]
                        random_pokemon.offensive_moves2[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves2[0][1]
                        random_pokemon.offensive_moves3[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves3[0][1]
                        random_pokemon.offensive_moves1[0][2]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves1[0][2]
                        random_pokemon.offensive_moves2[0][2]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves2[0][2]
                        random_pokemon.offensive_moves3[0][2]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves3[0][2]
                        print(f"{random_pokemon.name} used {random_pokemon.defensive_moves1[0][0]}")
                        if random_pokemon_speed<random_pokemon.speed:
                            print(f"{random_pokemon.name}'s speed increased")
                        if random_pokemon.defensive_moves1[0][4]==None:
                            chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][2]
                            chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][2]
                            chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][2]
                        if random_pokemon.defensive_moves1[0][2]>0:
                            random_pokemon.hp=(chosen_one.defensive_moves1[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                        if random_pokemon_check<random_pokemon.offensive_moves1[0][1]:
                            print(f"{random_pokemon.name}'s attack increased")
                        if random_pokemon_hp<random_pokemon.hp:
                            print(f"{random_pokemon.name} healed")
                        if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                            print(f"{random_pokemon.name}'s defence increased")
                        random_pokemon_paralasys=random2.randint(1,100)
                        if random_pokemon_paralasys<=random_pokemon.defensive_moves1[0][6]:
                            print(f"{chosen_one.name} paralyzed {random_pokemon.name}")
                            chosen_one_paralasys_mode=True
                        random_pokemon_burn=random2.randint(1,100)
                        if random_pokemon_burn<=random_pokemon.defensive_moves1[0][7]:
                            print(f"{random_pokemon.name} burned {chosen_one.name}")
                            random_pokemon_burn_mode=True
                        random_pokemon_freeze=random2.randint(1,100)
                        if random_pokemon_freeze<=random_pokemon.defensive_moves1[0][8]:
                            print(f"{random_pokemon.name} froze {chosen_one.name}")
                            random_pokemon_freeze_mode=True
                        random_pokemon_confusion_effect(random_pokemon, random_pokemon.defensive_moves1[0][9])
                        random_pokemon_sleep_effect(random_pokemon.defensive_moves1[0][10])
                        random_pokemon_poison_effect(4)
                        random_pokemon_badly_poison_effect(4)
                        print()
                        random_pokemon.energy-=3
                        round4=0
                        round5=0
                        round6=0
                    elif random_pokemon.defensive_moves2[0][3]>0:
                        random_pokemon.speed=(1+random_pokemon.defensive_moves2[0][5])*random_pokemon.speed
                        random_pokemon_check=random_pokemon.offensive_moves2[0][1]
                        chosen_one.offensive_moves1[0][1]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves1[0][1]
                        chosen_one.offensive_moves2[0][1]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves2[0][1]
                        chosen_one.offensive_moves3[0][1]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves3[0][1]
                        random_pokemon.offensive_moves1[0][1]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves1[0][1]
                        random_pokemon.offensive_moves2[0][1]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves2[0][1]
                        random_pokemon.offensive_moves3[0][1]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves3[0][1]
                        random_pokemon.offensive_moves1[0][2]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves1[0][2]
                        random_pokemon.offensive_moves2[0][2]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves2[0][2]
                        random_pokemon.offensive_moves3[0][2]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves3[0][2]
                        print(f"{random_pokemon.name} used {random_pokemon.defensive_moves2[0][0]}")
                        if random_pokemon_speed<random_pokemon.speed:
                            print(f"{random_pokemon.name}'s speed increased")
                        if random_pokemon.defensive_moves2[0][4]==None:
                            chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][2]
                            chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][2]
                            chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][2]                    
                        if random_pokemon.defensive_moves2[0][2]>0:
                            random_pokemon.hp=(chosen_one.defensive_moves2[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                        if random_pokemon_check<random_pokemon.offensive_moves2[0][1]:
                            print(f"{random_pokemon.name}'s attack increased")
                        if random_pokemon_hp<random_pokemon.hp:
                            print(f"{random_pokemon.name} healed")
                        if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                            print(f"{random_pokemon.name}'s defence increased")
                        random_pokemon_paralasys=random2.randint(1,100)
                        if random_pokemon_paralasys<=random_pokemon.defensive_moves2[0][6]:
                            print(f"{chosen_one.name} paralyzed {random_pokemon.name}")
                            chosen_one_paralasys_mode=True
                        random_pokemon_burn=random2.randint(1,100)
                        if random_pokemon_burn<=random_pokemon.defensive_moves2[0][7]:
                            print(f"{random_pokemon.name} burned {chosen_one.name}")
                            random_pokemon_burn_mode=True
                        random_pokemon_freeze=random2.randint(1,100)
                        if random_pokemon_freeze<=random_pokemon.defensive_moves2[0][8]:
                            print(f"{random_pokemon.name} froze {chosen_one.name}")
                            random_pokemon_freeze_mode=True
                        random_pokemon_confusion_effect(random_pokemon, random_pokemon.defensive_moves2[0][9])
                        random_pokemon_sleep_effect(random_pokemon.defensive_moves2[0][10])
                        random_pokemon_poison_effect(5)
                        random_pokemon_badly_poison_effect(5)
                        print()
                        random_pokemon.energy-=3
                        round4=0
                        round5=0
                        round6=0
                    else:
                        AI_choice=random2.randint(1,3)
                        if AI_choice==1:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage_1*random_pokemon.attack/100)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                            if random_pokemon_damage1>1:
                                print("It's super effective")
                            elif random_pokemon_damage1==0:
                                print("It's immune to it")
                            elif random_pokemon_damage1<1:
                                print("It's not effective")
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.offensive_moves1[0][4]:
                                print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                random_pokemon_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.offensive_moves1[0][5]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.offensive_moves1[0][6]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves1[0][7])
                            random_pokemon_poison_effect(1)
                            random_pokemon_badly_poison_effect(1)
                            print()
                        elif AI_choice==2:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage_2*random_pokemon.attack/100)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                            if random_pokemon_damage2>1:
                                print("It's super effective")
                            elif random_pokemon_damage2==0:
                                print("It's immune to it")
                            elif random_pokemon_damage2<1:
                                print("It's not effective")
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.offensive_moves2[0][4]:
                                print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                random_pokemon_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.offensive_moves2[0][5]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.offensive_moves2[0][6]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves2[0][7])
                            random_pokemon_poison_effect(2)
                            random_pokemon_badly_poison_effect(2)
                            print()
                        else:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage_3*random_pokemon.attack/100)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                            if random_pokemon_damage3>1:
                                print("It's super effective")
                            elif random_pokemon_damage3==0:
                                print("It's immune to it")
                            elif random_pokemon_damage3<1:
                                print("It's not effective")
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.offensive_moves3[0][4]:
                                print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                random_pokemon_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.offensive_moves3[0][5]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.offensive_moves3[0][6]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves3[0][7])
                            random_pokemon_poison_effect(3)
                            random_pokemon_badly_poison_effect(3)
                            print()
                elif random_pokemon.speed<chosen_one.speed:
                    if (1+random_pokemon.defensive_moves1[0][5])*random_pokemon.speed>chosen_one.speed:
                        random_pokemon_speed=random_pokemon.speed
                        random_pokemon.speed=(1+random_pokemon.defensive_moves1[0][5])*random_pokemon.speed
                        random_pokemon_check=random_pokemon.offensive_moves1[0][1]
                        chosen_one.offensive_moves1[0][1]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][1]
                        chosen_one.offensive_moves2[0][1]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][1]
                        chosen_one.offensive_moves3[0][1]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][1]
                        random_pokemon.offensive_moves1[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves1[0][1]
                        random_pokemon.offensive_moves2[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves2[0][1]
                        random_pokemon.offensive_moves3[0][1]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves3[0][1]
                        random_pokemon.offensive_moves1[0][2]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves1[0][2]
                        random_pokemon.offensive_moves2[0][2]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves2[0][2]
                        random_pokemon.offensive_moves3[0][2]= (1 + random_pokemon.defensive_moves1[0][3]) * random_pokemon.offensive_moves3[0][2]
                        print(f"{random_pokemon.name} used {random_pokemon.defensive_moves1[0][0]}")
                        if random_pokemon_speed<random_pokemon.speed:
                            print(f"{random_pokemon.name}'s speed increased")
                        if random_pokemon.defensive_moves1[0][2]>0:
                            random_pokemon.hp=(chosen_one.defensive_moves1[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                        if random_pokemon_check<random_pokemon.offensive_moves1[0][1]:
                            print(f"{random_pokemon.name}'s attack increased")
                        if random_pokemon_hp<random_pokemon.hp:
                            print(f"{random_pokemon.name} healed")
                        if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                            print(f"{random_pokemon.name}'s defence increased")
                        random_pokemon_paralasys=random2.randint(1,100)
                        if random_pokemon_paralasys<=random_pokemon.defensive_moves1[0][6]:
                            print(f"{chosen_one.name} paralyzed {random_pokemon.name}")
                            chosen_one_paralasys_mode=True
                        random_pokemon_burn=random2.randint(1,100)
                        if random_pokemon_burn<=random_pokemon.defensive_moves1[0][7]:
                            print(f"{random_pokemon.name} burned {chosen_one.name}")
                            random_pokemon_burn_mode=True
                        random_pokemon_freeze=random2.randint(1,100)
                        if random_pokemon_freeze<=random_pokemon.defensive_moves1[0][8]:
                            print(f"{random_pokemon.name} froze {chosen_one.name}")
                            random_pokemon_freeze_mode=True
                        random_pokemon_confusion_effect(random_pokemon, random_pokemon.defensive_moves1[0][9])
                        random_pokemon_sleep_effect(random_pokemon.defensive_moves1[0][10])
                        random_pokemon_poison_effect(4)
                        random_pokemon_badly_poison_effect(4)
                        print()
                        if random_pokemon.defensive_moves1[0][4]==None:
                            chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][2]
                            chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][2]
                            chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][2]
                    
                        random_pokemon.energy-=3
                        round4=0
                        round5=0
                        round6=0
                    elif (1+random_pokemon.defensive_moves2[0][5])*random_pokemon.speed>chosen_one.speed:
                        random_pokemon_speed=random_pokemon.speed
                        random_pokemon.speed=(1+random_pokemon.defensive_moves2[0][5])*random_pokemon.speed
                        random_pokemon_check=random_pokemon.offensive_moves1[0][1]
                        chosen_one.offensive_moves1[0][1]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves1[0][1]
                        chosen_one.offensive_moves2[0][1]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves2[0][1]
                        chosen_one.offensive_moves3[0][1]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves3[0][1]
                        random_pokemon.offensive_moves1[0][1]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves1[0][1]
                        random_pokemon.offensive_moves2[0][1]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves2[0][1]
                        random_pokemon.offensive_moves3[0][1]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves3[0][1]
                        random_pokemon.offensive_moves1[0][2]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves1[0][2]
                        random_pokemon.offensive_moves2[0][2]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves2[0][2]
                        random_pokemon.offensive_moves3[0][2]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves3[0][2]
                        print(f"{random_pokemon.name} used {random_pokemon.defensive_moves1[0][0]}")
                        if random_pokemon_speed<random_pokemon.speed:
                            print(f"{random_pokemon.name}'s speed increased")
                        if random_pokemon.defensive_moves1[0][2]>0:
                            random_pokemon.hp=(chosen_one.defensive_moves1[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                        if random_pokemon_check<random_pokemon.offensive_moves1[0][1]:
                            print(f"{random_pokemon.name}'s attack increased")
                        if random_pokemon_hp<random_pokemon.hp:
                            print(f"{random_pokemon.name} healed")
                        if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                            print(f"{random_pokemon.name}'s defence increased")
                        random_pokemon_paralasys=random2.randint(1,100)
                        if random_pokemon_paralasys<=random_pokemon.defensive_moves2[0][6]:
                            print(f"{chosen_one.name} paralyzed {random_pokemon.name}")
                            chosen_one_paralasys_mode=True
                        random_pokemon_burn=random2.randint(1,100)
                        if random_pokemon_burn<=random_pokemon.defensive_moves2[0][7]:
                            print(f"{random_pokemon.name} burned {chosen_one.name}")
                            random_pokemon_burn_mode=True
                        random_pokemon_freeze=random2.randint(1,100)
                        if random_pokemon_freeze<=random_pokemon.defensive_moves2[0][8]:
                            print(f"{random_pokemon.name} froze {chosen_one.name}")
                            random_pokemon_freeze_mode=True
                        random_pokemon_confusion_effect(random_pokemon, random_pokemon.defensive_moves2[0][9])
                        random_pokemon_sleep_effect(random_pokemon.defensive_moves2[0][10])
                        random_pokemon_poison_effect(5)
                        random_pokemon_badly_poison_effect(5)
                        print()
                        if random_pokemon.defensive_moves1[0][4]==None:
                           chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves1[0][2]
                           chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves2[0][2]
                           chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves3[0][2] 
                        random_pokemon.energy-=3
                        round4=0
                        round5=0
                        round6=0
                    else:
                        AI_choice=random2.randint(1,3)
                        if AI_choice==1:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage_1*random_pokemon.attack/100)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                            if random_pokemon_damage1>1:
                                print("It's super effective")
                            elif random_pokemon_damage1==0:
                                print("It's immune to it")
                            elif random_pokemon_damage1<1:
                                print("It's not effective")
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.offensive_moves1[0][4]:
                                print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                random_pokemon_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.offensive_moves1[0][5]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.offensive_moves1[0][6]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves1[0][7])
                            random_pokemon_poison_effect(1)
                            random_pokemon_badly_poison_effect(1)
                            print()
                        elif AI_choice==2:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage_2*random_pokemon.attack/100)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                            if random_pokemon_damage2>1:
                                print("It's super effective")
                            elif random_pokemon_damage2==0:
                                print("It's immune to it")
                            elif random_pokemon_damage2<1:
                                print("It's not effective")
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.offensive_moves2[0][4]:
                                print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                random_pokemon_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.offensive_moves2[0][5]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.offensive_moves2[0][6]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves2[0][7])
                            random_pokemon_poison_effect(2)
                            random_pokemon_badly_poison_effect(2)
                            print()
                        else:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage_3*random_pokemon.attack/100)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                            if random_pokemon_damage3>1:
                                print("It's super effective")
                            elif random_pokemon_damage3==0:
                                print("It's immune to it")
                            elif random_pokemon_damage3<1:
                                print("It's not effective")
                            random_pokemon_paralasys=random2.randint(1,100)
                            if random_pokemon_paralasys<=random_pokemon.offensive_moves3[0][4]:
                                print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                                random_pokemon_paralasys_mode=True
                            random_pokemon_burn=random2.randint(1,100)
                            if random_pokemon_burn<=random_pokemon.offensive_moves3[0][5]:
                                print(f"{random_pokemon.name} burned {chosen_one.name}")
                                random_pokemon_burn_mode=True
                            random_pokemon_freeze=random2.randint(1,100)
                            if random_pokemon_freeze<=random_pokemon.offensive_moves3[0][6]:
                                print(f"{random_pokemon.name} froze {chosen_one.name}")
                                random_pokemon_freeze_mode=True
                            random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves3[0][7])
                            random_pokemon_poison_effect(3)
                            random_pokemon_badly_poison_effect(3)
                            print()
                else:
                    AI_choice=random2.randint(1,3)
                    if AI_choice==1:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage_1*random_pokemon.attack/100)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                        if random_pokemon_damage1>1:
                            print("It's super effective")
                        elif random_pokemon_damage1==0:
                            print("It's immune to it")
                        elif random_pokemon_damage1<1:
                            print("It's not effective")
                        random_pokemon_paralasys=random2.randint(1,100)
                        if random_pokemon_paralasys<=random_pokemon.offensive_moves1[0][4]:
                            print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                            random_pokemon_paralasys_mode=True
                        random_pokemon_burn=random2.randint(1,100)
                        if random_pokemon_burn<=random_pokemon.offensive_moves1[0][5]:
                            print(f"{random_pokemon.name} burned {chosen_one.name}")
                            random_pokemon_burn_mode=True
                        random_pokemon_freeze=random2.randint(1,100)
                        if random_pokemon_freeze<=random_pokemon.offensive_moves1[0][6]:
                            print(f"{random_pokemon.name} froze {chosen_one.name}")
                            random_pokemon_freeze_mode=True
                        random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves1[0][7])
                        random_pokemon_poison_effect(1)
                        random_pokemon_badly_poison_effect(1)
                    elif AI_choice==2:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage_2*random_pokemon.attack/100)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                        if random_pokemon_damage2>1:
                            print("It's super effective")
                        elif random_pokemon_damage2==0:
                            print("It's immune to it")
                        elif random_pokemon_damage2<1:
                            print("It's not effective")
                        random_pokemon_paralasys=random2.randint(1,100)
                        if random_pokemon_paralasys<=random_pokemon.offensive_moves2[0][4]:
                            print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                            random_pokemon_paralasys_mode=True
                        random_pokemon_burn=random2.randint(1,100)
                        if random_pokemon_burn<=random_pokemon.offensive_moves2[0][5]:
                            print(f"{random_pokemon.name} burned {chosen_one.name}")
                            random_pokemon_burn_mode=True
                        chosen_one_freeze=random2.randint(1,100)
                        if chosen_one_freeze<=chosen_one.offensive_moves2[0][6]:
                            print(f"{chosen_one.name} froze {random_pokemon.name}")
                            chosen_one_freeze_mode=True
                        random_pokemon_freeze=random2.randint(1,100)
                        if random_pokemon_freeze<=random_pokemon.offensive_moves2[0][6]:
                            print(f"{random_pokemon.name} froze {chosen_one.name}")
                            random_pokemon_freeze_mode=True
                        random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves2[0][7])
                        random_pokemon_poison_effect(2)
                        random_pokemon_badly_poison_effect(2)
                    else:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage_3*random_pokemon.attack/100)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                        if random_pokemon_damage3>1:
                            print("It's super effective")
                        elif random_pokemon_damage3==0:
                            print("It's immune to it")
                        elif random_pokemon_damage3<1:
                            print("It's not effective")
                        random_pokemon_paralasys=random2.randint(1,100)
                        if random_pokemon_paralasys<=random_pokemon.offensive_moves3[0][4]:
                            print(f"{random_pokemon.name} paralyzed {chosen_one.name}")
                            random_pokemon_paralasys_mode=True
                        random_pokemon_burn=random2.randint(1,100)
                        if random_pokemon_burn<=random_pokemon.offensive_moves3[0][5]:
                            print(f"{random_pokemon.name} burned {chosen_one.name}")
                            random_pokemon_burn_mode=True
                        random_pokemon_freeze=random2.randint(1,100)
                        if random_pokemon_freeze<=random_pokemon.offensive_moves3[0][6]:
                            print(f"{random_pokemon.name} froze {chosen_one.name}")
                            random_pokemon_freeze_mode=True
                        random_pokemon_confusion_effect(random_pokemon, random_pokemon.offensive_moves3[0][7])
                        random_pokemon_poison_effect(3)
                        random_pokemon_badly_poison_effect(3)
                    print()
            round1+=1
            round4+=1
            if chosen_one.hp<=0:
                print("You lost")
                break
            elif random_pokemon.hp<=0:
                print("You won")
                break
            time.sleep(1)

        #Player's turn
        random_pokemon_damage_check=random_pokemon.offensive_moves1[0][1]
        chosen_one_damage_check=chosen_one.offensive_moves1[0][1]
        chosen_one.hp=int(chosen_one.hp)
        random_pokemon.hp=int(random_pokemon.hp)
        round3=round1-round2
        if round6==chosen_one.defensive_moves2[0][4] and chosen_one.defensive_moves2[0][4]!=None:
            #prevents the defensive moves from being too OP
            random_pokemon.offensive_moves1[0][1]=random_pokemon.offensive_moves1[0][2]
            random_pokemon.offensive_moves2[0][1]=random_pokemon.offensive_moves2[0][2]
            random_pokemon.offensive_moves3[0][1]=random_pokemon.offensive_moves3[0][2]

        if round6==chosen_one.defensive_moves1[0][4] and chosen_one.defensive_moves1[0][4]!=None:
            #prevents the defensive moves from being too OP
            random_pokemon.offensive_moves1[0][1]=random_pokemon.offensive_moves1[0][2]
            random_pokemon.offensive_moves2[0][1]=random_pokemon.offensive_moves1[0][2]
            random_pokemon.offensive_moves3[0][1]=random_pokemon.offensive_moves1[0][2]
        if random_pokemon_paralasys_number==5:
            random_pokemon_paralasys_mode=False
            random_pokemon_paralasys_number=0
        if random_pokemon_paralasys_mode==True and random_pokemon_paralasys_number<=5:
            random_pokemon_paralasys_number+=1
            print(f"{chosen_one.name} is paralyzed")
        if random_pokemon_freeze_mode==True:
            freeze_chance=random2.randint(1,256)
            if freeze_chance<=25:
                random_pokemon_freeze_mode=False
                print(f"{chosen_one.name} escaped the ice")
            else:
                print(f"{chosen_one.name} is frozen")
        if random_pokemon_sleep_mode[-1]==True:
            if random_pokemon_sleep_number==0:
                print(f"{chosen_one.name} is fast sleep")
                random_pokemon_sleep_number+=1
            else:
                wake_up=random2.randint(1, 5-random_pokemon_sleep_number)
                if wake_up==1:
                    print(f"{chosen_one.name} woke up")
                    random_pokemon_sleep_number=0
                    random_pokemon_sleep_mode.append(False)
                else:
                    print(f"{chosen_one.name} is fast sleep")
                    random_pokemon_sleep_number+=1
        if random_pokemon_paralasys_mode==False and random_pokemon_freeze_mode==False and random_pokemon_sleep_mode[-1]==False:
            if chosen_one.energy<=0:
                chosen_one.energy=0
                print(f"""{chosen_one.name}   hp:{chosen_one.hp}   energy:{chosen_one.energy} heals:{chosen_one.heal}
{random_pokemon.name}   hp:{random_pokemon.hp}   energy:{random_pokemon.energy} heals:{random_pokemon.heal}""")
                print(f"""{chosen_one.name} has no more energy
{chosen_one.name} used struggle""")
                print()
                chosen_one.hp=3/4*chosen_one.hp
                random_pokemon.hp=random_pokemon.hp-((chosen_one.offensive_moves1[0][1]+chosen_one.offensive_moves2[0][1]+chosen_one.offensive_moves3[0][1])*chosen_one.attack/100/3)
            #Player's turn
            elif chosen_one.energy>0:
                random_pokemon_damage_check=random_pokemon.offensive_moves1[0][1]
                chosen_one_damage_check=chosen_one.offensive_moves1[0][1]
                while choice==choice:
                    if choice=="6":
                        if chosen_one.heal>0:
                            chosen_one.hp+=100
                            print(f"You used a heal on {chosen_one.name}")
                            chosen_one.heal-=1
                            if chosen_one.hp>chosen_one.max_hp:
                                chosen_one.hp=chosen_one.max_hp
                        elif chosen_one.heal<=0:
                            print("You don't have any heals")
                    elif random_pokemon_confusion_mode[-1]==True and random_pokemon_confusion_number<4:
                        spin_the_wheel=random2.randint(1,2)
                        if spin_the_wheel==1:
                            print(f"{chosen_one.name} is confused")
                            chosen_one.hp-=((chosen_one.offensive_moves1[0][1]+chosen_one.offensive_moves2[0][1]+chosen_one.offensive_moves3[0][1])*chosen_one.attack/100/3)
                            random_pokemon_confusion_number+=1
                            break
                        if spin_the_wheel==2:
                            random_pokemon_confusion_number+=1
                    elif choice=="1":
                        random_pokemon.hp= random_pokemon.hp - ((chosen_one.offensive_moves1[0][1])*chosen_one_damage_1*chosen_one.attack/100)
                        chosen_one.energy=chosen_one.energy-1
                        print(f"{chosen_one.name} used {chosen_one.offensive_moves1[0][0]}")
                        if chosen_one_damage1>1:
                            print("It's super effective")
                        elif chosen_one_damage1==0:
                            print("It's immune to it")
                        elif chosen_one_damage1<1:
                            print("It's not effective")
                        chosen_one_paralasys=random2.randint(1,100)
                        if chosen_one_paralasys<=chosen_one.offensive_moves1[0][4]:
                            print(f"{chosen_one.name} paralyzed {random_pokemon.name}")
                            chosen_one_paralasys_mode=True
                        chosen_one_burn=random2.randint(1,100)
                        if random_pokemon_burn<=random_pokemon.offensive_moves1[0][5]:
                            print(f"{random_pokemon.name} burned {chosen_one.name}")
                            random_pokemon_burn_mode=True
                        chosen_one_freeze=random2.randint(1,100)
                        if chosen_one_freeze<=chosen_one.offensive_moves1[0][6]:
                            print(f"{chosen_one.name} froze {random_pokemon.name}")
                            chosen_one_freeze_mode=True
                        chosen_one_confusion_effect(chosen_one, chosen_one.offensive_moves1[0][7])
                        chosen_one_poison_effect(chosen_one.offensive_moves1[0][8])
                        chosen_one_badly_poison_effect(chosen_one.offensive_moves1[0][9])
                        break
                    elif choice=="2":
                        random_pokemon.hp= random_pokemon.hp - ((chosen_one.offensive_moves2[0][1])*chosen_one_damage_2*chosen_one.attack/100)
                        chosen_one.energy=chosen_one.energy-1
                        print(f"{chosen_one.name} used {chosen_one.offensive_moves2[0][0]}")
                        if chosen_one_damage2>1:
                            print("It's super effective")
                        elif chosen_one_damage2==0:
                            print("It's immune to it")
                        elif chosen_one_damage2<1:
                            print("It's not effective")
                        chosen_one_paralasys=random2.randint(1,100)
                        if chosen_one_paralasys<=chosen_one.offensive_moves2[0][4]:
                            print(f"{chosen_one.name} paralyzed {random_pokemon.name}")
                            chosen_one_paralasys_mode=True
                        chosen_one_burn=random2.randint(1,100)
                        if chosen_one_burn<=chosen_one.offensive_moves2[0][5]:
                            print(f"{chosen_one.name} burned {random_pokemon.name}")
                            chosen_one_burn_mode=True
                        chosen_one_freeze=random2.randint(1,100)
                        if chosen_one_freeze<=chosen_one.offensive_moves2[0][6]:
                            print(f"{chosen_one.name} froze {random_pokemon.name}")
                            chosen_one_freeze_mode=True
                        chosen_one_confusion_effect(chosen_one, chosen_one.offensive_moves2[0][7])
                        chosen_one_poison_effect(chosen_one.offensive_moves2[0][8])
                        chosen_one_badly_poison_effect(chosen_one.offensive_moves2[0][9])
                        break
                    elif choice=="3":
                        random_pokemon.hp= random_pokemon.hp - ((chosen_one.offensive_moves3[0][1])*chosen_one_damage_3*chosen_one.attack/100)
                        chosen_one.energy=chosen_one.energy-1
                        print(f"{chosen_one.name} used {chosen_one.offensive_moves3[0][0]}")
                        if chosen_one_damage3>1:
                            print("It's super effective")
                        elif chosen_one_damage3==0:
                            print("It's immune to it")
                        elif chosen_one_damage3<1:
                            print("It's not effective")
                        chosen_one_paralasys=random2.randint(1,100)
                        if chosen_one_paralasys<=chosen_one.offensive_moves3[0][4]:
                            print(f"{chosen_one.name} paralyzed {random_pokemon.name}")
                            chosen_one_paralasys_mode=True
                        chosen_one_burn=random2.randint(1,100)
                        if chosen_one_burn<=chosen_one.offensive_moves3[0][5]:
                            print(f"{chosen_one.name} burned {random_pokemon.name}")
                            chosen_one_burn_mode=True
                        chosen_one_freeze=random2.randint(1,100)
                        if chosen_one_freeze<=chosen_one.offensive_moves3[0][6]:
                            print(f"{chosen_one.name} froze {random_pokemon.name}")
                            chosen_one_freeze_mode=True
                        chosen_one_confusion_effect(chosen_one, chosen_one.offensive_moves3[0][7])
                        chosen_one_poison_effect(chosen_one.offensive_moves3[0][8])
                        chosen_one_badly_poison_effect(chosen_one.offensive_moves3[0][9])
                        break
                    elif choice=="4":
                        chosen_one_check=chosen_one.offensive_moves1[0][1]
                        random_pokemon.offensive_moves1[0][1]= (1 - chosen_one.defensive_moves1[0][1]) * random_pokemon.offensive_moves1[0][1]
                        random_pokemon.offensive_moves2[0][1]= (1 - chosen_one.defensive_moves1[0][1]) * random_pokemon.offensive_moves2[0][1]
                        random_pokemon.offensive_moves3[0][1]= (1 - chosen_one.defensive_moves1[0][1]) * random_pokemon.offensive_moves3[0][1]
                        chosen_one.offensive_moves1[0][1]=(1+chosen_one.defensive_moves1[0][3])*chosen_one.offensive_moves1[0][1]
                        chosen_one.offensive_moves2[0][1]=(1+chosen_one.defensive_moves1[0][3])*chosen_one.offensive_moves2[0][1]
                        chosen_one.offensive_moves3[0][1]=(1+chosen_one.defensive_moves1[0][3])*chosen_one.offensive_moves3[0][1]
                        chosen_one.offensive_moves1[0][2]=(1+chosen_one.defensive_moves1[0][3])*chosen_one.offensive_moves1[0][2]
                        chosen_one.offensive_moves2[0][2]=(1+chosen_one.defensive_moves1[0][3])*chosen_one.offensive_moves2[0][2]
                        chosen_one.offensive_moves3[0][2]=(1+chosen_one.defensive_moves1[0][3])*chosen_one.offensive_moves3[0][2]
                        chosen_one_hp=chosen_one.hp
                        chosen_one.hp= (chosen_one.defensive_moves1[0][2] / 100 * chosen_one.max_hp) + chosen_one.hp
                        chosen_one_speed=chosen_one.speed
                        chosen_one.speed=(1+chosen_one.defensive_moves1[0][5])*chosen_one.speed
                        print(f"{chosen_one.name} used {chosen_one.defensive_moves1[0][0]}")
                        if chosen_one_speed<chosen_one.speed:
                            print(f"{chosen_one.name}'s speed increased")
                        if chosen_one.defensive_moves1[0][3]==None:
                            random_pokemon.offensive_moves1[0][2]=(1-chosen_one.defensive_moves1[0][1])*random_pokemon.offensive_moves1[0][2]
                            random_pokemon.offensive_moves2[0][2]=(1-chosen_one.defensive_moves1[0][1])*random_pokemon.offensive_moves2[0][2]
                            random_pokemon.offensive_moves3[0][2]=(1-chosen_one.defensive_moves1[0][1])*random_pokemon.offensive_moves3[0][2]
                        if chosen_one_check<chosen_one.offensive_moves1[0][1]:
                            print(f"{chosen_one.name}'s attack increased")
                        if chosen_one.hp>chosen_one.max_hp:
                            chosen_one.hp=chosen_one.max_hp
                        chosen_one.energy=chosen_one.energy-3
                
                        if random_pokemon_damage_check>random_pokemon.offensive_moves1[0][1]:
                            print(f"{chosen_one.name}'s defence increased")
                        if chosen_one.hp>chosen_one_hp:
                            print(f"{chosen_one.name}'s hp increased")
                        
                        chosen_one_paralasys=random2.randint(1,100)
                        if chosen_one_paralasys<=chosen_one.defensive_moves1[0][6]:
                            print(f"{chosen_one.name} paralyzed {random_pokemon.name}")
                            chosen_one_paralasys_mode=True
                        chosen_one_burn=random2.randint(1,100)
                        if chosen_one_burn<=chosen_one.defensive_moves1[0][7]:
                            print(f"{chosen_one.name} burned {random_pokemon.name}")
                            chosen_one_paralasys_mode=True
                        chosen_one_freeze=random2.randint(1,100)
                        if chosen_one_freeze<=chosen_one.defensive_moves1[0][8]:
                            print(f"{chosen_one.name} froze {random_pokemon.name}")
                            chosen_one_freeze_mode=True
                        chosen_one_confusion_effect(chosen_one, chosen_one.defensive_moves1[0][9])
                        chosen_one_sleep_effect(chosen_one.defensive_moves1[0][10])
                        chosen_one_poison_effect(chosen_one.defensive_moves1[0][11])
                        chosen_one_badly_poison_effect(chosen_one.defensive_moves1[0][12])
                        round1=0
                        round2=0
                        round3=0
                        break
                    elif choice=="5":
                        chosen_one_check=chosen_one.offensive_moves2[0][1]
                        random_pokemon.offensive_moves1[0][1]= (1 - chosen_one.defensive_moves2[0][1]) * random_pokemon.offensive_moves1[0][1]
                        random_pokemon.offensive_moves2[0][1]= (1 - chosen_one.defensive_moves2[0][1]) * random_pokemon.offensive_moves2[0][1]
                        random_pokemon.offensive_moves3[0][1]= (1 - chosen_one.defensive_moves2[0][1]) * random_pokemon.offensive_moves3[0][1]
                        chosen_one.offensive_moves1[0][1]=(1+chosen_one.defensive_moves2[0][3])*chosen_one.offensive_moves1[0][1]
                        chosen_one.offensive_moves2[0][1]=(1+chosen_one.defensive_moves2[0][3])*chosen_one.offensive_moves2[0][1]
                        chosen_one.offensive_moves3[0][1]=(1+chosen_one.defensive_moves2[0][3])*chosen_one.offensive_moves3[0][1]
                        chosen_one.offensive_moves1[0][2]=(1+chosen_one.defensive_moves2[0][3])*chosen_one.offensive_moves1[0][2]
                        chosen_one.offensive_moves2[0][2]=(1+chosen_one.defensive_moves2[0][3])*chosen_one.offensive_moves2[0][2]
                        chosen_one.offensive_moves3[0][2]=(1+chosen_one.defensive_moves2[0][3])*chosen_one.offensive_moves3[0][2]
                        chosen_one_hp=chosen_one.hp
                        chosen_one.hp= (chosen_one.defensive_moves2[0][2] / 100 * chosen_one.max_hp) + chosen_one.hp
                        chosen_one_speed=chosen_one.speed
                        chosen_one.speed=(1+chosen_one.defensive_moves1[0][5])*chosen_one.speed
                        if chosen_one_speed<chosen_one.speed:
                            print(f"{chosen_one.name}'s speed increased")
                        if chosen_one.defensive_moves2[0][3]==None:
                            random_pokemon.offensive_moves1[0][2]=(1-chosen_one.defensive_moves2[0][1])*random_pokemon.offensive_moves1[0][2]
                            random_pokemon.offensive_moves2[0][2]=(1-chosen_one.defensive_moves2[0][1])*random_pokemon.offensive_moves2[0][2]
                            random_pokemon.offensive_moves3[0][2]=(1-chosen_one.defensive_moves2[0][1])*random_pokemon.offensive_moves3[0][2]
                        print(f"{chosen_one.name} used {chosen_one.defensive_moves2[0][0]}")                                     
                        if chosen_one.hp>chosen_one.max_hp:
                            chosen_one.hp=chosen_one.max_hp
                        if chosen_one_check<chosen_one.offensive_moves2[0][1]:
                            print(f"{chosen_one.name}'s attack increased")
                        chosen_one.energy=chosen_one.energy-3
                        if random_pokemon_damage_check>random_pokemon.offensive_moves1[0][1]:
                            print(f"{chosen_one.name}'s defence increased")
                        if chosen_one.hp>chosen_one_hp:
                            print(f"{chosen_one.name}'s hp increased")
                        
                        chosen_one_paralasys=random2.randint(1,100)
                        if chosen_one_paralasys<=chosen_one.defensive_moves2[0][6]:
                            print(f"{chosen_one.name} paralyzed {random_pokemon.name}")
                            chosen_one_paralasys_mode=True
                        chosen_one_burn=random2.randint(1,100)
                        if chosen_one_burn<=chosen_one.defensive_moves2[0][7]:
                            print(f"{chosen_one.name} burned {random_pokemon.name}")
                            chosen_one_burn_mode=True
                        chosen_one_freeze=random2.randint(1,100)
                        if chosen_one_freeze<=chosen_one.defensive_moves2[0][8]:
                            print(f"{chosen_one.name} froze {random_pokemon.name}")
                            chosen_one_freeze_mode=True
                        chosen_one_confusion_effect(chosen_one, chosen_one.defensive_moves2[0][9])
                        chosen_one_sleep_effect(chosen_one.defensive_moves2[0][10])
                        chosen_one_poison_effect(chosen_one.defensive_moves2[0][11])
                        chosen_one_badly_poison_effect(chosen_one.defensive_moves2[0][12])
                        round1=0
                        round2=0
                        round3=0
                        break
                    else:
                        print("You gave an invalid move try again\n")
                        choice=input("What is your move? Note:Do your moves in order from 1 to 6. 1 being the first offensive move and 6 being a heal." )
        
        
        for i in range(len(random_pokemon.element)):
            if random_pokemon.element[i]=="Fire" and chosen_one_burn_mode==True:
                chosen_one_burn_mode=False
                print(f"{random_pokemon.name} isn't affected by burn")
        for i in range(len(chosen_one.element)):
            if chosen_one.element[i]=="Fire" and random_pokemon_burn_mode==True:
                random_pokemon_burn_mode=False
                print(f"{chosen_one.name} isn't affected by burn")
        if random_pokemon_burn_number==10:
            random_pokemon_burn_number=0
            chosen_one.offensive_moves2[0][1]=chosen_one.offensive_moves2[0][1]*2
            chosen_one.offensive_moves2[0][2]=chosen_one.offensive_moves2[0][2]*2
            chosen_one.offensive_moves1[0][1]=chosen_one.offensive_moves1[0][1]*2
            chosen_one.offensive_moves1[0][2]=chosen_one.offensive_moves1[0][2]*2
            chosen_one.offensive_moves3[0][1]=chosen_one.offensive_moves3[0][1]*2
            chosen_one.offensive_moves3[0][2]=chosen_one.offensive_moves3[0][2]*2
            random_pokemon_burn_mode=False
        if random_pokemon_burn_mode== True:
            print(f"{chosen_one.name} is burned")
            chosen_one.hp-=chosen_one.max_hp/8
            random_pokemon_burn_number+=1
        if random_pokemon_burn_number==1:
            chosen_one.offensive_moves2[0][1]=chosen_one.offensive_moves2[0][1]/2
            chosen_one.offensive_moves2[0][2]=chosen_one.offensive_moves2[0][2]/2
            chosen_one.offensive_moves1[0][1]=chosen_one.offensive_moves1[0][1]/2
            chosen_one.offensive_moves1[0][2]=chosen_one.offensive_moves1[0][2]/2
            chosen_one.offensive_moves3[0][1]=chosen_one.offensive_moves3[0][1]/2
            chosen_one.offensive_moves3[0][2]=chosen_one.offensive_moves3[0][2]/2

        if chosen_one_burn_number==10:
            chosen_one_burn_number=0
            random_pokemon.offensive_moves2[0][1]=random_pokemon.offensive_moves2[0][1]*2
            random_pokemon.offensive_moves2[0][2]=random_pokemon.offensive_moves2[0][2]*2
            random_pokemon.offensive_moves1[0][1]=random_pokemon.offensive_moves1[0][1]*2
            random_pokemon.offensive_moves1[0][2]=random_pokemon.offensive_moves1[0][2]*2
            random_pokemon.offensive_moves3[0][1]=random_pokemon.offensive_moves3[0][1]*2
            random_pokemon.offensive_moves3[0][2]=random_pokemon.offensive_moves3[0][2]*2
            chosen_one_burn_mode=False
        if chosen_one_burn_mode==True:
            print(f"{random_pokemon.name} is burned")
            random_pokemon.hp-=random_pokemon.max_hp/8
            chosen_one_burn_number+=1
        if chosen_one_burn_number==1:
            random_pokemon.offensive_moves2[0][1]=random_pokemon.offensive_moves2[0][1]/2
            random_pokemon.offensive_moves2[0][2]=random_pokemon.offensive_moves2[0][2]/2
            random_pokemon.offensive_moves1[0][1]=random_pokemon.offensive_moves1[0][1]/2
            random_pokemon.offensive_moves1[0][2]=random_pokemon.offensive_moves1[0][2]/2
            random_pokemon.offensive_moves3[0][1]=random_pokemon.offensive_moves3[0][1]/2
            random_pokemon.offensive_moves3[0][2]=random_pokemon.offensive_moves3[0][2]/2
        
        if random_pokemon_poison_mode[-1]== True:
            print(f"{chosen_one.name} is poisoned")
            chosen_one.hp-=chosen_one.max_hp/16
            random_pokemon_poison_number+=1
        if random_pokemon_poison_number==20:
            random_pokemon_poison_number=0
            random_pokemon_poison_mode(False)

        if chosen_one_poison_mode[-1]== True:
            print(f"{random_pokemon.name} is poisoned")
            random_pokemon.hp-=chosen_one.max_hp/16
            chosen_one_poison_number+=1
        if chosen_one_poison_number==20:
            chosen_one_poison_number=0
            chosen_one_poison_mode.append(False)          
            
            
        if random_pokemon_badly_poison_mode[-1]== True:
            print(f"{chosen_one.name} is poisoned")
            chosen_one.hp-=chosen_one.max_hp/16*(random_pokemon_badly_poison_number+1)
        random_pokemon_badly_poison_number+=1
        if random_pokemon_badly_poison_number==20:
            random_pokemon_badly_poison_number=0
            random_pokemon_badly_poison_mode.append(False)
            

        if chosen_one_badly_poison_mode[-1]== True:
            print(f"{random_pokemon.name} is poisoned")
            random_pokemon.hp-=chosen_one.max_hp/16*(chosen_one_badly_poison_number+1)
            chosen_one_badly_poison_number+=1
        if chosen_one_badly_poison_number==20:
            chosen_one_badly_poison_number=0
            chosen_one_badly_poison_mode.append(False)

        if chosen_one_confusion_number>4:
            chosen_one_confusion_number=0
        if random_pokemon_confusion_number>4:
            random_pokemon_confusion_number=0
        
        if chosen_one.hp<=0:
            print("You lost")
            break
        elif random_pokemon.hp<=0:
            print("You won")
            break
        chosen_one.hp=int(chosen_one.hp)
        random_pokemon.hp=int(random_pokemon.hp)
        round1+=1
        round4+=1
        round2+=1
        round5+=1
        time.sleep(1)
    else:
        start=random2.randint(1,2)
        


#round end like boost of energy regen 
chosen_one.energy = chosen_one.energy +30
if chosen_one.energy>chosen_one.max_energy:
    chosen_one.energy=chosen_one.max_energy
