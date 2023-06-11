import random
import matplotlib.pyplot as plt
import numpy as np


class Simulation(object):

    """
    Initialize sim object with the radius of the circle and the number of samples
    """
    def __init__(self, r,n):

        self.r = r
        self.n = n

    """
    Uniform sampler in (0,1) interval
    """

    def uniform_sampler(self):

        sample = random.uniform(0,1)
        return sample


    def sample(self):

        """
        Sample r and theta
        """
        r = self.uniform_sampler() * self.r
        theta = self.uniform_sampler() * 2*np.pi

        x = r * np.cos(theta)
        y = r * np.sin(theta)

        return [x,y]

    def get_samples(self):

        x_s = []
        y_s = []

        for _ in range(self.n):

            point = self.sample()
            x_s.append(point[0])
            y_s.append(point[1])

        plt.scatter(x_s,y_s, s= 1)
        plt.show()


class Simulation_2(object):

    """
    Initialize sim object with the radius of the circle and the number of samples
    """
    def __init__(self, r,n):

        self.r = r
        self.n = n

    """
    Uniform sampler in (0,1) interval
    """

    def uniform_sampler(self):

        sample = random.uniform(0,1)
        return sample


    def sample(self):

        """
        Sample x and y
        """
        x = -self.r + self.uniform_sampler() * 2 * self.r
        y = -self.r + self.uniform_sampler() * 2 * self.r

        return [x,y]

    def get_samples(self):

        x_s = []
        y_s = []

        count = 0
        while(count < self.n):

            point = self.sample()
            x = point[0]
            y = point[1]
            if(x**2 + y**2 <= self.r**2):
                x_s.append(point[0])
                y_s.append(point[1])
                count += 1

        plt.scatter(x_s,y_s, s= 1)
        plt.show()


sim = Simulation(1,10000)
sim.get_samples()


sim = Simulation_2(1,10000)
sim.get_samples()
