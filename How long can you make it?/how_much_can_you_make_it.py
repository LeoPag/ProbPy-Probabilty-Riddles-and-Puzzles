import random
import numpy as np
from scipy.stats import norm

class Simulation(object):

    """
    Sample points along the stick
    """
    def run_simulation(self):

        last_element = 0
        length_sequence = 0

        while True:

            sample= np.random.uniform(0,1)
            length_sequence+=1
            if(sample < last_element):
                break
            last_element = sample

        return length_sequence - 1

    """
    Compute a confidence interval for the mean of the population
    """
    def get_confidence_interval(self, confidence, n):

        "Store observations"
        self.observations = []
        for i in range(n):
            self.observations.append(self.run_simulation())

        """
        Compute sample mean and sample_variance
        """
        sample_mean = sum(self.observations) / n

        sample_variance = 0
        for i in range(n):
            sample_variance += (self.observations[i] - sample_mean) ** 2
        sample_variance = sample_variance / (n - 1)

        z_alpha_halved = norm.ppf((1-confidence) / 2 + confidence, loc=0, scale=1)

        print("Sample mean of the observations is: ", sample_mean)

        print("The ", confidence*100, "% confidence interval for the mean of the population is: [",
                sample_mean - z_alpha_halved * (np.sqrt(sample_variance) /  np.sqrt(n)) ,
                sample_mean + z_alpha_halved * (np.sqrt(sample_variance) /  np.sqrt(n)),
                "]")
