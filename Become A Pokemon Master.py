# don't change the name of this dictionary!
poketypes = {"Fire": {"Water": 0.5, "Grass": 2, "Electric": 1, "Fire": 0.5}, "Water": {"Water": 0.5, "Grass": 0.5, "Fire": 2, "Electric": 1},
             "Electric": {"Water": 2, "Grass": 0.5, "Fire": 2, "Electric": 0.5}, "Grass": {"Water": 2, "Fire": 0.5, "Electric": 1, "Grass": 0.5}}

# don't change the name of this list!
evolution_names = [["Charmander", "Charmeleon", "Charizard"], ["Bulbasaur", "Ivysaur", "Venesaur"], ["Pichu", "Pikachu", "Raichu"], ["Squirtle", "Wartortle", "Blastoise"]]


class Pokemon:
    def __init__(self, name, type, speed_int, speed_str, level=1, health=10, max_health=10, experience=0, is_knocked_out=False):
        self.name = name
        self.level = level
        self.health = health
        self.max_health = max_health
        self.type = type
        self.experience = experience
        self.is_knocked_out = is_knocked_out
        self.speed_int = speed_int
        self.speed_str = speed_str

    def __repr__(self):
        return self.name

    def lose_health(self, lost_health):
        if self.is_knocked_out == False:
            if self.health - lost_health > 0:
                self.health -= lost_health
                print(
                    "{name} just lost {lost_health} health points, {name}'s total health is now {health}".format(name=self.name, lost_health=lost_health, health=self.health))
            elif self.health - lost_health <= 0:
                self.health = 0
                self.is_knocked_out = True
                print("{name} has been knocked out".format(name=self.name))
        elif self.is_knocked_out == True:
            print("{name} is already knocked out".format(name=self.name))
        return self.health

    def gain_health(self, gained_health):
        if self.is_knocked_out == False:
            if self.health + gained_health < self.max_health:
                self.health += gained_health
                print("{name} has gained {gained_health} health points, {name}'s current health is now {health}".format(name=self.name, gained_health=gained_health,
                                                                                                                        health=self.health))
            else:
                self.health = self.max_health
                print("{name} is now back to max health".format(name=self.name))
        else:
            print("{name} is still knocked out and must be revived first.".format(name=self.name))
        return self.health

    def revive(self):
        if self.is_knocked_out == True:
            if self.is_knocked_out == False:
                self.health = self.level
                print("{name} has been revived to {health}".format(name=self.name, health=self.health))
        else:
            print("{pokemon} isn't knocked_out".format(pokemon=self.name))
        return self.health

    # This method looks through the poketypes dictionary (the keys in the poketypes dictionary is a nested dictionary) and finds the attacking pokemon's type, the attacked pokemons type from the nested dictionary, and the damage that will be dealt. no paramater for passing in the dictionary of pokemon types, the list is directly named in the method, the dictionary name should therefor NOT be changed.
    def attack(self, p2):
        if self.is_knocked_out == False:
            if p2.is_knocked_out == False:
                print("{p1} has attacked {p2}!".format(p1=self.name, p2=p2.name))
                for p1_poketype in poketypes.keys():
                    if p1_poketype == self.type:
                        for opponent_type, damage in poketypes[p1_poketype].items():
                            if opponent_type == p2.type:
                                if damage == 0.5:
                                    print("{name}'s attack is weak.".format(name=self.name))
                                elif damage == 1:
                                    print("{name}'s attack is normal.".format(name=self.name))
                                elif damage == 2:
                                    print("{name}'s attack is Devastating!".format(name=self.name))
                                p2.lose_health(self.level * damage)
                                # add experience, double if the attacking pokemon knocks out the other pokemon
                                if p2.is_knocked_out == True:
                                    self.experience += 2
                                else:
                                    self.experience += 1
                                # level up the pokemon if it gains enough experience
                                if self.experience >= (2 * self.level):
                                    self.level_up()
                                if self.level % 10 == 0:
                                    self.evolve()
            else:
                print("{p2} is already knocked out, {p1} cannot attack {p2}".format(p2=p2.name, p1=self.name))

        else:
            print("{p1} is knocked out, {p1} cannot attack {p2}".format(p1=self.name, p2=p2.name))

            # method incorporates the pokemons speed and decides who goes first. otherwise the same as the attack method

    def attack2(self, p2):
        if self.is_knocked_out == False:
            if p2.is_knocked_out == False:
                if self.speed_int > p2.speed_int or self.speed_int == p2.speed_int:
                    print("{p1} has attacked {p2}!".format(p1=self.name, p2=p2.name))
                    self.attack_helper(p2)
                    print("{p2} has retaliated!".format(p2=p2.name))
                    p2.attack_helper(self)
                else:
                    print("{p1} has attacked {p2}!".format(p1=self.name, p2=p2.name))
                    print("{p2} is faster!".format(p2=p2.name))
                    p2.attack_helper(self)
                    print("{p1} has retaliated!".format(p1=p2.name))
                    self.attack_helper(p2)
            else:
                print("{p2} is already knocked out, {p1} cannot attack {p2}".format(p2=p2.name, p1=self.name))
        else:
            print("{p1} is knocked out, {p1} cannot attack {p2}".format(p1=self.name, p2=p2.name))

            # helper method for attack2 method

    def attack_helper(self, p2):
        for p1_poketype in poketypes.keys():
            if p1_poketype == self.type:
                for opponent_type, damage in poketypes[p1_poketype].items():
                    if opponent_type == p2.type:
                        if damage == 0.5:
                            print("{name}'s attack is weak.".format(name=self.name))
                        elif damage == 1:
                            print("{name}'s attack is normal.".format(name=self.name))
                        elif damage == 2:
                            print("{name}'s attack is Devastating!".format(name=self.name))
                        p2.lose_health(self.level * damage)
                        # add experience, double if the attacking pokemon knocks out the other pokemon
                        if p2.is_knocked_out == True:
                            self.experience += 2
                        else:
                            self.experience += 1
                            # level up the pokemon if it gains enough experience
                        if self.experience >= (2 * self.level):
                            self.level_up()
                        if self.level % 10 == 0:
                            self.evolve()

    # Method to increase pokemon's level
    def level_up(self):
        self.level += 1
        self.max_health += 10
        print("{pokemon} has increased a level to level {level}".format(pokemon=self.name, level=self.level))

    # Method for the pokemon to evolve, uses the evolution_names dictionary to do so. No parameter for passing in the name of the list, as the list is named in the function. The name of the list should therefore NOT be changed.
    def evolve(self):
        for index in evolution_names:
            for name in index:
                if self.name == name:
                    if index[-1] != self.name:
                        previous_name = self.name
                        name_index = index.index(name)
                        self.name = index[name_index + 1]
                        print("{pokemon} has evolved into {name}!".format(pokemon=previous_name, name=self.name))
                        break
                    else:
                        print("{name} is fully evolved!".format(name=self.name))
        return self.name


