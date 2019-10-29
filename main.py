import sys
from PyQt5 import QtWidgets
import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
from matplotlib import interactive
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import mainwindow
import firstwindow
import secondwindow


class MainWindow(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.openFirstWindow)
        self.pushButton_2.clicked.connect(self.openSecondWindow)
        self.pushButton_3.clicked.connect(self.close)

    def openFirstWindow(self):
        self.firstWindow = FirstWindow()
        self.firstWindow.show()
        self.hide()

    def openSecondWindow(self):
        self.secondWindow = SecondWindow()
        self.secondWindow.show()
        self.hide()


class FirstWindow(QtWidgets.QMainWindow, firstwindow.Ui_FirstWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.setTabel('users'))
        self.pushButton_2.clicked.connect(lambda: self.setTabel('characters'))
        self.pushButton_3.clicked.connect(lambda: self.setTabel('achievements'))
        self.pushButton_4.clicked.connect(lambda: self.setTabel('locations'))
        self.pushButton_5.clicked.connect(lambda: self.setTabel('general_statistic'))
        self.pushButton_6.clicked.connect(self.firstGraph)
        self.pushButton_7.clicked.connect(self.secondGraph)
        self.pushButton_8.clicked.connect(self.thirdGraph)
        self.pushButton_9.clicked.connect(self.openMainWindow)
        self.pushButton_10.clicked.connect(self.saveTabel)
        self.pushButton_11.clicked.connect(self.addRow)
        self.pushButton_12.clicked.connect(self.deleteRow)

    def openMainWindow(self):
        self.mainWindow = MainWindow()
        self.mainWindow.show()
        self.hide()

    def setTabel(self, table_name):
        conn = sqlite3.connect('database.db')
        conn.execute('PRAGMA foreign_keys = 1')
        self.name = table_name
        self.table = pd.read_sql_query('SELECT * from {0}'.format(self.name), conn)
        self.tableWidget.clear()
        self.tableWidget.setRowCount(self.table.shape[0])
        self.tableWidget.setColumnCount(self.table.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(self.table.keys())

        col = 0
        for j in self.table.keys():
            row = 0
            for i in self.table[j]:
                cellinfo = QtWidgets.QTableWidgetItem(str(i))
                self.tableWidget.setItem(row, col, cellinfo)
                row += 1
            col += 1

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(True)

    def saveTabel(self):
        try:
            conn = sqlite3.connect('database.db')
            conn.execute('PRAGMA foreign_keys = 1')
            cursor = conn.cursor()
            headers = []

            for row in conn.execute('''PRAGMA table_info('{0}')'''.format(self.name)).fetchall():
                headers.append(row[1])

            outer_data = []
            id = []
            for row in cursor.execute('SELECT {0} FROM {1}'.format(headers[0], self.name)):
                id.append('{0}'.format(row[0]))

            if len(id) == self.tableWidget.rowCount():
                for i in range(self.tableWidget.rowCount()):
                    inner_data = []
                    for j in range(1, self.tableWidget.columnCount()):
                        inner_data.append(self.tableWidget.item(i, j).text())
                    inner_data.append(id[i])
                    outer_data.append(inner_data)

                conc = ''
                for x in range(1, len(headers) - 1):
                    conc = conc + '{0}=?,'.format(headers[x]) + ' '
                conc = conc + headers[len(headers) - 1] + '=?'

                cursor.executemany('UPDATE {0} SET {1} WHERE {2}'.format(self.name, conc, headers[0] + '=?'), outer_data)
                conn.commit()

                outer_id = []
                for i in range(self.tableWidget.rowCount()):
                    inner_id = []
                    inner_id.append(self.tableWidget.item(i, 0).text())
                    inner_id.append(self.tableWidget.item(i, 1).text())
                    outer_id.append(inner_id)
                cursor.executemany('UPDATE {0} SET {1} WHERE {2}'.format(self.name, headers[0] + '=?', headers[1] + '=?'),
                                   outer_id)
                conn.commit()
            else:
                for i in range(len(id), self.tableWidget.rowCount()):
                    table_data = []
                    for j in range(self.tableWidget.columnCount()):
                        table_data.append(self.tableWidget.item(i, j).text())
                    table_data = tuple(table_data)
                    cursor.execute('INSERT INTO {0} VALUES {1}'.format(self.name, table_data))
                conn.commit()
            QtWidgets.QMessageBox.information(self, 'Информация', 'Сохранение успешно выполнено!',
                                              QtWidgets.QMessageBox.Ok)
        except AttributeError:
            if self.tableWidget.rowCount() == 0:
                QtWidgets.QMessageBox.question(self, 'Ошибка сохранения', 'Сначала откройте таблицу!',
                                               QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.question(self, 'Ошибка заполнения', 'Заполните таблицу!',
                                               QtWidgets.QMessageBox.Ok)
        except sqlite3.IntegrityError:
            QtWidgets.QMessageBox.question(self, 'Ошибка данных', 'Проверьте данные на соответствие типу '
                                           'или проверьте уникальность идентификатора!',
                                           QtWidgets.QMessageBox.Ok)

    def deleteRow(self):
        try:
            current_row = self.tableWidget.currentRow()
            conn = sqlite3.connect('database.db')
            conn.execute('PRAGMA foreign_keys = 1')
            cursor = conn.cursor()
            headers = []
            for row in conn.execute('''PRAGMA table_info('{0}')'''.format(self.name)).fetchall():
                headers.append(row[1])
            cursor.execute('DELETE FROM {0} WHERE {1} = {2}'.format(self.name, headers[0],
                                                                    self.tableWidget.item(current_row, 0).text()))
            conn.commit()
            self.tableWidget.removeRow(current_row)
        except AttributeError:
            QtWidgets.QMessageBox.question(self, 'Ошибка', 'Сначала откройте таблицу!', QtWidgets.QMessageBox.Ok)

    def addRow(self):
        if self.tableWidget.rowCount() == 0:
            QtWidgets.QMessageBox.question(self, 'Ошибка', 'Сначала откройте таблицу!', QtWidgets.QMessageBox.Ok)
        else:
            self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
            self.tableWidget.verticalHeader().setVisible(False)
            self.tableWidget.verticalHeader().setVisible(True)
            self.tableWidget.hide()
            self.tableWidget.show()

    def firstGraph(self):
        interactive(True)
        conn = sqlite3.connect('database.db')
        data_table = pd.read_sql_query('SELECT time_played_in_hours from {0}'.format('characters'), conn)
        data = [i for i in data_table['time_played_in_hours']]
        labels_table = pd.read_sql_query('SELECT nickname from {0}'.format('characters'), conn)
        labels = [i for i in labels_table['nickname']]

        def func(pct, allvals):
            absolute = int(pct / 100. * np.sum(allvals))
            return "{:.1f}%\n({:d} h)".format(pct, absolute)

        fig, ax = plt.subplots()
        ax.pie(data, labels=labels, autopct=lambda pct: func(pct, data))
        plt.title('Круговая диаграмма (количество сыгранных часов)')

    def secondGraph(self):
        interactive(True)
        conn = sqlite3.connect('database.db')
        gold_table = pd.read_sql_query('SELECT gold_earned from {0}'.format('general_statistic'), conn)
        gold = [i for i in gold_table['gold_earned']]
        days_table = pd.read_sql_query('SELECT day from {0}'.format('general_statistic'), conn)
        days = [i for i in days_table['day']]

        fig, ax = plt.subplots()
        ax.bar(days, gold, width=0.5)
        ax.set_xlabel('День')
        ax.set_ylabel('Количество золота')
        plt.title('Столбчатая диаграмма (заработанное золото по дням)')
        plt.xticks(np.arange(min(days), max(days)+1, 1.0))

    def thirdGraph(self):
        interactive(True)
        conn = sqlite3.connect('database.db')
        mobs_table = pd.read_sql_query('SELECT mobs_killed from {0}'.format('general_statistic'), conn)
        mobs = [i for i in mobs_table['mobs_killed']]
        days_table = pd.read_sql_query('SELECT day from {0}'.format('general_statistic'), conn)
        days = [i for i in days_table['day']]

        fig, ax = plt.subplots()
        ax.plot(days, mobs, '-r', marker='.', markersize=10)
        ax.set_xlabel('День')
        ax.set_ylabel('Число побеждённых мобов')
        plt.title('Линейная диаграмма (число побеждённых мобов по дням)')
        plt.xticks(np.arange(min(days), max(days)+1, 1.0))


class SecondWindow(QtWidgets.QMainWindow, secondwindow.Ui_SecondWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.openMainWindow)

        self.data = pd.read_csv('data.csv')
        self.graph = self.linear_regression(self.data['x'], self.data['y'])
        self.data['new_y'] = self.new_y

        self.setTable()
        self.setGraph()
        self.label.setText('loss = {0}'.format(self.loss))

    def openMainWindow(self):
        self.mainWindow = MainWindow()
        self.mainWindow.show()
        self.hide()

    def setTable(self):
        self.tableWidget.setRowCount(self.data.shape[0])
        self.tableWidget.setColumnCount(self.data.shape[1])

        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(self.data.keys())

        col = 0
        for i in self.data.keys():
            row = 0
            for j in self.data[i]:
                cellinfo = QtWidgets.QTableWidgetItem(str(j))
                self.tableWidget.setItem(row, col, cellinfo)
                row += 1
            col += 1

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setVisible(False)

    def setGraph(self):
        interactive(False)
        data = pd.read_csv('data.csv')
        fig, ax1 = plt.subplots()
        ax1.plot(data['x'], data['y'], marker='.')
        ax1.plot(data['x'], self.new_y)
        plotWidget = FigureCanvas(fig)
        toolbar = NavigationToolbar(plotWidget, self)
        toolbar.sizeHint()
        lay = QtWidgets.QVBoxLayout(self.widget)
        lay.addWidget(plotWidget)
        lay.addWidget(toolbar)

    def linear_regression(self, x, y):
        n = len(x)
        sum_xy = sum(x * y)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_x2 = sum(x ** 2)

        a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
        b = (sum_y - a * sum_x) / n

        self.new_y = a * x + b
        self.loss = sum(self.new_y - y) / n


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
