from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Registration(object):
    def setupUi(self, Registration):
        Registration.setObjectName("Registration")
        Registration.resize(742, 512)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/credit-card.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Registration.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Registration)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 741, 511))
        self.frame_2.setStyleSheet("background-color:rgb(7, 44, 112)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame = QtWidgets.QFrame(Registration)
        self.frame.setGeometry(QtCore.QRect(20, 20, 701, 471))
        self.frame.setStyleSheet("QFrame{background-color:rgb(11, 58, 151);border: 3px solid rgb(7, 44, 112)}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.btn_Minimize = QtWidgets.QPushButton(self.frame)
        self.btn_Minimize.setGeometry(QtCore.QRect(620, 0, 41, 38))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Minimize.setFont(font)
        self.btn_Minimize.setStyleSheet("background:none;border-radius: 16px;color:white")
        self.btn_Minimize.setFlat(True)
        self.btn_Minimize.setObjectName("btn_Minimize")
        self.btn_Exit = QtWidgets.QPushButton(self.frame)
        self.btn_Exit.setGeometry(QtCore.QRect(660, 0, 41, 38))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Exit.setFont(font)
        self.btn_Exit.setStyleSheet("background:none;border-radius: 16px;color:white")
        self.btn_Exit.setFlat(True)
        self.btn_Exit.setObjectName("btn_Exit")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(317, 41, 162, 54))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("border:none;color:white")
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(255, 43, 51, 51))
        self.label_7.setMinimumSize(QtCore.QSize(51, 51))
        self.label_7.setMaximumSize(QtCore.QSize(51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border:none;color:white")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("images/credit-card.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_ID = QtWidgets.QLabel(self.frame)
        self.label_ID.setGeometry(QtCore.QRect(20, 290, 55, 16))
        self.label_ID.setStyleSheet("background-color:rgb(11, 58, 151);color::rgb(11, 58, 151);border:none;")
        self.label_ID.setText("")
        self.label_ID.setObjectName("label_ID")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(110, 100, 481, 331))
        self.frame_3.setStyleSheet("background-color:rgb(7, 44, 111)")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.btn_Register = QtWidgets.QPushButton(self.frame_3)
        self.btn_Register.setGeometry(QtCore.QRect(370, 300, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.btn_Register.setFont(font)
        self.btn_Register.setStyleSheet("background-color:rgb(44, 48, 61);color:white")
        self.btn_Register.setObjectName("btn_Register")
        self.lineEdit_CardID = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_CardID.setGeometry(QtCore.QRect(30, 50, 191, 31))
        self.lineEdit_CardID.setStyleSheet("border:2px solid black;background-color:white;color:black;padding:2px")
        self.lineEdit_CardID.setText("")
        self.lineEdit_CardID.setObjectName("lineEdit_CardID")
        self.lineEdit_Pin = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_Pin.setGeometry(QtCore.QRect(260, 50, 191, 31))
        self.lineEdit_Pin.setStyleSheet("border:2px solid black;background-color:white;color:black;padding:2px")
        self.lineEdit_Pin.setText("")
        self.lineEdit_Pin.setObjectName("lineEdit_Pin")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 481, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border:none;color:white")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_Name = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_Name.setGeometry(QtCore.QRect(30, 100, 191, 31))
        self.lineEdit_Name.setStyleSheet("border:2px solid black;background-color:white;color:black;padding:2px")
        self.lineEdit_Name.setText("")
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.lineEdit_Email = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_Email.setGeometry(QtCore.QRect(260, 100, 191, 31))
        self.lineEdit_Email.setStyleSheet("border:2px solid black;background-color:white;color:black;padding:2px")
        self.lineEdit_Email.setText("")
        self.lineEdit_Email.setObjectName("lineEdit_Email")
        self.lineEdit_Contact = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_Contact.setGeometry(QtCore.QRect(30, 150, 191, 31))
        self.lineEdit_Contact.setStyleSheet("border:2px solid black;background-color:white;color:black;padding:2px")
        self.lineEdit_Contact.setText("")
        self.lineEdit_Contact.setObjectName("lineEdit_Contact")
        self.textEdit_Address = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit_Address.setGeometry(QtCore.QRect(30, 200, 421, 87))
        self.textEdit_Address.setStyleSheet("border:2px solid black;background-color:white;color:black;padding:2px")
        self.textEdit_Address.setObjectName("textEdit_Address")
        Registration.setCentralWidget(self.centralwidget)
        Registration.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        Registration.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.btn_Exit.clicked.connect(Registration.close)
        self.btn_Minimize.clicked.connect(Registration.showMinimized)
        self.btn_Register.clicked.connect(self.RegisterAccount)

        self.retranslateUi(Registration)
        QtCore.QMetaObject.connectSlotsByName(Registration)
    
    def RegisterAccount(self):
        CARD = self.lineEdit_CardID.text()
        PIN = self.lineEdit_Pin.text()
        NAME = self.lineEdit_Name.text()
        EMAIL = self.lineEdit_Email.text()
        CONTACT = self.lineEdit_Contact.text()
        ADDRESS = self.textEdit_Address.toPlainText()

        if len(CARD) != 0 and len(PIN) != 0 and len(NAME) != 0 and len(EMAIL) != 0 and len(CONTACT) != 0 and len(ADDRESS) != 0:
            import mysql.connector
            DATABASE = mysql.connector.connect(host='localhost',user='root',passwd='root')
            CURSOR = DATABASE.cursor()
            CURSOR.execute('CREATE DATABASE IF NOT EXISTS ATM_DB')

            DATABASE = mysql.connector.connect(host='localhost',user='root',passwd='root',database='ATM_DB')
            CURSOR = DATABASE.cursor()


            CURSOR.execute('CREATE TABLE IF NOT EXISTS ACCOUNT_INFORMATION(CARD VARCHAR(60) PRIMARY KEY NOT NULL,\
            PIN VARCHAR(60) NOT NULL,NAME VARCHAR(60) NOT NULL, EMAIL VARCHAR(60) NOT NULL, CONTACT VARCHAR(60) NOT NULL, ADDRESS TEXT NOT NULL)')
            
            CURSOR.execute('CREATE TABLE IF NOT EXISTS ACCOUNT_BALANCE(CARD VARCHAR(60) PRIMARY KEY NOT NULL, BALANCE FLOAT NOT NULL)')

            CURSOR.execute('INSERT INTO ACCOUNT_INFORMATION VALUES(%s,%s,%s,%s,%s,%s)',(CARD,PIN,NAME,EMAIL,CONTACT,ADDRESS))
            DATABASE.commit()
            CURSOR.execute('INSERT INTO ACCOUNT_BALANCE VALUES(%s,%s)',(CARD,0.00))
            DATABASE.commit()

            self.lineEdit_CardID.clear()
            self.lineEdit_Pin.clear()
            self.lineEdit_Name.clear()
            self.lineEdit_Email.clear()
            self.lineEdit_Contact.clear()
            self.textEdit_Address.clear()

            from PyQt6.QtWidgets import QMessageBox
            self.message = QMessageBox()
            self.message.setWindowIcon(QtGui.QIcon('images/credit-card.png'))
            self.message.setWindowTitle('HS ATM')
            self.message.setIcon(QMessageBox.Icon.NoIcon)
            self.message.setText('Your account has been successfully created.')
            self.message.show()
        else:
            from PyQt6.QtWidgets import QMessageBox
            self.message = QMessageBox()
            self.message.setWindowIcon(QtGui.QIcon('images/credit-card.png'))
            self.message.setWindowTitle('HS ATM')
            self.message.setIcon(QMessageBox.Icon.NoIcon)
            self.message.setText('Please fill all the fields.')
            self.message.show()

            '''
            import sqlite3
            DATABASE = sqlite3.connect('ATM_DB.db')
            CURSOR = DATABASE.cursor()
            CURSOR.execute('CREATE TABLE IF NOT EXISTS ACCOUNT_INFORMATION(CARD TEXT PRIMARY KEY NOT NULL,\
            PIN TEXT NOT NULL,NAME TEXT NOT NULL, EMAIL TEXT NOT NULL, CONTACT TEXT NOT NULL, ADDRESS TEXT NOT NULL)')
            CURSOR.execute('INSERT INTO ACCOUNT_INFORMATION VALUES(?,?,?,?,?,?)',(CARD,PIN,NAME,EMAIL,CONTACT,ADDRESS))
            DATABASE.commit()
            '''

        


    def retranslateUi(self, Registration):
        _translate = QtCore.QCoreApplication.translate
        Registration.setWindowTitle(_translate("Registration", "HS ATM Registration"))
        self.btn_Minimize.setText(_translate("Registration", "-"))
        self.btn_Exit.setText(_translate("Registration", "x"))
        self.label.setText(_translate("Registration", "HS ATM"))
        self.btn_Register.setText(_translate("Registration", "Register"))
        self.lineEdit_CardID.setPlaceholderText(_translate("Registration", "Card ID"))
        self.lineEdit_Pin.setPlaceholderText(_translate("Registration", "Pin"))
        self.label_2.setText(_translate("Registration", "Account Registration"))
        self.lineEdit_Name.setPlaceholderText(_translate("Registration", "Name"))
        self.lineEdit_Email.setPlaceholderText(_translate("Registration", "Email"))
        self.lineEdit_Contact.setPlaceholderText(_translate("Registration", "Contact No."))
        self.textEdit_Address.setPlaceholderText(_translate("Registration", "Address"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Registration = QtWidgets.QMainWindow()
    ui = Ui_Registration()
    ui.setupUi(Registration)
    Registration.show()
    sys.exit(app.exec())
