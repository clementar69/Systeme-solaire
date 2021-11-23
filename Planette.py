import random
from pygame import Vector2

class Planette:

    def __init__(self):
        self.rayon = (random.randint(15, 40))
        self.couleur = (random.randint(20, 215), random.randint(20, 215), random.randint(20, 215))
        self.position = Vector2(random.randint(0, 900), random.randint(0, 600))

