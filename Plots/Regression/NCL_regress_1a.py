"""
NCL_regress_1a.py
===============
This script illustrates the following concepts:
   - Calculating the least squared regression for a one dimensional array
   - Drawing a scatter plot with a regression line
   - Changing the size and color of markers
   - Calculate confidence interval statistics
See following URLs to see the reproduced NCL plot & script:
    - Original NCL script: https://www.ncl.ucar.edu/Applications/Scripts/regress_1.ncl
    - Original NCL plots: https://www.ncl.ucar.edu/Applications/Images/regress_1_lg.png
"""

###############################################################################
# Import packages

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


from geocat.viz import util as gvutil

###############################################################################
# Create data

# Data from original NCL file
x =  np.array([1190, 1455, 1550, 1730, 1745, 1770, 1900, 1920, 1960, 2295, 2335, 2490, 2720, 2710, 2530, 2900, 2760, 3010], dtype=float)
y =  np.array([1115, 1425, 1515, 1795, 1715, 1710, 1830, 1920, 1970, 2300, 2280, 2520, 2630, 2740, 2390, 2800, 2630, 2970], dtype=float)

###############################################################################
# Calculate regression

# Use numpy's polyfit to calculate a linear regression
# This function outputs [p, covariance], where p is in the form [a, b] and y = ax + b in the regression fit
[p, cov] = np.polyfit(x, y, 1, cov=True)
[a, b] = p

# Now that we have a y = ax + b, we can evaluate this model over a range,
# which will give us points to plot
x_space = np.linspace(int(min(x)), int(max(x)), 50)
y_regress = a * x_space + b

###############################################################################
# Calculate confidence intervals

# Set alpha value for a 95% confidence interval
alpha = 0.05

# Set statistics parameters from regression output
n = len(x)                      # number of observations
m = p.size                      # number of parameters
dof = n - m                     # degrees of freedom
t = stats.t.ppf(1-alpha, dof)   # t-value


# Error estimation
y_pred =  a * x + b                                 # predicted y values from model
residuals = y - y_pred
chi2 = np.sum((residuals / y_pred) ** 2) / dof
err_std = np.sqrt(np.sum(residuals**2) / dof)       # standard deviation of model error


# Calculate confidence interval
ci = t * err_std * np.sqrt(1/n + (np.mean(x_space))**2 / np.sum((x - np.mean(x_space)))**2)

###############################################################################
# First regression plot

# Generate figure (set its size (width, height) in inches) and axes
plt.figure(figsize=(6, 6))
ax = plt.gca()

# Plot original data
# Note that the s parameter sets the size of the markers in pts
s = plt.scatter(x, y, color='black', s=20)

# Plot regression
plt.plot(x_space, y_regress, color='black')

# Use geocat.viz.util convenience function to set axes parameters
gvutil.set_axes_limits_and_ticks(ax,
                                 xlim=(1190, 3010),
                                 xticks=np.arange(1200, 3010, 400),
                                 ylim=(900, 3000),
                                 yticks=np.arange(900, 3001, 300))

# Use geocat.viz.util convenience function to add minor and major tick lines
gvutil.add_major_minor_ticks(ax,
                             x_minor_per_major=4,
                             y_minor_per_major=3,
                             labelsize=12)

# Use geocat.viz.util convenience function to set titles and labels without calling several matplotlib functions
gvutil.set_titles_and_labels(ax,
                             maintitle="Brownlee Data",
                             xlabel="X",
                             ylabel="Y")

# Set clip on to false to allow plots to overlap axes instead of being clipped
s.set_clip_on(False)

# Show plot
plt.tight_layout()
plt.show()

###############################################################################
# Second regression plot with confidence interval

# Generate figure (set its size (width, height) in inches) and axes
plt.figure(figsize=(6, 6))
ax = plt.gca()

# Plot original data
# Note that the s parameter sets the size of the markers in pts
s = plt.scatter(x, y, color='black', s=20)

# Plot regression
plt.plot(x_space, y_regress, color='black')

# Plot confidence interval
plt.plot(x_space, y_regress - ci, x_space, y_regress + ci, color='cornflowerblue')


# Use geocat.viz.util convenience function to set axes parameters
gvutil.set_axes_limits_and_ticks(ax,
                                 xlim=(1190, 3010),
                                 xticks=np.arange(1200, 3010, 400),
                                 ylim=(800, 3600),
                                 yticks=np.arange(800, 3601, 400))

# Use geocat.viz.util convenience function to set titles and labels without calling several matplotlib functions
gvutil.set_titles_and_labels(ax,
                             maintitle="Brownlee Data",
                             xlabel="X",
                             ylabel="Y")

# Use geocat.viz.util convenience function to add minor and major tick lines
gvutil.add_major_minor_ticks(ax,
                             x_minor_per_major=4,
                             y_minor_per_major=4,
                             labelsize=12)

# Set clip on to false to allow plots to overlap axes instead of being clipped
s.set_clip_on(False)

# Show plot
plt.tight_layout()
plt.show()