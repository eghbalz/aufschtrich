from collections import OrderedDict
import numpy as np
import matplotlib.pyplot as plt
import random
from configs import *



plt.ion()

class Population():
    def __init__(self):
        self.organisms = OrderedDict()
        self.size = 0
        self.ids = []
        self.death_count = 0
        self.infected_count = 0
        self.iter = 0
        self.data = []
        fig, ax = plt.subplots()
        self.fig = fig
        self.ax = ax
        # self.im = self.ax.imshow(np.zeros((480, 640, 3)))

    def calc_positios(self):
        positions = []
        for id in self.ids:
            o = self.organisms[id]
            positions.insert(id, o.position)
        return positions


    def add(self, org):
        new_id = self.size
        self.ids.append(new_id)
        org.set_id(new_id)
        self.organisms[org.id] = org
        self.size += 1

    def remove(self, id):
        self.organisms.pop(id)
        for ix, i  in enumerate(self.ids):
            if i == id:
                self.ids.pop(ix)
        self.size -= 1



    def calc_dist(self):
        XA = np.array(self.calc_positios(),dtype=np.float32)
        if XA.size<=0:
            return []
        XB = XA
        XA_norm = np.sum(XA ** 2, axis=1)
        XB_norm = np.sum(XB ** 2, axis=1)
        XA_XB_T = np.dot(XA, XB.T)
        distances = XA_norm.reshape(-1, 1) + XB_norm - 2 * XA_XB_T
        return distances

    def infection_control(self):
        dist = self.calc_dist()
        if len(dist)==0:
            return
        rows, cols = np.where(dist<MIN_SAFE_DIST)
        for ix, iy in zip(rows, cols):
            if ix==iy:
                continue
            if (self.organisms[self.ids[ix]].infected
                and self.organisms[self.ids[ix]].alive)\
                    or (self.organisms[self.ids[iy]].infected
                        and self.organisms[self.ids[iy]].alive):
                if not self.organisms[self.ids[ix]].infected \
                        and self.organisms[self.ids[ix]].alive:
                    self.organisms[self.ids[ix]].become_infected()
                    self.infected_count += 1
                if not self.organisms[self.ids[iy]].infected \
                        and self.organisms[self.ids[iy]].alive:
                    self.organisms[self.ids[iy]].become_infected()
                    self.infected_count += 1

    def health_control(self):
        remove_id_lst = []
        for id in self.ids:
            if not self.organisms[id].alive:
                remove_id_lst.append(id)
                self.death_count += 1
        for id in remove_id_lst:
            self.remove(id)

    # define a function which returns an image as numpy array from figure
    def get_img_from_fig(self, fig):
        fig.canvas.draw()
        plt.axis('off')
        data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
        data = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        return data


    def display(self):
        plt.clf()
        for id in self.ids:
            o = self.organisms[id]
            if o.infected:
                infected = 'infected'
                c='r'
            else:
                infected = 'not infected'
                c='g'

            msg = "({:.2f})\n{}".format( o.health,o.name,)

            self.fig.text(o.position[0]/WORLD_LIMITS[0][1],  o.position[1]/WORLD_LIMITS[1][1],
                     msg, size = 10, rotation = random.randint(0,30),
                                    ha = "center", va = "center",color=c)

        self.fig.suptitle(
            'iter:{} , death: {} , infected: {} , alive: {}'.format(
                self.iter, self.death_count,
                self.infected_count, self.size),
                fontsize=11)

        d = self.get_img_from_fig(self.fig)
        self.data.insert(self.iter, d)
        self.fig.clf()


        # plt.pause(0.0001)

    def animate(self, i):
        # print(i, len(self.data))
        img = self.data[i]
        self.im.set_array(img)
        # a = self.ax.imshow(img)
        return [self.im]



