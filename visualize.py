from matplotlib import pyplot as plt
import numpy as np

def plot_graph(teams):
    plt.xlabel('Match')
    plt.ylabel('Score')

    for i in teams:
        x = []
        y = []
        avg = []
        team_name = i[0]
        team_data = i[1]
        print("Team "+team_name+"\n"+str(team_data))

        for match_num in range(0, len(team_data)):
            x.append(match_num)

            y.append(team_data[match_num][0])
            
            avg.append(np.nanmean(team_data[match_num][0]))

        plt.scatter(x, y, label=team_name)
        plt.legend(title="Team #")

    #plt.axhline(np.nanmean(avg), color="gray", alpha=0.3, label="Average")
    plt.savefig("test.png")
