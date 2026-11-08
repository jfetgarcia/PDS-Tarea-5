import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

sample_rate, audio = wavfile.read('la_muerte_del_angel_power_noise.wav')

if audio.ndim == 1:
    num_channels = 1
else:
    num_channels = audio.shape[1]

print(f"Number of channels: {num_channels}")
print(f"Sample Rate: {sample_rate} Hz")
print(f"Data Type: {audio.dtype}")
print(f"Shape: {audio.shape}")

# Normalizando datos con 2^15 (se tiene 16bits)
norm_audio = audio.astype(np.float64) / 32768.0 

# Obtener largo para normalizar el FFT
N = len(audio)

fft_audio = np.fft.fft(norm_audio)
frecuencia = np.fft.fftfreq(N, d=1/sample_rate)
print(N)


mask = (frecuencia >= -3000) & (frecuencia <= 3000)
magnitud = np.abs(fft_audio)




fig, ax = plt.subplots(2, 1, figsize=(12, 8))
ax[0].plot(
    np.fft.fftshift(frecuencia),
    np.fft.fftshift(np.abs(fft_audio))
)

ax[0].set_xlabel("Frecuencia (Hz)")
ax[0].set_ylabel("Magnitud")
ax[0].set_title("Espectro completo de la señal")
ax[0].grid(True)

# Continuar con script
plt.show(block=False)

ax[1].plot(frecuencia[mask], magnitud[mask])
ax[1].set_xlim(-1200, 1200)

# Marcar armónicos de 60 Hz
for freq in range(-1200, 1201, 60):
    ax[1].axvline(
        freq,
        color="green",
        linestyle="--",
        alpha=0.5
    )

ax[1].set_title("Ampliación del espectro: 60 Hz y sus armónicos")
ax[1].set_xlabel("Frecuencia (Hz)")
ax[1].set_ylabel("Magnitud")
ax[1].grid(True)

# Ajustar espacio entre gráficos
plt.tight_layout()

input("Presionar [Enter] para cerrar el gráfica y terminar")
plt.close()