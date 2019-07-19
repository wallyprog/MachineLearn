
from pontos import Pontos

class Recompensa(Pontos):
    def __init__(self, x, y, name):
        super(Recompensa,self).__init__(x,y)
        self.name = name
