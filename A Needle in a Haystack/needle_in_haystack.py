import random
import numpy as np
from scipy.stats import norm

class Simulation(object):

    def __init__(self, n):

        """
        Init with number of ladies.
        """
        self.max_straws = n


    def run_simulation(self):

        """
        Randomly extract a dowry (here we produce the whole extracted sequence)
        """

        curr_straws =  self.max_straws + 1
        turns = 0

        while curr_straws > 1:
            
            curr_straws = random.randint(1,curr_straws - 1)
            turns += 1

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

        print("Sample mean of the observations is: ", sample_mean)

        print("The ", confidence*100, "% confidence interval for the mean of the population is: [",
                sample_mean - z_alpha_halved * (np.sqrt(sample_variance) /  np.sqrt(n)) ,
                sample_mean + z_alpha_halved * (np.sqrt(sample_variance) /  np.sqrt(n)),
                "]")

        return observations


