import ieeg
import sys
import ieeg.auth
import numpy as np
import pandas as pd
s = ieeg.auth.Session('arevell', 'Zoro11!!')


ds = s.open_dataset('HUP138_phaseII')
channels = list(range(len(ds.ch_labels)))
data = ds.get_data(416023190000-300000000,300000000, channels)
416023190000-300000000
df = pd.DataFrame(data, columns=ds.ch_labels)
df.to_csv('data/HUP138_415723190000_300000000.csv', index=False, header=True, sep=',')
