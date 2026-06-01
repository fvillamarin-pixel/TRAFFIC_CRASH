import sys
import pandas as pd

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QLabel,
    QTableView,
    QTextEdit
)

from PyQt5.QtCore import (
    Qt,
    QAbstractTableModel
)
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from analisis import agrupar_por_tipo

plt.style.use("bmh")

from archivos import (
    mostrar_historial,
    guardar_resultado
)
class PandasModel(QAbstractTableModel):

    def __init__(self, dataframe):
        super().__init__()
        self._data = dataframe

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):

        if role == Qt.DisplayRole:

            return str(
                self._data.iloc[
                    index.row(),
                    index.column()
                ]
            )

        return None

    def headerData(
        self,
        section,
        orientation,
        role
    ):

        if role == Qt.DisplayRole:

            if orientation == Qt.Horizontal:

                return str(
                    self._data.columns[
                        section
                    ]
                )

            return str(section)

        return None

class Ventana(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("TRAFFIC CRASH - DataLab Hub")
        self.resize(1300, 900)
        self.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                min-height: 35px;
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
            "csvs/TRAFFIC_CRASH (1).csv",
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

        self.figura = Figure(figsize=(6,4))
        self.canvas = FigureCanvas(self.figura)

        self.canvas.hide()

        self.tabla = QTableView()

        self.tabla.setMinimumHeight(300)

        layout.addWidget(self.tabla)

        self.resultados = QTextEdit()

        self.resultados.hide()

        layout.addWidget(self.resultados)

        self.setLayout(layout)

    def mostrar_dataframe(self, df):

        modelo = PandasModel(df)

        self.tabla.setModel(modelo)

        self.tabla.resizeColumnsToContents()

        self.tabla.setSortingEnabled(True)

        self.tabla.show()

        self.resultados.hide()

    def buscar_datos(self):

        self.canvas.hide()

        termino = self.caja_busqueda.text()

        mascara = self.datos.astype(str).apply(
            lambda col: col.str.contains(
                termino,
                case=False,
                na=False
            )
        ).any(axis=1)

        resultados = self.datos[mascara]

        self.mostrar_dataframe(
            resultados.head(500)
        )

    def mostrar_estadisticas(self):

        self.canvas.hide()

        columnas_numericas = self.datos.select_dtypes(
            include="number"
        ).columns

        if len(columnas_numericas) == 0:
            self.resultados.show()

            self.tabla.hide()

            self.resultados.setText(
                "No hay columnas numéricas."
            )

            return

        columna = columnas_numericas[0]

        estadisticas = pd.DataFrame({

            "Medida": [
                "Máximo",
                "Mínimo",
                "Promedio"
            ],

            "Valor": [
                self.datos[columna].max(),
                self.datos[columna].min(),
                round(
                    self.datos[columna].mean(),
                    2
                )
            ]
        })

        self.mostrar_dataframe(
            estadisticas
        )

    def mostrar_grupos(self):

        self.canvas.hide()

        grupos = (
            self.datos[
                "TIPO_VEHICULO"
            ]
            .value_counts()
            .reset_index()
        )

        grupos.columns = [
            "Tipo de Vehículo",
            "Cantidad"
        ]

        self.mostrar_dataframe(
            grupos
        )

    def ver_historial(self):
        self.canvas.hide()
        self.tabla.hide()
        self.resultados.show()
        historial = mostrar_historial()

        texto = ""

        for registro in historial:
            texto += str(registro) + "\n"

        self.resultados.setText(texto)

    def grafico_tipo(self):

        self.canvas.show()
        self.resultados.hide()
        self.figura.clear()

        ax = self.figura.add_subplot(111)

        conteo = self.datos[
            "TIPO_VEHICULO"
        ].value_counts()

        conteo.plot(
            kind="barh",
            ax=ax
        )

        ax.set_title(
            "Accidentes por Tipo de Vehículo"
        )

        ax.set_xlabel(
            "Tipo de Vehículo"
        )

        ax.set_ylabel(
            "Cantidad de Accidentes"
        )

        self.canvas.draw()
    def grafico_edad(self):

        self.canvas.show()
        self.resultados.hide()

        self.figura.clear()

        ax = self.figura.add_subplot(111)

        edades = self.datos["EDAD_VEHICULO"]

        ax.hist(
            edades,
            bins=20
        )

        ax.set_title(
            "Distribución de Edad de los Vehículos"
        )

        ax.set_xlabel(
            "Edad del Vehículo"
        )

        ax.set_ylabel(
            "Frecuencia"
        )

        self.canvas.draw()

    def exportar_csv(self):

        datos = self.datos.values.tolist() #Expota todos los registros

        guardar_resultado(
            datos,
            "exportacion_datalab",
            "csv"
        )
        self.tabla.hide()
        self.resultados.show()
        self.resultados.setText(
            "Archivo exportacion_datalab.csv guardado correctamente."
        )

app = QApplication(sys.argv)

ventana = Ventana()
ventana.show()

sys.exit(app.exec_())