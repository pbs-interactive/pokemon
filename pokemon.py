class pokemon:
	def __init__(self, number, name, level, stats, moves):
		self.number = number;#int 001
		self.name = name;   #bulbasaur
		self.level = level; #int 5
		self.stats = stats; #array of ints? {hp/att/def/etc}
		self.moves = moves; #array of type move

	def print(self, pokemon): 	#print function
		print("Pokedex #:" + number);
		print("This pokemon is a level " + level + " " + name + ".");