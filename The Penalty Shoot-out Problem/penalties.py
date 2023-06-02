import random
import numpy as np
from scipy.stats import norm

class Simulation(object):

    def __init__(self,p):

        self.p = p


    def run_simulation(self):

        count_1 = 0
        count_2 = 0
        turns = 0

        for i in range(5):

            turns += 1
            count_1 += np.random.choice([1,0], p = [self.p, 1-self.p])
            count_2 += np.random.choice([1,0], p = [self.p, 1-self.p])


        while count_1 == count_2:
            turns += 1
            count_1 += np.random.choice([1,0], p = [self.p, 1-self.p])
            count_2 += np.random.choice([1,0], p = [self.p, 1-self.p])

        return turns


    """
    Compute a confidence interval for the mean of the population
    """
    def get_confidence_interval(self, confidence, n):

        "Store observations"
        observations = []
        for i in range(n):
            observations.append(self.run_simulation())

        """
        Compute sample mean and sample_variance
        """
        sample_mean = sum(observations) / n

        sample_variance = 0
        for i in range(n):
            sample_variance += (observations[i] - sample_mean) ** 2
        sample_variance = sample_variance / (n - 1)

        z_alpha_halved = norm.ppf((1-confidence) / 2 + confidence, loc=0, scale=1)

        print("The", confidence*100, "% confidence interval for the mean of the population, setting p = ", self.p, " is: [",
                sample_mean - z_alpha_halved * (np.sqrt(sample_variance) /  np.sqrt(n)) ,
                sample_mean + z_alpha_halved * (np.sqrt(sample_variance) /  np.sqrt(n)),
                "]")
        return observations