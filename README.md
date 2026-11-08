# PDS-Tarea-5
Tarea 5 curso de Procesamiento Digital de Señales 

## Archivos del directorio

| File | Descripción |
| --- | --- |
| `README.md` | Descripción general del contenido del proyecto. |
| `Tarea-5-reporte.pdf` | Reporte de resultados de la tarea. |
| `dft_signal.py` | Calcula y grafica la DFT de la señal con ruido. |
| `environment.yml` | Archivo con dependencias para crear ambiente de conda |
| `filter_signal.py` | Filtra el ruido armónico de 60 Hz, calcula métricas de calidad y genera el audio filtrado. |
| `la_muerte_del_angel.wav` | Audio original utilizado como señal de referencia. |
| `la_muerte_del_angel_power_noise.wav` | Audio contaminado con ruido armónico de 60 Hz. |
| `pole_zero.py` | Grafica los polos, los ceros y la respuesta en frecuencia del filtro peine IIR. |
| `sdft_signal.py` | Analiza y grafica el espectro de la señal en cuatro ventanas temporales. |

## Preparar ambiente
1.  Ejecutar archivo de ambiente 
```
conda env create -f environment.yml
conda activate pds-tarea5
```
2. Ejemplo de usar script
```
python3 pole_zero.py
```
3. Salir de ambiente
```
conda deactivate
```

### Script: pole_zero.py
Crea gráficas de polos y ceros y la respuesta en frecuencia de un filtro peine:
```
python3 pole_zero.py
```

### Script: filter_signal.py
Aplica el filtro peine sobre la señal y genera el audio de salida en `audio_filtrado.wav`. Se miden la PSNR, SNR y MSE para la señal antes y despues de filtrar.
```
python3 filter_signal.py
```

### Script: dft_signal.py
Esta ejecuta la DFT con el algoritmo de FFT sobre una señal con ruido de 60Hz. Se crea una figura con la respuesta en magnitud del espectro en frecuencia para la señal.
```
python3 dft_signal.py
```

### Script: sdft_signal.py
Esta ejecuta la STDFT con el algoritmo de FFT sobre una señal con ruido de 60Hz. Este algoritmo busca ventanas de tiempo de 0.5s y aplica la FFT por separado sobre cada una. Se crea una figura con las respuestas en magnitud del espectro en frecuencia para la señal.
```
python3 sdft_signal.py
```
## Troubleshooting
When installing the conda enviroment. The base enviroment might not activate. This can
result in the `conda` commands not being recognized. This can be fixed by running the
conda binary as follows:
```
<PATH TO MINIFORGE INSTALL>/miniforge3/bin/conda init
```
The terminal should show `(base)` at the start of the line if the conda base
enviroment was succesfully enabled.
