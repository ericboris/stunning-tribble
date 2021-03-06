"""HMM_Algorithms.py

by [Your name here]

date: [Your date here]

for CSE 473 Project Option 2, Autumn 2020
University of Washington

Provide your own implementations of the Forward algorithm and the Viterbi
algorithm in the provided function templates.

Your Forward algorithm should compute the belief vector B_t at each point t in
time. Here B_t(s) = P(S_t=s | E_1=e_1, E_2=e_2, ..., E_t=e_t). Here E_t
represents the emission at time step t. When show is True, it should display 
the belief values next to each of the nodes.

Your Viterbi algorithm should for each node compute the probability of reaching
that node from the start along the most probable path. When show is True, it
should display this probability next to each of the nodes, and it should
highlight the (or a) most probable path.
"""

import json

import hmm_vis as hv


class HMM:
    """ class that represents an HMM model with functions for the Forward and
        Viterbi algorithms """

    def __init__(self, filename=None):
        """ initialize parameters and other helper variables """
        self.S = None
        self.O = None
        self.P_trans = None
        self.P_emission = None
        if filename is not None:
            self.load_parameters(filename)
        # Add other instance variables you might need below.

    def load_parameters(self, filename):
        """ load HMM model parameters from JSON file """
        with open(filename, 'r') as f:
            parameters = json.load(f)
        self.S = parameters['S']
        self.O = parameters['O']
        self.P_trans = parameters['P_trans']
        self.P_emission = parameters['P_emission']

    def forward_algorithm(self, obs_sequence, show=False):

        if show:
            hv.show_entire_trellis(self.S, obs_sequence,
                                   has_initial_state=True)
            # Demo of node highlighting.
            hv.highlight_node(0, '<S>', highlight=True)
            # highlight/unhighlight other nodes as appropriate
            # to show progress.

        # Put your code implementing the Forward algorithm here. When 
        # debugging, use calls to highlight_node and show_node_label to 
        # illustrate the progress of your algorithm.

    def viterbi_algorithm(self, obs_sequence, show=False):
        if show:
            hv.show_entire_trellis(self.S, obs_sequence,
                                   has_initial_state=True)
            hv.highlight_node(0, '<S>')         # Demo of node highlighting.
            hv.highlight_edge(0, '<S>', 'M')    # Demo of edge highlighting.
            # highlight other nodes and edges as appropriate
            # to show progress and results.

        # Put your code implementing the Viterbi algorithm here. When 
        # debugging, use calls to highlight_node and show_node_label to 
        # illustrate the progress of your algorithm.


if __name__ == '__main__':
    sample_obs_seq = ['Jane', 'will', 'spot', 'Will']
    model = HMM('toy_pos_tagger.json')
    beliefs = model.forward_algorithm(sample_obs_seq, show=True)
    hv.hold()
    state_seq = model.viterbi_algorithm(sample_obs_seq, show=True)
    hv.hold()

