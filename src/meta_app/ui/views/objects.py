from PySide6.QtWidgets import QPushButton, QMainWindow

def generate_btn(cls: QMainWindow, parent) -> None:
    cls.pushButton = QPushButton(parent)
    cls.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
    "color: rgb(66, 66, 67);\n"
    "border-radius: 3px;\n"
    "padding: 5px;")