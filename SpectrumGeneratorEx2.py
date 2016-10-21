import Synthesizer as Synth
import matplotlib.pyplot as plt
import numpy as np

rectstart = 0.35 # position of left side of rectangle
# s = lambda x: 1000             # number of samples in frequency spectrum
s = lambda x: x/10 + 100       # linear
s = lambda x: 500 if x%40000 < 20000 else 1000

time = 3.01           # time to play sound for

# Spectral Desnisty function for rectangle
X = lambda x: 1 if x >= rectstart and x <= (1 - rectstart) else 0

SG = Synth.SpectrumGenerator(X,s)

data = SG.getSignalData(int(44100*time), mode='generic spectrum')

# outputting sound
Synth.AudioInterface().playData(data)

# plotting data
fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1)

ax1.plot(data[0:s(0)])
ax1.set_xlabel('samples', fontsize = 12)
ax1.set_ylabel('amplitude', fontsize = 12)
ax1.set_title('Time Domain', fontsize = 12)

ax2.plot(map(X, np.linspace(0,1,s(0))))
ax2.set_xlabel('samples', fontsize = 12)
ax2.set_ylabel('amplitude', fontsize = 12)
ax2.set_title('Frequency Domain', fontsize = 12)

ax3.plot(map(s, np.linspace(0,int(44100*time))))
ax3.set_xlabel('sample', fontsize = 12)
ax3.set_ylabel('chunksize', fontsize = 12)
ax3.set_title('# Samples', fontsize = 12)

plt.show()