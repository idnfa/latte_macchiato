# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verd_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.verd_btn.setGeometry(QtCore.QRect(160, 390, 311, 31))
        self.verd_btn.setObjectName("verd_btn")
        self.id_line = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.id_line.setEnabled(True)
        self.id_line.setGeometry(QtCore.QRect(120, 80, 113, 22))
        self.id_line.setText("")
        self.id_line.setObjectName("id_line")
        self.name_line = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.name_line.setEnabled(True)
        self.name_line.setGeometry(QtCore.QRect(120, 110, 113, 22))
        self.name_line.setText("")
        self.name_line.setObjectName("name_line")
        self.taste_line = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.taste_line.setEnabled(True)
        self.taste_line.setGeometry(QtCore.QRect(120, 210, 113, 22))
        self.taste_line.setObjectName("taste_line")
        self.price_line = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.price_line.setEnabled(True)
        self.price_line.setGeometry(QtCore.QRect(120, 240, 113, 22))
        self.price_line.setObjectName("price_line")
        self.volume_line = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.volume_line.setEnabled(True)
        self.volume_line.setGeometry(QtCore.QRect(120, 270, 113, 22))
        self.volume_line.setObjectName("volume_line")
        self.roast_box = QtWidgets.QComboBox(parent=self.centralwidget)
        self.roast_box.setEnabled(True)
        self.roast_box.setGeometry(QtCore.QRect(120, 140, 73, 22))
        self.roast_box.setObjectName("roast_box")
        self.roast_box.addItem("")
        self.roast_box.addItem("")
        self.roast_box.addItem("")
        self.grind_box = QtWidgets.QComboBox(parent=self.centralwidget)
        self.grind_box.setEnabled(True)
        self.grind_box.setGeometry(QtCore.QRect(120, 180, 73, 22))
        self.grind_box.setObjectName("grind_box")
        self.grind_box.addItem("")
        self.grind_box.addItem("")
        self.grind_box.addItem("")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(410, 90, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 120, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 150, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 180, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 210, 111, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(410, 240, 55, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(410, 270, 111, 16))
        self.label_7.setObjectName("label_7")
        self.statuslabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.statuslabel.setGeometry(QtCore.QRect(220, 20, 161, 16))
        self.statuslabel.setText("")
        self.statuslabel.setObjectName("statuslabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.verd_btn.setText(_translate("MainWindow", "потвердить изменения в бд"))
        self.roast_box.setItemText(0, _translate("MainWindow", "светлая"))
        self.roast_box.setItemText(1, _translate("MainWindow", "средняя"))
        self.roast_box.setItemText(2, _translate("MainWindow", "темная"))
        self.grind_box.setItemText(0, _translate("MainWindow", "мелкий"))
        self.grind_box.setItemText(1, _translate("MainWindow", "средний"))
        self.grind_box.setItemText(2, _translate("MainWindow", "крупный"))
        self.label.setText(_translate("MainWindow", "ID"))
        self.label_2.setText(_translate("MainWindow", "Сорт"))
        self.label_3.setText(_translate("MainWindow", "Обжарка"))
        self.label_4.setText(_translate("MainWindow", "Помол"))
        self.label_5.setText(_translate("MainWindow", "Описание вкуса"))
        self.label_6.setText(_translate("MainWindow", "Цена"))
        self.label_7.setText(_translate("MainWindow", "Объем упаковки"))