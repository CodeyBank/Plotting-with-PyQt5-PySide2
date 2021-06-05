from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen, QFont
from PyQt5.QtCore import Qt
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = MySQLdb.connect(host='localhost', user='root', password='Thebossm@#995', db="library", port=3310)
        self.cur = self.db.cursor()

        self.setWindowTitle("DonutChart Example")
        self.setGeometry(100, 100, 1280, 600)

        self.show()

        self.createDonutChart()

    def createDonutChart(self):
        # ---------------------- SQL QUERIES ------------------------------------------------------------------#
        self.cur.execute('SELECT count(book_category) from library.book where book_category = "Literature"')
        literature = self.cur.fetchone()
        self.cur.execute('SELECT count(book_category) from library.book where book_category = "Science and Technology"')
        sci_tech = self.cur.fetchone()
        self.cur.execute('SELECT count(book_category) from library.book where book_category = "Art"')
        arts = self.cur.fetchone()
        self.cur.execute('SELECT count(book_category) from library.book where book_category = "International Politics"')
        int_pol = self.cur.fetchone()
        # ---------------------------- END of SQL QUERIES _------------------------------------------------------#

        # Create all the normalized values for the table
        total = literature[0] + sci_tech[0] + arts[0] + int_pol[0]
        norm_lit = literature[0] / total * 100
        norm_sc = sci_tech[0] / total * 100
        norm_arts = arts[0] / total * 100
        norm_intPol = int_pol[0] / total * 100

        # Start creating the chart object
        # series = QPieSeries()
        # series.setHoleSize(0.35)
        # lit = ("Literature" + str(norm_lit))
        # series.append(lit, norm_lit)
        # slice1 = QPieSlice()
        # slice1 = series.append(("Arts " + str(norm_arts)), norm_arts)
        # slice1.setExploded()
        # slice1.setLabelVisible()
        # science = ("Science " + str(norm_sc))
        # series.append(science, norm_sc)
        # intPolitics = ("International Politics " + str(norm_intPol))
        # series.append(intPolitics, norm_intPol)

        series = QPieSeries()
        series.setHoleSize(0.35)
        series.append("Literature", norm_lit)
        series.append("International Politics", norm_intPol)
        series.append("Arts", norm_arts)
        series.append("Science", norm_sc)
        series.setLabelsVisible(True)

        categories = ["Literature", "International Politics", "Arts", "Science"]

        series.setLabelsPosition(QPieSlice.LabelOutside)
        for slice, description in zip(series.slices(), categories):
            slice.setLabel("{} {:.2f}%".format(description, (100 * slice.percentage())))

        chart = QChart()
        chart.createDefaultAxes()
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignRight)

        chart.addSeries(series)
        series.setLabelsPosition(QPieSlice.LabelInsideHorizontal)

        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTheme(QChart.ChartThemeLight)

        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chartView)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
