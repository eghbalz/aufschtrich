import random
from configs import *


class Organism:
    def __init__(self, position, name):
        self.position = position
        self.health = 1
        self.infected = False
        self.alive = True
        self.direction = [1, 1]
        self.name = name
        self.id = -1

    def set_id(self, id):
        self.id = id

    def become_infected(self):
        print('{} had an interact with infected. roll the dice...'.format(self.name))
        if random.random() < INFECTION_PROB:
            self.infected = True
            self.health -= SICKNESS_RATIO
            print('{} is infected! health: {}'.format(self.name, self.health))
        else:
            print('{} is not infected! '.format(self.name))

    def infect_organism(self, other_organism):
        other_organism.become_infected()

    def health_check(self):
        if self.infected and self.health > 0:
            self.health -= SICKNESS_RATIO
            print('{} is sick! health reduced to {}.'.format(self.name, self.health))
        if self.health <= 0:
            self.alive = False
            print('{} is DEAD! '.format(self.name))

    def check_position(self):
        for i in range(2):
            if self.position[i] < WORLD_LIMITS[i][0] or self.position[i] > WORLD_LIMITS[i][1]:
                # self.position[i] = WORLD_LIMITS[i][0]
                self.direction[i] *=-1
            if self.position[i] < WORLD_LIMITS[i][0]:
                self.position[i] = WORLD_LIMITS[i][0]

            if self.position[i] > WORLD_LIMITS[i][1]:
                self.position[i] = WORLD_LIMITS[i][1]

    def change_direction(self):
        for i in range(2):
            if random.random() < CHANGE_DIRECTION_PROB:
                self.direction[i] *=-1


    def walk_around(self):
        print('{} is moving! pos:({})'.format(self.name, self.position))
        x = random.random()
        y = random.random()
        walk = [x, y]
        for i in range(2):
            self.position[i] += walk[i] * self.direction[i]
        self.check_position()
        self.health_check()
        self.change_direction()

    def is_infected(self):
        return self.infected










