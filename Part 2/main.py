#!/usr/bin/env python

import hopfield
from pylab import *

# Experiment parameters
N = 400     # Run tests for 100, 250 and 500
c = 0.1

# Initialization of the Hopfield network
network = hopfield.hopfield_network(N)

# Test parameters
maxTests = 10

# Test data
buffer = zeros(maxTests)
mean = 0

# Run several tests to determine network mean capacity
for i in range(maxTests):
    
    # Create first pattern
    P = 1
    network.make_pattern(P)
    
    # Successively add patterns until a retrieval error higher than 2 is reached
    while True:
        avg = 0
        P += 1
        
        # Add a new pattern
        network.create_pattern()
        
        # Average the retrieval error over all stored patterns
        for mu in range(P):
            avg += network.run(mu,c) / P
            
        # If a retrieval error average is above 2, stop the simulation
        if avg > 2:
            capacity = 1.0*P / N
            print capacity
            break
        
    buffer[i] = capacity
    mean += capacity / maxTests
        
# Determine error (95% confidence interval) from the buffer
error = 1.96*std(buffer)/sqrt(maxTests)
    
print 'alpha_max = %f  |  confidence interval : +/- %f'%(mean, error)
    

