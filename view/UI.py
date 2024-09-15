import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QMessageBox
from controller.inputValid import validateInput
from controller.checkCow import checkTeats
import tkinter as tk
from tkinter import messagebox

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Cow')
        self.setGeometry(700, 500, 600, 400)
        
        self.input = QLineEdit(self)
        self.input.setPlaceholderText('Enter your Cow ID...')
        
        button = QPushButton('Cow Detail', self)
        button.clicked.connect(self.on_button_click_id)
        
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(button)
        
        self.setLayout(layout)

    def on_button_click_id(self):
        inp_id = self.input.text()
    
        isValid = validateInput(inp_id)
        if isValid:
            teats = checkTeats(int(inp_id))
            # if teats is None:
                # QMessageBox.information(self, 'Input', f'its Goat')
                # tk.Label(msg_box, text="its Goat.").pack(pady=10)
                # ok_button = tk.Button(msg_box, text="OK", command=msg_box.destroy)
                # ok_button.pack(pady=10)
            if int(teats) == 4:
                QMessageBox.information(self, 'Input', f'its Cow and have {teats} teats')
                result = messagebox.askquestion("Custom Message Box", "want milk?", icon='question')
                if result == 'yes':
                    QMessageBox.information(self, 'Input', f'its Cow')
                else:
                    print("No button clicked")
            else:
                QMessageBox.information(self, 'Input', f'cant give milk')
            
        else:
            QMessageBox.information(self, 'Input', f'ID is invalid')

    def get_input_id(self):
        return self.input.text()
    
    def show_message_box():
        result = messagebox.askquestion("Custom Message Box", "This is a custom message box with custom buttons.", icon='question')

        if result == 'yes':
            QMessageBox.information(self, 'Input', f'its Cow')
        else:
            print("No button clicked")
