from matplotlib import pyplot as plt
import numpy as np

from models import MatchValues

# Scatter plot of a score
def plot_graph(teams, match_value):
    fig, ax = plt.subplots()

    ax.set_xlabel('Match')
    ax.set_ylabel(match_value.name)

    for i in teams: # loop through each team given
        x = []
        y = []
        avg = []
        team_name = i[0] # separate team name & data from tuple
        team_data = i[1]

        print("Team "+team_name+"\n"+str(team_data))

        for match_num in range(0, len(team_data)): # go through each match the team has
            x.append(match_num)

            y.append(team_data[match_num][match_value.value])
            
            avg.append(np.nanmean(team_data[match_num][match_value.value]))

        ax.scatter(x, y, label=team_name)
        ax.legend(title="Team #")
    ax.set_title(match_value.name)

    #plt.axhline(np.nanmean(avg), color="gray", alpha=0.3, label="Average")

# Bar graph of the actual scores of each team
def score_graph(teams):
    fig, ax = plt.subplots()

    team_numbers = []
    scores = []
    colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange'] # TODO: make this non-hardcoded

    for i in teams: # Just go through the scores ig
        team_numbers.append(i[0])
        scores.append(i[1].round())

    ax.bar(team_numbers, scores, label=team_numbers, color=colors)
    ax.set_ylabel('Score %')
    ax.set_title('Team Scores')

    plt.show()
