from PySide6.QtWidgets import (QApplication, QMainWindow, QFrame, QHBoxLayout, QLabel, QVBoxLayout, QSpacerItem,
                               QSizePolicy, QPushButton)
from PySide6.QtGui import QDragEnterEvent, QDropEvent
from meta_app.ui.views.ui_main import Ui_MainWindow
from meta_app.core.file_handler import get_photo_data
from meta_app.core.funcs import *
from pathlib import Path
import logging


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Meta App")
        self.__init()
        self.tag_labels = {}

    def __init(self):
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        urls = event.mimeData().urls()
        if urls:
            file_path = urls[0].toLocalFile()
            self.pages.setCurrentWidget(self.info_page)
            self.show_file_info(file_path)

    def show_file_info(self, file_path):
        self.clear_layout(self.verticalLayout_4)

        file_data = get_photo_data(file_path)

        for key, value in file_data.items():
            self.create_file_feature(key, value)

        self.add_spacer()

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()

            if widget is not None:
                widget.deleteLater()
            elif item.spacerItem() is not None:
                del item


    def create_file_feature(self, feature, value):
        frame = QFrame(self.left_frame_info)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)

        frame_layout = QHBoxLayout(frame)
        self.tag_labels[feature] = value

        if len(feature) > 30:
            feature = f"{feature[:30]}..."
        if len(str(value)) > 20:
            value = f"{str(value)[:20]}..."

        label_feature = QLabel(feature)
        label_value = QLabel(str(value))

        frame_layout.addWidget(label_feature)
        frame_layout.addWidget(label_value)
        self.check_feature(feature, frame_layout, frame)

        self.verticalLayout_4.addWidget(frame)

    def create_btn(self, layout: QHBoxLayout, frame, text) -> None:
        pushButton = QPushButton(frame)
        pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                     "color: rgb(66, 66, 67);\n"
                                     "border-radius: 3px;\n"
                                     "padding: 5px;")
        pushButton.setText(text)
        layout.addWidget(pushButton)
        pushButton.clicked.connect(self.gps_info_open)

    def check_feature(self, feature, layout, frame):
        if feature == 'GPSInfo':
            self.create_btn(layout, frame, u'Посмотреть')

    def get_label_text(self, tag: str) -> tuple:
        return self.tag_labels[tag]

    def add_spacer(self):
        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacer)

    def gps_info_open(self):
        open_url(self.tag_labels['GPSInfo'])

def start_app():
    logging.info("Запуск приложения")
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()