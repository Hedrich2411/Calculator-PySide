import sys
from unittest import result
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from styles import *

class Calculator(QWidget):
    
    operators = ("/","-","+","*","%")

    def __init__(self):
        super().__init__()
        self.data = " "
        self.widgets_init()
        self.resizeEvent = self.change_size_event

    
    def widgets_init(self):

        #Configure window
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("calculator_img.png"))
        self.setStyleSheet(window_style)
        self.setMinimumSize(300,400)

        #create widgets

        self.display = QLineEdit()
        self.display.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding))
        self.display.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.display.setReadOnly(True)
        self.display.setText("0")
        self.display.setFrame(False)
        self.display.setStyleSheet(display_style)

        display_font = QFont()
        display_font.setPointSize(15)
        display_font.setBold(True)
        self.display.setFont(display_font)


        self.frame = QFrame()
        self.frame.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding))
        self.frame.setStyleSheet(frame_style)


        #create layouts
        self.general_layout = QVBoxLayout()
        self.general_layout.setContentsMargins(0,0,0,0)
        self.general_layout.setSpacing(0)
        self.setLayout(self.general_layout)
        self.general_layout.addWidget(self.display)
        self.general_layout.addWidget(self.frame)

        self.frame_layout = QGridLayout()
        self.frame_layout.setContentsMargins(0,0,0,0)
        self.frame_layout.setSpacing(0)
        self.frame.setLayout(self.frame_layout)


        buttons = { '(' : (1,0), ")" : (1, 1), "%" : (1, 2), "AC" : (1, 3),
                    '7' : (2,0), "8" : (2, 1), "9" : (2, 2), "/" : (2, 3),  
                    '4' : (3,0), "5" : (3, 1), "6" : (3, 2), "*" : (3, 3), 
                    '1' : (4,0), "2" : (4, 1), "3" : (4, 2), "-" : (4, 3), 
                    '0' : (5,0), "." : (5, 1), "=" : (5, 2), "+" : (5, 3) 
        }

        button_font = QFont()
        button_font.setPointSize(12)
        button_font.setBold(True)


        for name,(x,y) in buttons.items():

            button = QPushButton(name)
            button.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding))
            button.setCursor(QCursor(Qt.PointingHandCursor))
            button.setStyleSheet(buttons_style)
            button.setFont(button_font)
            self.frame_layout.addWidget(button,x,y)
            button.clicked.connect(self.press_btns)

        
        
    def change_size_event(self,event):
        print(event)
        self.display.setMaximumHeight(self.size().height()/3.3)
        font = QFont()
        font.setPointSize(self.size().height()/10-10)
        self.display.setFont(font)

    def press_btns(self):

        btn_text = self.sender().text()

        if btn_text == "AC":
            self.clear_display()

        elif btn_text in self.operators:
            if self.data[-1].isdigit():
                self.data += btn_text
                self.display.setText(self.data)
        
        elif btn_text == "=":

            try:
                result = str(eval(self.data))
                self.display.setText(result)
            except:
                self.clear_display()
        else:
            self.data = self.data + btn_text
            self.display.setText(self.data)


    def clear_display(self):
        self.data = " "
        self.display.setText("0")



if __name__ == "__main__":

    app = QApplication([])
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())

    