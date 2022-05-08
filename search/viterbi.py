###############################################################################
# A HMM counting by Viterbi algorithm.
# Hidden states are health or fever, and observations are feelings
# normal, cold, dizzy
###############################################################################

from os import stat
from random import choice
from tkinter import W

states = ('Healthy', 'Fever')

observations = ('normal', 'cold', 'dizzy')

start_probability = {'Healthy': 0.6, 'Fever': 0.4}

transition_probability = {
    'Healthy': {
        'Healthy': 0.7,
        'Fever': 0.3
    },
    'Fever': {
        'Healthy': 0.4,
        'Fever': 0.6
    },
}

emission_probability = {
    'Healthy': {
        'normal': 0.5,
        'cold': 0.4,
        'dizzy': 0.1
    },
    'Fever': {
        'normal': 0.1,
        'cold': 0.3,
        'dizzy': 0.6
    },
}


def viterbi(obs, states, start_p, trans_p, emit_p):
    """
        return: (prob, path) viterbi path consist of hidden states
    """
    V = [{}]  # viterbi matrix N * T
    path = {}  # viterbi path of all current state

    for HSt in states:
        V[0][HSt] = start_p[HSt] * emit_p[HSt][obs[0]]
        path[HSt] = [HSt]

    for t in range(1, len(obs)):
        V.append({})
        new_paths = {}

        for Hst in states:
            tmp_probs = []
            for prev_Hst in states:
                tmp_probs.append((V[t - 1][prev_Hst] * trans_p[prev_Hst][Hst] *
                                  emit_p[Hst][obs[t]], prev_Hst))

            curr_prob, prev_state = max(tmp_probs)
            new_paths[Hst] = path[prev_Hst] + [Hst]
            V[t][Hst] = curr_prob

        path = new_paths
        
    prob, state = max([(V[len(obs) - 1][HSt], HSt) for HSt in states])
    return prob, path[state]



if __name__ == "__main__":
    L = 5
    obs = [choice(observations) for i in range(L)]

    prob, viterbi_path = viterbi(obs, states, start_probability,
                           transition_probability, emission_probability)

    print(obs)
    print(viterbi_path, "with prob: ", prob)