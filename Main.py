#Test and debugging
import time
import random2

#intro message & disclaimer
print('In a land far far away...')
print("is the land of textemon. A world were text based monsters roamed.")
print('This idea and all names are from the Nintendo company and Game Freak.')
print("Pokémon is a trademark of Nintendo. This project is not affiliated with or endorsed by Nintendo.")
print("Copyright © ByteCatch Games 2023")
print("All rights reserved. This project and its contents are protected by copyright law. No part of this project may be reproduced, distributed, or transmitted in any form or by any means, without the prior written permission of the copyright owner.")
print("\n\n\n\n")
time.sleep(5)
#core engine
class Pokemon:
    def __init__(self, name, element, max_hp, max_energy,speed):
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

    # noinspection PyArgumentList
    def add_offensive_move1(self, move_name,damage, damage2,move_element):
        # Add an offensive move to the list of moves
        self.offensive_moves1.append([move_name,damage,damage2, move_element,self.energy])
    
    def add_offensive_move2(self, move_name,damage, damage2, move_element):
        # Add an offensive move to the list of moves
        self.offensive_moves2.append([move_name,damage,damage2, move_element,self.energy])

    def add_offensive_move3(self, move_name,damage, damage2, move_element):
        # Add an offensive move to the list of moves
        self.offensive_moves3.append([move_name,damage,damage2, move_element, self.energy])

    def add_defensive_move1(self, move_name, reduce_damage, heal, increase_damage,turns,speed_increase,):
        # Add a defensive move to the list of moves
        self.defensive_moves1.append([move_name, reduce_damage, heal, increase_damage,turns,speed_increase,])

    def add_defensive_move2(self, move_name, reduce_damage, heal, increase_damage,turns,speed_increase,):
        # Add a defensive move to the list of moves
        self.defensive_moves2.append([move_name, reduce_damage, heal, increase_damage,turns,speed_increase,])

# create a Pikachu instance with moves
pikachu = Pokemon("Pikachu", ["Electric"], 400, 60,90,)
pikachu.add_offensive_move1("Thunderbolt", 70,70, "Electric",)
pikachu.add_offensive_move2("Iron Tail", 40,40, "Steel",)
pikachu.add_offensive_move3("Quick Attack", 30,30, "Normal",)
pikachu.add_defensive_move1("Agility", 0, 0,0,None,1,)
pikachu.add_defensive_move2("Double Team", 0, 0,0,None,0.5)

# create a Charizard instance with moves
charizard = Pokemon("Charizard", ["Fire", "Flying"], 520, 50,100,)
charizard.add_offensive_move1("Flamethrower", 60,60, "Fire",)
charizard.add_offensive_move2("Dragon Claw", 50,50,"Dragon",)
charizard.add_offensive_move3("Air Slash", 40,40,"Flying",)
charizard.add_defensive_move1("Dragon Dance",0.3, 0, 0.3,None,0,)
charizard.add_defensive_move2("Roost", 0, 60,0,None,0,)

# create a Blastoise instance with moves
blastoise = Pokemon("Blastoise", ["Water"], 520, 50,78,)
blastoise.add_offensive_move1("Hydro Pump", 60,60,"Water",)
blastoise.add_offensive_move2("Ice Beam", 50,50,"Ice",)
blastoise.add_offensive_move3("Earthquake", 40,40,"Ground",)
blastoise.add_defensive_move1("Protect", 1,0,0,0,0,)
blastoise.add_defensive_move2("Withdraw", 0.5,0,0,None,0,)

# create a Venusaur instance with moves
venusaur = Pokemon("Venusaur", ["Grass", "Poison"], 520, 50,80,)
venusaur.add_offensive_move1("Solar Beam", 60,60,"Grass",)
venusaur.add_offensive_move2("Sludge Bomb", 50,50,"Poison",)
venusaur.add_offensive_move3("Earthquake", 40,40,"Ground",)
venusaur.add_defensive_move1("Leech Seed", 0, 20,0,None,0,)
venusaur.add_defensive_move2("Sleep Powder", 0.4,10,0,None,0,)

# create a Lycanroc instance with moves
lycanroc = Pokemon("Lycanroc", ["Rock"], 480, 45,112,)
lycanroc.add_offensive_move1("Stone Edge", 70,70,"Rock",)
lycanroc.add_offensive_move2("Accelerock", 50,50,"Rock",)
lycanroc.add_offensive_move3("Crunch", 40,40,"Dark",)
lycanroc.add_defensive_move1("Swords Dance", 0,0,0.3,None,0,)
lycanroc.add_defensive_move2("Stealth Rock", 0.3,0,0.3,None,0.3)

# create a Beedrill instance with types Bug and Poison
beedrill = Pokemon("Beedrill", ["Bug", "Poison"], 400, 60,75,)
beedrill.add_offensive_move1("Twineedle", 60,60,"Bug",)
beedrill.add_offensive_move2("Poison Jab", 40,40,"Poison",)
beedrill.add_offensive_move3("U-turn", 60,60,"Bug",)
beedrill.add_defensive_move1("Harden", 0.5,0,0,None,0,)
beedrill.add_defensive_move2("Protect", 1,0,0,0,0,)

# create a Crobat instance with types Poison and Flying
crobat = Pokemon("Crobat", ["Poison", "Flying"], 400, 60,130,)
crobat.add_offensive_move1("Cross Poison", 60,60,"Poison",)
crobat.add_offensive_move2("Air Slash", 50,50,"Flying",)
crobat.add_offensive_move3("Brave Bird", 80,80,"Flying",)
crobat.add_defensive_move1("Roost", 0,60,0,None,0,)
crobat.add_defensive_move2("Toxic", 0.4,10,0,None,0,)

# create a Gengar instance with types Ghost and Poison
gengar = Pokemon("Gengar", ["Ghost", "Poison"], 440, 60,110,)
gengar.add_offensive_move1("Shadow Ball", 60,60,"Ghost",)
gengar.add_offensive_move2("Sludge Bomb", 50,50,"Poison",)
gengar.add_offensive_move3("Venom Drench", 40,40,"Poison",)
gengar.add_defensive_move1("Hypnosis", 0.5,0,0,None,0.5)
gengar.add_defensive_move2("Destiny Bond", 0.3,10,0,None,0.3)

# create a Metagross instance with types Steel and Psychic
metagross = Pokemon("Metagross", ["Steel", "Psychic"], 520, 45,70,)
metagross.add_offensive_move1("Meteor Mash", 70,70,"Steel",)
metagross.add_offensive_move2("Zen Headbutt", 50,50,"Psychic",)
metagross.add_offensive_move3("Psychic", 80,80,"Psychic",)
metagross.add_defensive_move1("Agility", 0,0,0,None,1,)
metagross.add_defensive_move2("Light Screen", 0.3,10,0,None,0,)

# create a Noivern instance with types Flying and Dragon
noivern = Pokemon("Noivern", ["Flying", "Dragon"], 480, 50,123,)
noivern.add_offensive_move1("Dragon Pulse", 60,60,"Dragon",)
noivern.add_offensive_move2("Air Slash", 50,50,"Flying",)
noivern.add_offensive_move3("Hurricane", 70,70,"Flying",)
noivern.add_defensive_move1("Roost",0,60,0,None,0,)
noivern.add_defensive_move2("Protect", 1,0,0,None,0,)

