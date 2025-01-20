from PySide6.QtWidgets import (QApplication, QMainWindow, QFrame, QHBoxLayout, QLabel, QVBoxLayout, QSpacerItem,
                               QSizePolicy)
from PySide6.QtGui import QDragEnterEvent, QDropEvent
from meta_app.ui.views.ui_main import Ui_MainWindow
from meta_app.core.file_handler import get_photo_data
from pathlib import Path
import logging

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Meta App")
        self.__init()

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
            file_name = Path(file_path).name
            self.pages.setCurrentWidget(self.info_page)
            self.show_file_info(file_path)

    def show_file_info(self, file_path):
        self.clear_layout(self.verticalLayout_4)

        file_name = Path(file_path).name
        # self.create_file_feature("Имя файла", file_name)

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

        label_feature = QLabel(feature)
        label_value = QLabel(str(value))

        frame_layout.addWidget(label_feature)
        frame_layout.addWidget(label_value)

        self.verticalLayout_4.addWidget(frame)

    def add_spacer(self):
        # self.verticalLayout_4.addStretch()
        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacer)



def start_app():
    logging.info("Запуск приложения")
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()