class Trainer:
    def __init__(self, name, owned_pokemon, potions=0, active_pokemon=None):
        self.name = name
        self.owned_pokemon = owned_pokemon
        self.potions = potions
        self.active_pokemon = active_pokemon
        if len(owned_pokemon) > 6:
            print("You can't own more than six pokemon")

    def __repr__(self):
        return self.name

    # This method will take care of switching either players pokemon if they are knocked out, or printing that the player is unable to fight, use attack_player 2 if you want to do it manually
    def attack_player(self, player2):
        if self.active_pokemon.is_knocked_out == False and player2.active_pokemon.is_knocked_out == False:
            print("{p1} has attacked {p2}!".format(p1=self.name, p2=player2.name))
            self.active_pokemon.attack(player2.active_pokemon)
            # if player 2 gets knocked out in the fight, switch to a new pokemon or print p2 can't fight
            if player2.active_pokemon.is_knocked_out == True:
                player2.player2_knocked_out()
        elif self.active_pokemon.is_knocked_out == True and player2.active_pokemon.is_knocked_out == False:
            # use potion on player one pokemon to revive it, if player one has a potion
            self.use_potion()
            # if player one had a potion, attack the other player
            if self.active_pokemon.is_knocked_out == False:
                print("{p1} has attacked {p2}!".format(p1=self.name, p2=player2.name))
                self.active_pokemon.attack(player2.active_pokemon)
            # if player one has no more potions, switch to another pokemon or print that player one can't fight
            elif self.active_pokemon.is_knocked_out == True:
                print("Attempting to switch pokemon...")
                self.player_active_ko()
                # if player one had another pokemon that isn't knocked out, and is now active, attack the other player
                if self.active_pokemon.is_knocked_out == False:
                    print("{p1} switching to {pokemon}...".format(p1=self.name, pokemon=self.active_pokemon.name))
                    self.active_pokemon.attack(player2.active_pokemon)
            # if player 2 gets knocked out in the fight, switch to a new pokemon or print p2 can't fight
            if player2.active_pokemon.is_knocked_out == True:
                player2.player2_knocked_out()
        elif self.active_pokemon.is_knocked_out == False and player2.active_pokemon.is_knocked_out == True:
            # Check for another pokemon that is not knocked out from list of owned pokemon, set first one found to active pokemon. If all pokemon are knocked out, print player 2 can't fight.
            player2.player_active_ko()
            # if another pokemon was found for player 2, begin the fight.
            if player2.active_pokemon.is_knocked_out == False:
                print("{p1} has attacked {p2}!".format(p1=self.name, p2=player2.name))
                print("{p2} switching to {pokemon}...".format(p2=player2.name, pokemon=player2.active_pokemon.name))
                self.active_pokemon.attack(player2.active_pokemon)
                # if player 2 gets knocked out in the fight, switch to a new pokemon or print p2 can't fight.
                if player2.active_pokemon.is_knocked_out == True:
                    player2.player2_knocked_out()
        elif self.active_pokemon.is_knocked_out == True and player2.active_pokemon.is_knocked_out == True:
            # player one use a potion on active pokemon to revive it
            self.use_potion()
            if self.active_pokemon.is_knocked_out == False:
                player2.player_active_ko()
                if player2.active_pokemon.is_knocked_out == False:
                    print("{p2} switching to {pokemon}...".format(p2=player2.name, pokemon=player2.active_pokemon.name))
                    self.active_pokemon.attack(player2.active_pokemon)
                    # if player2 gets knocked out in the fight, switch pokemon or print player2 can't fight
                    if player2.active_pokemon.is_knocked_out == True:
                        player2.player2_knocked_out()
            # if no more potions available, player one attempt to switch pokemon
            elif self.active_pokemon.is_knocked_out == True:
                print("{name} attempting to switch pokemon...".format(name=self.name))
                self.player_active_ko()
                # if another pokemon is found for player one check if player 2 has another pokemon and can fight
                if self.active_pokemon.is_knocked_out == False:
                    print("{p1} switching to {pokemon}...".format(p1=self.name, pokemon=self.active_pokemon.name))
                    player2.player_active_ko()
                    # if player2 has another pokemon that can fight, begin fight
                    if player2.active_pokemon.is_knocked_out == False:
                        print("{p1} has attacked {p2}!".format(p1=self.name, p2=player2.name))
                        print("{p2} switching to {pokemon}...".format(p2=player2.name, pokemon=player2.active_pokemon.name))
                        self.active_pokemon.attack(player2.active_pokemon)
                        # if player 2 pokemon gets knocked out in the fight, switch pokemon or print all pokemon knocked out.
                        if player2.active_pokemon.is_knocked_out == True:
                            player2.player2_knocked_out()

    # This method is a helper method for the attack_player() method. It will switch player 2's active pokemon if player 2's pokemon gets knocked out in the fight preparing player 2 for the next round
    def player2_knocked_out(player2):
        p2_knocked_out = 0
        for pokemon in player2.owned_pokemon:
            if pokemon.is_knocked_out == False:
                player2.active_pokemon = pokemon
                print("{p2} switching to {pokemon}!".format(p2=player2.name, pokemon=player2.active_pokemon.name))
                break
            elif pokemon.is_knocked_out == True:
                p2_knocked_out += 1
        if p2_knocked_out == len(player2.owned_pokemon):
            print("All of {p2}'s Pokmeon have been knocked out.".format(p2=player2.name))
        return player2.active_pokemon.is_knocked_out

    # This method is very similar to the player2_knocked_out function, but prints a different message, it is used to switch pokemon when entering a fight if the active pokemon is currently knocked out.
    def player_active_ko(player):
        p_knocked_out = 0
        for pokemon in player.owned_pokemon:
            if pokemon.is_knocked_out == False:
                player.active_pokemon = pokemon
                break
            elif pokemon.is_knocked_out == True:
                p_knocked_out += 1
        if p_knocked_out == len(player.owned_pokemon):
            print("All of {p}'s Pokmeon are already knocked out, {p} cannot fight.".format(p=player.name))
        return player.active_pokemon.is_knocked_out

    # This method requires manually switching to another pokemon if the currently active pokemon is knocked out
    def attack_player2(self, player2):
        if self.active_pokemon.is_knocked_out == False:
            if player2.active_pokemon.is_knocked_out == False:
                print("{p1} has attacked {p2}!".format(p1=self.name, p2=player2.name))
                self.active_pokemon.attack(player2.active_pokemon)
            else:
                print("{p2}'s pokemon is already knocked out, you can't attack {p2}!".format(p2=player2.name))
        else:
            print("Your pokemon is knocked out, you can't attack!")

    # alternate method of attack_player2 to see which one is easier to read
    def attack_player3(self, player2):
        if self.active_pokemon.is_knocked_out == False and player2.active_pokemon.is_knocked_out == False:
            print("{p1} has attacked {p2}!".format(p1=self.name, p2=player2.name))
            self.active_pokemon.attack(player2.active_pokemon)
        elif self.active_pokemon.is_knocked_out == True and player2.active_pokemon.is_knocked_out == False:
            print("Your pokemon is knocked out, you cannot attack!")
        elif self.active_pokemon.is_knocked_out == False and player2.active_pokemon.is_knocked_out == True:
            print("{p2}'s pokemon is already knocked out, you cannot attack!".format(p2=player2.name))
        elif self.active_pokemon.is_knocked_out == True and player2.active_pokemon.is_knocked_out == True:
            print("Both player's pokemon are knocked out and cannot fight.")

    def use_potion(self):
        if self.potions > 0:
            if self.active_pokemon.is_knocked_out == False:
                print("Using Potion on {name}...".format(name=self.active_pokemon.name))
                self.active_pokemon.health = self.active_pokemon.gain_health(self.active_pokemon.level)
            elif self.active_pokemon.is_knocked_out == True:
                print("Potion reviving {name}...".format(name=self.active_pokemon.name))
                self.active_pokemon.is_knocked_out = False
                self.active_pokemon.health = self.active_pokemon.gain_health(self.active_pokemon.level)
        else:
            print("{name} has no more potions!".format(name=self.name))

    def switch_pokemon(self, pokemon):
        if pokemon in self.owned_pokemon:
            if pokemon.is_knocked_out == False:
                self.active_pokemon = pokemon
                print("Switching to {pokemon}.".format(pokemon=pokemon.name))
            else:
                print("{pokemon} is knocked out, you can't switch to that pokemon".format(pokemon=pokemon.name))
        else:
            print("You don't own that Pokemon.")
        return self.active_pokemon


