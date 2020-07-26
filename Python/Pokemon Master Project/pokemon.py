class Trainer:
    def __init__(self, name, pokemons, potions, current_pokemon):
        self.name = name
        self.pokemons = pokemons
        self.potions = potions
        self.current_pokemon = current_pokemon
    
    
    def use_potion(self):
        if self.potions != 0:
            self.potions -= 1
            print("%s is using a potion on %s" % (self.name, self.pokemons[self.current_pokemon].name))
            self.pokemons[self.current_pokemon].gain_health(self.pokemons[self.current_pokemon].maxhp * .7)
        else:
            print("You are out of potions!\n")
            
            
    def attack_other_trainer(self, other_trainer):
        their_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
        my_pokemon = self.pokemons[self.current_pokemon]
        print("%s is using %s to attack %s's %s!" % (self.name, my_pokemon.name, other_trainer.name, their_pokemon.name))
        Pokemon.attack(my_pokemon, their_pokemon)
    
    
    def switch_pokemon(self, num_of_pokemon):
        if self.current_pokemon == num_of_pokemon:
            print("%s is already active!" % (self.pokemons[self.current_pokemon].name))
        elif self.pokemons[num_of_pokemon].knocked_out == True:
            print("Unable to swap to a knocked out pokemon!")
        else:
            self.current_pokemon = num_of_pokemon
            print("Swapped to %s!" % (self.pokemons[self.current_pokemon].name))
        
        
class Pokemon:
    def __init__(self, name, level, poke_type, maxhp, hp, knocked_out):
        self.name = name
        self.level = level
        self.poke_type = poke_type
        self.maxhp = maxhp
        self.hp = hp
        self.knocked_out = knocked_out
    
    
    def lose_health(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            self.knock_out()
        print("%s lost %d health and now has %d health\n" % (self.name, amount, self.hp))
        
    
    def gain_health(self, amount):
        self.hp += amount
        if self.hp >= self.maxhp:
            self.hp = self.maxhp
        print("%s regained %d health and now has %d health\n" % (self.name, amount, self.hp))
        
        
    def knock_out(self):
        self.knocked_out = True
        print("%s has been knocked out!" % (self.name))
        

    def revive(self):
        self.knocked_out = False
        self.hp = (self.maxhp * .1)
        print("%s has been revived and now has %d health!\n" % (self.name, self.hp))
        
    
    def attack(self, other_pokemon):
        if self.knock_out == False:
            print("%s is knocked out and unable to attack!\n" % (self.name))
        else:
            damage = 0
            if self.poke_type == "Fire" and other_pokemon.poke_type == "Grass":
                damage = self.level * 2
            elif self.poke_type == "Fire" and other_pokemon.poke_type == "Water":
                damage = self.level / 2
            elif self.poke_type == "Grass" and other_pokemon.poke_type == "Water":
                damage = self.level * 2
            elif self.poke_type == "Grass" and other_pokemon.poke_type == "Fire":
                damage = self.level / 2
            elif self.poke_type == "Water" and other_pokemon.poke_type == "Fire":
                damage = self.level * 2
            elif self.poke_type == "Water" and other_pokemon.poke_type == "Grass":
                damage = self.level / 2
            else:
                damage = self.level
            if damage == self.level * 2:
                print("%s is SUPER EFFECTIVE against %s\n" % (self.name, other_pokemon.name))
            elif damage == self.level / 2:
                print("%s is WEAK against %s\n" % (self.name, other_pokemon.name))
            else: print("%s attacks %s" % (self.name, other_pokemon.name))
            other_pokemon.lose_health(damage)        
            
# CREATE 12 RANDOM POKEMON 
chara = Pokemon("Chara", 10, "Fire", 100, 40, False)
noraa = Pokemon("Noraa", 15, "Grass", 125, 125, False)
lunu = Pokemon("Lunu", 6, "Fire", 60, 60, False)
shaki = Pokemon("Shaki", 15, "Water", 200, 200, False)
viiso = Pokemon("Viiso", 10, "Fire", 100, 40, False)
kumine = Pokemon("Kumine", 15, "Grass", 125, 125, False)
noob = Pokemon("Noob", 60, "Fire", 100, 40, False)
megaman = Pokemon("Megaman", 15, "Grass", 125, 60, False)
paks = Pokemon("Paks", 10, "Fire", 100, 40, False)
sipsu = Pokemon("Sipsu", 15, "Grass", 125, 125, False)
lassi = Pokemon("Lassi", 6, "Fire", 60, 60, False)
sharana = Pokemon("Sharana", 18, "Water", 200, 200, False)

# CREATE 2 TRAINERS CALLED ASH AND KASSU, ASSIGN THEM WITH THE 12 POKEMON
ash_list = [noob, megaman, paks, sipsu, lassi, sharana]
ash = Trainer("Ash", ash_list, 5, 0)
kassu_list = [chara, noraa, lunu, shaki, viiso, kumine]
kassu = Trainer("Kassu", kassu_list, 5, 0)

# TRAINER KASSU USING POTION TO HEAL ACTIVE POKEMON
kassu.use_potion()

# KASSU USING ACTIVE POKEMON TO ATTACK ASH'S ACTIVE POKEMON
kassu.attack_other_trainer(ash)

# ASH USING ACTIVE POKEMON TO ATTACK KASSU'S ACTIVE POKEMON
ash.attack_other_trainer(kassu)

# KASSU SWAPPING ACTIVE POKEMON
kassu.switch_pokemon(3)

# KASSU USING NEW ACTIVE POKEMON TO ATTACK ASH'S ACTIVE POKEMON
kassu.attack_other_trainer(ash)
