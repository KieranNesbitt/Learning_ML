import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as st
bar_ends: list[int] = [0.0, 1.0]
expected_segments: int = 100
material_encoding: tuple[int] = (0,1)
# Creating a distribution that represents the possible segemnts of the bar
segments = st.poisson(mu =expected_segments)

#Next will need to create a distrbiution that represents the possible coordinates of the segements
# This is a sorted uniform distribution between 0 and 1, representing the possible coordinates of the segments
#However, the end coordinates are known so we need [0, 1] to be included in the distribution
x_coord = np.hstack([[bar_ends[0]], 
                     np.sort(np.random.uniform(0, 1, 100)), 
                     [bar_ends[1]]])
