import random
from configs import *

def rand_pos():
    return [random.random()*WORLD_LIMITS[0][1],random.random()*WORLD_LIMITS[1][1]]

