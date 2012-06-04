import Image
from copy import copy
from time import sleep
from pylab import *


plot_dic={'cmap':cm.gray,'interpolation':'nearest'}

tmax = 50

class hopfield_network:
    def __init__(self,N):
        self.N = N
        """
        DEFINITION
        initialization of the class

        INPUT
        N: size of the network, i.e. if N=10 it will consists of 10x1 pixels

        -L.Ziegler 03.2009.
        """

    def make_pattern(self,P=1,ratio=0.5):
        self.pattern = -ones([P,self.N], int)
        idx = int(ratio*self.N)
        for i in range(P):
            self.pattern[i,:idx] = 1
            self.pattern[i] = permutation(self.pattern[i])
        self.weight = zeros((self.N,self.N))
        for i in range(self.N):
            for j in range(self.N):
                if i == j:
                    self.weight[i,j] = 0
                else:
                    self.weight[i,j] = 1./self.N*sum(self.pattern[k,i]*self.pattern[k,j] for k in range(self.pattern.shape[0]))
    
    def dynamic(self):
        """
        DEFINITION
        executes one step of the dynamics

        -L.Ziegler 03.2009.
        """
        for i in range(self.N):
            h = sum(self.weight[i,j]*self.x[j] for j in range(self.N))
            if h >= 0:
                self.x[i] = 1
            else:
                self.x[i] = -1
				
    def overlap(self,mu):
        """
        DEFINITION
        computes the overlap of the test pattern with pattern nb mu

        INPUT
        mu: the index of the pattern to compare with the test pattern

        -L.Ziegler 03.2009.
        """
        return 1./self.N*sum(self.pattern[mu]*self.x)
		

    def energy(self,mu):
		"""
		DEFINITION
		computes the energy of the test pattern with pattern nb mu

		INPUT
		mu: the index of the pattern to compare with the test pattern

		-L.Ziegler 03.2009.
		"""
		
		return -sum(sum(self.weight[i,j]*self.x[i]*self.x[j] for j in range(self.N)) for i in range(self.N))
		
		
    def run(self,mu=0,flip_ratio=0.1):
        """
        DEFINITION
        runs the dynamics and plots it in an awesome way
        
        INPUT
        mu: pattern number to use as test pattern
        flip_ratio: ratio of flipped pixels
                    ex. for pattern nb 5 with 5% flipped pixels use run(mu=5,flip_ratio=0.05)
        
        -L.Ziegler 03.2009.
        -N.Fremaux 03.2010.
        """
        
        try:
            self.pattern[mu]
        except:
            raise IndexError, 'pattern index too high'
        
        # set the initial state of the net
        self.x = copy(self.pattern[mu])
        flip = permutation(arange(self.N))
        idx = int(self.N*flip_ratio)
        self.x[flip[0:idx]] *= -1
        t = [0]
        #energy = [self.energy(mu)]
        overlap = [self.overlap(mu)]
          

        x_old = copy(self.x)
        
        for i in range(tmax):

            # run a step
            self.dynamic()
            t.append(i+1)
            overlap.append(self.overlap(mu))
            #energy.append(self.energy(mu))

            # check the exit condition
            i_fin = i+1
            if sum(abs(x_old-self.x))==0:
                break
            x_old = copy(self.x)
            
        #print 'pattern recovered in %i time steps with final overlap %.3f'%(i_fin,overlap[-1])
        
        return 100-100*(overlap[-1]+1)/2
