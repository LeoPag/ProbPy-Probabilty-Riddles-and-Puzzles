"""
This code implemnts the algorithmic solution to Problem 40 of Mosteller book
"""

class Solution():

    def __init__(self):
        self.probabilities = [-1] * 50 #1 based index array to store probability that ace is turned exactly at round i.
        self.cumulatives = [0] * 50 #1 based index array to store probability that ace is turbed before or at round i.

    def compute_probability(self,i):
        if(i == 1):
            self.probabilities[1] = 4/52
            self.cumulatives[1] = 4/52
            return (4/52)
        else:
            if(self.cumulatives[i-1] == 0): raise ValueError('You must compute probability at ', i-1, ' first')
            self.probabilities[i]  = (1 - self.cumulatives[i-1]) * (4 / (52-(i-1)))
            self.cumulatives[i] = self.probabilities[i] + self.cumulatives[i-1]
            return(self.probabilities[i])

    def check_sum(self):
        if(self.cumulatives[49] == 0): raise ValueError('You must run the expected_value_function')
        elif(self.cumulatives[49] != 1): raise ValueError('Probability of turning an ace before or at card 49 should be 1')
    
    def expected_value(self):
        E = 0
        for i in range(1,50):
            E += i * self.compute_probability(i)

        return E


sol = Solution()
print("Average number of card to be turned is: ", sol.expected_value())
sol.check_sum()
