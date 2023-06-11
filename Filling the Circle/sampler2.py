import random
import matplotlib.pyplot as plt
import numpy as np


class Sampler_2(object):


    def __init__(self, r,n):

        """
        Initialize object with the radius of the circle and the number of samples
        """

        self.r = r
        self.n = n
        self.x_s = []
        self.y_s = []
        self.count_waste = 0


    def uniform_sampler(self):

        """
        Uniform sampler in (0,1) interval
        """

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

        """
        Get N sample points
        """

        count = 0

        while(count < self.n):

            point = self.sample()
            x = point[0]
            y = point[1]
            if(x**2 + y**2 <= self.r**2):
                self.x_s.append(point[0])
                self.y_s.append(point[1])
                count += 1

            else:
                self.count_waste += 1

        return self.x_s, self.y_s

    def get_count_waste(self):

        """
        Return wasted samples
        """

        return self.count_waste


    def plot(self):

        """
        Plot points in the circle
        """

        if(len(self.x_s) == 0):
            print("Get_samples must be called first")

        else:
            plt.scatter(self.x_s,self.y_s, s= 1)
            plt.show()
