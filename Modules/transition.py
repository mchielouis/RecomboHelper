import numpy as np

class Transition(object):
    """A class describing an association of two Topologies"""
    def __init__(self, from_topo = None, to_topo = None, n_transitions = 0, 
                 percent = 0, partner = None, visited = False):
        self.from_topo = from_topo
        self.to_topo = to_topo
        self.n_transitions = n_transitions
        self.transition_vector = []
        self.transition_counter = 0 #temp, only used in the parse function
        #Ratio Estimation Confidence Interval
        self.percent = percent
        self.reci = None
        #for graph algorithms
        self.partner = partner
        self.visited = visited
        return super(Transition, self).__init__()

    def compute_reci(self):
        #change of variables
        n = float(len(self.from_topo.topo_vector))
        x = self.from_topo.topo_vector
        y = self.transition_vector

        def getVar(x): #sample variance
            #var = ((n*mean)/(n-1))*(1-mean)
            #return var
            return np.var(x,ddof=1)

        def getCovar(x,y):
            return np.cov(x,y,ddof=1)[0][1] #scalar sample covariance

        def getCsaon(alpha, n):
            csaon = ((1-alpha)**2)/n
            return csaon

        def getThetaTilde(xbar,ybar,xvar,yvar,covar):
            if ybar == 0.0:
                return 0.0
            #if ybar != 0
            thetaTilde = (ybar/xbar)*(1+(1/n)*((covar/(xbar*ybar))-(xvar/(xbar**2))))
            return thetaTilde
    
        #main method
        def computeCIs():
            #alpha is the significance level for the confidence intervals
            alpha = .05
            xbar = np.mean(x)
            ybar = np.mean(y)
            xvar = getVar(x)
            yvar = getVar(y)
            covar = getCovar(x,y)
            csaon = getCsaon(alpha,n)
            lowerBound = (xbar*ybar-csaon*covar-((xbar*ybar-csaon*covar)**2-(xbar**2-csaon*xvar)*(ybar**2-csaon*yvar))**.5)/(xbar**2-csaon*xvar)
            upperBound = (xbar*ybar-csaon*covar+((xbar*ybar-csaon*covar)**2-(xbar**2-csaon*xvar)*(ybar**2-csaon*yvar))**.5)/(xbar**2-csaon*xvar)
            result = repr(lowerBound) + '-' + repr(getThetaTilde(xbar,ybar,xvar,yvar,covar)) + '-' + repr(upperBound)
            return result
            
            
        self.reci = computeCIs()




