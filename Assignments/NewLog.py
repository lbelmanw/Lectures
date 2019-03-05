import numpy as np
import matplotlib.pyplot as plt           

class LogisticMap(object):

    def __init__(self, x=0.5, mu=3.2):

        self.x = x
        self.xList = [x]
        self.mu = mu
        self.muList = [mu]
            
    def map(self):
        
        self.x = self.mu * self.x * (1.0 - self.x)
        self.xList.append(self.x)
        self.muList.append(self.mu)
            
    def clear(self):
        self.xList = []
        self.muList = []
        
    def iterate(self, number=1000):
        for i in range(number): self.map()
                    
    def initialize(self, transient):
        # used to remove transient
            self.iterate(transient)
            self.clear()
            
    def lyapunov(self, number = 1000, transient = 100):
        lam = 0.0
        self.initialize(transient)
        self.iterate(number)
        xList_new = np.array(self.xList)
        
        for x in xList_new:
            lam += np.log(self.mu * abs(1.0 - 2.0 * x))
        
        return lam / len(xList_new)
                        