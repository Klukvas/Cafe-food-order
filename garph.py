# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graph.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindows(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(823, 443)
        MainWindow.setMinimumSize(QtCore.QSize(567, 186))
        MainWindow.setMaximumSize(QtCore.QSize(1111111, 16777215))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon.fromTheme("Школьнаястоловая")
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-color: rgb(179, 179, 179);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(76, 76, 76);\n"
"    color: rgb(255, 255, 255)\n"
"\n"
"}\n"
"")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        MainWindow.setDocumentMode(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 0, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(470, 180, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setMouseTracking(True)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setLineWidth(0)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setIndent(1)
        self.label_2.setObjectName("label_2")
        self.del_dish = QtWidgets.QPushButton(self.centralwidget)
        self.del_dish.setGeometry(QtCore.QRect(690, 190, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.del_dish.setFont(font)
        self.del_dish.setObjectName("del_dish")
        self.make_order = QtWidgets.QPushButton(self.centralwidget)
        self.make_order.setGeometry(QtCore.QRect(300, 360, 521, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.make_order.setFont(font)
        self.make_order.setObjectName("make_order")
        self.order = QtWidgets.QListWidget(self.centralwidget)
        self.order.setGeometry(QtCore.QRect(470, 200, 211, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.order.setFont(font)
        self.order.setStyleSheet("")
        self.order.setObjectName("order")
        self.del_all = QtWidgets.QPushButton(self.centralwidget)
        self.del_all.setGeometry(QtCore.QRect(690, 230, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.del_all.setFont(font)
        self.del_all.setObjectName("del_all")
        self.menuWidg = QtWidgets.QListWidget(self.centralwidget)
        self.menuWidg.setGeometry(QtCore.QRect(300, 20, 321, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.menuWidg.setFont(font)
        self.menuWidg.setStyleSheet("")
        self.menuWidg.setObjectName("menuWidg")
        self.for_pic = QtWidgets.QLabel(self.centralwidget)
        self.for_pic.setGeometry(QtCore.QRect(10, 290, 271, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.for_pic.setFont(font)
        self.for_pic.setAutoFillBackground(False)
        self.for_pic.setText("")
        self.for_pic.setObjectName("for_pic")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(690, 270, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.menuWidg_2 = QtWidgets.QListWidget(self.centralwidget)
        self.menuWidg_2.setGeometry(QtCore.QRect(690, 290, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.menuWidg_2.setFont(font)
        self.menuWidg_2.setStyleSheet("")
        self.menuWidg_2.setObjectName("menuWidg_2")
        self.pizza = QtWidgets.QPushButton(self.centralwidget)
        self.pizza.setGeometry(QtCore.QRect(10, 40, 121, 101))
        self.pizza.setMinimumSize(QtCore.QSize(121, 101))
        self.pizza.setMaximumSize(QtCore.QSize(121, 101))
        self.pizza.setText("")
        self.pizza.setObjectName("pizza")
        self.drinks = QtWidgets.QPushButton(self.centralwidget)
        self.drinks.setGeometry(QtCore.QRect(10, 180, 121, 101))
        self.drinks.setMinimumSize(QtCore.QSize(121, 101))
        self.drinks.setMaximumSize(QtCore.QSize(121, 101))
        self.drinks.setText("")
        self.drinks.setObjectName("drinks")
        self.desserts = QtWidgets.QPushButton(self.centralwidget)
        self.desserts.setGeometry(QtCore.QRect(150, 40, 121, 101))
        self.desserts.setMinimumSize(QtCore.QSize(121, 101))
        self.desserts.setMaximumSize(QtCore.QSize(121, 101))
        self.desserts.setText("")
        self.desserts.setObjectName("desserts")
        self.sides = QtWidgets.QPushButton(self.centralwidget)
        self.sides.setGeometry(QtCore.QRect(150, 180, 121, 101))
        self.sides.setText("")
        self.sides.setObjectName("sides")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(300, 200, 161, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 180, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.price_dish = QtWidgets.QLineEdit(self.centralwidget)
        self.price_dish.setGeometry(QtCore.QRect(640, 20, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.price_dish.setFont(font)
        self.price_dish.setObjectName("price_dish")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(640, 0, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(150, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(150, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(150, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label.raise_()
        self.label_2.raise_()
        self.del_dish.raise_()
        self.make_order.raise_()
        self.order.raise_()
        self.del_all.raise_()
        self.menuWidg.raise_()
        self.label_4.raise_()
        self.menuWidg_2.raise_()
        self.pizza.raise_()
        self.drinks.raise_()
        self.desserts.raise_()
        self.sides.raise_()
        self.listWidget.raise_()
        self.label_3.raise_()
        self.for_pic.raise_()
        self.price_dish.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 823, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuTheme = QtWidgets.QMenu(self.menuBar)
        self.menuTheme.setObjectName("menuTheme")
        MainWindow.setMenuBar(self.menuBar)
        self.actionGreen = QtWidgets.QAction(MainWindow)
        self.actionGreen.setObjectName("actionGreen")
        self.actionWhite = QtWidgets.QAction(MainWindow)
        self.actionWhite.setObjectName("actionWhite")
        self.menuTheme.addAction(self.actionGreen)
        self.menuTheme.addAction(self.actionWhite)
        self.menuBar.addAction(self.menuTheme.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Школьная столовая"))
        self.label.setText(_translate("MainWindow", "Меню"))
        self.label_2.setText(_translate("MainWindow", "Заказ"))
        self.del_dish.setText(_translate("MainWindow", "Удалить"))
        self.make_order.setText(_translate("MainWindow", "Заказать"))
        self.del_all.setText(_translate("MainWindow", "Удалить все"))
        self.label_4.setText(_translate("MainWindow", "Сумма заказа"))
        self.label_3.setText(_translate("MainWindow", "Ингредиенты"))
        self.label_5.setText(_translate("MainWindow", "Цена"))
        self.label_6.setText(_translate("MainWindow", "Пицца"))
        self.label_7.setText(_translate("MainWindow", "Напитки"))
        self.label_8.setText(_translate("MainWindow", "Десерты"))
        self.label_9.setText(_translate("MainWindow", "Десерты"))
        self.label_10.setText(_translate("MainWindow", "Сайды"))
        self.menuTheme.setTitle(_translate("MainWindow", "Theme"))
        self.actionGreen.setText(_translate("MainWindow", "Green"))
        self.actionWhite.setText(_translate("MainWindow", "White"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindows()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

