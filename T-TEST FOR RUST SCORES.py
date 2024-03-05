# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Get started with interactive Python!
# Supports Python Modules: builtins, math,pandas, scipy 
# matplotlib.pyplot, numpy, operator, processing, pygal, random, 
# re, string, time, turtle, urllib.request
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp
from scipy.stats import ttest_ind
import numpy as np

# Data
imf_rust_scores = np.array([3, 3, 3, 3, 3, 3, 3, np.nan, 4, 3, 4, 4, 3, 3, 3, 4, 4, 4, 3, np.nan, 3, 3, 4, np.nan, np.nan, np.nan, 4, np.nan, 3, np.nan])
orif_rust_scores = np.array([4, 4, 4, 4, 4, np.nan, 4, 4, 4, 4, 4, 4, 4, 4, 4, np.nan, 4, 4, np.nan, 4, 4, 4, 4, np.nan, np.nan, np.nan, 4, np.nan, 4, 4])

# Remove NaN values
imf_rust_scores = imf_rust_scores[~np.isnan(imf_rust_scores)]
orif_rust_scores = orif_rust_scores[~np.isnan(orif_rust_scores)]

# Perform t-test
t_statistic, p_value = ttest_ind(imf_rust_scores, orif_rust_scores)

# Print results
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")