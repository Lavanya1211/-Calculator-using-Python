import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QDialog, QApplication, QDesktopWidget
from PyQt5.uic import loadUi
from PyQt5.uic.properties import QtGui


class MainLogin(QDialog):

    def __init__(self):
        super(MainLogin, self).__init__()
        loadUi("Calculator1.ui", self)
        self.mainloginbutton_13.clicked.connect(self.method_1)
        self.mainloginbutton_19.clicked.connect(self.method_2)
        self.mainloginbutton_24.clicked.connect(self.method_3)
        self.mainloginbutton_14.clicked.connect(self.method_4)
        self.mainloginbutton_20.clicked.connect(self.method_5)
        self.mainloginbutton_21.clicked.connect(self.method_6)
        self.mainloginbutton_15.clicked.connect(self.method_7)
        self.mainloginbutton_18.clicked.connect(self.method_8)
        self.mainloginbutton_22.clicked.connect(self.method_9)
        self.mainloginbutton_16.clicked.connect(self.method_zero)
        self.mainloginbutton.clicked.connect(self.method_clear)
        self.mainloginbutton_2.clicked.connect(self.method_del)
        self.mainloginbutton_23.clicked.connect(self.method_dot)
        self.mainloginbutton_12.clicked.connect(self.method_add)
        self.mainloginbutton_11.clicked.connect(self.method_sub)
        self.mainloginbutton_10.clicked.connect(self.method_mul)
        self.mainloginbutton_9.clicked.connect(self.method_div)
        self.mainloginbutton_8.clicked.connect(self.method_equal)

    def method_1(self):
        text = self.label.text()
        self.label.setText(text + "1")

    def method_2(self):
        text = self.label.text()
        self.label.setText(text + "2")

    def method_3(self):
        text = self.label.text()
        self.label.setText(text + "3")

    def method_4(self):
        text = self.label.text()
        self.label.setText(text + "4")

    def method_5(self):
        text = self.label.text()
        self.label.setText(text + "5")

    def method_6(self):
        text = self.label.text()
        self.label.setText(text + "6")

    def method_7(self):
        text = self.label.text()
        self.label.setText(text + "7")

    def method_8(self):
        text = self.label.text()
        self.label.setText(text + "8")

    def method_9(self):
        text = self.label.text()
        self.label.setText(text + "9")

    def method_zero(self):
        text = self.label.text()
        self.label.setText(text + "0")

    def method_dot(self):
        text = self.label.text()
        self.label.setText(text + ".")

    def method_add(self):
        text = self.label.text()
        self.label.setText(text + "+")

    def method_sub(self):
        text = self.label.text()
        self.label.setText(text + "-")

    def method_mul(self):
        text = self.label.text()
        self.label.setText(text + "*")

    def method_div(self):
        text = self.label.text()
        self.label.setText(text + "/")

    def method_clear(self):
        from pydoc import text
        self.label.setText("")

    def method_del(self):
        text = self.label.text()
        self.label.setText(text[:len(text) - 1])

    def method_equal(self):
        text = self.label.text()

        try:
            ans =eval(text)
            self.label.setText(str(round(ans ,2)))
        except:
            self.label.setText("Wrong Input")


app = QApplication(sys.argv)
window = MainLogin()
widget = QtWidgets.QStackedWidget()
widget.addWidget(window)
widget.setFixedHeight(474)
widget.setFixedWidth(310)
widget.show()
app.exec_()
