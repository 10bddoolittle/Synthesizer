import Synthesizer as Synth
import matplotlib.pyplot as plt
import math as m


amplitude = lambda x: 1
timbre = lambda x: m.sin(x*2*m.pi)
timbre = lambda x: 1 if x < 0.5 else -1
timbre = lambda x: -2*x + 1
frequency = lambda x: 420
time = 3.01           # time to play sound for
numsamples = int(44100*time)

WG = Synth.WaveformGenerator(amplitude, timbre, frequency)
data = WG.getSignalData(numsamples)

# outputting sound
Synth.AudioInterface().playData(data)

# plotting data
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

ax1.plot(data[0:1000])
ax1.set_xlabel('sample', fontsize = 12)
ax1.set_ylabel('amplitude', fontsize = 12)
ax1.set_title('first 1000 samples', fontsize = 12)

ax2.plot(data)
ax2.set_xlabel('sample', fontsize = 12)
ax2.set_ylabel('amplitude', fontsize = 12)
ax2.set_title('Full Waveform', fontsize = 12)

plt.show()