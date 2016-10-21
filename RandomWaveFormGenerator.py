import Synthesizer as Synth
import matplotlib.pyplot as plt
import math as m
import random


data = []
for i in range(0,100):

	print i
	const_frequency = random.randint(60,1000)

	amplitudes = [lambda x: 1, lambda x: 0.5*m.sin(x*2*m.pi) + 1, lambda x: x]
	timbres = [lambda x: m.sin(x*2*m.pi), lambda x: 1 if x < 0.5 else -1, lambda x: -2*x + 1]
	frequencies = [
					lambda x: const_frequency,
					lambda x: 2**(7 + (float(x) % 0.5)) + 40,
					lambda x: const_frequency*m.sin(2*m.pi*x/5) + const_frequency + 60
				]

	amplitude = random.choice(amplitudes)
	timbre = random.choice(timbres)
	frequency = random.choice(frequencies)

	numsamples = random.randint(30000,150000)
	startsample = random.randint(0,10000*(i+1))

	

	signaldata = Synth.WaveformGenerator(amplitude, timbre, frequency).getSignalData(numsamples)

	signallength = startsample + numsamples

	if len(data) < signallength:
		dif = signallength - len(data)
		data.extend([0]*dif)

	data[startsample:signallength] = map((lambda n: data[n + startsample] + signaldata[n]) , range(0,numsamples) )

maxvalue = max(abs(max(data)),abs(min(data)))


if maxvalue != 0:
	data = map((lambda x: x*32766/maxvalue), data)

# outputting sound
Synth.AudioInterface().playData(data)
