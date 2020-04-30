class Kalman:
    def __init__(self, R, Q):
        self.X = 0.0
        self.R = R
        self.Q = Q
        self.C = 0.0

    def Update(self, value):
        if (self.X == 0): 
            self.X = value
            self.C = self.Q
        else:    
            predX = self.X
            predCov = self.C + self.R
            K = predCov * (1 / (predCov + self.Q))
            self.X += K * (value - predX)
            self.C = predCov - (K * predCov)
        return self.X