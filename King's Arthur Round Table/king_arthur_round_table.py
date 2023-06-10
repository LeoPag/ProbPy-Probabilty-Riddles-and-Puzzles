import random
import numpy as np
from scipy.stats import norm

class Simulation(object):

    def sample_chords(self):

        """
        Sample chords with its end and starting point:
        We sample the angle in a uniform distribution (0,360)
        """
        chord_start = random.uniform(0,360)
        chord_end = random.uniform(0,360)

        return [chord_start,chord_end]



    def check_interception(self, chord1, chord2):

        """
        Check if the chords intercept, returning a Boolean
        """

        min_1 = min(chord1[0], chord1[1])
        min_2 = min(chord2[0], chord2[1])

        max_1 = max(chord1[0], chord1[1])
        max_2 = max(chord2[0], chord2[1])

        if(min_1 <= min_2 <= max_1 <= max_2): return True
        if(min_2 <= min_1 <= max_2 <= max_1): return True

        return False


    def run_simulation(self):

        chord1 = self.sample_chords()
        chord2 = self.sample_chords()

        return self.check_interception(chord1, chord2)

    """
    Compute a confidence interval for the Bernoulli mean p
    """
    def get_confidence_interval(self, confidence, n):

        "Store observations"
        observations = []
        for i in range(n):
            observations.append(self.run_simulation())

        """
        Compute sample mean and sample_variance
        """
        sample_proportion = sum(observations) / n

        sample_variance = sample_proportion * (1 - sample_proportion)

        z_alpha_halved = norm.ppf((1-confidence) / 2 + confidence, loc=0, scale=1)
        print("The sample proportion is: ", sample_proportion)
        print("The ", confidence*100, "% confidence interval for the mean of the population is: [",
                sample_proportion - z_alpha_halved * (np.sqrt(sample_variance) /  np.sqrt(n)) ,
                sample_proportion + z_alpha_halved * (np.sqrt(sample_variance) /  np.sqrt(n)),
                "]")
