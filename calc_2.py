# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equal.setGeometry(QtCore.QRect(330, 210, 110, 210))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_equal.setFont(font)
        self.btn_equal.setMouseTracking(False)
        self.btn_equal.setTabletTracking(False)
        self.btn_equal.setStyleSheet("background-color: rgb(247, 138, 49);")
        self.btn_equal.setObjectName("btn_equal")
        self.entered = QtWidgets.QLabel(self.centralwidget)
        self.entered.setGeometry(QtCore.QRect(0, 0, 440, 70))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.entered.setFont(font)
        self.entered.setStyleSheet("background-color: rgb(224, 205, 255);\n"
"color: rgb(3, 1, 74);\n"
"")
        self.entered.setObjectName("entered")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 70, 110, 70))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("background-color: rgb(123, 133, 170);")
        self.btn_1.setObjectName("btn_1")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(220, 70, 110, 70))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("background-color: rgb(123, 133, 170);")
        self.btn_3.setObjectName("btn_3")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(110, 140, 110, 70))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("background-color: rgb(123, 133, 170);")
        self.btn_5.setObjectName("btn_5")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 210, 110, 70))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("background-color: rgb(123, 133, 170);")
        self.btn_7.setObjectName("btn_7")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(110, 280, 110, 70))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("background-color: rgb(123, 133, 170);")
        self.btn_0.setObjectName("btn_0")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(220, 210, 110, 70))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("background-color: rgb(123, 133, 170);")
        self.btn_9.setObjectName("btn_9")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(110, 70, 110, 70))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("background-color: rgb(123, 133, 170);")
        self.btn_2.setObjectName("btn_2")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(220, 140, 110, 70))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("background-color: rgb(123, 133, 170);")
        self.btn_6.setObjectName("btn_6")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 140, 110, 70))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("background-color: rgb(123, 133, 170);")
        self.btn_4.setObjectName("btn_4")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(110, 210, 110, 70))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("background-color: rgb(123, 133, 170);")
        self.btn_8.setObjectName("btn_8")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(0, 280, 110, 70))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet("background-color: rgb(145, 0, 0);")
        self.btn_plus.setObjectName("btn_plus")
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(220, 280, 110, 70))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_minus.setFont(font)
        self.btn_minus.setStyleSheet("background-color: rgb(145, 0, 0);")
        self.btn_minus.setObjectName("btn_minus")
        self.btn_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.btn_multiply.setGeometry(QtCore.QRect(0, 350, 165, 70))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_multiply.setFont(font)
        self.btn_multiply.setStyleSheet("background-color: rgb(145, 0, 0);")
        self.btn_multiply.setObjectName("btn_multiply")
        self.btn_divide = QtWidgets.QPushButton(self.centralwidget)
        self.btn_divide.setGeometry(QtCore.QRect(165, 350, 165, 70))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_divide.setFont(font)
        self.btn_divide.setStyleSheet("background-color: rgb(145, 0, 0);")
        self.btn_divide.setObjectName("btn_divide")
        self.btn_del = QtWidgets.QPushButton(self.centralwidget)
        self.btn_del.setGeometry(QtCore.QRect(330, 70, 110, 70))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_del.setFont(font)
        self.btn_del.setStyleSheet("background-color: rgb(255, 193, 34);")
        self.btn_del.setObjectName("btn_del")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(330, 140, 110, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("background-color: rgb(255, 193, 34);")
        self.btn_clear.setObjectName("btn_clear")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MaSmallCalc"))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.entered.setText(_translate("MainWindow", "0"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_multiply.setText(_translate("MainWindow", "*"))
        self.btn_divide.setText(_translate("MainWindow", "/"))
        self.btn_del.setText(_translate("MainWindow", "<--"))
        self.btn_clear.setText(_translate("MainWindow", "C"))

    def add_functions(self):
        self.btn_0.clicked.connect(lambda: self.write_number(self.btn_0.text()))
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
        self.btn_plus.clicked.connect(lambda: self.write_operation(self.btn_plus.text()))
        self.btn_minus.clicked.connect(lambda: self.write_operation(self.btn_minus.text()))
        self.btn_divide.clicked.connect(lambda: self.write_operation(self.btn_divide.text()))
        self.btn_multiply.clicked.connect(lambda: self.write_operation(self.btn_multiply.text()))
        self.btn_equal.clicked.connect(self.calculate)
        self.btn_del.clicked.connect(self.delete)
        self.btn_clear.clicked.connect(self.clear)

    def clear(self):
        self.entered.setText('0')

    def delete(self):
        self.entered.setText(self.entered.text()[:-1])

    def write_number(self, number):
        if self.entered.text() == '0':
            self.entered.setText(number)
        else:
            self.entered.setText(self.entered.text() + number)

    def write_operation(self, operation):
        text = self.entered.text()
        if text in ("-", "0", ""):
            if operation == '-':
                self.entered.setText(operation)
            else:
                print("plug")
        elif text[-1] in ('+', '-', '*', '/'):
            self.entered.setText(text[:-1] + operation)
        else:
            self.entered.setText(text + operation)

    def calculate(self):
        error_window = QMessageBox()
        try:
            res = str(eval(self.entered.text()))
            self.entered.setText(res)
        except Exception as error:
            error_window.setWindowTitle("Error")
            error_window.setText("ERROR")
            error_window.setIcon(QMessageBox.Warning)
            error_window.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel|QMessageBox.Reset)
            error_window.setDefaultButton(QMessageBox.Ok)
            error_window.setInformativeText("An error occurred")
            error_window.setDetailedText(f"{error}")

            error_window.buttonClicked.connect(self.popup_action)

            error_window.exec_()

    def popup_action(self, btn):
        text = btn.text()
        if text == "Ok":
            print("OK pressed")
        elif text == "Reset":
            self.entered.setText('0')
        elif text == "Cancel":
            self.entered.setText(self.entered.text()[:-1])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
