import random
import numpy as np
from scipy.stats import norm

class Simulation(object):

    def __init__(self, n):

        """
        Init with number of ladies.
        """
        self.n_ladies = n
        self.dowry = [i for i in range(1, n+1)]


    def find_optimal_l(self):

        """
        Find optimal l by solving the pdf equation numerically.
        """

        sum_reciprocals = 0
        for j in range(1,self.n_ladies):
            sum_reciprocals += 1/j

        """
        Find optimal l -- O(N)
        """
        for i in range(1, self.n_ladies):
            if ((i / self.n_ladies) > (i / self.n_ladies)* sum_reciprocals):
                return i

            else: sum_reciprocals -= 1/i



    def run_simulation(self, optimal_l):

        """
        Randomly extract a dowry (here we produce the whole extracted sequence)
        """
        random.shuffle(self.dowry)

        max_before_l = max(self.dowry[:optimal_l])

        for i in range(optimal_l, len(self.dowry)):

            """
            First candidate found
            """
            if self.dowry[i] > max_before_l:
                """
                First candidate is max - we win the game
                """
                if self.dowry[i] == self.n_ladies:
                    return 1

                else: return 0

        return 0

    """
    Compute a confidence interval for the mean of the population
    """
    def get_confidence_interval(self, confidence, n_simulations):

        optimal_l = self.find_optimal_l()

        observations = []
        for sim in range(n_simulations):
            observations.append(self.run_simulation(optimal_l))

        """
        Compute sample mean and sample_variance
        """

        sample_proportion_rights = sum(observations) / n_simulations

        sample_variance = sample_proportion_rights * (1 - sample_proportion_rights)

        z_alpha_halved = norm.ppf((1-confidence) / 2 + confidence, loc=0, scale=1)

        print("The average proportion of the times our strategy gives the correct answer is: ", sample_proportion_rights)
        print("The", confidence*100, "% confidence interval for the average proportion of the times our strategy gives the correct answer is: [",
                sample_proportion_rights - z_alpha_halved * (np.sqrt(sample_variance) /  np.sqrt(n_simulations)) ,
                sample_proportion_rights + z_alpha_halved * (np.sqrt(sample_variance) /  np.sqrt(n_simulations)),
                "]")
        #return self.find_optimal_l(), observations

sim = Simulation(1000)
sim.get_confidence_interval(0.95,10000)
