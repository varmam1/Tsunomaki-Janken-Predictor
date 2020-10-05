import numpy as np
import pandas as pd
import random

def generateFirstOrderMarkov(data):
    """
    Given a list of the past moves of RPS, generate a transition matrix for it.

    Args:
        data: A list of strings of R, P, S, or O for other (List[String])

    Returns:
        A dictionary mapping the last move to a dictionary which maps the possible moves to their probabilities
            (String -> (String -> float))
    """
    return pd.crosstab(pd.Series(data[1:],name='LastMove'),pd.Series(data[:-1],name='NextMove'),normalize=1).to_dict()

def rpsMarkovModel(data):
    """
    Returns the proper markov model in case of future development with higher order Markov models

    Args:
        data: a list of the past moves that were done (List[String])

    Returns:
        A dictionary mapping the last move to a dictionary which maps the possible moves to their probabilities
            (String -> (String -> float))
    """
    return generateFirstOrderMarkov(data)

def prediction(lastMove, model):
    """
    Given the Markov model and the last move that was done, predicts the next move 

    Args:
        lastMove: A string which has what the last move played was. (String)
        model: A dictionary mapping the last move to a dictionary which maps the possible moves to their probabilities
            (String -> (String -> float))

    """
    return random.choices(list(model[lastMove].keys()), weights=model[lastMove].values())[0]
