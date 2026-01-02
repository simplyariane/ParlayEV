import math

def convertOdds(odds):
    if odds > 0:
        return 100 / (odds + 100)
    else:
        return abs(odds) / (abs(odds) + 100)

def removeVig(over, under):
    #ds3