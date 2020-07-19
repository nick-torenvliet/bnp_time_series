# the required python libraries imported
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from trcrpm import TRCRP_Mixture
from collections import Counter

data = pd.read_csv("/bnp_time_series/data/anomaly0245.csv", index_col=0)
data = data.iloc[156600:240000].reset_index(drop=True)

# Setup the placekeeping and initilizing variables
chain = 0
x, eng_val, states, num_states = [], [], [], []
i = 0
step = 20
print(i)

rng = np.random.RandomState(1)
model = TRCRP_Mixture(chains=1, lag=10, variables=data.columns, rng=rng)
model.incorporate(data[i:i + step])
model.resample_all(seconds=10)
model.resample_hyperparameters(seconds=10)
s = model.get_temporal_regimes('anomaly')[chain]
num_states = step * [len(sorted(set(s)))]
states = list(s[i:i + step])
eng_val = data.iloc[i:i + step, 0].tolist()
x = list(range(i, i + step ))

for i in range(step, len(data) - step, step):
    model.incorporate(data[i:i + step])
    model.resample_all(seconds=10)
    model.resample_hyperparameters(seconds=10)
    s = model.get_temporal_regimes("anomaly")[chain]
    num_states = step * [len(sorted(set(s)))]
    states = list(s[i:i + step])
    eng_val = data.iloc[i:i + step, 0].tolist()
    x = list(range(i, i + step ))
    print(i)