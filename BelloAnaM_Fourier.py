# Tiene una serie de tiempo, donde los datos de tiempo estan almacenados en un arreglo t y los datos de amplitud en un arreglo amp.
#1) Usando los paquetes de scipy de la transformada de Fourier, haga un FILTRO de la senial que elimine las frecuencias mayores a 1000Hz en las senial original.
#2) Haga una grafica de la senial original y la senial filtarada y guardela SIN MOSTRARLA en filtro.pdf
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, ifft


n = 1280 # number of point in the whole interval
f = 200.0 #  frequency in Hz
dt = 1 / (f * 320 ) #320 samples per unit frequency
t = np.linspace( 0, (n-1)*dt, n)
amp = np.cos(2 * np.pi * f * t) - 0.4 * np.sin(2 * np.pi * (2*f) * t ) + np.random.random(n)

transformada= fft(amp)
#print(transformada)

frecuencias= fftfreq(n,dt)
print(frecuencias)

parafiltro=np.copy(transformada)

# SU FILTRO

for i in range(n):
    if(frecuencias[i]>1000):
        parafiltro[i]=0
    else:
        parafiltro[i]=parafiltro[i]

        

# SU GRAFICA
inversafiltro= np.fft.ifft(parafiltro)

plt.figure()

plt.subplot(2,1,1)
plt.plot(t,amp, color= "cyan", label= "original")
plt.title("Senial original")
plt.xlabel("t(s)")
plt.ylabel("Amplitud")

plt.subplot(2,1,2)
plt.plot(t,inversafiltro)
plt.title("Senial filtrada")
plt.xlabel("t(s)")
plt.ylabel("Amplitud")
plt.subplots_adjust(hspace=0.5)

plt.savefig("filtro.pdf")





# Puede usar los siguientes paquetes:
#from scipy.fftpack import fft, fftfreq, ifft

