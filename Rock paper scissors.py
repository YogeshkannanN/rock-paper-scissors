from __future__ import division
import random
import itertools

beat = {'R': 'P', 'P': 'S', 'S': 'R'}


class MarkovChain():...


class RandomPredictor():...


# the first round
if input == '':

    random_predictor = RandomPredictor()
    markov_model = MarkovChain(1, 0.9)

    pair_diff2 = ''
    pair_diff1 = ''


# further rounds
else:
    pair_diff2 = pair_diff1
    pair_diff1 = output + input


if pair_diff2 != '':
    markov_model.update_matrix(pair_diff2, input)
    output = beat[markov_model.predict(pair_diff1)]

else:
    output = random_predictor.predict()