import numpy as np
import random
from scipy.stats import norm
import matplotlib.pyplot as plt

class Simulation():

    def __init__(self, rho,N):

        self.rho = rho
        self.N = N


    def uniform_sampler(self):

        sample = random.uniform(0,1);

        return sample


    def gaussian_sample(self):

        uni_sample = self.uniform_sampler()
        gaussian_sample = norm.ppf(uni_sample,0,1)

        return gaussian_sample



    def plot_distribition(self, obs):

        plt.hist(obs,300, density = True)
        plt.show()


    def get_observations(self):

        obs_x = []
        obs_y = []

        for _ in range(self.N):

            z1 = self.gaussian_sample()
            z2 = self.gaussian_sample()

            x = z1
            y = self.rho * z1 + np.sqrt(1-self.rho**2) * z2

            obs_x.append(x)
            obs_y.append(y)

        return obs_x, obs_y

    def compute_expected_value_product(self,obs_x,obs_y):

        e_xy = 0

        for i in range(len(obs_x)):

            e_xy += obs_x[i]*obs_y[i]

        return e_xy / len(obs_x)


    def compute_covariance(self, obs_x, obs_y):

        e_xy = self.compute_expected_value_product(obs_x,obs_y)

        e_x = sum(obs_x) / len(obs_x)
        e_y = sum(obs_y) / len(obs_y)

        return e_xy - e_x*e_y

    def compute_sample_variance(self, obs):

        sample_mean = sum(obs) / len(obs)

        sample_variance = 0

        for o in obs:
            sample_variance += (o - sample_mean)**2

        sample_variance = sample_variance / len(obs)

        return sample_variance


    def estimate_pearson(self, obs_x,obs_y):

        if(len(obs_x) != len(obs_y)): print("No chance to estimate Pearson")

        cov_xy = self.compute_covariance(obs_x,obs_y)
        var_x = self.compute_sample_variance(obs_x)
        var_y = self.compute_sample_variance(obs_y)

        return cov_xy / (np.sqrt(var_x*var_y))

    def get_pearson(self, obs_x,obs_y):

        print("Pearson coefficient on the samples: ", self.estimate_pearson(obs_x,obs_y))

