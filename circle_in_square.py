#Testing monte-carlo for finding the area of an unknown circle within the boundary of a square
#Numpy was used to avoid for loops in python
#Improvements to be done: 
    ##Diminishing returns past 4000 samples for this situation
    ###Will look into how to improve this


import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import seaborn as sns
import pandas as pd
sns.set_context("paper")
sns.set_style("ticks")

#Setting up Square boundaries
square = np.array([#vertices of a square
    [-1,-1],[1,1],[-1,1],[1,-1]
          ])
area_square = 4
#pick a random radius of the circle and find theortical area
radius = np.random.uniform(0,1)
centre_x, centre_y = 0,0
area_circle = np.pi*radius**2

class Monte_carlo_square:
    def __init__(self, 
                square: np.ndarray =np.array([[-1,-1],[1,1],[-1,1],[1,-1]]),
                 ):
        self.square = square
        #circle equation
        self.r = lambda x,y: np.sqrt((x-centre_x)**2 +(y - centre_y)**2) #standard circle equation
        #Monte-carlo 
 # samples to be used
    def find_Area(self,                
                  N: int=10000
                    ):
        self.N = N
        self.sample_coords= np.random.uniform(self.square[0][0],self.square[1][0], (2,self.N)) #
        self.radius_mask = self.r(self.sample_coords[0],self.sample_coords[1]) <=radius # Heart of the function, checks if coords are inside circle boundaries
        self.coords_outside = self.sample_coords[:, ~self.radius_mask]
        self.coords_inside = self.sample_coords[:, self.radius_mask]
        self.m = self.coords_inside.shape[1]
        return self.m/self.N *area_square
    def print(self):
        print(f"Monte Carlo Area: {self.m/self.N *area_square:.4f}")
        print(f"Expected Area: {area_circle:.4f}")
        print(f"Error: {np.abs(area_circle -self.m/self.N *area_square):.4f}")
    def plot(self):
        x_coord = [v[0] for v in square]
        y_coord = [v[1] for v in square]


        fig, ax = plt.subplots()

        from matplotlib.patches import Rectangle
        box_boundary = Rectangle((-1,-1), 2, 2, fill=False)
        ax.add_patch(box_boundary)

        ax.scatter(self.coords_outside[0],self.coords_outside[1], c="r", marker=".", label= "")
        ax.scatter(self.coords_inside[0], self.coords_inside[1], c= "b", marker= ".")
        circle = plt.Circle((centre_x, centre_y), radius, color='g', fill=False)
        ax.add_patch(circle)
        sns.despine(trim=True)

        plt.show()

Monte = Monte_carlo_square()
#Do Monte.plot() to show the last area calculated
N_sample = np.random.randint(100,10000,1000)
v_func = np.vectorize(Monte.find_Area)
fig, ax = plt.subplots()

X = v_func(N_sample)
ax.scatter(N_sample, X)
ax.axhline(y=area_circle, color='r', linestyle='-', label = f"Expected Area of Circle: {area_circle:.4f}")
ax.set_xlabel("Number of Samples")
ax.set_ylabel("Calculated Sample Area")
plt.legend(loc="best", frameon=False)
sns.despine(trim=True)
plt.show()
