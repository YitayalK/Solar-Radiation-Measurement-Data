import pandas as pd
import numpy as np
from scipy.stats import zscore
# Calculate Z-scores for all numeric columns
df_zscore = df.apply(zscore)

# Display the resulting DataFrame with Z-scores
print(df_zscore)