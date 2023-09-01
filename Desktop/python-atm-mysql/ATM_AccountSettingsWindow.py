from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector


class Ui_AccountSettings(object):
    def setupUi(self, AccountSettings):
        AccountSettings.setObjectName("AccountSettings")
        AccountSettings.resize(742, 512)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/credit-card.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        AccountSettings.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(AccountSettings)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 741, 511))
        self.frame_2.setStyleSheet("background-color:rgb(7, 44, 112)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame = QtWidgets.QFrame(self.frame_2)
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
        self.btn_Save = QtWidgets.QPushButton(self.frame_3)
        self.btn_Save.setGeometry(QtCore.QRect(340, 300, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.btn_Save.setFont(font)
        self.btn_Save.setStyleSheet("background-color:rgb(44, 48, 61);color:white")
        self.btn_Save.setObjectName("btn_Register")
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
        AccountSettings.setCentralWidget(self.centralwidget)
        AccountSettings.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        AccountSettings.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.btn_Exit.clicked.connect(self.ShowDashboard)
        self.btn_Exit.clicked.connect(AccountSettings.close)
        self.btn_Minimize.clicked.connect(AccountSettings.showMinimized)
        #self.lineEdit_CardID.setEnabled(False)
        self.btn_Save.clicked.connect(self.UpdateAccount)

        from ATM_DashboardWindow import Ui_Dashboard
        self.dashboard = QtWidgets.QMainWindow()
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self.dashboard)
        self.dashboard.close()

        self.retranslateUi(AccountSettings)
        QtCore.QMetaObject.connectSlotsByName(AccountSettings)
    
    def ShowDashboard(self):
        CARD_ID = self.lineEdit_CardID.text()
        CARD_PIN = self.lineEdit_Pin.text()
        if len(CARD_ID) !=0 and len(CARD_PIN) != 0:
            try:
                DATABASE = mysql.connector.connect(host='localhost',user='root',passwd='root',database='ATM_DB')
                CURSOR = DATABASE.cursor()
                CURSOR.execute(f'SELECT * FROM account_information')
                ACCOUNTS_CHECK = CURSOR.fetchall()
                ACCOUNTS_COUNT = 0
                for ACCOUNT_CHECK in ACCOUNTS_CHECK:
                    if CARD_ID == ACCOUNT_CHECK[0]:
                        ACCOUNTS_COUNT+=1
                        break


                if ACCOUNTS_COUNT == 0:
                    from PyQt6.QtWidgets import QMessageBox
                    self.message = QMessageBox()
                    self.message.setWindowIcon(QtGui.QIcon('images/credit-card.png'))
                    self.message.setWindowTitle('HS ATM')
                    self.message.setIcon(QMessageBox.Icon.Warning)
                    self.message.setText("Account doesn't exists")
                    self.message.show()

                CURSOR.execute(f'SELECT * FROM account_information WHERE CARD = "{CARD_ID}"')
                ACCOUNTS = CURSOR.fetchall()
                for ACCOUNT in ACCOUNTS:
                    if CARD_ID == ACCOUNT[0] and CARD_PIN == ACCOUNT[1]:
                    
                        from ATM_DashboardWindow import Ui_Dashboard
                        self.dashboard = QtWidgets.QMainWindow()
                        self.ui = Ui_Dashboard()
                        self.ui.setupUi(self.dashboard)
                        self.ui.label_User.setText(ACCOUNT[2])
                        self.ui.label_ID.setText(ACCOUNT[0])

                        DATABASE = mysql.connector.connect(host='localhost',user='root',passwd='root',database='ATM_DB')
                        CURSOR = DATABASE.cursor()
                        CURSOR.execute(f'SELECT * FROM account_balance WHERE CARD = "{CARD_ID}"')
                        ACCOUNTS = CURSOR.fetchall()
                        for ACCOUNT in ACCOUNTS:
                            self.ui.label_Balance.setText(str(ACCOUNT[1]))

                        self.dashboard.show()

                    else:
                        from PyQt6.QtWidgets import QMessageBox
                        self.message = QMessageBox()
                        self.message.setWindowIcon(QtGui.QIcon('images/credit-card.png'))
                        self.message.setWindowTitle('HS ATM')
                        self.message.setIcon(QMessageBox.Icon.Warning)
                        self.message.setText('Incorrect Username/Password. Please try again.')
                        self.message.show()
            except:
                    from PyQt6.QtWidgets import QMessageBox
                    self.message = QMessageBox()
                    self.message.setWindowIcon(QtGui.QIcon('images/credit-card.png'))
                    self.message.setWindowTitle('HS ATM')
                    self.message.setIcon(QMessageBox.Icon.Warning)
                    self.message.setText("Account doesn't exists")
                    self.message.show()


        else:
            from PyQt6.QtWidgets import QMessageBox
            self.message = QMessageBox()
            self.message.setWindowIcon(QtGui.QIcon('images/credit-card.png'))
            self.message.setWindowTitle('HS ATM')
            self.message.setIcon(QMessageBox.Icon.NoIcon)
            self.message.setText('Please fill all the fields.')
            self.message.show()

    def UpdateAccount(self):
            PIN = self.lineEdit_Pin.text()
            NAME = self.lineEdit_Name.text()
            EMAIL = self.lineEdit_Email.text()
            CONTACT = self.lineEdit_Contact.text()
            ADDRESS = self.textEdit_Address.toPlainText()
            DATABASE = mysql.connector.connect(host='localhost',user='root',passwd='root',database='ATM_DB')
            CURSOR = DATABASE.cursor()
            CURSOR.execute(f'UPDATE account_information set PIN = "{PIN}",NAME = "{NAME}",EMAIL = "{EMAIL}",CONTACT = "{CONTACT}",ADDRESS = "{ADDRESS}" WHERE CARD = "{self.lineEdit_CardID.text()}"')
            DATABASE.commit()

            from PyQt6.QtWidgets import QMessageBox
            self.message = QMessageBox()
            self.message.setWindowIcon(QtGui.QIcon('images/credit-card.png'))
            self.message.setWindowTitle('HS ATM')
            self.message.setIcon(QMessageBox.Icon.Information)
            self.message.setText('Your account has been successfully updated.')
            self.message.show()


    def retranslateUi(self, AccountSettings):
        _translate = QtCore.QCoreApplication.translate
        AccountSettings.setWindowTitle(_translate("AccountSettings", "HS ATM Account Settings"))
        self.btn_Minimize.setText(_translate("AccountSettings", "-"))
        self.btn_Exit.setText(_translate("AccountSettings", "x"))
        self.label.setText(_translate("AccountSettings", "HS ATM"))
        self.btn_Save.setText(_translate("AccountSettings", "Save Changes"))
        self.lineEdit_CardID.setPlaceholderText(_translate("AccountSettings", "Card ID"))
        self.lineEdit_Pin.setPlaceholderText(_translate("AccountSettings", "Pin"))
        self.label_2.setText(_translate("AccountSettings", "Update Account"))
        self.lineEdit_Name.setPlaceholderText(_translate("AccountSettings", "Name"))
        self.lineEdit_Email.setPlaceholderText(_translate("AccountSettings", "Email"))
        self.lineEdit_Contact.setPlaceholderText(_translate("AccountSettings", "Contact No."))
        self.textEdit_Address.setPlaceholderText(_translate("AccountSettings", "Address"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AccountSettings = QtWidgets.QMainWindow()
    ui = Ui_AccountSettings()
    ui.setupUi(AccountSettings)
    AccountSettings.show()
    sys.exit(app.exec())