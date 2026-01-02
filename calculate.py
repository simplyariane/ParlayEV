import math

def convertOdds(odds):
    if odds > 0:
        return 100 / (odds + 100)
    else:
        return abs(odds) / (abs(odds) + 100)

def removeVig(over, under):
    
    percentOver = convertOdds(over)
    percentUnder = convertOdds(under)
    
    totalOdds = percentOver + percentUnder
    trueOver = percentOver / totalOdds
    trueUnder = percentUnder / totalOdds
    return trueOver, trueUnder

def evCheck(trueOver, trueUnder):
    if trueOver > 0.5414:
        print(f"Positive EV; {trueOver - 0.5414:.2%} edge")
    if trueUnder > 0.5414:
        print(f"Positive EV; {trueUnder - 0.5414:.2%} edge")