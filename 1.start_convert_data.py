import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import os


def readFile():
    pd.read_csv(
        'D:/archive/data_eeg_age_v1/data2kaggle/eval/00000647_s002_t000.csv', skiprows=1)

    # Drop last 4 columns
    df.drop(columns=df.columns[-4:],
            axis=1,
            inplace=True)

    name = {
        'EEG FP1-REF': 'FP1',
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
    return df.rename(columns=name)


def processData():
  # P2=[]
  # P2_1=[]
  # if df2[b]=="F3":
  #     F3.append(df1[b])
  #     F3_1.append(df2[b])
  print(1)


def storeData():
  print("check")

  df4 = pd.DataFrame([])
  df4['C'] = FP1
  df4['C1'] = FP2
  df4['C2'] = F7
  df4['C3'] = F8
  print("check1")

  df4['C4'] = AF1
  df4['C5'] = AF2
  df4['C6'] = FZ1
  df4['C7'] = F4
  df4['C8'] = F3
  df4['C9'] = FC6
  df4['C10'] = FC5
  df4['C11'] = FC2
  df4['C12'] = FC1
  df4['C13'] = T8
  df4['C14'] = T7
  df4['C15'] = CZ
  df4['C16'] = C3
  df4['C17'] = C4
  df4['C18'] = CP5
  df4['C19'] = CP6
  df4['C20'] = CP1
  df4['C21'] = CP2
  df4['C22'] = P3
  print("check2")

  #df4['C1'] = z
  df4['C23'] = P4
  df4['C24'] = PZ
  df4['C25'] = P8
  df4['C26'] = P7
  df4['C27'] = PO2
  df4['C28'] = PO1
  df4['C29'] = O2
  df4['C30'] = O1
  df4['C31'] = X

  print(df4)


  df4.to_csv("output.csv")

if __name__ == "__main__":
    signal_electrode = []
    df = readFile()

    #df1=df["sensor value"] - eeg signal
    #df2=df["sensor position"] - index


    for index, row in df.iterrows():
        print(index)
        print(row)

        if(index == 10):
            break
    processData()
    exit()