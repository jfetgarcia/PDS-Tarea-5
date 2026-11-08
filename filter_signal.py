import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import lfilter

def abrir_archivo(archivo):

    # Leer archivos WAV
    fs, audio = wavfile.read(archivo)

    audio_norm = audio.astype(np.float64) / 32768.0

    return fs, audio_norm

def calcular_metricas(referencia, senal_procesada):
    
    # Verificar dimensiones
    if referencia.shape != senal_procesada.shape:
        raise ValueError("Las señales tienen dimensiones diferentes")
    
    # Calcular MSE
    mse = np.mean((referencia - senal_procesada) ** 2)

    # Calcular PSNR
    if mse == 0:
        psnr = np.inf
    else:
        psnr = 10 * np.log10(1.0 / mse)

    # Calcular SNR
    error = referencia - senal_procesada
    potencia_senal = np.mean(referencia**2)
    potencia_error = np.mean(error**2)

    if potencia_senal == 0:
        return np.nan

    if potencia_error == 0:
        return np.inf

    # SNR en dB
    snr = 10 * np.log10(potencia_senal / potencia_error)

    return mse, psnr, snr

fs, audio_norm = abrir_archivo('la_muerte_del_angel_power_noise.wav')


f0 = 60
alpha = 0.9
N = fs // f0
K = (1 + alpha) / 2


# Numerador
b = np.zeros(N + 1)
b[0] = K
b[N] = -K

# Denominador
a = np.zeros(N + 1)
a[0] = 1.0
a[N] = -alpha

# Filtrado
audio_filtrado = lfilter(
    b,
    a,
    audio_norm,
    axis=0
)

fs_ref, audio_ref = abrir_archivo("la_muerte_del_angel.wav")

mse_original, psnr_original, snr_original = calcular_metricas(audio_ref, audio_norm)

print(f"MSE original: {mse_original:.8f}")
print(f"PSNR original: {psnr_original:.2f} dB")
print(f"SNR original: {snr_original:.2f} dB")

mse, psnr, snr = calcular_metricas(audio_ref, audio_filtrado)
print(f"MSE filtrado: {mse:.8f}")
print(f"PSNR filtrado: {psnr:.2f} dB")
print(f"SNR filtrado: {snr:.2f} dB")

# Convertir a PCM
audio_filtrado = np.clip(audio_filtrado, -1.0, 1.0)

audio_salida = np.clip(
    np.round(audio_filtrado * 32768.0),
    -32768,
    32767
).astype(np.int16)

wavfile.write(
    "audio_filtrado.wav",
    fs,
    audio_salida
)

print("Guardado en audio_filtrado.wav")


