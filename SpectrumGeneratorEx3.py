import Synthesizer as Synth
import matplotlib.pyplot as plt
import random

s = lambda x: 44100              # number of samples in frequency spectrum
time = 3.01           # time to play sound for


# Spectral Desnisty function for rectangle
X = lambda n: random.randint(0,100)

SG = Synth.SpectrumGenerator(X,s)

data = SG.getSignalData(int(44100*time))

# outputting sound
Synth.AudioInterface().playData(data)

# plotting data
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

ax1.plot(data[0:s(0)])
ax1.set_xlabel('samples', fontsize = 12)
ax1.set_ylabel('amplitude', fontsize = 12)
ax1.set_title('Time Domain', fontsize = 12)

ax2.plot(map(X, range(0, s(0))))
ax2.set_xlabel('samples', fontsize = 12)
ax2.set_ylabel('amplitude', fontsize = 12)
ax2.set_title('Frequency Domain', fontsize = 12)

plt.show()