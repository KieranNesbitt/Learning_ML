import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import seaborn as sns
import timeit 
from functools import wraps
from time import time


square = np.array([#vertices of a square
    [0,0],[1,1],[1,0],[0,1]
          ])
radius = 1
centre_x, centre_y = 0,0

class Monte_carlo_pi:
    def timing(f):
        @wraps(f)
        def wrap(*args, **kw):
            ts = time()
            result = f(*args, **kw)
            te = time()
            print('func:%r args:[%r, %r] took: %2.4f sec' % \
            (f.__name__, args, kw, te-ts))
            return result
        return wrap
    def __init__(self,
                square: np.ndarray=np.array([#vertices of a square
    [0,0],[1,1],[1,0],[0,1]
          ]),
                 ):
            self.square = square
        #circle equation
            self.r = lambda x,y: np.sqrt((x-centre_x)**2 +(y - centre_y)**2) #standard circle equation
        #Monte-carlo 
 # samples to be used
    def calculate(self, N: int = 10000):

        self.N = N
        

        self.sample_coords= np.random.uniform(self.square[0][0],self.square[1][0], (2,self.N)) #
        
        self.radius_mask = self.r(self.sample_coords[0],self.sample_coords[1]) <=radius # Heart of the function, checks if coords are inside circle boundaries
        self.coords_outside = self.sample_coords[:, ~self.radius_mask]
        self.coords_inside = self.sample_coords[:, self.radius_mask]
        self.m = self.coords_inside.shape[1]
        
        return self.m/self.N * 4

    def plot(self):
        x_coord = [v[0] for v in square]
        y_coord = [v[1] for v in square]


        fig, ax = plt.subplots()
        ax.set_xlim(0,1)
        ax.set_ylim(0,1)

        from matplotlib.patches import Rectangle
        box_boundary = Rectangle((0,0), 1, 1, fill=False)
        ax.add_patch(box_boundary)

        ax.scatter(self.coords_outside[0],self.coords_outside[1], c="r", marker=".", label= "")
        ax.scatter(self.coords_inside[0], self.coords_inside[1], c= "b", marker= ".")
        circle = plt.Circle((centre_x, centre_y), radius, color='g', fill=False)
        ax.add_patch(circle)
        sns.despine(trim=True)

        plt.show()
    def print(self):
        print(f"Monte Carlo Calculated Pi: {self.m/self.N *4:.4f}")
        print(f"Expected Pi: {np.pi:.4f}")
        print(f"Error: {np.abs(np.pi -self.m/self.N * 4):.4f}")

find_pi = Monte_carlo_pi()
N_sample = np.linspace(100,1e6, 100, dtype= int)
v_func = np.vectorize(find_pi.calculate)
fig, ax = plt.subplots()
X = v_func(N_sample)
ax.scatter(N_sample, X, marker = ".")
ax.axhline(y=0, color='r', linestyle='-', label = f"{0:.4f}")
ax.set_xlabel("Number of Samples")
ax.set_ylabel(r"Estimate $\pi$")
plt.legend(loc="best", frameon=False)
sns.despine(trim=True)
plt.show()
