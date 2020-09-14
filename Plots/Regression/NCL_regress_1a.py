"""
NCL_regress_1a.py
===============
This script illustrates the following concepts:
   - Calculating the least squared regression for a one dimensional array
   - Drawing a scatter plot with a regression line
   - Changing the size and color of markers, thickness of line
See following URLs to see the reproduced NCL plot & script:
    - Original NCL script: https://www.ncl.ucar.edu/Applications/Scripts/regress_1.ncl
    - Original NCL plots: https://www.ncl.ucar.edu/Applications/Images/regress_1_lg.png
"""

###############################################################################
# Import packages

import numpy as np
import matplotlib.pyplot as plt

import geocat.datafiles as gdf
from geocat.viz import util as gvutil

###############################################################################
# Create data

# Data from original NCL file
x =  np.array([1190, 1455, 1550, 1730, 1745, 1770, 1900, 1920, 1960, 2295, 2335, 2490, 2720, 2710, 2530, 2900, 2760, 3010], dtype=float)
y =  np.array([1115, 1425, 1515, 1795, 1715, 1710, 1830, 1920, 1970, 2300, 2280, 2520, 2630, 2740, 2390, 2800, 2630, 2970], dtype=float)

