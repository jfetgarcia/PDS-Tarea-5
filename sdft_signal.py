import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Leer archivo WAV
fs, audio = wavfile.read("la_muerte_del_angel_power_noise.wav")

# Normalizar
audio = audio.astype(np.float64) / 32768.0

duracion = 0.5  # segundos
# Cantidad de muestras por ventana
L = int(duracion * fs)

inicios = np.linspace(0, len(audio) - L, 4, dtype=int)


fig, ax = plt.subplots(4, 1, figsize=(12, 12))

for i, inicio in enumerate(inicios):

    segmento = audio[inicio:inicio + L]
    fft_audio = np.fft.fft(segmento)
    frecuencias = np.fft.fftfreq(L, d=1/fs)


    magnitud = np.abs(fft_audio)

    mask = (frecuencias >= -1200) & (frecuencias <= 1200)


    ax[i].plot(frecuencias[mask], magnitud[mask])
    # Marcar armónicos de 60 Hz
    for f in range(-1200, 1201, 60):
        ax[i].axvline(
            f,
            color="green",
            linestyle="--",
            alpha=0.5
        )

    # Tiempo correspondiente a la ventana
    tiempo_inicio = inicio / fs
    tiempo_fin = (inicio + L) / fs

    ax[i].set_title(
        f"Ventana {i+1}: "
        f"{tiempo_inicio:.2f} - {tiempo_fin:.2f} s"
    )

    ax[i].set_xlabel("Frecuencia (Hz)")
    ax[i].set_ylabel("Magnitud")
    ax[i].set_xlim(-1200, 1200)
    ax[i].grid(True)

# Utilizar la misma escala vertical en todos los gráficos
ylim_max = max(axis.get_ylim()[1] for axis in ax)

for axis in ax:
    axis.set_ylim(0, ylim_max)

plt.tight_layout()
plt.show()