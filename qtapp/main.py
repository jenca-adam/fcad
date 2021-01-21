#!/usr/bin/python
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import sip
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('FCaD 3.2.0')
        self.resize(1920,1005)
        self.label=QLabel(self)
        self.label.setStyleSheet("border: 1px solid black; text-align:center;") 
        self.label.move(1920//2-100,10)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText('FCaD 3.2')
        self.label.setFont(QFont("Forte",40))
        self.label.adjustSize()
        self.butt_encrypt=QPushButton('Encrypt')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget (self.butt_encrypt)
        self.butt_encrypt.clicked.connect(self.view_encrypter)
        self.setLayout(self.layout)
    def view_encrypter(self):
        sip.delete(self.label)
        sip.delete(self.butt_encrypt)
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
