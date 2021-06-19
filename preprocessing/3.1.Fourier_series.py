#%%
import numpy as np
import pandas as pd
import scipy.fftpack
import sys
import matplotlib.pyplot as plotter

df = pd.read_csv('C:/Users/ygh19/Downloads/3.eeg_recognation-master/3.eeg_recognation-master/csv/00000647_s002_t000.csv')

mapping = { 'C' : 'FP1',
   'C1' : 'FP2',
   'C2' : 'F3',
   'C3' : 'F4',
   'C4' : 'C3',
   'C5' : 'C4',
   'C6' : 'P3',
   'C7' : 'P4',
   'C8' : 'O1',
   'C9' : 'O2',
   'C10' : 'F7',
   'C11' : 'F8',
   'C12' : 'T3',
   'C13' : 'T4',
   'C14' : 'T5',
   'C15' : 'T6',
   'C16' : 'A1',
   'C17' : 'A2',
   'C18' : 'FZ',
   'C19' : 'CZ',
   'C20' : 'PZ',
   'C21' : 'ROC',
   'C22' : 'LOC',
   'C23' : 'EKG1',
   'C24' : 'EMG',
   'C25' : '26',
   'C26' : '27',
   'C27' : '28',
   'C28' : '29',
   'C29' : '30',
   'C30' : 'T1',
   'C31' : 'T2'
  }

FP1   = df.loc[:,'C'].tolist()
FP2   = df.loc[:,'C1'].tolist()
FP1_1 = df.iloc[:,0].tolist()
FP2_1 = FP1_1

# Python example - Fourier transform using numpy.fft method

# How many time points are needed i,e., Sampling Frequency

samplingFrequency   = 300500;
# At what intervals time points are sampled
samplingInterval = 1 / samplingFrequency;
# Begin time period of the signals
beginTime           = 0;
# End time period of the signals
endTime             = 1; 
# Frequency of the signals
signal1Frequency     = 4;
signal2Frequency     = 7;
# Time points
time        = np.arange(beginTime, endTime, samplingInterval);
# Create two sine waves

amplitude1 = FP2
amplitude2 = np.sin(2*np.pi*signal2Frequency*time)
# Create subplot
figure, axis = plotter.subplots(4, 1)
plotter.subplots_adjust(hspace=1)
# Time domain representation for sine wave 1
axis[0].set_title('Sine wave with a frequency of 4 Hz')
axis[0].plot(time, amplitude1)
axis[0].set_xlabel('Time')
axis[0].set_ylabel('Amplitude')
# Time domain representation for sine wave 2
axis[1].set_title('Sine wave with a frequency of 7 Hz')
axis[1].plot(time, amplitude2)
axis[1].set_xlabel('Time')
axis[1].set_ylabel('Amplitude')
# Add the sine waves
amplitude = amplitude1 + amplitude2
# Time domain representation of the resultant sine wave
axis[2].set_title('Sine wave with multiple frequencies')
axis[2].plot(time, amplitude)
axis[2].set_xlabel('Time')
axis[2].set_ylabel('Amplitude')
# Frequency domain representation
fourierTransform = np.fft.fft(amplitude)/len(amplitude)           # Normalize amplitude
fourierTransform = fourierTransform[range(int(len(amplitude)/2))] # Exclude sampling frequency
tpCount     = len(amplitude)
values      = np.arange(int(tpCount/2))
timePeriod  = tpCount/samplingFrequency
frequencies = values/timePeriod
# Frequency domain representation
axis[3].set_title('Fourier transform depicting the frequency components')
axis[3].plot(frequencies, abs(fourierTransform))
axis[3].set_xlabel('Frequency')
axis[3].set_ylabel('Amplitude')

plotter.show()

# %%
