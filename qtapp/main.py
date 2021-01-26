#!/usr/bin/python
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import sip
import time
from fcad import *
import fcad.keys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title='FCaD 3.2.0'
        self.setWindowTitle(self.title)
        self.resize(1920,1005)
        self.label=QLabel(self)
        self.label.setStyleSheet("border: 1px solid black; text-align:center;") 
        #self.label.move(1920//2-100,10)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText('FCaD 3.2')
        self.label.setFont(QFont("Forte",40))
        self.label.adjustSize()
        self.butt_encrypt=QPushButton('Encrypt')
        self.butt_nk=QPushButton('New Key')
    
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget (self.butt_encrypt)
        self.layout.addWidget (self.butt_nk)
        self.butt_encrypt.clicked.connect(self.view_encrypter)
        self.butt_nk.clicked.connect(self.view_nk)
        self.InfoLabel=QLabel(self)
        self.InfoLabel.setText('')
        self.setLayout(self.layout)
    def view_encrypter(self):
        self.label.setText('FCaD Encrypter')
        self.butt_nk.hide()
        self.InfoLabel.setText('This encrypter needs key file. If you have not any, you should generate one.')
        self.InfoLabel.move(1920//2-250,1005-100)
        self.InfoLabel.adjustSize()
        self.title='FCaD Encrypter'
        self.lefk=QLineEdit("",self)
        self.lefk.setGeometry(80, 80, 150, 40)
        self.setWindowTitle(self.title)
        self.butt_encrypt.setText('Encrypt File')
        self.butt_encrypt.clicked.connect(self.get_enc)
        self.show()
    def view_nk(self):
        
        self.label.setText('FCaDKey generator')
        self.butt_nk.hide()
        self.title='FCaDKey generator'
        self.lefk=QLineEdit("",self)
        self.lefk.setGeometry(80, 80, 150, 40)
        self.setWindowTitle(self.title)
        self.butt_encrypt.setText('Generate')
        self.butt_encrypt.clicked.connect(self.get_newk)
        self.show()

    def get_enc(self):
        self.InfoLabel.setText('')
        self.label.setText('Encrypting...')

        filename=self.get("Filename")
        keyname=self.get("Keyfile")
        self.label.setText('Encrypting...')
        h=fcad.iencrypt(filename,keyname)
        if h is None:
            self.label.setText('Sucessfully encrypted.')
            time.sleep(1)
            self.label.setText('FCaD Encrypter')
        elif h=='EEFNF':
            self.label.setText('ERROR')
            self.InfoLabel.setText(f'Error during encrypting: encrypting file {filename} does not exist.')
            self.InfoLabel.adjustSize()
        elif h=='EKFNF':
            self.label.setText('ERROR')
            self.InfoLabel.setText(f'Error during encrypting: key file {keyename} does not exist.')
            self.InfoLabel.adjustSize()
    def get_newk(self):
         filename=self.get("Filename")
         fcad.irandom_key(filename)
    def get(self,label):
        text, okPressed = QInputDialog.getText(self,self.title+' Dialog',label, QLineEdit.Normal, "")
        if text:
            return text
if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