# create a Garchomp instance with types Dragon and Ground
garchomp = Pokemon("Garchomp", ["Dragon", "Ground"], 560, 40,102,)
garchomp.add_offensive_move1("Dragon Claw", 70,70,"Dragon",)
garchomp.add_offensive_move2("Earthquake", 60,60,"Ground",)
garchomp.add_offensive_move3("Stone Edge", 80,80,"Rock",)
garchomp.add_defensive_move1("Swords Dance", 0,0,0.2,None,0,)
garchomp.add_defensive_move2("Sandstorm", 0,0,0.2,None,0,)

# create a Krookodile instance with types Ground and Dark
krookodile = Pokemon("Krookodile", ["Ground", "Dark"], 440, 55,92,)
krookodile.add_offensive_move1("Earthquake", 60,60,"Ground",)
krookodile.add_offensive_move2("Stone Edge", 80,80,"Rock",)
krookodile.add_offensive_move3("Crunch", 70,70,"Dark",)
krookodile.add_defensive_move1("Sandstorm", 0,0,1,None,0,)
krookodile.add_defensive_move2("Swagger", -0.1,0,.3,None,0,)


# Create a Tyranitar instance
tyranitar = Pokemon("Tyranitar", ["Dark", "Rock"], 480, 40,61,)
tyranitar.add_offensive_move1("Crunch", 50,50,"Dark",)
tyranitar.add_offensive_move2("Stone Edge", 60,60,"Rock",)
tyranitar.add_offensive_move3("Earthquake", 70,70,"Ground",)
tyranitar.add_defensive_move1("Protect", 1,0,0,None,0,)
tyranitar.add_defensive_move2("Sandstorm", 0,0,1,None,0,)

# Create a Machamp instance
machamp = Pokemon("Machamp", ["Fighting"], 440, 55,55,)
machamp.add_offensive_move1("Cross Chop", 50,50,"Fighting",)
machamp.add_offensive_move2("Submission", 60,60,"Fighting",)
machamp.add_offensive_move3("Dynamic Punch", 70,70,"Fighting",)
machamp.add_defensive_move1("Bulk Up", 0.2,0,0.2,None,0,)
machamp.add_defensive_move2("Detect", 0,0,0,None,0.2,) 

# Create a Gardevoir instance
gardevoir = Pokemon("Gardevoir", ["Psychic", "Fairy"], 400, 60,80,)
gardevoir.add_offensive_move1("Psychic", 50,50,"Psychic",)
gardevoir.add_offensive_move2("Moonblast", 60,60,"Fairy",)
gardevoir.add_offensive_move3("Dazzling Gleam", 40,40,"Fairy",)
gardevoir.add_defensive_move1("Calm Mind", 0.2,0,0.2,None,0,)
gardevoir.add_defensive_move2("Will-O-Wisp", 0,0,0.3,None,0,)


# Create a Mimikyu instance
mimikyu = Pokemon("Mimikyu", ["Ghost", "Fairy"], 400, 60,96,)
mimikyu.add_offensive_move1("Shadow Claw", 50,50,"Ghost",)
mimikyu.add_offensive_move2("Play Rough", 60,60,"Fairy",)
mimikyu.add_offensive_move3("Phantom Force", 70,70,"Ghost",)
mimikyu.add_defensive_move1("Protect", 1, 0, 0,0,0,)
mimikyu.add_defensive_move2("Substitute", 1,-25,0,1,0,)

# Create a Silvally instance
silvally = Pokemon("Silvally", ["Normal"], 480, 55,95,)
silvally.add_offensive_move1("Multi-Attack", 70,70,"Normal",)
silvally.add_offensive_move2("Crunch", 50,50,"Dark")
silvally.add_offensive_move3("X-Scissor", 60,60,"Bug",)
silvally.add_defensive_move1("Iron Defense", 0.4,0,0,None,0,)
silvally.add_defensive_move2("Roar", 0.25,0,0,None,0,) 

# Create a Cryogonal instance
cryogonal = Pokemon("Cryogonal", ["Ice"], 400, 60,105)
cryogonal.add_offensive_move1("Ice Beam", 50,50,"Ice",)
cryogonal.add_offensive_move2("Blizzard", 70,70,"Ice",)
cryogonal.add_offensive_move3("Freeze-Dry", 70,70,"Ice",)
cryogonal.add_defensive_move1("Reflect", 0.5,0,0,None,0,)
cryogonal.add_defensive_move2("Light Screen", 0.5,0,0,None,0,)

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
    print(f"Defensive moves: {pokemon.defensive_moves1[0][0]},{pokemon.defensive_moves2[0][0]}\n")
    time.sleep(1)
    
elemental_chart = {}

types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]

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

#pokemon picking
pokemons = [pikachu,charizard,blastoise,venusaur,lycanroc,beedrill,crobat,gengar,noivern,metagross,garchomp,krookodile,tyranitar,machamp,gardevoir,mimikyu,silvally,cryogonal]
chosen_one=input("Which pokemon would you want to have?")
if chosen_one=="Pikachu" or chosen_one=="pikachu":
    chosen_one=pikachu
    del pokemons[0]
elif chosen_one=="Charizard" or chosen_one=="charizard":
    chosen_one=charizard
    del pokemons[1]
elif chosen_one == "Blastoise" or chosen_one == "blastoise":
    chosen_one = blastoise
    del pokemons[2]
elif chosen_one == "Venusaur" or chosen_one == "venusaur":
    chosen_one = venusaur
    del pokemons[3]
elif chosen_one == "Lycanroc" or chosen_one == "lycanroc":
    chosen_one = lycanroc
    del pokemons[4]
elif chosen_one == "Beedrill" or chosen_one == "beedrill":
    chosen_one = beedrill
    del pokemons[5]
elif chosen_one == "Crobat" or chosen_one == "crobat":
    chosen_one = crobat
    del pokemons[6]
elif chosen_one == "Gengar" or chosen_one == "gengar":
    chosen_one = gengar
    del pokemons[7]
elif chosen_one == "Metagross" or chosen_one == "metagross":
    chosen_one = metagross
    del pokemons[9]
elif chosen_one == "Garchomp" or chosen_one == "garchomp":
    chosen_one = garchomp
    del pokemons[10]
elif chosen_one == "Krookodile" or chosen_one == "krookodile":
    chosen_one = krookodile
    del pokemons[11]
elif chosen_one == "Cryogonal" or chosen_one == "cryogonal":
    chosen_one = cryogonal
    del pokemons[17]
elif chosen_one == "Tyranitar" or chosen_one == "tyranitar":
    chosen_one = tyranitar
    del pokemons[12]
elif chosen_one == "Machamp" or chosen_one == "machamp":
    chosen_one = machamp
    del pokemons[13]
elif chosen_one == "noivern" or chosen_one == "Noivern":
    chosen_one = noivern
    del pokemons[8]
elif chosen_one == "Gardevoir" or chosen_one == "gardevoir":
    chosen_one = gardevoir
    del pokemons[14]
