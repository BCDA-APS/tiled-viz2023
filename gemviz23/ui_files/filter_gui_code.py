import typing
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *  
from PyQt5.QtGui import *
import sys

from PyQt5.QtWidgets import QWidget


class Ui_MainWindow(MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName(u"MainWindow")
        self.resize(442, 474)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 10, 411, 401))
        self.TabWidgetPage1 = QWidget()
        self.TabWidgetPage1.setObjectName(u"TabWidgetPage1")
        self.InputLabel1 = QLabel(self.TabWidgetPage1)
        self.InputLabel1.setObjectName(u"InputLabel1")
        self.InputLabel1.setGeometry(QRect(20, 90, 61, 31))
        self.InputLabel2 = QLabel(self.TabWidgetPage1)
        self.InputLabel2.setObjectName(u"InputLabel2")
        self.InputLabel2.setGeometry(QRect(20, 130, 61, 31))
        self.InputLabel3 = QLabel(self.TabWidgetPage1)
        self.InputLabel3.setObjectName(u"InputLabel3")
        self.InputLabel3.setGeometry(QRect(20, 170, 61, 31))
        self.InputLabel4 = QLabel(self.TabWidgetPage1)
        self.InputLabel4.setObjectName(u"InputLabel4")
        self.InputLabel4.setGeometry(QRect(20, 210, 61, 31))
        self.InputLabel5 = QLabel(self.TabWidgetPage1)
        self.InputLabel5.setObjectName(u"InputLabel5")
        self.InputLabel5.setGeometry(QRect(20, 250, 61, 31))
        self.InputLabel6 = QLabel(self.TabWidgetPage1)
        self.InputLabel6.setObjectName(u"InputLabel6")
        self.InputLabel6.setGeometry(QRect(20, 290, 61, 31))
        self.InputLabel7 = QLabel(self.TabWidgetPage1)
        self.InputLabel7.setObjectName(u"InputLabel7")
        self.InputLabel7.setGeometry(QRect(20, 330, 61, 31))
        self.StartDateSelect = QDateEdit(self.TabWidgetPage1)
        self.StartDateSelect.setObjectName(u"StartDateSelect")
        self.StartDateSelect.setGeometry(QRect(290, 10, 91, 31))
        self.EndDateSelect = QDateEdit(self.TabWidgetPage1)
        self.EndDateSelect.setObjectName(u"EndDateSelect")
        self.EndDateSelect.setGeometry(QRect(290, 50, 91, 31))
        self.EndDateLabel = QLabel(self.TabWidgetPage1)
        self.EndDateLabel.setObjectName(u"EndDateLabel")
        self.EndDateLabel.setGeometry(QRect(210, 50, 81, 31))
        self.StartDateLabel = QLabel(self.TabWidgetPage1)
        self.StartDateLabel.setObjectName(u"StartDateLabel")
        self.StartDateLabel.setGeometry(QRect(210, 10, 71, 31))
        self.Status = QLabel(self.TabWidgetPage1)
        self.Status.setObjectName(u"Status")
        self.Status.setGeometry(QRect(20, 50, 61, 31))
        self.InputBox1 = QComboBox(self.TabWidgetPage1)
        self.InputBox1.setObjectName(u"InputBox1")
        self.InputBox1.setGeometry(QRect(80, 90, 311, 32))
        self.InputBox2 = QComboBox(self.TabWidgetPage1)
        self.InputBox2.setObjectName(u"InputBox2")
        self.InputBox2.setGeometry(QRect(80, 130, 311, 32))
        self.InputBox3 = QComboBox(self.TabWidgetPage1)
        self.InputBox3.setObjectName(u"InputBox3")
        self.InputBox3.setGeometry(QRect(80, 170, 311, 32))
        self.InputBox4 = QComboBox(self.TabWidgetPage1)
        self.InputBox4.setObjectName(u"InputBox4")
        self.InputBox4.setGeometry(QRect(80, 210, 311, 32))
        self.InputBox5 = QComboBox(self.TabWidgetPage1)
        self.InputBox5.setObjectName(u"InputBox5")
        self.InputBox5.setGeometry(QRect(80, 250, 311, 32))
        self.InputBox16 = QComboBox(self.TabWidgetPage1)
        self.InputBox16.setObjectName(u"InputBox16")
        self.InputBox16.setGeometry(QRect(80, 290, 311, 32))
        self.InputBox7 = QComboBox(self.TabWidgetPage1)
        self.InputBox7.setObjectName(u"InputBox7")
        self.InputBox7.setGeometry(QRect(80, 330, 311, 32))
        self.InputBox18 = QComboBox(self.TabWidgetPage1)
        self.InputBox18.setObjectName(u"InputBox18")
        self.InputBox18.setGeometry(QRect(80, 50, 121, 32))
        self.tabWidget.addTab(self.TabWidgetPage1, "")
        self.TabWidgetPage2 = QWidget()
        self.TabWidgetPage2.setObjectName(u"TabWidgetPage2")
        self.tabWidget.addTab(self.TabWidgetPage2, "")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.InputLabel1.setText(QCoreApplication.translate("MainWindow", u"Input 1", None))
        self.InputLabel2.setText(QCoreApplication.translate("MainWindow", u"Input 2", None))
        self.InputLabel3.setText(QCoreApplication.translate("MainWindow", u"Input 1", None))
        self.InputLabel4.setText(QCoreApplication.translate("MainWindow", u"Input 1", None))
        self.InputLabel5.setText(QCoreApplication.translate("MainWindow", u"Input 1", None))
        self.InputLabel6.setText(QCoreApplication.translate("MainWindow", u"Input 1", None))
        self.InputLabel7.setText(QCoreApplication.translate("MainWindow", u"Input 1", None))
        self.EndDateLabel.setText(QCoreApplication.translate("MainWindow", u"End Date", None))
        self.StartDateLabel.setText(QCoreApplication.translate("MainWindow", u"Start Date", None))
        self.Status.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabWidgetPage1), "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabWidgetPage2), QCoreApplication.translate("MainWindow", u"Page", None))
    # retranslateUi



def gui():
    """display the main widget"""
    app = QApplication(sys.argv)
    main_window = Ui_MainWindow()
    # print(f"{main_window.label=}")
    # print(f"{main_window.label.text()=}")
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    gui()

