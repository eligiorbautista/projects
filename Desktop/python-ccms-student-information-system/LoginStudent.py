# Form implementation generated from reading ui file 'LoginStudent.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets



class Ui_LoginStudent(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(542, 272)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/ccmslogo.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 271, 271))
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setStyleSheet("QFrame{background-color:rgb(243, 243, 243);}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(20, 150, 241, 81))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(999, 999))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(25, 39, 65);border:none")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(80, 30, 121, 121))
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(999, 999))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border:none")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/ccmslogo.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(270, 0, 271, 271))
        self.frame.setStyleSheet("background-color:rgb(34, 54, 90)")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 251, 231))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("border:1px solid white;color:white;")
        self.groupBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.groupBox.setObjectName("groupBox")
        self.LineEditPassword = QtWidgets.QLineEdit(self.groupBox)
        self.LineEditPassword.setGeometry(QtCore.QRect(40, 100, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.LineEditPassword.setFont(font)
        self.LineEditPassword.setStyleSheet("background-color:white;color:black;border:1px solid black")
        self.LineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.LineEditPassword.setPlaceholderText(" Password")
        self.LineEditPassword.setObjectName("LineEditPassword")
        self.LineEditUsername = QtWidgets.QLineEdit(self.groupBox)
        self.LineEditUsername.setGeometry(QtCore.QRect(40, 60, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.LineEditUsername.setFont(font)
        self.LineEditUsername.setStyleSheet("background-color:white;color:black;border:1px solid black")
        self.LineEditUsername.setObjectName("LineEditUsername")
        self.ButtonLogin = QtWidgets.QPushButton(self.groupBox)
        self.ButtonLogin.setGeometry(QtCore.QRect(150, 140, 71, 22))
        self.ButtonLogin.setStyleSheet("background-color:rgb(177, 177, 177);color:black")
        self.ButtonLogin.setIconSize(QtCore.QSize(15, 15))
        self.ButtonLogin.setObjectName("ButtonLogin")
        self.ButtonLogin.clicked.connect(self.LoginAccount)
        Form.setTabOrder(self.LineEditUsername,self.LineEditPassword)
        Form.setTabOrder(self.LineEditPassword,self.ButtonLogin)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def LoginAccount(self):
        if len(self.LineEditUsername.text()) != 0 and len(self.LineEditPassword.text()) != 0:
            import mysql.connector
            DatabaseConnection = mysql.connector.connect(host = 'localhost',user = 'root', password = 'root',database = 'ccms_studentinfosystem')
            DatabaseCursor = DatabaseConnection.cursor()
            DatabaseCursor.execute('select * from studentaccountstb')
            Accounts = DatabaseCursor.fetchall()

            Validation = 0
            for Account in Accounts:
                if Account[0] == self.LineEditUsername.text() and Account[1] == self.LineEditPassword.text():
                    Validation += 1


            if Validation > 0:
                from PyQt6.QtWidgets import QMessageBox
                self.mbox = QMessageBox()
                self.mbox.setWindowIcon(QtGui.QIcon("images/ccmslogo.jpg"))
                self.mbox.setWindowTitle(' ')
                self.mbox.setIcon(QMessageBox.Icon.Information)
                self.mbox.setText('Login Success.')
                self.mbox.setInformativeText(f'Welcome {self.LineEditUsername.text()}.')
                self.mbox.show()
            else:
                from PyQt6.QtWidgets import QMessageBox
                self.mbox = QMessageBox()
                self.mbox.setWindowIcon(QtGui.QIcon("images/ccmslogo.jpg"))
                self.mbox.setIcon(QMessageBox.Icon.Warning)
                self.mbox.setWindowTitle(' ')
                self.mbox.setText('Incorrect username / password.')
                self.mbox.setInformativeText('Please check your inputs.')
                self.mbox.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowIcon(QtGui.QIcon('images/ccmslogo.jpg'))
        Form.setWindowTitle(_translate("Form", "CCMS Student Information System | Student Login"))
        self.label.setText(_translate("Form", "CCMS Student\n"
"Information System"))
        self.groupBox.setTitle(_translate("Form", "STUDENT LOGIN"))
        self.LineEditUsername.setPlaceholderText(_translate("Form", " Username"))
        self.ButtonLogin.setText(_translate("Form", "Login"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_LoginStudent()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())