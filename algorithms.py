from models import MatchResult
from time import localtime, strftime
from random import seed, randint
import numpy as np
import pandas as pd
from random import seed, randrange
from visualize import graph

seed()

def generate_matrice(team_num):
    # test numpy matrix of matches
    results_matrix = np.empty((0, 4))

    # add a couple of test entries
    for i in range(1,50):
        test_add = MatchResult(i, team_num, randrange(10,30), randrange(60,130), randrange(5, 15), randrange(0,3))
        results_matrix = np.append(results_matrix, [test_add.array()], axis=0)

    return (str(team_num), results_matrix)

def generate_rank(results_matrix):
    # array for the weights
    weights = np.array([0.7, 0.6, 0.2, 4])

    # print out each match
    for i in range(0, len(results_matrix)):
        print("Match #"+str(i+1)+": " + str(results_matrix[i,:]))

    # print out the different values
    print("\nAuto Scores: " + str(results_matrix[:,0]))
    print("Teleop Scores: " + str(results_matrix[:,1]))
    print("Endgame Times: " + str(results_matrix[:,2]))
    print("Penalties: " + str(results_matrix[:,3]))
    
    # calculate the averages
    averages = results_matrix.sum(axis=0) / len(results_matrix)
    print("\nAverages: " + str(averages))
    weighted_averages = averages * weights
    print("Weighted Averages: " + str(weighted_averages))

    weighted_averages[2] *= -1 # negative cause they're being subtracted
    weighted_averages[3] *= -1
    total = weighted_averages.sum()
    print("Total: " + str(total.round()) + "%") # print out the total

one = generate_matrice(8089)
two = generate_matrice(2022)
three = generate_matrice(1024)

plot_graph([one,two, three])

# df = pd.DataFrame(np.flipud(np.rot90(results_matrix)), columns = ['Match #1','Match #2','Match #3', 'Match #4'])
# df.to_csv("test.csv")
