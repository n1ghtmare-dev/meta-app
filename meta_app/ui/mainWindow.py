from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QHBoxLayout, QLabel, QVBoxLayout
from PySide6.QtGui import QDragEnterEvent, QDropEvent
from meta_app.ui.views.ui_main import Ui_MainWindow
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
        if not self.left_frame_info.layout():
            scroll_widget = QVBoxLayout(self.left_frame_info)
        else:
            scroll_widget = self.left_frame_info.layout()

        for i in reversed(range(scroll_widget.count())):
            widget = scroll_widget.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        file_name = Path(file_path).name
        self.create_file_feature("Имя файла", file_name)


    def create_file_feature(self, feature, value):
        frame = QFrame(self.left_frame_info)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)

        layout = QHBoxLayout(frame)

        label_feature = QLabel(feature)
        label_value = QLabel(str(value))

        layout.addWidget(label_feature)
        layout.addWidget(label_value)

        self.left_frame_info.addWidget(frame)


def start_app():
    logging.info("Запуск приложения")
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()