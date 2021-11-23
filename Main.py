import pygame

import core
from Planette import Planette
from Soleil import Soleil


def setup():
    core.fps = 60
    core.WINDOW_SIZE = [1000, 700]


    core.memory("Soleil","Soleil")
    core.memory("TableauDeSoleils", [])
    for s in range(1):
        core.memory("TableauDeSoleils").append(Soleil())


    core.memory("Planette", "Planette.N°")
    core.memory("TableauDePlanettes", [])
    for i in range(8):
        core.memory("TableauDePlanettes").append(Planette())

    core.memory("gravity", 9.81)



def run():
    core.cleanScreen()

    for s in core.memory("TableauDeSoleils"):
        pygame.draw.circle(core.screen, s.couleur, s.position, s.rayon)
        print(Soleil().position)

    for i in core.memory("TableauDePlanettes"):
        pygame.draw.circle(core.screen, i.couleur, i.position, i.rayon)
        print(Planette().position)

    i.position, pygame.Vector2(i.position).x,i.position.y + core.memory("gravity")

    if i.position.y + i.rayon > core.WINDOW_SIZE[1]:
        core.memory("gravity", core.memory("gravity") * -1)

    if i.position.y - i.rayon < 0:
        core.memory("gravity", core.memory("gravity") * -1)







core.main(setup, run)
