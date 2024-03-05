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
imf_hdci_scores = np.array([1, 1, 1, 2, 1, np.nan, 1, 1, 1, 1, 1, 1, 2, np.nan, 3, 1, 1, np.nan, np.nan, np.nan, np.nan, np.nan, 3, np.nan, 1, np.nan, np.nan, 1, 1, 2, 1])
orif_hdci_scores = np.array([1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, np.nan, 2, 1, 1, np.nan, np.nan, np.nan, 3, np.nan, 1, np.nan, 1, np.nan, np.nan, 3, 1])

# Remove NaN values
imf_hdci_scores = imf_hdci_scores[~np.isnan(imf_hdci_scores)]
orif_hdci_scores = orif_hdci_scores[~np.isnan(orif_hdci_scores)]

# Perform t-test
t_statistic, p_value = ttest_ind(imf_hdci_scores, orif_hdci_scores)

# Print results
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")