class Charmander(Pokemon):
    def __init__(self, name="Charmander", type="Fire", speed_int=3, speed_str="Fast"):
        super().__init__(name, type, speed_int, speed_str)


class Bulbasaur(Pokemon):
    def __init__(self, name="Bulbasaur", type="Grass", speed_int=3, speed_str="Fast"):
        super().__init__(name, type, speed_int, speed_str)


class Pichu(Pokemon):
    def __init__(self, name="Pichu", type="Electric", speed_int=1, speed_str="Slow"):
        super().__init__(name, type, speed_int, speed_str)


class Squirtle(Pokemon):
    def __init__(self, name="Squirtle", type="Water", speed_int=2, speed_str="Medium"):
        super().__init__(name, type, speed_int, speed_str)


Ash_Charmander = Charmander()
Ash_Squirtle = Pokemon("Squirtle", "Water", 3, "Fast")
Ash_Pichu = Pokemon("Pichu", "Electric", 1, "Slow")
Ash_Bulbasaur = Pokemon("Bulbasaur", "Grass", 2, "Medium")

Misty_Charmander = Pokemon("Charmander", "Fire", 3, "Fast")
Misty_Squirtle = Squirtle()
Misty_Pichu = Pokemon("Pichu", "Electric", 1, "Slow")
Misty_Bulbasaur = Pokemon("Bulbasaur", "Grass", 2, "Medium")

Ash = Trainer("Ash", [Ash_Pichu, Ash_Squirtle, Ash_Charmander, Ash_Bulbasaur], 50, Ash_Charmander)
Misty = Trainer("Misty", [Misty_Squirtle, Misty_Bulbasaur, Misty_Charmander, Misty_Pichu], 50, Misty_Squirtle)
char = Charmander()
pichu = Pichu()
squir = Squirtle()
print(char.experience)
char.attack2(pichu)
char.attack2(pichu)
char.attack2(pichu)
print(char.experience)
print(char.level)
# pichu.attack2(char)
# char.attack2(squir)

# Ash_Pichu.attack2(Ash_Charmander)

