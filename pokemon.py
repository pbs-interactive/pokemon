class pokemon:
    def __init__(self, number, name, level, stats, moves):
        self.number = number#int 001
        self.name = name   #bulbasaur
        self.level = level #int 5
        self.stats = stats #array of ints? {hp/att/def/etc}
        self.moves = moves #array of type move

    def printMe(self): 	#print function
        print("Pokedex#: " + str(self.number).zfill(3))
        print ("This pokemon is a level " + str(self.level) + " " + self.name + ".")

#Testing __init__ and printMe
bulbasaur = pokemon(001, 'bulbasaur', 005, 'placeholder', 'placeholder')
bulbasaur.printMe()
