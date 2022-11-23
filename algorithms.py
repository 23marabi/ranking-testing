from time import localtime, strftime
from random import seed, randint
import numpy as np
import pandas as pd
from random import seed, randrange

from visualize import plot_graph, score_graph
from models import MatchResult, MatchValues

seed()

def generate_matrice(team_num):
    # test numpy matrix of matches
    results_matrix = np.empty((0, 4))

    # add a couple of test entries
    for i in range(1,50):
        test_add = MatchResult(
                i, # Match #
                team_num, # Team num
                np.random.normal(loc=30.0, scale=10.0), # Auto Score
                np.clip(np.random.normal(loc=50, scale=45.0), 0, 150), # Teleop score
                np.random.normal(loc=15, scale=2.5), # Engame Times
                randrange(0,5)) # Penalities
        results_matrix = np.append(results_matrix, [test_add.array()], axis=0)

    return (str(team_num), results_matrix) # tuple w/ team num and actual matrix

def generate_rank(team_data):
    results_matrix = team_data[1] # get the actual data from the tuple

    match_weights = np.array([0.1, 0.2, 0.3, 0.4]) # kernel for weighing matches
    weights = np.array([0.7, 0.6, 0.2, 4]) # weights for different scores

    ### DEBUG ###

    # print out each match
    #for i in range(0, len(results_matrix)):
    #    print("Match #"+str(i+1)+": " + str(results_matrix[i,:]))

    # print out the different values
    # print("\nAuto Scores: " + str(results_matrix[:,MatchValues.AutoScore.value]))
    # print("Teleop Scores: " + str(results_matrix[:,MatchValues.TeleopScore.value]))
    # print("Endgame Times: " + str(results_matrix[:,MatchValues.EndgameTime.value]))
    # print("Penalties: " + str(results_matrix[:,MatchValues.Penalties.value]))
    
    # test convolutions for valueing more recent matches more, broken rn
    # TODO
    for n in range(0, 4):
        print(np.convolve(results_matrix[:,n], match_weight))
    exit()

    med_results = results_matrix[1:-1] # remove the oldest & most recent matches
    # calculate the averages
    averages = np.average(med_results, axis=0)

    # print("\nAverages: " + str(averages))
    # weighted_averages = averages * weights
    # print("Weighted Averages: " + str(weighted_averages))

    weighted_averages[2] *= -1 # negative cause they're being subtracted
    weighted_averages[3] *= -1

    total = weighted_averages.sum()
    print("Total: " + str(total.round()) + "%") # print out the total

    return (team_data[0], total)

# generate some test data
one = generate_matrice(8089)
two = generate_matrice(2022)
three = generate_matrice(1024)
four = generate_matrice(5345)

# plot the test data
plot_graph([one,two, three, four], MatchValues.AutoScore)
plot_graph([one,two, three, four], MatchValues.TeleopScore)
plot_graph([one,two, three, four], MatchValues.Penalties)
score_graph([generate_rank(one), generate_rank(two), generate_rank(three), generate_rank(four)])

# df = pd.DataFrame(np.flipud(np.rot90(results_matrix)), columns = ['Match #1','Match #2','Match #3', 'Match #4'])
# df.to_csv("test.csv")
