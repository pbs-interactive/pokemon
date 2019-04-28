class pokemon:
	def __init__(self, number, name, level, stats, moves):
		self.number = number#int 001
		self.name = name   #bulbasaur
		self.level = level #int 5
		self.stats = stats #array of ints? {hp/att/def/etc}
		self.moves = moves #array of type move

	def str(self): 	#print function
		print "Pokedex #:" + self.number
		print "This pokemon is a level " + self.level + " " + self.name + "."


    def main(): #MAIN FUNCTION (for testing)
        print()

