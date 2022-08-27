from scipy import optimize
from scipy.optimize import Bounds

def obj(x):
    return (x[0] - x[1])**2 + (x[1] + x[2] - 2)**2 + (x[3] - 1)**2 + (x[4] - 1)**2

def cont1(x):
    return x[0] + 3*x[1]

def cont2(x):
    return x[2] + x[3] - 2*x[4]

def cont3(x):
    return x[1] - x[4]

bnds = ((-10, 10), (-10, 10), (-10, 10), (-10, 10), (-10, 10))

const = ({'type': 'eq', 'fun': cont1},
         {'type': 'eq', 'fun': cont2},
         {'type': 'eq', 'fun': cont3})

x0 = [0, 0, 0, 0, 0]

res = optimize.minimize(obj, x0, bounds=bnds, constraints=const)

print(res)
