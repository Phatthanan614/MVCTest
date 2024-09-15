import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QMessageBox
from controller.inputValid import validateInput
from controller.checkCow import checkTeats
from controller.readCSV import teats_list
import tkinter as tk
from tkinter import messagebox
import random

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
                result = messagebox.askquestion("Cow have milk", "want milk?", icon='question')
                if result == 'yes':
                    if random.random() < 0.05:
                        # teats_list[inp_id].set(3)
                        messagebox.showinfo("Milking...","Milking... Number of teats reduced to 3.")
                    else:
                        messagebox.showinfo("Milking...","Milking...")                    
            elif int(teats) == 3:
                QMessageBox.information(self, 'Cow don\'t have milk', f'Can\'t give milk')
                if random.random() < 0.20:
                    # teats_list[inp_id].set(4)
                    messagebox.showinfo("Cow Detail", "Cow has 3 teats. Recovery... Number of teats restored to 4.")
                else:
                    messagebox.showinfo("Cow Detail", "Cow has 3 teats. No recovery.")
            # self.update_teat_label()
            
        else:
            QMessageBox.information(self, 'Input', f'ID is invalid')


    def get_input_id(self):
        return self.input.text()
