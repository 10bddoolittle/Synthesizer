import Synthesizer as Synth
import matplotlib.pyplot as plt
import math as m
import numpy as np
import random

amplitude = lambda x: 1
timbre = lambda x: m.sin(x*2*m.pi)
frequency = lambda x: 2**(7 + (float(x) % 0.5)) + 40 # exponential
# frequency = lambda x: 130.81 if x%.6 < .2 else  155.56 if x%.6 > .45 else 164.81
time = 3.01           # time to play sound for
numsamples = int(44100*time)


WG = Synth.WaveformGenerator(amplitude, timbre, frequency)

data = WG.getSignalData(numsamples)

#outputting sound
Synth.AudioInterface().playData(data)

# plotting data
fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1)

ax1.plot(data[0:1000])
ax1.set_xlabel('sample', fontsize = 12)
ax1.set_ylabel('amplitude', fontsize = 12)
ax1.set_title('1000 Samples', fontsize = 12)

ax2.plot(data)
ax2.set_xlabel('sample', fontsize = 12)
ax2.set_ylabel('amplitude', fontsize = 12)
ax2.set_title('Full Waveform', fontsize = 12)

ax3.plot(map(frequency,np.linspace(0,time,1000)))
ax3.set_xlabel('sample', fontsize = 12)
ax3.set_ylabel('Frequency', fontsize = 12)
ax3.set_title('Frequency Modulation', fontsize = 12)

plt.show()