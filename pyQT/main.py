import sys
from random import randint

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QMessageBox, QPushButton, QVBoxLayout, QProgressBar)
from PyQt5.QtCore import QCoreApplication, QTimer

StyleSheet = '''
#BlueProgressBar::chunk {
    background-color: #2196F3;
    width: 10px; 
    margin: 0.5px;
}
'''


class ProgressBar(QProgressBar):

    def __init__(self, *args, **kwargs):
        super(ProgressBar, self).__init__(*args, **kwargs)
        self.setValue(0)
        if self.minimum() != self.maximum():
            self.timer = QTimer(self, timeout=self.onTimeout)
            self.timer.start(randint(1, 3) * 1000)

    def onTimeout(self):
        if self.value() >= 100:
            self.timer.stop()
            self.timer.deleteLater()
            del self.timer
            return
        self.setValue(self.value() + 1)





app = QApplication(sys.argv)
LoginWindow = QWidget()
LoginWindow.setWindowTitle('Fall Detection System')
LoginWindow.resize(1050, 600)

bg = QLabel(LoginWindow)
bg.resize(1050, 600)
bg.setStyleSheet("background-image:url(./main_fall2.jpg)")

title = QLabel(LoginWindow)
title.setText('Longin System ')
title.setStyleSheet("border: 1px solid black;background-color:yellow;")
title.setFont(QFont('Arial', 30))
title.move(330, 50)

labEmail = QLabel(LoginWindow)
labEmail.setText('Email: ')
labEmail.setStyleSheet("border: 1px solid black;background-color:lightyellow;")
labEmail.setFont(QFont('Arial', 15))
labEmail.move(330, 220)

txtEmail = QLineEdit(LoginWindow)
txtEmail.setFont(QFont("Arial",15))
txtEmail.setStyleSheet("color: red; border: 1px solid black;")
txtEmail.move(440, 220)
txtEmail.resize(250, 30)

labPassword = QLabel(LoginWindow)
labPassword.setText('Password: ')
labPassword.setStyleSheet("border: 1px solid black;background-color:lightyellow;")
labPassword.setFont(QFont('Arial', 15))
labPassword.move(283, 270)

txtPassword = QLineEdit(LoginWindow)
txtPassword.setFont(QFont("Arial",15))
txtPassword.setStyleSheet("color: red; border: 1px solid black;")
txtPassword.move(440, 270)
txtPassword.setEchoMode(QLineEdit.Password)
txtPassword.resize(250, 30)

def end_event():
    if txtEmail.text() == "":
        QMessageBox.about(LoginWindow, 'Message', 'Please input the email!')
    elif txtPassword.text() == "":
        QMessageBox.about(LoginWindow, 'Message', 'Please input the password!')
    else:
        QMessageBox.about(LoginWindow, 'Message', txtEmail.text() + ' Welcome!')
        bg.setStyleSheet("background-color:black;")
        txtEmail.close()
        txtPassword.close()
        btnExit.close()
        btnLogin.close()
        labEmail.close()
        labPassword.close()
        title.setStyleSheet("color:green; border: 10px solid black;")
        title.setText("Starting System<br/><br/>Loading Library...")
        title.setFont(QFont("Arial",25))
        title.move(70,70)
        title.resize(500,200)
        LoginWindow.show()
        app.setStyleSheet(StyleSheet)
        LoginWindow.resize(500, 600)
        layout = QVBoxLayout(LoginWindow)
        layout.addWidget(
            ProgressBar(LoginWindow, minimum=0, maximum=0, textVisible=False,
                        objectName="BlueProgressBar"))



btnLogin = QPushButton('  Login  ', LoginWindow)
btnLogin.setStyleSheet("border: 1px solid black;color: black;background-color:powderblue;")
btnLogin.setFont(QFont('Arial', 15))
btnLogin.clicked.connect(end_event)
btnLogin.move(310, 350)
btnLogin.resize(130, 50)

btnExit = QPushButton('    Exit    ', LoginWindow)
btnExit.clicked.connect(QCoreApplication.instance().quit)
btnExit.setStyleSheet("border: 1px solid black;color: black;background-color:powderblue;")
btnExit.setFont(QFont('Arial', 15))
btnExit.clicked.connect(end_event)
btnExit.move(510, 350)
btnExit.resize(130, 50)

LoginWindow.show()
sys.exit(app.exec_())