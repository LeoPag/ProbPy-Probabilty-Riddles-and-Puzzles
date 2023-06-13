import random
from scipy.stats import norm
import numpy as np


class Simulation():


    """
    This class represents the situation illustrated in the problem.
    In the following code, we always assume that Leo is initially
    located northward and eastward with respect to Angelo.
    """

    def __init__(self,times_square, angelo, leo):

        """
        Grid dimensions with positions of Angelo and Leo
        """

        self.Times_Square = [times_square[0], times_square[1]]
        self.Angelo = [angelo[0],angelo[1]]
        self.Leo = [leo[0],leo[1]]

        self.computed_A_to_L = False
        self.computed_L_to_A = False

        #Store the paths
        self.paths_A_to_L = []
        self.paths_L_to_A = []



    """
    Compute all the possible paths from Angelo to Leo with Backtracking
    """
    def backtrack_paths_A_to_L(self, past_moves, curr_pos):

        x = curr_pos[0]
        y = curr_pos[1]

        if(x == self.Leo[0]) and (y == self.Leo[1]):
            self.paths_A_to_L.append(past_moves)
            return

        if(x < self.Leo[0]):
            self.backtrack_paths_A_to_L(past_moves + '→', [x+1, y])

        if(y < self.Leo[1]):
            self.backtrack_paths_A_to_L(past_moves + '↑', [x, y+1])


    """
    Compute all the possible paths from Leo to Angelo with Backtracking
    """
    def backtrack_paths_L_to_A(self, past_moves, curr_pos):

        x = curr_pos[0]
        y = curr_pos[1]

        if(x == self.Angelo[0]) and (y == self.Angelo[1]):
            self.paths_L_to_A.append(past_moves)
            return

        if(x > self.Angelo[0]):
            self.backtrack_paths_L_to_A(past_moves + '←', [x-1, y])

        if(y > self.Angelo[1]):
            self.backtrack_paths_L_to_A(past_moves + '↓', [x, y-1])


    """
    Compute and store all paths from A to L
    """
    def get_paths_A_to_L(self):

        if(self.computed_A_to_L == False):
            self.backtrack_paths_A_to_L("",self.Angelo)
            self.computed_A_to_L = True

        return self.paths_A_to_L


    """
    Compute and store all paths from L to A
    """
    def get_paths_L_to_A(self):

        if(self.computed_L_to_A == False):
            self.backtrack_paths_L_to_A("",self.Leo)
            self.computed_L_to_A = True

        return self.paths_L_to_A


    """
    Pick a random path
    """
    def get_random_path(self, paths):

        path_idx = random.randint(0,len(paths)-1)

        return paths[path_idx]



    """
    Run a full simulation, with A and L moving toward each other
    """
    def run_simulation(self):

        if (self.computed_A_to_L == False):
            self.get_paths_A_to_L()
        if (self.computed_L_to_A == False):
            self.get_paths_L_to_A()

        """
        Set current position to starting position
        """

        curr_leo = [self.Leo[0],self.Leo[1]]
        curr_angelo = [self.Angelo[0],self.Angelo[1]]


        """
        Get a random path for both A and L
        """
        path_leo = self.get_random_path(self.paths_L_to_A)
        path_angelo = self.get_random_path(self.paths_A_to_L)


        for i in range(len(path_leo)):

            if(path_leo[i] == '←'):
                curr_leo[0] -= 1

            if(path_leo[i] == '↓'):
                curr_leo[1] -= 1

            if(path_angelo[i] == '→'):
                curr_angelo[0] += 1

            if(path_angelo[i] == '↑'):
                curr_angelo[1] += 1


            if(curr_leo[0] == curr_angelo[0] and curr_leo[1] == curr_angelo[1]):

                if(curr_leo[0] == self.Times_Square[0] and curr_leo[1] == self.Times_Square[1]):

                    return 1,1

                else: return 0,1

        return 0,0


    """
    Compute a confidence interval for the population proportion
    """
    def get_confidence_interval(self, confidence, n):

        "Store observations"
        meetings_in_times_square = []
        meetings = []

        for i in range(n):
            observations = self.run_simulation()
            meetings_in_times_square.append(observations[0])
            meetings.append(observations[1])


        """
        Compute sample mean and sample_variance
        """
        sample_proportion_times_square = sum(meetings_in_times_square) / n
        sample_proportion_meeting = sum(meetings) / n

        sample_variance_times_square = sample_proportion_times_square * (1 - sample_proportion_times_square)
        sample_variance_meeting = sample_proportion_meeting * (1 - sample_proportion_meeting)

        z_alpha_halved = norm.ppf((1-confidence) / 2 + confidence, loc=0, scale=1)
        print("\n")

        print("The sample proportion of the meetings in Times Square is: ", sample_proportion_times_square)


        print("The ", confidence*100, "% confidence interval for sample_proportion of the meetings in Times Square is: [",
                sample_proportion_times_square- z_alpha_halved * (np.sqrt(sample_variance_times_square) /  np.sqrt(n)) ,
                sample_proportion_times_square + z_alpha_halved * (np.sqrt(sample_variance_times_square) /  np.sqrt(n)),
                "]")

        print("\n")

        print("The sample proportion of the meetings is: ", sample_proportion_meeting)


        print("The ", confidence*100, "% confidence interval for sample_proportion of the meetings is: [",
                sample_proportion_meeting- z_alpha_halved * (np.sqrt(sample_variance_meeting) /  np.sqrt(n)) ,
                sample_proportion_meeting + z_alpha_halved * (np.sqrt(sample_variance_meeting) /  np.sqrt(n)),
                "]")


        return sample_proportion_times_square, sample_proportion_meeting


times_square =[2,2]
angelo = [0,0]
leo = [4,4]

g = Simulation(times_square, angelo, leo)
print(len(g.get_paths_A_to_L()))
print(g.get_paths_L_to_A())
g.get_confidence_interval(0.95,1000000)
