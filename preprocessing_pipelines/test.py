import numpy as np
import mne
import sys
sys.path.append(".")

from preprocessing_pipelines.EEG_preprocessing import PreprocessingPipeline

filepath = '/Users/franklee/fyp/raw_csv/00000021_s004_t000.csv'

# Read the CSV file as a NumPy array
data = np.loadtxt(
    filepath, delimiter=',', skiprows=1)
data = np.transpose(data)

# Some information about the channels
ch_names = ['# EEG FP1-REF',
            'EEG FP2-REF',
            'EEG F3-REF',
            'EEG F4-REF',
            'EEG C3-REF',
            'EEG C4-REF',
            'EEG P3-REF',
            'EEG P4-REF',
            'EEG O1-REF',
            'EEG O2-REF',
            'EEG F7-REF',
            'EEG F8-REF',
            'EEG T3-REF',
            'EEG T4-REF',
            'EEG T5-REF',
            'EEG T6-REF',
            'EEG A1-REF',
            'EEG A2-REF',
            'EEG FZ-REF',
            'EEG CZ-REF',
            'EEG PZ-REF',
            'EEG ROC-REF',
            'EEG LOC-REF',
            'EEG EKG1-REF',
            'EEG T1-REF',
            'EEG T2-REF',
            'PHOTIC-REF',
            'IBI',
            'BURSTS',
            'SUPPR', ]  # TODO: finish this list

# Sampling rate of the Nautilus machine

sfreq = 500  # Hz

# Create the info structure needed by MNE
info = mne.create_info(ch_names, sfreq, 'eeg')

# Finally, create the Raw object
raw = mne.io.RawArray(data, info)

# Plot it!
# raw.plot()

events = mne.make_fixed_length_events(raw, start=5, stop=50, duration=2.)
event_id = None

# first we initialize the pipeline as a data container
pipeline = PreprocessingPipeline(raw,
                                 events,
                                 event_id,
                                 )
# now we preprocess the data step by step
pipeline.re_refernce()
pipeline.notch_filtering()
pipeline.filtering()
pipeline.epoching()
pipeline.mark_bad_channels()
pipeline.mark_bad_epochs()
pipeline.mark_bad_channels_for_each_epoch()
pipeline.fit_ica()
pipeline.mark_bad_ica_components_by_FASTER()
pipeline.detect_artifacts()
pipeline.apply_ica()
pipeline.final_step()
# clean_epochs = pipeline.clean_epochs
# for event_name, val in event_id.items():
#     evoked = clean_epochs[event_name].average()
#     evoked.plot_joint(title=event_name)
