import Image
from copy import copy
from time import sleep
from pylab import *

plot_dic={'cmap':cm.gray,'interpolation':'nearest'}

tmax = 30

class hopfield_network:
    def __init__(self,N):
        self.N = N
        """
        DEFINITION
        initialization of the class

        INPUT
        N: size of the network, i.e. if N=10 it will consists of 10x10 pixels

        -L.Ziegler 03.2009.
        """

    def make_pattern(self,P=1,ratio=0.5):
        """
        DEFINITION
        creates and stores patterns

        INPUT
        P: number of patterns (used only for random patterns)
        ratio: percentage of 'on' pixels for random patterns
        letters: to store characters use as input a string with the desired letters
            ex. make_pattern(letters='abcdjft')

        -L.Ziegler 03.2009.
        """

        # Modifications : changed size of the network from N**2 to N, and nullify the diagonal of the weight matrix.
        
        # Create patterns
        self.pattern = -ones((P,self.N),int)
        idx = int(ratio*self.N)
        for i in range(P):
            self.pattern[i,:idx] = 1
            self.pattern[i] = permutation(self.pattern[i])
            
        # Calculate new weight matrix
        self.weight = zeros((self.N,self.N))
        for i in range(self.N):
            for j in range(self.N):
                if i != j:
                    self.weight[i,j] = 1./self.N * sum(self.pattern[k,i]*self.pattern[k,j] for k in range(self.pattern.shape[0]))



    def create_pattern(self,ratio=0.5):
        """
        DEFINITION
        creates a nes pattern and adds it at the end of the self.pattern matrix

        INPUT
        P: number of patterns (used only for random patterns)
        ratio: percentage of 'on' pixels for random patterns
        letters: to store characters use as input a string with the desired letters
            ex. make_pattern(letters='abcdjft')

        -L.Masson 06.2012.
        """

        # Increase size of the self.pattern matrix and initialize all values to -1
        self.pattern = np.append(self.pattern, -ones([1,self.N], int), axis=0)

        # Create a new pattern
        idx = int(ratio*self.N)
        self.pattern[len(self.pattern)-1,:idx] = 1
        self.pattern[len(self.pattern)-1] = permutation(self.pattern[len(self.pattern)-1])
            
        # Calculate new weight matrix
        self.weight = zeros((self.N,self.N))
        for i in range(self.N):
            for j in range(self.N):
                if i != j:
                    self.weight[i,j] = 1./self.N * sum(self.pattern[k,i]*self.pattern[k,j] for k in range(self.pattern.shape[0]))




    def dynamic(self):
        """
        DEFINITION
        executes one step of the dynamics

        -L.Ziegler 03.2009.
        """

        # Modifications : all nodes updated sequentially instead of simultaneously, dot() function used
        for i in range(self.N):
            #h = sum(self.x[k]*self.weight[i,k] for k in range(self.N) )
            h = np.dot( self.x, self.weight[i,:] )
            self.x[i] = 1;
            if h < 0:
                self.x[i] = -1;



    def overlap(self,mu):
        """
        DEFINITION
        computes the overlap of the test pattern with pattern nb mu

        INPUT
        mu: the index of the pattern to compare with the test pattern

        -L.Ziegler 03.2009.
        """

        # Modifications : 1/N instead of 1/N^2, dot() function used
        #return 1./self.N*sum(self.pattern[mu]*self.x)
        return 1./self.N*np.dot(self.pattern[mu], self.x)
    

    def energy(self,mu):
        """
        DEFINITION
        computes the energy of the test pattern with pattern nb mu

        INPUT
        mu: the index of the pattern to compare with the test pattern

        -L.Masson 05.2012.
        """

        return -sum( sum(self.x[i]*self.x[j]*self.weight[i,j] for j in range(self.N)) for i in range(self.N) )
    
    

    def run(self,mu=0,flip_ratio=0):
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
        
        # Modifications : all 1/N^2 terms changed to 1/N
        
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
        overlap = [self.overlap(mu)]
        #energy = [self.energy(mu)]
        
        """
        # prepare the figure
        figure()
        
        # plot the time course of the energy
        subplot(211)
        g1, = plot(t,energy,'k',lw=2) # we keep a handle to the curve
        axis([0,tmax,-1000,0])
        xlabel('time step')
        ylabel('energy')
        
        # plot the time course of the overlap
        subplot(212)
        g2, = plot(t,overlap,'k',lw=2) # we keep a handle to the curve
        axis([0,tmax,-1,1])
        xlabel('time step')
        ylabel('overlap')
        
        # this forces pylab to update and show the fig.
        draw()
        """
        x_old = copy(self.x)
        
        for i in range(tmax):

            # run a step
            self.dynamic()
            t.append(i+1)
            overlap.append(self.overlap(mu))
            #energy.append(self.energy(mu))
            
            # update the plotted data
            """
            g1.set_data(t,energy)
            g2.set_data(t,overlap)
            
            # update the figure so that we see the changes
            draw()
            """

            # check the exit condition
            i_fin = i+1
            if sum(abs(x_old-self.x))==0:
                break
            x_old = copy(self.x)
            
            #sleep(0.5)
        
    
        # Return the normalized pixel distance
        # print '%.3f'( 100.*(1-(overlap[-1]+1)/2) )
        return 100.*(1-(overlap[-1]+1)/2)



class alphabet():
    def __init__(self):
        """
        DEFINITION
        loads the gif files in alphabet/ and stores them as arrays of length 10x10

        -L.Ziegler 03.2009.
        """

        for i in 'abcdefghijklmnopqrstuvwyxz':
            im = Image.open('alphabet/'+i+'.gif')
            pix = array(list(im.getdata()))
            self.__dict__[i]= sign(pix-1)
