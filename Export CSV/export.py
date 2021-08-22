import pandas as pd
import numpy as np
import mne
import os


directory = r'/Users/franklee/fyp/Preprocessed data'

for filename in os.listdir(directory):
    if filename.endswith(".set"):
        data_path = os.path.join(directory, filename)
        raw =  mne.io.read_raw_eeglab(input_fname=data_path, preload=True, verbose=True)

        columns = raw.info['ch_names']
        data = np.rot90(raw.get_data()).tolist()

        if(os.path.isdir('./csv')):
            os.chdir('csv')

        path = os.path.join(os.getcwd(), filename);
        pre, ext = os.path.splitext(path)

        export_path = pre + '.csv'
        pd.DataFrame(data, columns=columns).to_csv(export_path, index=False);
    else:
        continue
