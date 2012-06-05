#!/usr/bin/env python

import hopfield
from pylab import *

# Experiment parameters
N = 200     # Run tests for 100, 250 and 500
c = 0.1

# Initialization of the Hopfield network
network = hopfield.hopfield_network(N)

# Test parameters
maxTests = 10
maxE = 10
detectionFlag = False

# Initialize plot data
x_axis = range(maxE+1)
mean = zeros(maxE+1)
error = zeros(maxE+1)
buffer = zeros(maxTests)

# Plot initialization
figure()
axis([0,maxE,0.00,0.20])
xlabel('10*E')
ylabel('alpha_max')

# Run tests for several values of pcut
for E in range(maxE+1):

    # Run several tests to determine network mean capacity
    for i in range(maxTests):
        
        # Create first pattern
        P = 1
        network.make_pattern(P, 0.5, 1.0*E/10)
        
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
                # print capacity
                break
            
        print '.'
        buffer[i] = capacity
        mean[E] += capacity / maxTests
            
    # Determine error (95% confidence interval) from the buffer
    error[E] = 1.96*std(buffer)/sqrt(maxTests)
    
    # Display results for this value of pcut
    print 'E = %i percent  |  alpha_max = %f  |  confidence interval : +/- %f'%(E*10, mean[E], error[E])
    
    # Warning message if alpha is below 0.50*alpha_max for the first time
    if mean[E] < 0.07 and detectionFlag == False:
        print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
        detectionFlag = True
    
# Plot data
plot(x_axis, mean, 'g', lw=2)
errorbar(x_axis, mean, yerr=error, fmt='ro')

# Show plot
show()


    

