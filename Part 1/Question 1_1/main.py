#!/usr/bin/env python

import hopfield

# Q1.1 given parameters
N = 200
P = 5
c = 0.2

# Initialization of the Hopfield network
network = hopfield.hopfield_network(N)
network.make_pattern(P)

network.run(0,c)




