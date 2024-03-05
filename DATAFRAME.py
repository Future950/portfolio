import pandas as pd

# Creating a  dataframe to showcase the evolution of liquidity and gearing
data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Current Ratio': [2.5, 2.3, 2.1, 2.0, 1.8],
    'Debt-to-Equity Ratio': [0.4, 0.5, 0.6, 0.7, 0.8]
}

df = pd.DataFrame(data)
df