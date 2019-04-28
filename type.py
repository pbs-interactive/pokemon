class Type:
    def __init__(self, name, wkn, str):
        self.name = name
        self.wkn = wkn
        self.str = str

    def printType(self):
        print("Type: " + self.name)
        print("Weak to: ") #might have to iterate across arrays unless python has fancy stuff


class Grass(Type):
    def __init__(self):
        Type.__init__(self, 'Grass', [Fire], [Water])


class Fire(Type):
    def __init__(self):
        Type.__init__(self, 'Fire', [Water], [Grass])


class Water(Type):
    def __init__(self):
        Type.__init__(self, 'Water', [Grass, Electric], [Fire, Ground])


class Ground(Type):
    def __init__(self):
        Type.__init__(self, 'Ground', [Water, Grass], [Electric])


class Electric(Type):
    def __init__(self):
        Type.__init__(self, 'Electric', [Ground], [Water])


#Testing...
pikachu = Fire()
pikachu.printType()
