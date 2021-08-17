from scipy.signal import medfilt
import pandas as pd
import numpy as np
import mne
import os

data_path = '/Users/franklee/fyp/Preprocessed data/malee23.set'  # change here only
raw =  mne.io.read_raw_eeglab(input_fname=data_path, preload=True, verbose=True)

filename = os.path.basename(data_path)

columns = raw.info['ch_names']
data = np.rot90(raw.get_data()).tolist()

os.chdir('csv')
path = os.path.join(os.getcwd(), filename);
pre, ext = os.path.splitext(path)

export_path = pre + '.csv'
pd.DataFrame(data, columns=columns).to_csv(export_path, index=False);