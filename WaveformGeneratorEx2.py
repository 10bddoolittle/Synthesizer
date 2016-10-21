import Synthesizer as Synth
import matplotlib.pyplot as plt
import math as m
import numpy as np

amplitude = lambda x: 100*m.sin(x*2*m.pi) + 100  # sinusoidal envelope
amplitude = lambda x: 10*x                       # linear envelope
# amplitude = lambda x: m.exp(-2*(x-1.5)**2)       # gaussian envelope
timbre = lambda x: m.sin(x*2*m.pi)
frequency = lambda x: 220
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

ax3.plot(np.linspace(0,time,1000),map(amplitude,np.linspace(0,time,1000)))
ax3.set_xlabel('sample', fontsize = 12)
ax3.set_ylabel('amplitude', fontsize = 12)
ax3.set_title('Amplitude Modulation', fontsize = 12)

plt.show()