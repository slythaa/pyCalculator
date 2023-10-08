
# TODO: fix adding as it currently sucks doo doo ass water

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton
from PyQt5.QtGui import *

#initiallize GUI application
app = QApplication(sys.argv)

#window settings
window = QWidget()
window.setMinimumWidth(500)
window.setMinimumHeight(700)
window.setStyleSheet("""
    background-color: rgb(34, 48, 60)
""")
window.setWindowTitle("Simple PyQt5 Calculator")

grid = QGridLayout()

# basically the input field for calculator (using keyboard makes it shit itself)
tracker = []

number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
def addButton(row, col, rs, cs, name):
    global line_edit
    button = QPushButton(name)

    def inputNumber():
        print(name)
        tracker.append(name)
        line_edit.setText(''.join(tracker))

    def mathSign():
        print(name)
        tracker.append(name)
        line_edit.setText(''.join(tracker))

    if name in number_list:
        button.clicked.connect(inputNumber)
    elif name == "=":
        button.clicked.connect(evaluate)
    elif name == "CLEAR":
        button.clicked.connect(clear)
    else:
        button.clicked.connect(mathSign)

    button.setMinimumSize(90,90)
    button.setStyleSheet("""
        *{
            background-color: rgb(34, 48, 60);
            border-radius: 10px;
            color: white;
            font-size: 35px
        }
        *:hover{background-color: rgb(136,153,166)} 
    """)
    grid.addWidget(button, row, col, rs, cs)

# take the tracker and evaluate and updates its value or smth like that idk
def evaluate():
    # making an equation to work on
    signs = ["+", "-", "x", "÷", "(", ")"]
    number = []
    equation = []
    for i in tracker:
        if i not in signs:
            number.append(i)
        else:
            num = "".join([str(item) for item in number])
            equation.append(num)
            equation.append(i)
            number.clear()

    # for some reason if i repeat these 3 lines of code everything works smoothly...how/why does it work? no clue
    num = "".join([str(item) for item in number])
    equation.append(num)
    number.clear()

    print(f"[NUMBER]: {number}")
    print(f"[EQUATION]: {equation}")

    equation_str = ''.join(equation)

    try:
        result = eval(equation_str)
        tracker.clear()
        tracker.append(str(result))
        line_edit.setText(str(result))
        print(result)
        print(tracker)
    except Exception as e:
        print(f"Error: {e}")

# clear everything
def clear():
    tracker.clear()
    line_edit.setText('')

def calculator_widgets():
    global line_edit
    line_edit = QLineEdit()

    # only accept numbers
    validator = QIntValidator()
    line_edit.setValidator(validator)

    line_edit.setMinimumHeight(200)
    line_edit.setStyleSheet("""
        font-size: 50px;
        background-color: rgb(25, 39, 52);
        border-radius: 30px;
        color: white;
        border: 0
    """)

    grid.addWidget(line_edit, 0, 0, 1, 5)

    # first row (of buttons)
    addButton(1, 0, 1, 1, "func")
    addButton(1, 1, 1, 1, "func")
    addButton(1, 2, 1, 1, "func")
    addButton(1, 3, 1, 1, "func")
    addButton(1, 4, 1, 1, "÷")

    # second row
    addButton(2, 0, 1, 1, "7")
    addButton(2, 1, 1, 1, "8")
    addButton(2, 2, 1, 1, "9")
    addButton(2, 3, 1, 1, "(")
    addButton(2, 4, 1, 1, "x")

    # third row
    addButton(3, 0, 1, 1, "4")
    addButton(3, 1, 1, 1, "5")
    addButton(3, 2, 1, 1, "6")
    addButton(3, 3, 1, 1, ")")
    addButton(3, 4, 1, 1, "-")

    # fourth row
    addButton(4, 0, 1, 1, "1")
    addButton(4, 1, 1, 1, "2")
    addButton(4, 2, 1, 1, "3")
    addButton(4, 3, 1, 1, "^")
    addButton(4, 4, 1, 1, "+")

    # fifth row
    addButton(5, 0, 1, 1, "+/-")
    addButton(5, 1, 1, 1, "0")
    addButton(5, 2, 1, 1, "CLEAR")
    addButton(5, 3, 1, 1, ".")
    addButton(5, 4, 1, 1, "=")

calculator_widgets()

window.setLayout(grid)
window.show()
sys.exit(app.exec())
