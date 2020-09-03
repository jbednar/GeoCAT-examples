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
