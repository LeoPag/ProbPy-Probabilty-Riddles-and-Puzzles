import random
import numpy as np
from scipy.stats import norm

class Simulation(object):

    def __init__(self, n):
        self.n_ladies = n
        self.dowry = [i for i in range(1, n+1)]
    
    def find_optimal_stop(self):
        for i in range(1, self.n_ladies):
            if i / self.n_ladies > i / self.n_ladies*(sum([1/j for j in range(i, self.n_ladies-1)])):
                return i

    def run_simulation(self):

        # Randomly extract a dowry (here we produce the whole extracted sequence)
        optimal_stop = self.find_optimal_stop()
        random.shuffle(self.dowry)
        
        for i in range(optimal_stop, len(self.dowry)):

            # Check if the card is an ace
            if self.dowry[i] > max(self.dowry[:optimal_stop]):
                return i, self.dowry[i]

    """
    Compute a confidence interval for the mean of the population
    """
    def get_confidence_interval(self, confidence, n_simulations):
        
        observations = []
        for sim in range(n_simulations):
            observations.append(self.run_simulation()[1])
        
        """
        Compute sample mean and sample_variance
        """

        sample_proportion_rights = sum([1 for i in observations if i == self.n_ladies]) / n_simulations
        
        sample_variance = sample_proportion_rights * (1 - sample_proportion_rights)

        z_alpha_halved = norm.ppf((1-confidence) / 2 + confidence, loc=0, scale=1)

        print("The average proportion of the times our strategy gives the correct answer is: ", sample_proportion_rights)
        print("The", confidence*100, "% confidence interval for the average proportion of the times our strategy gives the correct answer is: [",
                sample_proportion_rights - z_alpha_halved * (np.sqrt(sample_variance) /  np.sqrt(n_simulations)) ,
                sample_proportion_rights + z_alpha_halved * (np.sqrt(sample_variance) /  np.sqrt(n_simulations)),
                "]")
        return self.find_optimal_stop(), observations