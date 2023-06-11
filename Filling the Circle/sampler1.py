import random
import matplotlib.pyplot as plt
import numpy as np


class Sampler_1(object):

    def __init__(self, r,n):

        """
        Initialize sim object with the radius of the circle and the number of samples
        """

        self.r = r
        self.n = n
        self.x_s = []
        self.y_s = []

    def uniform_sampler(self):

        """
        Uniform sampler in (0,1) interval
        """

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

        """
        Get N sample points
        """

        for _ in range(self.n):

            point = self.sample()
            self.x_s.append(point[0])
            self.y_s.append(point[1])

        return self.x_s, self.y_s

    def plot(self):

        """
        Plot points in the circle
        """

        if(len(self.x_s) == 0):
            print("Get_samples must be called first")

        else:
            plt.scatter(self.x_s,self.y_s, s= 1)
            plt.show()
