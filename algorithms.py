from models import MatchResult
from time import localtime, strftime
from random import seed, randint
import numpy as np
import pandas as pd

results_matrix = np.array([[26, 100, 8, 0], # match 1
                   [23, 110, 2, 0], # match 2
                   [19, 80, 4, 0], # match 3
                   [21, 93, 19, 0]]) # match 4
results_matrix = np.append(results_matrix, [[20, 89, 7, 0]], axis=0)

weights = np.array([0.7, 0.6, 0.2, 4])

for i in range(0, len(results_matrix)):
    print("Match #"+str(i+1)+": " + str(results_matrix[i,:]))

print("\nAuto Scores: " + str(results_matrix[:,0]))
print("Teleop Scores: " + str(results_matrix[:,1]))
print("Endgame Times: " + str(results_matrix[:,2]))
print("Penalties: " + str(results_matrix[:,3]))

averages = results_matrix.sum(axis=0) / len(results_matrix)
print("\nAverages: " + str(averages))
weighted_averages = averages * weights
print("Weighted Averages: " + str(weighted_averages))

weighted_averages[2] *= -1
weighted_averages[3] *= -1
total = weighted_averages.sum()
print("Total: " + str(total.round()) + "%")

# df = pd.DataFrame(np.flipud(np.rot90(results_matrix)), columns = ['Match #1','Match #2','Match #3', 'Match #4'])
# df.to_csv("test.csv")
