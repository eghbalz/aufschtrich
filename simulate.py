from organism import Organism
from population import Population
from utils import rand_pos
from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np

if __name__=="__main__":

    names = ['Rick Sanchez', 'Morty Smith', 'Jerry Smith', 'Summer Smith', 'Beth Smith', 'Jerry C-137', 'Birdperson',
             'Squanchy', 'Mr. P**pyb****ole','Noob Noob','Doofus Rick','Evil Morty','Scary Terry','The Cromulons',
             'Mr. Meeseeks','Mr. Goldenfold','Jessica','MC Haps','Beth Smith','Dr. Xenon Bloom','Unity','Crocubot',
             'Elon Tusk','Mr. Lucius Needful','King Jellybean','King Jellybean','Zeep Xanflorp', 'Beta VII',
             'Glexo Slim Slom','Cornvelious Daniel','Frank Palicky', 'Pickle Rick', 'Toby Matthews']

    population = Population()

    for name in names:
        colleague = Organism(rand_pos(), name)
        population.add(colleague)


    amish_cyborg = Organism([1,1], 'Amish Cyborg')
    amish_cyborg .infected = True
    population.add(amish_cyborg)

    baby_wizard = Organism([1,1], 'Baby Wizard')
    baby_wizard.infected = True
    population.add(baby_wizard)

    cousin_nicky = Organism([1,1], 'Cousin Nicky')
    cousin_nicky .infected = True
    population.add(cousin_nicky)


    population.infected_count = 3

    iter = 0
    while population.size>0 and iter<=500:
    # for _ in range(100):
        if population.size<=0:
            print('Simulation end. Everyone is dead!')
        print('step {} (population size:{})\n'.format(iter, population.size))
        for id in population.ids:
            population.organisms[id].walk_around()

        population.display()
        population.infection_control()
        population.health_control()
        population.iter = iter

        iter += 1
        print('\n')




    fig = plt.figure(figsize=(8, 8))
    plt.axis('off')

    im = plt.imshow(np.zeros((480, 640, 3)))
    data = population.data

    def init():
        im.set_data(np.zeros((480, 640, 3)))
        return [im]

    def animate_func(i):
        if i%10==0:
            print('preparing {}/{} '.format(i, len(data)))
        im.set_array(data[i])
        return [im]


    anim = animation.FuncAnimation(fig, animate_func,
                                   init_func=init,
                                   frames=(iter-1), interval=2000)
    anim.save('anime.mp4', fps=15, extra_args=['-vcodec', 'libx264'])


