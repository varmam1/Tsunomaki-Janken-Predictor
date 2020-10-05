import numpy as np
import pandas as pd

def generateFirstOrderMarkov(data):
    """
    Given a list of the past moves of RPS, generate a transition matrix for it.

    Input: A list of strings of R, P, S, or O for other

    Output: A dictionary to a dictionary to a probability
    """
    return pd.crosstab(pd.Series(data[1:],name='LastMove'),pd.Series(data[:-1],name='NextMove'),normalize=1).to_dict()

def rpsMarkovModel(data):
    return generateFirstOrderMarkov(data)

def prediction(move, model):
    return 0

print(rpsMarkovModel(["R", "P", "S", "P", "R", "P", "S", "R", "R", "P"]))