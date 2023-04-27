from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
class AuthDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AuthDialog, self).__init__(*args, **kwargs)
        
        self.isAdmin =None

        self.setFixedWidth(300)
        self.setFixedHeight(120)

        layout = QVBoxLayout()
        self.logininput = QLineEdit()
        
        self.logininput.setPlaceholderText("Введите логин")

        self.passinput = QLineEdit()

        self.passinput.setEchoMode(QLineEdit.Password)
        self.passinput.setPlaceholderText("Введите пароль")
        self.QBtn = QPushButton()
        self.QBtn.setText("Войти")
        self.setWindowTitle('Окно входа')
        self.QBtn.clicked.connect(self.login)

        title = QLabel("Введите логин и пароль\n")
        font = title.font()
        font.setPointSize(12)
        title.setFont(font)

        layout.addWidget(title)
        layout.addWidget(self.logininput)
        layout.addWidget(self.passinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)
    
    def login(self):
        
            if((self.passinput.text() == "1111" and self.logininput.text() == "admin") or (self.passinput.text() == '' and self.logininput.text() == '')):
                self.accept()
                self.isAdmin =  True
            elif(self.passinput.text() == "" and self.logininput.text() == "user"):
                self.accept()
                self.isAdmin = False

            else:
                QMessageBox.warning(self, 'Ошибка', 'Неверный логин или пароль')


