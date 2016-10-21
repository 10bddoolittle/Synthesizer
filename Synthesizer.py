import math as m
import numpy as np
from numpy import fft
import struct
import pyaudio

class AudioInterface:
	def __init__(self):
		self.sampwidth = 2
		self.channels = 1
		self.framerate = 44100

	# setting parameters of audio stream
	def initializeStream(self):
		self.p = pyaudio.PyAudio()
		self.stream = self.p.open(
			format=self.p.get_format_from_width(self.sampwidth),
            channels=self.channels,
            rate=self.framerate,
            output=True
        )

	def closeStream(self):
		self.stream.close()
		self.p.terminate()

	def playData(self, data):
		self.initializeStream()
		self.stream.write( struct.pack('h'*len(data),*data) )
		self.closeStream()

class SpectrumGenerator:
	def __init__(self, X, s):
		self.X = X      # Lambda describing frequency [0, s-1]
		self.s = s   # number of samples

	def getTimeSamples(self, s, mode):

		if mode == 'generic spectrum':  # spectrum defined from [0,1)
			Xdata = map(self.X, np.linspace(0,1,s))
		else:                           # spectrum defined in terms of samples
			Xdata = map(self.X, range(0,s))

		# for performance reasons the FFT algorithm requires a flipped signal
		# [1,2,3,4] -> [3,4,1,2]
		Xshift = fft.fftshift(Xdata)

		# complex values are returned by the fft, just taking the reals now
		xshift = np.real(np.fft.ifft(Xshift))

		x = fft.fftshift(xshift)

		return x

	def getSignalData(self, n, mode=''):

		signaldata = []

		while len(signaldata) < n:
			signaldata.extend(self.getTimeSamples(self.s(len(signaldata)),mode))

		# normalization
		maxvalue = max(abs(max(signaldata)),abs(min(signaldata)))
		if maxvalue != 0:
			signaldata = map((lambda x: x*32766/maxvalue), signaldata)

		return signaldata


class WaveformGenerator:
	def __init__(self, amplitude, timbre, frequency):
		self.fs = 44100.0
		self.amplitude = amplitude
		self.timbre = timbre
		self.frequency = frequency

	def getSignalData(self, chunksize, chunknum=0, mode='discrete FM'):

		# getting time data from samples
		tstart = chunknum * chunksize / self.fs
		tend = tstart + ((chunksize - 1) / self.fs)
		
		n = chunksize

		tdata = np.linspace(tstart,tend,n) # time stamps of sample
		data = []

		# only modulate frequency at the start of each signal period
		if mode == 'discrete FM':

			fdata = map(self.frequency,tdata)     # frequency data over time			
			framecount = 0                        # keep track of current frame
			df = int(self.fs/fdata[0])            # initial digital frequency

			maxvalue = 0

			for i in range(0, n):

				if framecount == df: # have we written an entire period of data
					framecount = 0
					df = int(self.fs/fdata[i]) # get new digital frequency

				sample = self.amplitude(tdata[i])*self.timbre(framecount/float(df))
				maxvalue = abs(sample) if abs(sample) > maxvalue else maxvalue
				data.append(sample)
				
				framecount = framecount + 1
			
			# normalization
			data = data if maxvalue == 0 else map((lambda x: x*32766/maxvalue), data) 

		return data