elif chosen_one == "Mimikyu" or chosen_one == "mimikyu":
    chosen_one = mimikyu
    del pokemons[15]
elif chosen_one == "Silvally" or chosen_one == "silvally":
    chosen_one = silvally
    del pokemons[16]
else:
    random_chosen_one=random2.randint(0,17)
    chosen_one=pokemons[random_chosen_one]
    del pokemons[random_chosen_one]
#pokemon check
print()
print(f"You picked {chosen_one.name}")

#weakness and strength of chosen one
chosen_one_weakness=[]
chosen_one_strength=[]
for i in range(len(chosen_one.element)):
    chosen_one_type_chart = elemental_chart[chosen_one.element[i]]
    chosen_one_weakness += [chosen_one_type_chart["weaknesses"]]
    chosen_one_strength += [chosen_one_type_chart["strengths"]]
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
for i in range(len(random_pokemon.element)):
    random_pokemon_type_chart = elemental_chart[random_pokemon.element[i]]
    random_pokemon_weakness += [random_pokemon_type_chart["weaknesses"]]
    random_pokemon_strength += [random_pokemon_type_chart["strengths"]]

#type effectiveness
chosen_one_damage1=1
chosen_one_damage2=1
chosen_one_damage3=1
random_pokemon_damage1=1
random_pokemon_damage2=1
random_pokemon_damage3=1

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
while chosen_one.hp>0 and random_pokemon.hp>0:

    random_pokemon_damage_check=random_pokemon.offensive_moves1[0][1]
    chosen_one_damage_check=chosen_one.offensive_moves1[0][1]


    if chosen_one.speed>random_pokemon.speed or start==1:
        round3=round1-round2
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

        if chosen_one.energy<=0:
            chosen_one.energy=0
            print(f"""{chosen_one.name}   hp:{chosen_one.hp}   energy:{chosen_one.energy}
{random_pokemon.name}   hp:{random_pokemon.hp}   energy:{random_pokemon.energy}""")
            print(f"""{chosen_one.name} has no more energy
{chosen_one.name} used struggle""")
            print()
            chosen_one.hp=3/4*chosen_one.hp
            random_pokemon.hp=random_pokemon.hp-((chosen_one.offensive_moves1[0][1]+chosen_one.offensive_moves2[0][1]+chosen_one.offensive_moves3[0][1])/3)
        #Player's turn
        elif chosen_one.energy>0:
            print(f"""{chosen_one.name}   hp:{chosen_one.hp}   energy:{chosen_one.energy}
{random_pokemon.name}   hp:{random_pokemon.hp}   energy:{random_pokemon.energy}
{chosen_one.name}'s moves:
Offensive moves: {chosen_one.offensive_moves1[0][0]}(uses 1 energy),{chosen_one.offensive_moves2[0][0]}(uses 1 energy),{chosen_one.offensive_moves3[0][0]}(uses 1 energy)
Defensive moves: {chosen_one.defensive_moves1[0][0]}(uses 3 energy),{chosen_one.defensive_moves2[0][0]}(uses 3 energy)""")
            print()

            choice=int(input("What is your move? Note:Do your moves in order from 1 to 5. 1 being the first offensive move and 5 being the last defensive move." ))
            if choice==1:
                random_pokemon.hp= random_pokemon.hp - ((chosen_one.offensive_moves1[0][1])*chosen_one_damage1)
                chosen_one.energy=chosen_one.energy-1
                print(f"{chosen_one.name} used {chosen_one.offensive_moves1[0][0]}")
                if chosen_one_damage1>1:
                    print("It's super effective")
                elif chosen_one_damage1<1:
                    print("It's not effective")
                print()
            elif choice==2:
                random_pokemon.hp= random_pokemon.hp - ((chosen_one.offensive_moves2[0][1])*chosen_one_damage2)
                chosen_one.energy=chosen_one.energy-1
                print(f"{chosen_one.name} used {chosen_one.offensive_moves2[0][0]}")
                if chosen_one_damage2>1:
                    print("It's super effective")
                elif chosen_one_damage2<1:
                    print("It's not effective")
                print()
            elif choice==3:
                random_pokemon.hp= random_pokemon.hp - ((chosen_one.offensive_moves3[0][1])*chosen_one_damage3)
                chosen_one.energy=chosen_one.energy-1
                print(f"{chosen_one.name} used {chosen_one.offensive_moves3[0][0]}")
                if chosen_one_damage3>1:
                    print("It's super effective")
                elif chosen_one_damage3<1:
                    print("It's not effective")
                print()
            elif choice==4:
                if chosen_one.defensive_moves1[0][4]==None:
                    random_pokemon.offensive_moves1[0][2]=(1-chosen_one.defensive_moves2[0][1])*random_pokemon.offensive_moves1[0][2]
                    random_pokemon.offensive_moves2[0][2]=(1-chosen_one.defensive_moves2[0][1])*random_pokemon.offensive_moves2[0][2]
                    random_pokemon.offensive_moves3[0][2]=(1-chosen_one.defensive_moves2[0][1])*random_pokemon.offensive_moves3[0][2]
                    
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
                chosen_one_speed=chosen_one.speed
                chosen_one.speed=(1+chosen_one.defensive_moves1[0][5])*chosen_one.speed
                chosen_one_hp=chosen_one.hp
                chosen_one.hp= (chosen_one.defensive_moves1[0][2] / 100 * chosen_one.max_hp) + chosen_one.hp
                if chosen_one.speed>chosen_one_speed:
                    print(f"{chosen_one.name}'s speed increased")
                if chosen_one.hp>chosen_one.max_hp:
                    chosen_one.hp=chosen_one.max_hp
                if chosen_one_check<chosen_one.offensive_moves1[0][1]:
                    print(f"{chosen_one.name}'s attack increased")
                chosen_one.energy=chosen_one.energy-3
                print(f"{chosen_one.name} used {chosen_one.defensive_moves1[0][0]}")
                if random_pokemon_damage_check>random_pokemon.offensive_moves1[0][1]:
                    print(f"{chosen_one.name}'s defence increased")
                if chosen_one.hp>chosen_one_hp:
                    print(f"{chosen_one.name}'s hp increased")
                print()
                round1=round2
            else:
                chosen_one_speed=chosen_one.speed
                if chosen_one.defensive_moves1[0][4]==None:
                    random_pokemon.offensive_moves1[0][2]=(1-chosen_one.defensive_moves2[0][1])*random_pokemon.offensive_moves1[0][2]
                    random_pokemon.offensive_moves2[0][2]=(1-chosen_one.defensive_moves2[0][1])*random_pokemon.offensive_moves2[0][2]
                    random_pokemon.offensive_moves3[0][2]=(1-chosen_one.defensive_moves2[0][1])*random_pokemon.offensive_moves3[0][2]
                
                random_pokemon.offensive_moves1[0][1]= (1 - chosen_one.defensive_moves2[0][1]) * random_pokemon.offensive_moves1[0][1]
                random_pokemon.offensive_moves2[0][1]= (1 - chosen_one.defensive_moves2[0][1]) * random_pokemon.offensive_moves2[0][1]
                random_pokemon.offensive_moves3[0][1]= (1 - chosen_one.defensive_moves2[0][1]) * random_pokemon.offensive_moves3[0][1]
                chosen_one_check=chosen_one.offensive_moves2[0][1]

                chosen_one.speed=(1+chosen_one.defensive_moves2[0][5])*chosen_one.speed

                chosen_one.offensive_moves1[0][1]=(1+chosen_one.defensive_moves2[0][3])*chosen_one.offensive_moves1[0][1]
                chosen_one.offensive_moves2[0][1]=(1+chosen_one.defensive_moves2[0][3])*chosen_one.offensive_moves2[0][1]
                chosen_one.offensive_moves3[0][1]=(1+chosen_one.defensive_moves2[0][3])*chosen_one.offensive_moves3[0][1]
                
                chosen_one.offensive_moves1[0][2]=(1+chosen_one.defensive_moves2[0][3])*chosen_one.offensive_moves1[0][2]
                chosen_one.offensive_moves2[0][2]=(1+chosen_one.defensive_moves2[0][3])*chosen_one.offensive_moves2[0][2]
                chosen_one.offensive_moves3[0][2]=(1+chosen_one.defensive_moves2[0][3])*chosen_one.offensive_moves3[0][2]
                chosen_one_hp=chosen_one.hp
                chosen_one.hp= (chosen_one.defensive_moves2[0][2] / 100 * chosen_one.max_hp) + chosen_one.hp
                if random_pokemon_damage_check>random_pokemon.offensive_moves1[0][1]:
                    print(f"{chosen_one.name}'s defence increased")
                if chosen_one.speed>chosen_one_speed:
                    print(f"{chosen_one.name}'s speed increased")
                if chosen_one_check<chosen_one.offensive_moves1[0][1]:
                    print(f"{chosen_one.name}'s attack increased")
                if chosen_one.hp>chosen_one.max_hp:
                    chosen_one.hp=chosen_one.max_hp

                print(f"{chosen_one.name} used {chosen_one.defensive_moves2[0][0]}")
                chosen_one.energy=chosen_one.energy-3
                if random_pokemon.offensive_moves1[0][1]<random_pokemon.offensive_moves1[0][2] and random_pokemon.offensive_moves2[0][1]<random_pokemon.offensive_moves2[0][2] and random_pokemon.offensive_moves3[0][1]<random_pokemon.offensive_moves3[0][2]:
                    print(f"{chosen_one.name}'s defence increased")
                if chosen_one.hp>chosen_one_hp:
                    print(f"{chosen_one.name}'s hp increased")
                print()
                round1=round2
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
        if random_pokemon.energy<=0:
            random_pokemon.energy=0
        print(f"""{chosen_one.name}   hp:{chosen_one.hp}   energy:{chosen_one.energy}
{random_pokemon.name}   hp:{random_pokemon.hp}   energy:{random_pokemon.energy}""")
        print()
        round6=round4-round5
        if round6==chosen_one.defensive_moves2[0][4] and chosen_one.defensive_moves2[0][4]!=None:
            #prevents the defensive moves from being too OP
            random_pokemon.offensive_moves1[0][1]=random_pokemon.offensive_moves1[0][2]
            random_pokemon.offensive_moves2[0][1]=random_pokemon.offensive_moves2[0][2]
            random_pokemon.offensive_moves3[0][1]=random_pokemon.offensive_moves3[0][2]

        if round6==chosen_one.defensive_moves1[0][4] and chosen_one.defensive_moves1[0][4]!=None:
            #prevents the defensive moves from being too OP
            random_pokemon.offensive_moves1[0][1]=random_pokemon.offensive_moves1[0][1]/(1-chosen_one.defensive_moves2[0][1])
            random_pokemon.offensive_moves2[0][1]=random_pokemon.offensive_moves2[0][1]/(1-chosen_one.defensive_moves2[0][1])
            random_pokemon.offensive_moves3[0][1]=random_pokemon.offensive_moves3[0][1]/(1-chosen_one.defensive_moves2[0][1])

        if random_pokemon.energy<=0:
            print(f"{random_pokemon.name} used struggle")
            random_pokemon.energy=0
            print()
            random_pokemon.hp=3/4*random_pokemon.hp
            chosen_one.hp=chosen_one.hp-((random_pokemon.offensive_moves1[0][1]+random_pokemon.offensive_moves2[0][1]+random_pokemon.offensive_moves3[0][1])/3)
        elif random_pokemon.energy>=0:
            random_pokemon_hp=random_pokemon.hp
            if chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage1)<=0:
                chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage1)
                random_pokemon.energy-=1
                print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                if random_pokemon_damage1>1:
                    print("It's super effective")
                elif random_pokemon_damage1<1:
                    print("It's not effective")
                    print()
            elif chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage2)<=0:
                chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage2)
                random_pokemon.energy-=1
                print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                if random_pokemon_damage1>1:
                    print("It's super effective")
                elif random_pokemon_damage1<1:
                    print("It's not effective")
                print()
            elif chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage3)<=0:
                chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage3)
                random_pokemon.energy-=1
                print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                if random_pokemon_damage1>1:
                    print("It's super effective")
                elif random_pokemon_damage1<1:
                    print("It's not effective")                          
                print()
            elif random_pokemon.hp<=random_pokemon.max_hp/4:
                if random_pokemon.defensive_moves1[0][2]>0 and (random_pokemon.defensive_moves1[0][2] / 100 * random_pokemon.max_hp)>((chosen_one.offensive_moves1[0][1]*chosen_one_damage1+chosen_one.offensive_moves2[0][1]*chosen_one_damage2+chosen_one.offensive_moves3[0][1]*chosen_one_damage3)/3):
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
                    print()
                    if random_pokemon.defensive_moves1[0][4]==None:
                        chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][2]
                        chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][2]
                        chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][2]
                    random_pokemon.energy-=3
                    round4=round5
                elif random_pokemon.defensive_moves2[0][2]>0 and (random_pokemon.defensive_moves2[0][2] / 100 * random_pokemon.max_hp)>((chosen_one.offensive_moves1[0][1]*chosen_one_damage1+chosen_one.offensive_moves2[0][1]*chosen_one_damage2+chosen_one.offensive_moves3[0][1]*chosen_one_damage3)/3):
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
                    print()
                    if random_pokemon.defensive_moves1[0][4]==None:
                        chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves1[0][2]
                        chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves2[0][2]
                        chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves3[0][2]
                    random_pokemon.energy-=3
                    round4=round5
                else:
                    AI_choice=random2.randint(1,3)
                    if AI_choice==1:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage1)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                        if random_pokemon_damage1>1:
                            print("It's super effective")
                        elif random_pokemon_damage1<1:
                            print("It's not effective")
                        print()
                    elif AI_choice==2:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage2)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                        if random_pokemon_damage2>1:
                            print("It's super effective")
                        elif random_pokemon_damage2<1:
                            print("It's not effective")
                        print()
                    else:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage3)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                        if random_pokemon_damage3>1:
                            print("It's super effective")
                        elif random_pokemon_damage3<1:
                            print("It's not effective")
                        print()
            elif random_pokemon.hp<=random_pokemon.max_hp/2:
                random_pokemon_hp=random_pokemon.hp
                if round6>=2:
                    if random_pokemon.defensive_moves1[0][1]>0:
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
                        if random_pokemon_speed<random_pokemon.speed:
                            print(f"{random_pokemon.name}'s speed increased")
                        if random_pokemon.defensive_moves1[0][2]>0:
                            random_pokemon.hp=(chosen_one.defensive_moves1[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                        print(f"{random_pokemon.name} used {random_pokemon.defensive_moves1[0][0]}")
                        if random_pokemon_check<random_pokemon.offensive_moves1[0][1]:
                            print(f"{random_pokemon.name}'s attack increased")
                        if random_pokemon_hp<random_pokemon.hp:
                            print(f"{random_pokemon.name} healed")
                        if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                            print(f"{random_pokemon.name}'s defence increased")
                        print()
                        if random_pokemon.defensive_moves1[0][4]==None:
                            chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][2]
                            chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][2]
                            chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][2]
                        random_pokemon.energy-=3
                        round4=round5
                    elif random_pokemon.defensive_moves2[0][1]>0:
                        random_pokemon_speed=random_pokemon.speed
                        random_pokemon.speed=(1+random_pokemon.defensive_moves2[0][5])*random_pokemon.speed
                        random_pokemon_check=random_pokemon.offensive_moves2[0][1]
                        chosen_one.offensive_moves1[0][1]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves1[0][1]
                        chosen_one.offensive_moves2[0][1]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves2[0][1]
                        chosen_one.offensive_moves3[0][1]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves3[0][1]

                        random_pokemon.offensive_moves1[0][1]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves1[0][1]
                        random_pokemon.offensive_moves2[0][1]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves2[0][1]
                        random_pokemon.offensive_moves3[0][1]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves3[0][1]
                        
                        random_pokemon.offensive_moves1[0][2]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves1[0][1]
                        random_pokemon.offensive_moves2[0][2]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves2[0][1]
                        random_pokemon.offensive_moves3[0][2]= (1 + random_pokemon.defensive_moves2[0][3]) * random_pokemon.offensive_moves3[0][1]
                        if random_pokemon_speed<random_pokemon.speed:
                            print(f"{random_pokemon.name}'s speed increased")
                        if random_pokemon.defensive_moves2[0][2]>0:
                            random_pokemon.hp=(chosen_one.defensive_moves1[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                        print(f"{random_pokemon.name} used {random_pokemon.defensive_moves2[0][0]}")
                        if random_pokemon_check<random_pokemon.offensive_moves2[0][1]:
                            print(f"{random_pokemon.name}'s attack increased")
                        if random_pokemon_hp<random_pokemon.hp:
                            print(f"{random_pokemon.name} healed")
                        if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                            print(f"{random_pokemon.name}'s defence increased")
                        print()
                        if random_pokemon.defensive_moves1[0][4]==None:
                            chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][2]
                            chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][2]
                            chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][2]
                        random_pokemon.energy-=3
                        round4=round5
                    else:
                        AI_choice=random2.randint(1,3)
                        if AI_choice==1:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage1)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                            if random_pokemon_damage1>1:
                                print("It's super effective")
                            elif random_pokemon_damage1<1:
                                print("It's not effective")
                            print()
                        elif AI_choice==2:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage2)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                            if random_pokemon_damage2>1:
                                print("It's super effective")
                            elif random_pokemon_damage2<1:
                                print("It's not effective")
                            print()
                        else:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage3)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                            if random_pokemon_damage3>1:
                                print("It's super effective")
                            elif random_pokemon_damage3<1:
                                print("It's not effective")
                            print()
                else:
                    AI_choice=random2.randint(1,3)
                    if AI_choice==1:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage1)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                        if random_pokemon_damage1>1:
                            print("It's super effective")
                        elif random_pokemon_damage1<1:
                            print("It's not effective")
                        print()
                    elif AI_choice==2:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage2)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                        if random_pokemon_damage1>1:
                            print("It's super effective")
                        elif random_pokemon_damage1<1:
                            print("It's not effective")
                        print()
                    else:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage3)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                        if random_pokemon_damage1>1:
                            print("It's super effective")
                        elif random_pokemon_damage1<1:
                            print("It's not effective")
                        print()
            elif random_pokemon.max_hp/8*7<random_pokemon.hp:
                random_pokemon_hp=random_pokemon.hp
                if random_pokemon.defensive_moves1[0][3]>0:
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
                    if random_pokemon_speed<random_pokemon.speed:
                        print(f"{random_pokemon.name}'s speed increased")
                    if random_pokemon.defensive_moves1[0][2]>0:
                        random_pokemon.hp=(chosen_one.defensive_moves1[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                    print(f"{random_pokemon.name} used {random_pokemon.defensive_moves1[0][0]}")
                    if random_pokemon_check<random_pokemon.offensive_moves1[0][1]:
                        print(f"{random_pokemon.name}'s attack increased")
                    if random_pokemon_hp<random_pokemon.hp:
                        print(f"{random_pokemon.name} healed")
                    if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                        print(f"{random_pokemon.name}'s defence increased")
                    print()
                    if random_pokemon.defensive_moves1[0][4]==None:
                        chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][2]
                        chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][2]
                        chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][2]
                    
                    random_pokemon.energy-=3
                    round4=round5
                elif random_pokemon.defensive_moves2[0][3]>0:
                    random_pokemon_speed=random_pokemon.speed
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
                    if random_pokemon_speed<random_pokemon.speed:
                        print(f"{random_pokemon.name}'s speed increased")
                    if random_pokemon.defensive_moves2[0][2]>0:
                        random_pokemon.hp=(chosen_one.defensive_moves1[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                    print(f"{random_pokemon.name} used {random_pokemon.defensive_moves2[0][0]}")
                    if random_pokemon_check<random_pokemon.offensive_moves2[0][1]:
                        print(f"{random_pokemon.name}'s attack increased")
                    if random_pokemon_hp<random_pokemon.hp:
                        print(f"{random_pokemon.name} healed")
                    if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                        print(f"{random_pokemon.name}'s defence increased")
                    print()
                    if random_pokemon.defensive_moves2[0][4]==None:
                        chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][2]
                        chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][2]
                        chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][2]
                    random_pokemon.energy-=3
                    round4=round5
                else:
                    AI_choice=random2.randint(1,3)
                    if AI_choice==1:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage1)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                        if random_pokemon_damage1>1:
                            print("It's super effective")
                        elif random_pokemon_damage1<1:
                            print("It's not effective")
                        print()
                    elif AI_choice==2:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage2)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                        if random_pokemon_damage2>1:
                            print("It's super effective")
                        elif random_pokemon_damage2<1:
                            print("It's not effective")
                        print()
                    else:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage3)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                        if random_pokemon_damage3>1:
                            print("It's super effective")
                        elif random_pokemon_damage3<1:
                            print("It's not effective")
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
                    if random_pokemon_speed<random_pokemon.speed:
                        print(f"{random_pokemon.name}'s speed increased")
                    if random_pokemon.defensive_moves1[0][2]>0:
                        random_pokemon.hp=(chosen_one.defensive_moves1[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                    print(f"{random_pokemon.name} used {random_pokemon.defensive_moves1[0][0]}")
                    if random_pokemon_check<random_pokemon.offensive_moves1[0][1]:
                        print(f"{random_pokemon.name}'s attack increased")
                    if random_pokemon_hp<random_pokemon.hp:
                        print(f"{random_pokemon.name} healed")
                    if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                        print(f"{random_pokemon.name}'s defence increased")
                    print()
                    if random_pokemon.defensive_moves1[0][4]==None:
                        chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][2]
                        chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][2]
                        chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][2]
                    
                    random_pokemon.energy-=3
                    round4=round5
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
                    if random_pokemon_speed<random_pokemon.speed:
                        print(f"{random_pokemon.name}'s speed increased")
                    if random_pokemon.defensive_moves1[0][2]>0:
                        random_pokemon.hp=(chosen_one.defensive_moves1[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                    print(f"{random_pokemon.name} used {random_pokemon.defensive_moves1[0][0]}")
                    if random_pokemon_check<random_pokemon.offensive_moves1[0][1]:
                        print(f"{random_pokemon.name}'s attack increased")
                    if random_pokemon_hp<random_pokemon.hp:
                        print(f"{random_pokemon.name} healed")
                    if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                        print(f"{random_pokemon.name}'s defence increased")
                    print()
                    if random_pokemon.defensive_moves1[0][4]==None:
                        chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves1[0][2]
                        chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves2[0][2]
                        chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves3[0][2]
                    
                    random_pokemon.energy-=3
                    round4=round5
                else:
                    AI_choice=random2.randint(1,3)
                    if AI_choice==1:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage1)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                        if random_pokemon_damage1>1:
                            print("It's super effective")
                        elif random_pokemon_damage1<1:
                            print("It's not effective")
                        print()
                    elif AI_choice==2:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage2)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                        if random_pokemon_damage2>1:
                            print("It's super effective")
                        elif random_pokemon_damage2<1:
                            print("It's not effective")
                        print()
                    else:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage3)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                        if random_pokemon_damage3>1:
                            print("It's super effective")
                        elif random_pokemon_damage3<1:
                            print("It's not effective")
                        print()
            else:
                AI_choice=random2.randint(1,3)
                if AI_choice==1:
                    chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage1)
                    random_pokemon.energy-=1
                    print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                    if random_pokemon_damage1>1:
                        print("It's super effective")
                    elif random_pokemon_damage1<1:
                        print("It's not effective")
                    print()
                elif AI_choice==2:
                    chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage2)
                    random_pokemon.energy-=1
                    print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                    if random_pokemon_damage2>1:
                        print("It's super effective")
                    elif random_pokemon_damage2<1:
                        print("It's not effective")
                    print()
                else:
                    chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage3)
                    random_pokemon.energy-=1
                    print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                    if random_pokemon_damage3>1:
                        print("It's super effective")
                    elif random_pokemon_damage3<1:
                        print("It's not effective")
                    print()
        if chosen_one.hp<=0:
            print("You lost")
            break
        elif random_pokemon.hp<=0:
            print("You won")
            break
        chosen_one.hp=int(chosen_one.hp)
        random_pokemon.hp=int(random_pokemon.hp)
        round1+=1
        round2+=1
        round4+=1
        round5+=1
        start=0
        time.sleep(1)
    
    


    elif chosen_one.speed<random_pokemon.speed or start==2:
        #AI's turn
        chosen_one.hp=int(chosen_one.hp)
        random_pokemon.hp=int(random_pokemon.hp)
        if random_pokemon.energy<=0:
            random_pokemon.energy=0
        print(f"""{chosen_one.name}   hp:{chosen_one.hp}   energy:{chosen_one.energy}
{random_pokemon.name}   hp:{random_pokemon.hp}   energy:{random_pokemon.energy}""")  
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

        if random_pokemon.energy<=0:
            print(f"{random_pokemon.name} used struggle")
            print()
            random_pokemon.hp=3/4*random_pokemon.hp
            chosen_one.hp=chosen_one.hp-((random_pokemon.offensive_moves1[0][1]+random_pokemon.offensive_moves2[0][1]+random_pokemon.offensive_moves3[0][1])/3)
        elif random_pokemon.energy>=0:
            random_pokemon_speed=random_pokemon.speed
            if chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage1)<=0:
                chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage1)
                random_pokemon.energy-=1
                print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                if random_pokemon_damage1>1:
                    print("It's super effective")
                elif random_pokemon_damage1<1:
                    print("It's not effective")
                    print()
            elif chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage2)<=0:
                chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage2)
                random_pokemon.energy-=1
                print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                if random_pokemon_damage1>1:
                    print("It's super effective")
                elif random_pokemon_damage1<1:
                    print("It's not effective")
                print()
            elif chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage3)<=0:
                chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage3)
                random_pokemon.energy-=1
                print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                if random_pokemon_damage1>1:
                    print("It's super effective")
                elif random_pokemon_damage1<1:
                    print("It's not effective")                          
                print()
            elif random_pokemon.hp<=random_pokemon.max_hp/4:
                if random_pokemon.defensive_moves1[0][2]>0 and (random_pokemon.defensive_moves1[0][2] / 100 * random_pokemon.max_hp)>((chosen_one.offensive_moves1[0][1]*chosen_one_damage1+chosen_one.offensive_moves2[0][1]*chosen_one_damage2+chosen_one.offensive_moves3[0][1]*chosen_one_damage3)/3):
                    random_pokemon_speed=random_pokemon.speed
                    random_pokemon.speed=(1+random_pokemon.defensive_moves1[0][5])*random_pokemon.speed
                    random_pokemon_check=random_pokemon.offensive_moves1[0][1]
                    random_pokemon_hp=random_pokemon.hp
                    random_pokemon.hp=(random_pokemon.defensive_moves1[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
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
                    if random_pokemon_check<random_pokemon.offensive_moves1[0][1]:
                        print(f"{random_pokemon.name}'s attack increased")
                    if random_pokemon_hp<random_pokemon.hp:
                        print(f"{random_pokemon.name} healed")
                    if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                        print(f"{random_pokemon.name}'s defence increased")
                    print()
                    if random_pokemon.defensive_moves1[0][4]==None:
                        chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][2]
                        chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][2]
                        chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][2]
                    random_pokemon.energy-=3
                    round4=round5
                elif random_pokemon.defensive_moves2[0][2]>0 and (random_pokemon.defensive_moves2[0][2] / 100 * random_pokemon.max_hp)>((chosen_one.offensive_moves1[0][1]*chosen_one_damage1+chosen_one.offensive_moves2[0][1]*chosen_one_damage2+chosen_one.offensive_moves3[0][1]*chosen_one_damage3)/3):
                    random_pokemon_speed=random_pokemon.speed
                    random_pokemon.speed=(1+random_pokemon.defensive_moves2[0][5])*random_pokemon.speed
                    random_pokemon_check=random_pokemon.offensive_moves1[0][1]
                    random_pokemon_hp=random_pokemon.hp
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
                    if random_pokemon_check<random_pokemon.offensive_moves1[0][1]:
                        print(f"{random_pokemon.name}'s attack increased")
                    if random_pokemon_hp<random_pokemon.hp:
                        print(f"{random_pokemon.name} healed")
                    if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                        print(f"{random_pokemon.name}'s defence increased")
                    print()
                    random_pokemon.energy-=3
                    round4=round5
                    if random_pokemon.defensive_moves2[0][4]==None:
                        chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][2]
                        chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][2]
                        chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][2]
                else:
                    AI_choice=random2.randint(1,3)
                    if AI_choice==1:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage1)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                        if random_pokemon_damage1>1:
                            print("It's super effective")
                        elif random_pokemon_damage1<1:
                            print("It's not effective")
                        print()
                    elif AI_choice==2:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage2)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                        if random_pokemon_damage2>1:
                            print("It's super effective")
                        elif random_pokemon_damage2<1:
                            print("It's not effective")
                        print()
                    else:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage3)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                        if random_pokemon_damage3>1:
                            print("It's super effective")
                        elif random_pokemon_damage3<1:
                            print("It's not effective")
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
                        if random_pokemon_speed<random_pokemon.speed:
                           print(f"{random_pokemon.name}'s speed increased")
                        if random_pokemon.defensive_moves1[0][2]>0:
                            random_pokemon.hp=(random_pokemon.defensive_moves1[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                        print(f"{random_pokemon.name} used {random_pokemon.defensive_moves1[0][0]}")
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
                        random_pokemon.energy-=3
                        round4=round5
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
                        if random_pokemon_speed<random_pokemon.speed:
                            print(f"{random_pokemon.name}'s speed increased")
                        if random_pokemon.defensive_moves1[0][2]>0:
                            random_pokemon.hp=(random_pokemon.defensive_moves2[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                        print(f"{random_pokemon.name} used {random_pokemon.defensive_moves2[0][0]}")
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
                        random_pokemon.energy-=3
                        round4=round5
                    else:
                        AI_choice=random2.randint(1,3)
                        if AI_choice==1:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage1)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                            if random_pokemon_damage1>1:
                                print("It's super effective")
                            elif random_pokemon_damage1<1:
                                print("It's not effective")
                        elif AI_choice==2:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage2)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                            if random_pokemon_damage2>1:
                                print("It's super effective")
                            elif random_pokemon_damage2<1:
                                print("It's not effective")
                        else:
                            chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage3)
                            random_pokemon.energy-=1
                            print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                            if random_pokemon_damage3>1:
                                print("It's super effective")
                            elif random_pokemon_damage3<1:
                                print("It's not effective")
                else:
                    AI_choice=random2.randint(1,3)
                    if AI_choice==1:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage1)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                        if random_pokemon_damage1>1:
                            print("It's super effective")
                        elif random_pokemon_damage1<1:
                            print("It's not effective")
                    elif AI_choice==2:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage2)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                        if random_pokemon_damage2>1:
                            print("It's super effective")
                        elif random_pokemon_damage2<1:
                            print("It's not effective")
                    else:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage3)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                        if random_pokemon_damage3>1:
                            print("It's super effective")
                        elif random_pokemon_damage3<1:
                            print("It's not effective")
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
                    if random_pokemon_speed<random_pokemon.speed:
                        print(f"{random_pokemon.name}'s speed increased")
                    if random_pokemon.defensive_moves1[0][4]==None:
                        chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][2]
                        chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][2]
                        chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][2]
                    if random_pokemon.defensive_moves1[0][2]>0:
                        random_pokemon.hp=(chosen_one.defensive_moves1[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                    print(f"{random_pokemon.name} used {random_pokemon.defensive_moves1[0][0]}")
                    if random_pokemon_check<random_pokemon.offensive_moves1[0][1]:
                        print(f"{random_pokemon.name}'s attack increased")
                    if random_pokemon_hp<random_pokemon.hp:
                        print(f"{random_pokemon.name} healed")
                    if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                        print(f"{random_pokemon.name}'s defence increased")
                    print()
                    random_pokemon.energy-=3
                    round4=round5
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
                    if random_pokemon_speed<random_pokemon.speed:
                        print(f"{random_pokemon.name}'s speed increased")
                    if random_pokemon.defensive_moves2[0][4]==None:
                        chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][2]
                        chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][2]
                        chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][2]                    
                    if random_pokemon.defensive_moves2[0][2]>0:
                        random_pokemon.hp=(chosen_one.defensive_moves2[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                    print(f"{random_pokemon.name} used {random_pokemon.defensive_moves2[0][0]}")
                    if random_pokemon_check<random_pokemon.offensive_moves2[0][1]:
                        print(f"{random_pokemon.name}'s attack increased")
                    if random_pokemon_hp<random_pokemon.hp:
                        print(f"{random_pokemon.name} healed")
                    if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                        print(f"{random_pokemon.name}'s defence increased")
                    print()
                    random_pokemon.energy-=3
                    round4=round5
                else:
                    AI_choice=random2.randint(1,3)
                    if AI_choice==1:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage1)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                        if random_pokemon_damage1>1:
                            print("It's super effective")
                        elif random_pokemon_damage1<1:
                            print("It's not effective")
                        print()
                    elif AI_choice==2:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage2)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                        if random_pokemon_damage2>1:
                            print("It's super effective")
                        elif random_pokemon_damage2<1:
                            print("It's not effective")
                        print()
                    else:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage3)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                        if random_pokemon_damage3>1:
                            print("It's super effective")
                        elif random_pokemon_damage3<1:
                            print("It's not effective")
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
                    if random_pokemon_speed<random_pokemon.speed:
                        print(f"{random_pokemon.name}'s speed increased")
                    if random_pokemon.defensive_moves1[0][2]>0:
                        random_pokemon.hp=(chosen_one.defensive_moves1[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                    print(f"{random_pokemon.name} used {random_pokemon.defensive_moves1[0][0]}")
                    if random_pokemon_check<random_pokemon.offensive_moves1[0][1]:
                        print(f"{random_pokemon.name}'s attack increased")
                    if random_pokemon_hp<random_pokemon.hp:
                        print(f"{random_pokemon.name} healed")
                    if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                        print(f"{random_pokemon.name}'s defence increased")
                    print()
                    if random_pokemon.defensive_moves1[0][4]==None:
                        chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves1[0][2]
                        chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves2[0][2]
                        chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves1[0][1])*chosen_one.offensive_moves3[0][2]
                    
                    random_pokemon.energy-=3
                    round4=round5
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
                    if random_pokemon_speed<random_pokemon.speed:
                        print(f"{random_pokemon.name}'s speed increased")
                    if random_pokemon.defensive_moves1[0][2]>0:
                        random_pokemon.hp=(chosen_one.defensive_moves1[0][2] / 100 * random_pokemon.max_hp) + random_pokemon.hp
                    print(f"{random_pokemon.name} used {random_pokemon.defensive_moves1[0][0]}")
                    if random_pokemon_check<random_pokemon.offensive_moves1[0][1]:
                        print(f"{random_pokemon.name}'s attack increased")
                    if random_pokemon_hp<random_pokemon.hp:
                        print(f"{random_pokemon.name} healed")
                    if chosen_one_damage_check>chosen_one.offensive_moves1[0][1]:
                        print(f"{random_pokemon.name}'s defence increased")
                    print()
                    if random_pokemon.defensive_moves1[0][4]==None:
                        chosen_one.offensive_moves1[0][2]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves1[0][2]
                        chosen_one.offensive_moves2[0][2]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves2[0][2]
                        chosen_one.offensive_moves3[0][2]=(1-random_pokemon.defensive_moves2[0][1])*chosen_one.offensive_moves3[0][2]
                    
                    random_pokemon.energy-=3
                    round4=round5
                else:
                    AI_choice=random2.randint(1,3)
                    if AI_choice==1:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage1)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                        if random_pokemon_damage1>1:
                            print("It's super effective")
                        elif random_pokemon_damage1<1:
                            print("It's not effective")
                        print()
                    elif AI_choice==2:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage2)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                        if random_pokemon_damage2>1:
                            print("It's super effective")
                        elif random_pokemon_damage2<1:
                            print("It's not effective")
                        print()
                    else:
                        chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage3)
                        random_pokemon.energy-=1
                        print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                        if random_pokemon_damage3>1:
                            print("It's super effective")
                        elif random_pokemon_damage3<1:
                            print("It's not effective")
                        print()
            else:
                AI_choice=random2.randint(1,3)
                if AI_choice==1:
                    chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves1[0][1]*random_pokemon_damage1)
                    random_pokemon.energy-=1
                    print(f"{random_pokemon.name} used {random_pokemon.offensive_moves1[0][0]}")
                    if random_pokemon_damage1>1:
                        print("It's super effective")
                    elif random_pokemon_damage1<1:
                        print("It's not effective")
                elif AI_choice==2:
                    chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves2[0][1]*random_pokemon_damage2)
                    random_pokemon.energy-=1
                    print(f"{random_pokemon.name} used {random_pokemon.offensive_moves2[0][0]}")
                    if random_pokemon_damage2>1:
                        print("It's super effective")
                    elif random_pokemon_damage2<1:
                        print("It's not effective")
                else:
                    chosen_one.hp=chosen_one.hp-(random_pokemon.offensive_moves3[0][1]*random_pokemon_damage3)
                    random_pokemon.energy-=1
                    print(f"{random_pokemon.name} used {random_pokemon.offensive_moves3[0][0]}")
                    if random_pokemon_damage3>1:
                        print("It's super effective")
                    elif random_pokemon_damage3<1:
                        print("It's not effective")
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
        chosen_one.hp=int(chosen_one.hp)
        random_pokemon.hp=int(random_pokemon.hp)
        round3=round1-round2
        if round3==chosen_one.defensive_moves2[0][4] and chosen_one.defensive_moves2[0][4]!=None :
            #prevents the defensive moves from being too OP
            random_pokemon.offensive_moves1[0][1]=random_pokemon.offensive_moves1[0][2]
            random_pokemon.offensive_moves2[0][1]=random_pokemon.offensive_moves2[0][2]
            random_pokemon.offensive_moves3[0][1]=random_pokemon.offensive_moves3[0][2]

        if round3==chosen_one.defensive_moves1[0][4]and chosen_one.defensive_moves2[0][4]!=None:
            #prevents the defensive moves from being too OP
            random_pokemon.offensive_moves1[0][1]=random_pokemon.offensive_moves1[0][2]
            random_pokemon.offensive_moves2[0][1]=random_pokemon.offensive_moves2[0][2]
            random_pokemon.offensive_moves3[0][1]=random_pokemon.offensive_moves3[0][2]
        if chosen_one.energy<=0:
            chosen_one.energy=0
            print(f"""{chosen_one.name}   hp:{chosen_one.hp}   energy:{chosen_one.energy}
{random_pokemon.name}   hp:{random_pokemon.hp}   energy:{random_pokemon.energy}""")
            print(f"""{chosen_one.name} has no more energy
{chosen_one.name} used struggle""")
            print()
            chosen_one.hp=3/4*chosen_one.hp
            random_pokemon.hp=random_pokemon.hp-((chosen_one.offensive_moves1[0][1]+chosen_one.offensive_moves2[0][1]+chosen_one.offensive_moves3[0][1])/3)
        elif chosen_one.energy>0:
            print(f"""{chosen_one.name}   hp:{chosen_one.hp}   energy:{chosen_one.energy}
{random_pokemon.name}   hp:{random_pokemon.hp}   energy:{random_pokemon.energy}
{chosen_one.name}'s moves:
Offensive moves: {chosen_one.offensive_moves1[0][0]}(uses 1 energy),{chosen_one.offensive_moves2[0][0]}(uses 1 energy),{chosen_one.offensive_moves3[0][0]}(uses 1 energy)
Defensive moves: {chosen_one.defensive_moves1[0][0]}(uses 3 energy),{chosen_one.defensive_moves2[0][0]}(uses 3 energy)""")
            print()

            choice=int(input("What is your move? Note:Do your moves in order from 1 to 5. 1 being the first offensive move and 5 being the last defensive move." ))
            if choice==1:
                random_pokemon.hp= random_pokemon.hp - ((chosen_one.offensive_moves1[0][1])*chosen_one_damage1)
                chosen_one.energy=chosen_one.energy-1
                print(f"{chosen_one.name} used {chosen_one.offensive_moves1[0][0]}")
                if chosen_one_damage1>1:
                    print("It's super effective")
                elif chosen_one_damage1<1:
                    print("It's not effective")
            elif choice==2:
                random_pokemon.hp= random_pokemon.hp - ((chosen_one.offensive_moves2[0][1])*chosen_one_damage2)
                chosen_one.energy=chosen_one.energy-1
                print(f"{chosen_one.name} used {chosen_one.offensive_moves2[0][0]}")
                if chosen_one_damage2>1:
                    print("It's super effective")
                elif chosen_one_damage2<1:
                    print("It's not effective")
            elif choice==3:
                random_pokemon.hp= random_pokemon.hp - ((chosen_one.offensive_moves3[0][1])*chosen_one_damage3)
                chosen_one.energy=chosen_one.energy-1
                print(f"{chosen_one.name} used {chosen_one.offensive_moves3[0][0]}")
                if chosen_one_damage3>1:
                    print("It's super effective")
                elif chosen_one_damage3<1:
                    print("It's not effective")
            elif choice==4:
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
                round1=round2
            else:
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
                round1=round2
            print()
        if chosen_one.hp<=0:
            print("You lost")
            break
        elif random_pokemon.hp<=0:
            print("You won")
            break
        round1+=1
        round2+=1
        round4+=1
        round5+=1
        start=0
        time.sleep(1)
    else:
        start=random2.randint(1,2)
        


#round end like boost of energy regen 
chosen_one.energy = chosen_one.energy +30
if chosen_one.energy>chosen_one.max_energy:
    chosen_one.energy=chosen_one.max_energy