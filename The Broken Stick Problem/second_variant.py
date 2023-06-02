import random
import numpy as np
from scipy.stats import norm

class Simulation(object):

    def run_simulation(self):

        """
        Sample points along the stick
        """
        p1 = np.random.uniform(0,1)
        p2 = np.random.uniform(p1,1)
        segs = [0,0,0]

        segs[0] = p1
        segs[1] = p2-p1
        segs[2] = 1-p2
        segs.sort()

        return (segs[2] <= segs[0]+segs[1])

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

        print("The ", confidence*100, "% confidence interval for the mean of the population is: [",
                sample_mean - z_alpha_halved * (np.sqrt(sample_variance) /  np.sqrt(n)) ,
                sample_mean + z_alpha_halved * (np.sqrt(sample_variance) /  np.sqrt(n)),
                "]")



