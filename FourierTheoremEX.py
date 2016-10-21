import matplotlib.pyplot as plt
import math as m

# Fourier Series of a single period of a square wave:
#
# 	SquareWave(x) =  Sum ( (1/n)*sin(2*pi*n*x/L), n = 1,3,5,... )

fig, ax = plt.subplots(nrows=5, ncols=1)

it = 0

# looping through number of applied fourier terms
for i in [1,3,5,10,100]:
	data = [0]*1000

	# looping through one period of the signal
	for j in range(0,i):
		n = 2*j + 1

		# accumulating data for each new fourier term
		data = map(
				lambda x, y: x + y,
				map(
					lambda x: 1.0/(n)*m.sin(2*m.pi*n*(x)/1000),
					range(0,1000)
				),
				data
			)

	# plotting data
	ax[it].plot(data)
	ax[it].set_title(str(i) + ' Fourier terms', fontsize = 12)
	it = it + 1

plt.subplots_adjust(hspace=0.6)
plt.show()