from scipy.signal import medfilt

import mne

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import (train_test_split, StratifiedKFold)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from mne_features.feature_extraction import FeatureExtractor


def compute_medfilt(arr):
    """Median filtered signal as features.

    Parameters
    ----------
    arr : ndarray, shape (n_channels, n_times)

    Returns
    -------
    output : (n_channels * n_times,)
    """
    return medfilt(arr, kernel_size=(1, 5)).ravel()

# print(__doc__)

data_path = '/Users/franklee/fyp/Preprocessed data/malee23.set'


raw_fname = data_path
event_fname = data_path
tmin, tmax = -0.2, 0.5

# Setup for reading the raw data
raw =  mne.io.read_raw_eeglab(input_fname=data_path, preload=True, verbose=True)

events, event_ids = mne.events_from_annotations(raw)
# print(raw.info)
# print(type(list(event_ids.items())))
# print(f"{events=}\n");

picks = mne.pick_types(raw.info, meg=False, eeg=True)

raw.filter(.5, None, fir_design='firwin')
# raw.plot();
# print(f"{raw=}\n")
# print(f"{events=}]\n")
# print(f"{picks=}")


# Read epochs
epochs = mne.Epochs(raw, events, event_ids, tmin, tmax, picks=picks, proj=True,
                    baseline=None, preload=True, event_repeated='merge')

# print(f"{epochs=}\n")   # uncomment to see Epochs output
labels = epochs.events[:, -1]

# get MEG and EEG data
data = epochs.get_data()

# Prepare for the classification task

selected_funcs = [('medfilt', compute_medfilt), 'mean']

pipe = Pipeline([('fe', FeatureExtractor(sfreq=raw.info['sfreq'],
                                         selected_funcs=selected_funcs)),
                 ('scaler', StandardScaler()),
                 ('clf', LogisticRegression(random_state=42, solver='lbfgs'))])
skf = StratifiedKFold(n_splits=3, random_state=42, shuffle=True)
y = labels

# Print the accuracy score on a dataset.

X_train, X_test, y_train, y_test = train_test_split(data, y, test_size=0.2)
accuracy = pipe.fit(X_train, y_train).score(X_test, y_test)
print('Accuracy score = %1.3f' % accuracy)