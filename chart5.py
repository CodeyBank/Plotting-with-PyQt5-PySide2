import sys, random
from PyQt5 import QtWidgets, uic
from pyqtgraph import PlotWidget
import pyqtgraph as pg
from PyQt5.QtChart import QChart, QChartView, QBarSet, QPercentBarSeries, QBarCategoryAxis, QBarSet, QValueAxis, QBarSeries
from PyQt5.QtGui import QPainter
from PyQt5.uic import loadUiType
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPainter

ui, _ = loadUiType('frameForPlot.ui')


class MainWindow(QMainWindow, ui):

    def __init__(self, *args, **kwargs):
        # super(MainWindow, self).__init__(*args, **kwargs)
        # initialise window widgets
        QMainWindow.__init__(self)
        self.resize(800, 600)
        self.setupUi(self)
        self.plotGraph()
        self.plotGraph2()

    def plotGraph(self):
        set0 = QBarSet("Parwiz")
        set1 = QBarSet("Bob")
        set2 = QBarSet("Tom")
        set3 = QBarSet("Logan")
        set4 = QBarSet("Karim")

        set0 << 1 << 2 << 3 << 4 << 5 << 6
        set1 << 5 << 0 << 0 << 4 << 0 << 7
        set2 << 3 << 5 << 8 << 13 << 8 << 5
        set3 << 5 << 6 << 7 << 3 << 4 << 5
        set4 << 9 << 7 << 5 << 3 << 1 << 2

        series = QPercentBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)
        series.append(set3)
        series.append(set4)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Percent Example")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
        axis = QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)

        self.container.setContentsMargins(0, 0, 0, 0)

        lay = QtWidgets.QVBoxLayout(self.container)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(chartView)

    def plotGraph2(self):
        set0 = QBarSet('X0')
        set1 = QBarSet('X1')
        set2 = QBarSet('X2')
        set3 = QBarSet('X3')
        set4 = QBarSet('X4')

        set0.append([random.randint(1, 10) for i in range(0, 6)])
        set1.append([random.randint(1, 10) for i in range(0, 6)])
        set2.append([random.randint(1, 10) for i in range(0, 6)])
        set3.append([random.randint(1, 10) for i in range(0, 6)])
        set4.append([random.randint(1, 10) for i in range(0, 6)])

        series = QBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)
        series.append(set3)
        series.append(set4)

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

        self.container2.setContentsMargins(0, 0, 0, 0)

        lay1 = QtWidgets.QVBoxLayout(self.container2)
        lay1.setContentsMargins(0, 0, 0, 0)
        lay1.addWidget(chartView)
        # self.setCentralWidget(chartView2)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
