from PyQt5 import QtChart
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtChart import QChart, QChartView, QValueAxis, QPieSeries, QPieSlice, QBarSet, QValueAxis, QBarCategoryAxis, QBarSeries
from PyQt5.QtGui import QPainter, QFont
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUiType
import random
import numpy as np
import matplotlib.pyplot as plt

mainApp, _ = loadUiType('frameForPlot.ui')


class Window(QMainWindow, mainApp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("PyQtChart Pie Chart")
        self.setGeometry(100, 100, 1280, 600)

        self.show()
        self.create_piechart()
        self.createDonutChart()
        # self.mathplot()

    def create_piechart(self):
        series = QtChart.QPieSeries()
        series.setHoleSize(0.35)
        series.append("Python", 80)
        series.append("C++", 70)
        series.append("Java", 50)
        series.append("C#", 40)
        series.append("PHP", 30)
        series.setLabelsVisible(True)

        series.setLabelsPosition(QtChart.QPieSlice.LabelInsideHorizontal)
        for slice1 in series.slices():
            slice1.setLabel("{:.2f}%".format(100 * slice1.percentage()))

        chart = QChart()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Pie Chart Example")
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chart.legend().markers(series)[0].setLabel("Python")
        chart.legend().markers(series)[1].setLabel("C++")
        chart.legend().markers(series)[2].setLabel("Java")
        chart.legend().markers(series)[3].setLabel("C#")
        chart.legend().markers(series)[4].setLabel("PHP")

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        self.container.setContentsMargins(0, 0, 0, 0)

        lay1 = QtWidgets.QHBoxLayout(self.container)
        lay1.setContentsMargins(0, 0, 0, 0)
        lay1.addWidget(chartview)

    def createDonutChart(self):
        set0 = QBarSet('X0')
        # set1 = QBarSet('X1')
        # set2 = QBarSet('X2')
        # set3 = QBarSet('X3')
        # set4 = QBarSet('X4')

        set0.append([random.randint(1, 10) for i in range(0, 6)])
        # set1.append([random.randint(1, 10) for i in range(0, 6)])
        # set2.append([random.randint(1, 10) for i in range(0, 6)])
        # set3.append([random.randint(1, 10) for i in range(0, 6)])
        # set4.append([random.randint(1, 10) for i in range(0, 6)])

        series = QBarSeries()
        series.append(set0)
        # series.append(set1)
        # series.append(set2)
        # series.append(set3)
        # series.append(set4)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Demonstration of Bar Charts")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun')

        axisX = QBarCategoryAxis()
        axisX.append(months)
        axisY = QValueAxis()
        axisY.setRange(0, 15)

        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
        # self.setCentralWidget(chartView)

        self.container2.setContentsMargins(0, 0, 0, 0)

        lay1 = QtWidgets.QVBoxLayout(self.container2)
        lay1.setContentsMargins(0, 0, 0, 0)
        lay1.addWidget(chartView)

    # def mathplot(self):
    #     house_prices = np.random.normal(200000, 25000, 5000)
    #     plt.hist(house_prices, 50)
    #     plt.show()


App = QApplication(sys.argv)
window = Window()
# window.show()
sys.exit(App.exec_())
