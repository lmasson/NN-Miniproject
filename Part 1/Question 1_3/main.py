#!/usr/bin/env python

import hopfield
from pylab import *

# Q1.3 given parameters
N = 200
c = 0.1

# Initialization of the Hopfield network
network = hopfield.hopfield_network(N)

# Test parameters
maxPatterns = 3
maxTests = 3

# Initialize plot data
x_axis = range(maxPatterns)+ones(maxPatterns)
mean   = zeros(maxPatterns)
error  = zeros(maxPatterns)
buffer = zeros(maxTests)

# Plot initialization
figure()
axis([1,maxPatterns,-5,25])
xlabel('Nb. of patterns')
ylabel('Retrieval error [ % ]')

# Run tests several numbers of patterns P
for P in range(maxPatterns):
    
    # Run tests several times for a given P
    for i in range(maxTests):
        network.make_pattern(P+1)
        buffer[i] = network.run(0,c)
        mean[P] += 1.96*buffer[i]/maxTests
        
    # Determine error (95% confidence interval) from the buffer
    error[P] = std(buffer)/sqrt(maxTests)
    

plot(x_axis, mean, 'g', lw=2)
errorbar(x_axis, mean, yerr=error, fmt='ro')



show()



