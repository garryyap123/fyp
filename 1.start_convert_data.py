import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import os
from os import walk
import time

def readFile(name):

    print("READING FILE " + name)

    df = pd.read_csv(
        name, skiprows=1)

    # Drop last 4 columns
    df.drop(columns=df.columns[-4:],
            axis=1,
            inplace=True)

    name = {
        '# EEG FP1-REF': 'FP1',
        'EEG FP2-REF': 'FP2',
        'EEG F3-REF': 'F3',
        'EEG F4-REF': 'F4',
        'EEG C3-REF': 'C3',
        'EEG C4-REF': 'C4',
        'EEG P3-REF': 'P3',
        'EEG P4-REF': 'P4',
        'EEG O1-REF': 'O1',
        'EEG O2-REF': 'O2',
        'EEG F7-REF': 'F7',
        'EEG F8-REF': 'F8',
        'EEG T3-REF': 'T3',
        'EEG T4-REF': 'T4',
        'EEG T5-REF': 'T5',
        'EEG T6-REF': 'T6',
        'EEG A1-REF': 'A1',
        'EEG A2-REF': 'A2',
        'EEG FZ-REF': 'FZ',
        'EEG CZ-REF': 'CZ',
        'EEG PZ-REF': 'PZ',
        'EEG ROC-REF': 'ROC',
        'EEG LOC-REF': 'LOC',
        'EEG EKG1-REF': 'EKG1',
        'EMG-REF': 'EMG',
        'EEG 26-REF': '26',
        'EEG 27-REF': '27',
        'EEG 28-REF': '28',
        'EEG 29-REF': '29',
        'EEG 30-REF': '30',
        'EEG T1-REF': 'T1',
        'EEG T2-REF': 'T2'
    }

    print("READING FILE COMPLETED ")

    return df.rename(columns=name)


def processData():
    global signal_electrodes

    # row layer
    for index, row in df.iterrows():

        # column layer
        for (index, value) in row.iteritems():
            if(index in signal_electrodes):
                signal_electrodes[index].append(value)
            else:
                signal_electrodes[index] = [value]
            #print(f"Index : {index}, Value : {value}")

        #break  # TODO: remove this later
   # print(signal_electrodes)


def storeData():
    global signal_electrodes

    print("check")

    df4 = pd.DataFrame([])
    df4['C'] = signal_electrodes['FP1']
    df4['C1'] = signal_electrodes['FP2']
    df4['C2'] = signal_electrodes['F3']
    df4['C3'] = signal_electrodes['F4']
    df4['C4'] = signal_electrodes['C3']
    df4['C5'] = signal_electrodes['C4']
    df4['C6'] = signal_electrodes['P3']
    df4['C7'] = signal_electrodes['P4']
    df4['C8'] = signal_electrodes['O1']
    df4['C9'] = signal_electrodes['O2']
    df4['C10'] = signal_electrodes['F7']
    df4['C11'] = signal_electrodes['F8']
    df4['C12'] = signal_electrodes['T3']
    df4['C13'] = signal_electrodes['T4']
    df4['C14'] = signal_electrodes['T5']
    df4['C15'] = signal_electrodes['T6']
    df4['C16'] = signal_electrodes['A1']
    df4['C17'] = signal_electrodes['A2']
    df4['C18'] = signal_electrodes['FZ']
    df4['C19'] = signal_electrodes['CZ']
    df4['C20'] = signal_electrodes['PZ']
    df4['C21'] = signal_electrodes['ROC']
    df4['C22'] = signal_electrodes['LOC']
    df4['C23'] = signal_electrodes['EKG1']
    df4['C24'] = signal_electrodes['EMG']
    df4['C25'] = signal_electrodes['26']
    df4['C26'] = signal_electrodes['27']
    df4['C27'] = signal_electrodes['28']
    df4['C28'] = signal_electrodes['29']
    df4['C29'] = signal_electrodes['30']
    df4['C30'] = signal_electrodes['T1']
    df4['C31'] = signal_electrodes['T2']

    global name
    path = os.path.basename(os.path.normpath(name))
    df4.to_csv("csv/"+path)


if __name__ == "__main__":
    start_time = time.time()

    signal_electrodes = {}

    # put your folder path here
    name = '/Users/franklee/fyp/raw_csv'


    filepaths = []
    for (dirpath, dirnames, filenames) in walk(name):
        for name in filenames:
            filepaths.append(dirpath + '/' + name)
        break

    for i in filepaths:
        df = readFile(i)
        print(i)
        processData()
        storeData()
        print("--- %s seconds ---" % (time.time() - start_time))
