import random
import numpy as np
from scipy.stats import norm

class Simulation(object):

    def __init__(self, p):
        self.p = p

    def get_next_state(self,state):

        movement = np.random.choice([-1, 1], p = [1-self.p, self.p]) # -1: left, 1: right
        
        #Start
        if state == 0:
            next_state = state + movement
        # Leonardo wins: absorbing state
        elif state == -1:
            next_state = -1

        # Transition state
        elif state == 1:
            next_state = state + movement
        #Angleo wins: absorbing state 
        elif state == 2:
            next_state = 2
        
        return next_state

    def run_simulation(self):

        current_state = 0

        while current_state != 2 or current_state != -1:
            current_state = self.get_next_state(current_state)
            if current_state == 2:
                return 1 # Angelo wins
            elif current_state == -1:
                return 0 # Leonardo wins

    """
    Compute a confidence interval for the population proportion
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
        return observations
    

class Generalized_Simulation(object):
    
    def __init__(self, p, angelo_start, leonardo_start):
        self.p = p
        self.m = angelo_start
        self.n = leonardo_start

    def get_next_state(self,state):

        movement = np.random.choice([-1, 1], p = [1-self.p, self.p]) # -1: left, 1: right
        
        #Start
        if state == 0:
            next_state = 0
        elif state ==  self.m+self.n:
            next_state = self.m+self.n
        else:
            next_state = state + movement
        
        return next_state

    def run_simulation(self):

        current_state = self.m

        while current_state != (self.m+self.n) or current_state != 0:
            current_state = self.get_next_state(current_state)
            if current_state == (self.m+self.n):
                return 1 # Angelo wins
            elif current_state == 0:
                return 0 # Leonardo wins

    """
    Compute a confidence interval for the population proportion
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
        print("The sample proportion, for p = ", self.p,", angelo_start = ", self.m,", leonardo_start = ", self.n, " is: ", sample_proportion)
        print("The ", confidence*100, "% confidence interval for the mean of the population is: [",
                sample_proportion - z_alpha_halved * (np.sqrt(sample_variance) /  np.sqrt(n)) ,
                sample_proportion + z_alpha_halved * (np.sqrt(sample_variance) /  np.sqrt(n)),
                "]")
        return sample_proportion