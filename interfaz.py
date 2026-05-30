import sys
import pandas as pd

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTextEdit,
    QLineEdit,
    QLabel
)
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from analisis import agrupar_por_tipo

from archivos import (
    mostrar_historial,
    guardar_resultado
)

class Ventana(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("TRAFFIC CRASH - DataLab Hub")
        self.resize(900, 700)
        self.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                min-height: 50px;
            }

            QLineEdit {
                font-size: 14px;
                min-height: 35px;
            }

            QTextEdit {
                font-size: 13px;
            }

            QLabel {
                font-size: 18px;
                font-weight: bold;
            }
        """)
        # CARGA CON PANDAS
        self.datos = pd.read_csv(
            "TRAFFIC_CRASH (1).csv",
            sep=";"
        )
        layout = QVBoxLayout()

        titulo = QLabel("TRAFFIC CRASH - DataLab Hub")
        titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(titulo)

        self.caja_busqueda = QLineEdit()
        self.caja_busqueda.setPlaceholderText(
            "Ingrese término de búsqueda"
        )
        layout.addWidget(self.caja_busqueda)

        boton_buscar = QPushButton("Buscar")
        boton_buscar.clicked.connect(
            self.buscar_datos
        )
        layout.addWidget(boton_buscar)

        boton_estadisticas = QPushButton(
            "Estadísticas"
        )
        boton_estadisticas.clicked.connect(
            self.mostrar_estadisticas
        )
        layout.addWidget(boton_estadisticas)

        boton_historial = QPushButton(
            "Historial"
        )
        boton_historial.clicked.connect(
            self.ver_historial
        )
        layout.addWidget(boton_historial)

        boton_agrupar = QPushButton(
            "Agrupar por Tipo"
        )

        boton_agrupar.clicked.connect(
            self.mostrar_grupos
        )

        layout.addWidget(boton_agrupar)

        boton_grafico1 = QPushButton(
            "Gráfico por Tipo de Vehículo"
        )

        boton_grafico1.clicked.connect(
            self.grafico_tipo
        )

        layout.addWidget(boton_grafico1)

        boton_grafico2 = QPushButton(
            "Gráfico Edad de Vehículos"
        )

        boton_grafico2.clicked.connect(
            self.grafico_edad
        )

        layout.addWidget(boton_grafico2)

        boton_exportar = QPushButton(
            "Exportar CSV"
        )

        boton_exportar.clicked.connect(
            self.exportar_csv
        )

        layout.addWidget(boton_exportar)

        boton_salir = QPushButton("Salir")

        boton_salir.clicked.connect(self.close)

        layout.addWidget(boton_salir)

        self.resultados = QTextEdit()

        layout.addWidget(self.resultados)

        self.setLayout(layout)

    def buscar_datos(self):

        termino = self.caja_busqueda.text()

        mascara = self.datos.astype(str).apply(
            lambda col: col.str.contains(
                termino,
                case=False,
                na=False
            )
        ).any(axis=1)

        resultados = self.datos[mascara]

        texto = (
            f"Se encontraron "
            f"{len(resultados)} registros\n\n"
        )

        texto += resultados.head(50).to_string()

        self.resultados.setText(texto)

    def mostrar_estadisticas(self):

        columnas_numericas = self.datos.select_dtypes(
            include="number"
        ).columns

        if len(columnas_numericas) == 0:

            self.resultados.setText(
                "No hay columnas numéricas."
            )

            return

        columna = columnas_numericas[0]

        texto = (
            f"Columna: {columna}\n\n"
            f"Máximo: {self.datos[columna].max()}\n"
            f"Mínimo: {self.datos[columna].min()}\n"
            f"Promedio: {round(self.datos[columna].mean(),2)}"
        )

        self.resultados.setText(texto)

    def mostrar_grupos(self):

        datos_lista = [
            self.datos.columns.tolist()
        ] + self.datos.values.tolist()

        grupos = agrupar_por_tipo(
            datos_lista
        )

        texto = ""

        for tipo, cantidad in grupos.items():

            texto += (
                f"{tipo}: {cantidad}\n"
            )

        self.resultados.setText(
            texto
        )

    def ver_historial(self):

        historial = mostrar_historial()

        texto = ""

        for registro in historial:
            texto += str(registro) + "\n"

        self.resultados.setText(texto)

    def grafico_tipo(self):

        conteo = self.datos[
            "TIPO_VEHICULO"
        ].value_counts()

        plt.figure(figsize=(8,5))

        conteo.plot(kind="bar")

        plt.title(
            "Accidentes por Tipo de Vehículo"
        )

        plt.xlabel(
            "Tipo de Vehículo"
        )

        plt.ylabel(
            "Cantidad de Accidentes"
        )

        plt.tight_layout()

        plt.show()

    def grafico_edad(self):

        plt.figure(figsize=(8,5))

        self.datos[
            "EDAD_VEHICULO"
        ].hist(
            bins=20
        )

        plt.title(
            "Distribución de Edad de los Vehículos"
        )

        plt.xlabel(
            "Edad del Vehículo"
        )

        plt.ylabel(
            "Frecuencia"
        )

        plt.tight_layout()

        plt.show()

    def exportar_csv(self):

        datos = self.datos.values.tolist() #Expota todos los registros

        guardar_resultado(
            datos,
            "exportacion_datalab",
            "csv"
        )

        self.resultados.setText(
            "Archivo exportacion_datalab.csv guardado correctamente."
        )

app = QApplication(sys.argv)

ventana = Ventana()
ventana.show()

sys.exit(app.exec_())