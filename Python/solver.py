
"""
Implements least-squares curve fitting.
@author: J.M.C.Tas
"""

from scipy import optimize

class Parameter:
    
    def __init__(self, value):
        self.value = value

    def set(self, value):
        self.value = value

    def __call__(self):
        return self.value
	
    def __repr__(self):
	msg = ("{}(value={value})")
	return msg.format(self.__class__.__name__,**vars(self))

def fit(func, parameters, y, x = None):
    
    def f(params):
        i = 0
        for p in parameters:
            p.set(params[i])
            i += 1
        return y - func(x)

    if x is None: x = np.arange(y.shape[0])
    p = [param() for param in parameters]
    optimize.leastsq(f, p)


