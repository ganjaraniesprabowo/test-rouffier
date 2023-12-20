from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from instr import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.start()

    def initUI(self):
        self.btn_next = QPushButton(txt_next)
        self.hello_text = QLabel('Welcome to the health status detection program!')
        self.instruction = QLabel('This application allows you to use the Rufier test to make an initial diagnosis of your health.\n'
                   'The Rufier test is a set of physical exercises designed to assess your cardiac performance during physical exertion.\n'
                   'The subject lies in the supine position for 5 minutes and has their pulse rate measured for 15 seconds;\n'
                   'then, within 45 seconds, the subject performs 30 squats.\n'
                   'When the exercise ends, the subject lies down and their pulse is measured again for the first 15 seconds\n'
                   'and then for the last 15 seconds of the first minute of the recovery period.\n'
                   'Important! If you feel unwell during the test (dizziness,\n'
                   'tinnitus, shortness of breath, etc.), stop the test and consult a physician.')
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.btn_next, alignment = Qt.AlignCenter)
    
