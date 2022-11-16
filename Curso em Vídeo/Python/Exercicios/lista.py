# Voce quer fazer um sorteio entre 5 nomes de uma lista

import random

class Sorteio:
    def Sortear(self):
        self.lista = ['Felipe','Larissa','Carlos','Luciana','Priscila']
        print(random.choice(self.lista))
Nomes = Sorteio()
Nomes.Sortear()