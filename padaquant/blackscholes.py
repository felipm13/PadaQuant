from scipy import log,exp,sqrt,stats

class blackscholes:
    def __init__(self, S, E, T, rf, sigma):
        self.S = S
        self.E = E
        self.T = T
        self.rf = rf
        self.sigma = sigma
        self.d1 = (log(self.S/self.E)+(self.rf+self.sigma*self.sigma/2.0)*self.T)/(self.sigma*sqrt(self.T))
        self.d2 = self.d1-self.sigma*sqrt(self.T)

    def get_call(self):
        return self.S*stats.norm.cdf(self.d1)-self.E*exp(-self.rf*self.T)*stats.norm.cdf(self.d2)

    def get_put(self):
        return -self.S*stats.norm.cdf(-self.d1)+self.E*exp(-self.rf*self.T)*stats.norm.cdf(-self.d2)
