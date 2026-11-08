import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, lfilter

# Parámetros
fs = 48000
f0 = 60
alpha = 0.9

N = int(fs / f0)

# Cálculo analítico (más preciso para N grande)
k = np.arange(N)
theta = 2 * np.pi * k / N

# Ceros
z = np.exp(1j * theta)
# Polos
p = alpha**(1/N) * np.exp(1j * theta)

# Circunferencia unitaria
theta_circle = np.linspace(0, 2 * np.pi, 1000)

plt.figure(figsize=(7, 7))

plt.plot(
    np.cos(theta_circle),
    np.sin(theta_circle),
    "k--",
    label="Circunferencia unitaria"
)

plt.scatter(
    z.real,
    z.imag,
    marker="o",
    facecolors="none",
    edgecolors="blue",
    s=20,
    label="Ceros"
)

plt.plot(
    np.cos(theta_circle),
    np.sin(theta_circle),
    "k--",
    label="Circunferencia unitaria"
)

plt.scatter(
    p.real,
    p.imag,
    marker="x",
    color="red",
    s=20,
    label="Polos"
)

plt.xlabel("Parte real")
plt.ylabel("Parte imaginaria")
plt.title("Diagrama de polos y ceros del filtro peine IIR")

plt.axis("equal")
plt.grid()
plt.legend()

plt.show(block=False)

# Mostrar respuesta en frecuencia

# Coeficientes del numerador
K = (1 + alpha) / 2
b = np.zeros(N + 1)
b[0] = K
b[N] = -K

# Coeficientes del denominador
a = np.zeros(N + 1)
a[0] = 1
a[N] = -alpha

# Respuesta en frecuencia (0 a fs/2)
f, h = freqz(b, a, worN=65536, fs=fs)

H_db = 20 * np.log10(np.maximum(np.abs(h), 1e-12))

# Graficar
plt.figure(figsize=(12, 5))
plt.plot(f, H_db)

plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud (dB)")
plt.title("Respuesta en frecuencia del filtro peine IIR")

plt.xlim(0, 1200)
plt.ylim(-100, 5)
plt.xticks(np.arange(0, 1201, 60))

plt.grid()
plt.tight_layout()
plt.show(block=False)

input("Presionar [Enter] para cerrar el gráfica y terminar")
plt.close()