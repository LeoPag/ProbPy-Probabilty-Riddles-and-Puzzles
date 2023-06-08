import itertools, random
import numpy as np
from scipy.stats import norm

class Simulation(object):

    def __init__(self):
        self.deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
        self.aces = [(1, 'Spade'), (1, 'Heart'), (1, 'Diamond'), (1, 'Club')]
    def run_simulation(self):

        # Shuffle the deck
        random.shuffle(self.deck)
        
        for i in range(len(self.deck)):

            # Check if the card is an ace
            if self.deck[i] in self.aces:
                return i + 1, self.deck[i]

    """
    Compute a confidence interval for the mean of the population
    """
    def get_confidence_interval(self, confidence, n):

        "Store observations"
        observations = []
        which_cards = []
        for i in range(n):
            observations.append(self.run_simulation()[0])
            which_cards.append(self.run_simulation()[1][1])

        """
        Compute sample mean and sample_variance
        """
        sample_mean = sum(observations) / n

        sample_variance = 0
        for i in range(n):
            sample_variance += (observations[i] - sample_mean) ** 2
        sample_variance = sample_variance / (n - 1)

        z_alpha_halved = norm.ppf((1-confidence) / 2 + confidence, loc=0, scale=1)

        print("The average number of cards required to produce the first ace is: ", sample_mean)
        print("The", confidence*100, "% confidence interval for the average number of cards required to produce the first ace is: [",
                sample_mean - z_alpha_halved * (np.sqrt(sample_variance) /  np.sqrt(n)) ,
                sample_mean + z_alpha_halved * (np.sqrt(sample_variance) /  np.sqrt(n)),
                "]")
        return observations, which_cards
    

class AnalyticalComputation(object):
    # In this class we compute the expected value of the number of cards required to produce the first ace using a recursive formula
    def __init__(self):
        self.deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
        self.aces = [(1, 'Spade'), (1, 'Heart'), (1, 'Diamond'), (1, 'Club')]
        self.probabilities = [-1] * 50 #1 based index array to store probability that ace is turned exactly at round i.
        self.cumulatives = [0] * 50 #1 based index array to store probability that ace is turned before or at round i.

    def compute_probability(self, turn):
        if (turn == 1): # First turn of the cards
            self.probabilities[1] = 4/52
            self.cumulatives[1] = 4/52
            return (4/52)
        else:
            if(self.cumulatives[turn-1] == 0): raise ValueError('You must compute probability at ', turn-1, ' first')
            self.probabilities[turn]  = (1 - self.cumulatives[turn-1]) * (4 / (52-(turn-1)))
            self.cumulatives[turn] = self.probabilities[turn] + self.cumulatives[turn-1]
            return(self.probabilities[turn])

    def check_sum(self):
        if(self.cumulatives[49] == 0): raise ValueError('You must run the expected_value_function')
        elif(self.cumulatives[49] != 1): raise ValueError('Probability of turning an ace before or at card 49 should be 1')
    
    def expected_value(self):
        E = 0
        for i in range(1,50):
            E += i * self.compute_probability(i)
        return E, self.probabilities, self.cumulatives
