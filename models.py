import time
from numpy import array
from enum import Enum

class MatchResult():
    rank = 0.0 # ranking score
    ranks = []

    def __init__(self, match_num, team_num, auto_score, teleop_score, endgame_time, penalty):
        self.match_num = match_num # Increasing number for each match
        self.team_num = team_num # The team ID scouted
        self.auto_score = auto_score # points scored in auto mode
        self.teleop_score = teleop_score # points scored in teleop mode
        self.endgame_time = endgame_time # mm:ss
        self.penalty = penalty # penalties the team had

    def __str__(self):
        return "Match #" + str(self.match_num) + " Team #" + str(self.team_num)

    def results(self):
        return "Results -\nMatch #" + str(self.match_num) + "\nTeam #" + str(self.team_num) + "\nAuto Score: " + str(self.auto_score) + "\nTeleop Score: " + str(self.teleop_score) + "\nEndgame Time: " + "\nPenalty: " + str(self.penalty)

    def array(self):
        return array([self.auto_score, self.teleop_score, self.endgame_time, self.penalty])

class MatchValues(Enum):
    AutoScore = 0
    TeleopScore = 1
    EndgameTime = 2
    Penalties = 3
