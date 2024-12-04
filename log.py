from PyQt5 import QtCore, QtGui, QtWidgets
from signup import Ui_Dialog_1


class Ui_Dialog(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_1()
        self.ui.setupUi(self.window)
        self.window.show()



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 620)
        Dialog.setStyleSheet("background-color: rgb(16, 16, 16);\n"
"color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 100, 111, 71))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size:28pt;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 230, 81, 31))
        self.label_2.setStyleSheet("color: rgb(170, 0, 0);\n"
"font-size:15pt;")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(180, 230, 261, 31))
        self.lineEdit.setStyleSheet("font-size:14pt;\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 310, 261, 31))
        self.lineEdit_2.setStyleSheet("font-size:14pt;\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 310, 121, 31))
        self.label_3.setStyleSheet("color: rgb(170, 0, 0);\n"
"font-size:15pt;")
        self.label_3.setObjectName("label_3")
        self.login = QtWidgets.QPushButton(Dialog)
        self.login.setGeometry(QtCore.QRect(312, 420, 121, 28))
        self.login.setStyleSheet("background-color: rgb(137, 137, 159);\n"
"color: rgb(255, 255, 255);\n"
"font-size:14pt")
        self.login.setObjectName("login")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(170, 380, 141, 16))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.Signup_1 = QtWidgets.QPushButton(Dialog)
        self.Signup_1.setGeometry(QtCore.QRect(310, 370, 93, 28))
        self.Signup_1.setStyleSheet("background-color: rgb(79, 79, 79);")
        self.Signup_1.setObjectName("Signup_1")
        self.Signup_1.clicked.connect(self.openWindow)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Login"))
        self.label_2.setText(_translate("Dialog", "Email"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.login.setText(_translate("Dialog", "Login"))
        self.label_4.setText(_translate("Dialog", "Don\'t have an account?"))
        self.Signup_1.setText(_translate("Dialog", "Sign Up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())