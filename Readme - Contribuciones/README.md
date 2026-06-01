# TRAFFIC_CRASH

TRAFFIC_CRASH<br>
dataset - Vehículos involucrados en accidentes de tránsito en Bogotá (2022 – 2025)<br>
DataLab – Análisis de Accidentes de Tránsito<br>


**¿Qué es?:**<br>
Este proyecto consiste en el desarrollo de una herramienta en Python que permite analizar un dataset de accidentes de tránsito mediante un programa en consola y posteriormente en una GUI y una interfaz en PyQt5
El sistema permite explorar los datos, realizar búsquedas, calcular estadísticas y agrupar información para responder preguntas relevantes sobre los accidentes.
El dataset corresponde a registros de accidentes de tránsito y contiene 5 columnas.
- Marca del vehículo
- Modelo del vehículo
- Tipo de vehículo
- Edad del vehículo
- Fecha del accidente
- Gravedad del accidente<br>

Filas = 31928

La carpeta contiene 2 archivos.CSV <br>
TRAFFIC_CRASH: Este es el dataset completo y el que se va a analizar en general<br>
TRAFFIC_CRASHpequeño: Este es el dataset de 50 filas y el que se va a correr en consola en la primera entrega <br>

**Preguntas del proyecto:**<br>
-¿Qué tipo de vehículo presenta más accidentes?<br>
-¿Los vehículos más antiguos están más involucrados en accidentes?<br>
-¿Qué características son más comunes en los accidentes registrados?<br>

<b>Instrucciones:<br>
Paso 1: Abre la terminal en la carpeta del proyecto (Hecho en Vs code)<br>
Paso 2: Usa el comando "python main.py"<br>
Paso 3: Usa el menú interactivo para seleccionar las opciones disponibles <br>

**Integrantes:**<br>
- Fredy Alejandro Villamarin Garcia<br>
- Juan Manuel Villabon Nuñez<br>
- Laura Sofia Muñeton Balcazar<br>


**Link del poster:**
<br>
https://drive.google.com/file/d/1zxuWMYdwVt48T6puj5FzfW4ANXxJNdZZ/view?usp=drive_link

**Link del repositorio:**
<br>
https://github.com/fvillamarin-pixel/TRAFFIC_CRASH

**Link del video:**
<br> 
https://drive.google.com/file/d/1QvMmm6EbU6nRBlkmOACK8TqSUTllekvv/view?usp=sharing

## ENTREGA 2

**Funcionalidades Entrega 2:** <br>

- Búsqueda de registros.
- Estadísticas básicas.
- Agrupación por tipo de vehículo.
- Guardar resultados en CSV y JSON.
- Recuperar archivos guardados.
- Historial automático de consultas.
- Comparación de grupos.

 **Link del diagrama de flujo de datos:**
 <br>
 https://drive.google.com/file/d/1R1Dmptn2mx06i8fguutc84CWCkfwKH5u/view?usp=drive_link
 
 **Link del video:** 
 <br>
 https://drive.google.com/file/d/1o6FUwplxAXTsrM3mUYsqhX546BYp0jGg/view?usp=drive_link

 ## ENTREGA FINAL

**Funcionalidades Entrega final:**

- Búsqueda de registros dentro del dataset.
- Cálculo de estadísticas descriptivas.
- Agrupación de vehículos por tipo.
- Visualización de gráficos mediante Matplotlib.
- Exportación de resultados a CSV.
- Historial de consultas realizadas.

**Gráficos implementados:**<br>

- Gráfico 1: Accidentes por tipo de vehículo:
    Muestra la cantidad de accidentes registrados para cada tipo de vehículo mediante un gráfico de barras.
- Gráfico 2: Distribución de la edad de los vehículos:
    Muestra la distribución de la edad de los vehículos involucrados en accidentes mediante un histograma.

**Librerías utilizadas:**<br>

- Pandas
- Matplotlib
- PyQt5
- CSV
- JSON

**Estructura del proyecto:**<br>
```text
TRAFFIC_CRASH/
│
├── analisis.py
├── archivos.py
├── interfaz.py
├── main.py
│
├── csvs/
│   ├── TRAFFIC_CRASH (1).csv
│   ├── TRAFFIC_CRASHpequeño.csv
│   ├── historial.csv
│   ├── exportacion_datalab.csv
│   └── resultados_busqueda.csv
│
├── documentacion/
│   ├── Documentacion TRAFFIC_CRASH.pdf
│   └── conclusion_visual.png
│
└── Readme - Contribuciones/
    ├── README.md
    └── Contribuciones.md
```

**Ejecución del programa:**

    **- Clonar el repositorio**

    **- Instalar dependencias**

    ```bash
    pip install pandas matplotlib pyqt5
    ```

    **- Ejecutar la aplicación**

    ```bash
    python main.py
    ```

    **- Utilizar la interfaz gráfica**


**Documentación:**

La documentación del proyecto se encuentra en:
    documentacion/Documentacion TRAFFIC_CRASH.pdf
    documentacion/TRAFFIC_CRASH-DataLab Hub.pdf

**Conclusión visual:**

La infografía final del proyecto se encuentra en:
    documentacion/Conclusion Visual TRAFFIC_CRASH.png