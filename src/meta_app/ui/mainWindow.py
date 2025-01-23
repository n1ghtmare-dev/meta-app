from PySide6.QtCore import QRect
from PySide6.QtWidgets import (QApplication, QMainWindow, QFrame, QHBoxLayout, QLabel, QVBoxLayout, QSpacerItem,
                               QSizePolicy, QPushButton, QWidget, QScrollArea, QLineEdit, QMessageBox)
from PySide6.QtGui import QDragEnterEvent, QDropEvent
from meta_app.ui.views.ui_main import Ui_MainWindow
from meta_app.core.file_handler import get_photo_data, update_exif_data
from meta_app.core.funcs import *
import logging


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Meta App")
        self.__init()
        self.file_tags = {}
        self.path_in_widget = []

    def __init(self) -> None:
        self.setAcceptDrops(True)
        self._btn_connects()
        self.remove_tab(self.test_tab)

    def _btn_connects(self) -> None:
        self.main_btn.clicked.connect(self.open_main_page)
        self.settings_btn.clicked.connect(self.open_settings_page)
        self.btn_channels_open.clicked.connect(self.open_channels)
        self.btn_tg_open.clicked.connect(self.open_tg)

    def open_main_page(self) -> None:
        self.pages.setCurrentWidget(self.main_page)

    def open_settings_page(self) -> None:
        self.pages.setCurrentWidget(self.settings_page)

    def dropEvent(self, event: QDropEvent) -> None:
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if urls:
                file_path = urls[0].toLocalFile()
                file_name = file_path.split("/")[-1]
                self.path_in_widget.append(file_path)
                self.file_tags[file_name] = {}
                if self.pages.currentWidget() != self.info_page:
                    self.pages.setCurrentWidget(self.info_page)
                self.show_file_info(file_path)


    def show_file_info(self, file_path):
        file_data = get_photo_data(file_path)
        file_name = file_path.split("/")[-1]
        left_frame_info = self.add_new_tab(file_name)

        for key, value in file_data.items():
            self.create_file_feature(key, value, left_frame_info)

        self.add_spacer()
        self.create_save_button(left_frame_info)

    def add_new_tab(self, name: str) -> QVBoxLayout:
        new_tab = QWidget(self.files_tab)
        tab_layout = QVBoxLayout(new_tab)

        scroll_area = QScrollArea(new_tab)
        scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        scroll_area.setWidgetResizable(True)

        scroll_file_content = QWidget()
        scroll_file_content.setGeometry(QRect(0, 0, 694, 439))
        scroll_fl_layout = QHBoxLayout(scroll_file_content)
        scroll_fl_layout.setSpacing(0)
        scroll_fl_layout.setContentsMargins(0, 0, 0, 0)

        left_frame_info = QFrame(scroll_file_content)
        left_frame_info.setFrameShape(QFrame.Shape.NoFrame)
        left_frame_info.setFrameShadow(QFrame.Shadow.Raised)

        left_f_vlayout = QVBoxLayout(left_frame_info)

        scroll_fl_layout.addWidget(left_frame_info)
        scroll_area.setWidget(scroll_file_content)
        tab_layout.addWidget(scroll_area)

        self.files_tab.addTab(new_tab, name)

        return left_f_vlayout

    def remove_tab(self, tab: int) -> None:
        if tab != -1:
            self.files_tab.removeTab(0)

    def create_file_feature(self, feature, value, left_frame_info: QVBoxLayout) -> None:
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)

        frame_layout = QHBoxLayout(frame)

        current_file = self.get_current_file()
        self.file_tags[current_file][feature] = value

        if len(feature) > 30:
            feature = f"{feature[:30]}..."
        if len(str(value)) > 20:
            value = f"{str(value)[:20]}..."

        label_feature = QLabel(feature)
        line_edit_value = QLineEdit(str(value))
        line_edit_value.setObjectName(feature)
        line_edit_value.setFixedWidth(200)
        line_edit_value.editingFinished.connect(self.update_metadata)

        frame_layout.addWidget(label_feature)
        frame_layout.addWidget(line_edit_value)
        self.check_feature(feature, frame_layout, frame)

        left_frame_info.addWidget(frame)

    def update_metadata(self) -> None:
        sender = self.sender()
        if sender:
            current_file = self.get_current_file()
            feature = sender.objectName()
            new_value = sender.text()
            self.file_tags[current_file][feature] = new_value

    def create_save_button(self, layout: QVBoxLayout) -> None:
        save_button = QPushButton("Сохранить")
        save_button.setStyleSheet(
            "background-color: rgb(46, 204, 113); color: white; font-weight: bold; padding: 5px; border-radius: 5px;"
        )
        save_button.clicked.connect(self.save_file)
        layout.addWidget(save_button)

    def create_btn(self, layout: QHBoxLayout, frame, text) -> None:
        pushButton = QPushButton(frame)
        pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                     "color: rgb(66, 66, 67);\n"
                                     "border-radius: 3px;\n"
                                     "padding: 5px;")
        pushButton.setText(text)
        layout.addWidget(pushButton)
        pushButton.clicked.connect(self.gps_info_open)

    def check_feature(self, feature, layout, frame) -> None:
        if feature == 'GPSInfo':
            self.create_btn(layout, frame, u'Посмотреть')

    def save_file(self):
        tab_index = self.files_tab.currentIndex()
        file_path = self.path_in_widget[tab_index]
        current_file = self.get_current_file()

        if not file_path:
            return

        updated_metadata = self.file_tags[current_file]
        try:
            update_exif_data(file_path, updated_metadata)
            QMessageBox.information(self, "Успешно", "Изменения успешно сохранены!")
        except Exception as e:
            print(e)
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл: {str(e)}")

    def get_current_file(self) -> str:
        tab_index = self.files_tab.currentIndex()
        file_path = self.path_in_widget[tab_index]
        file_name = file_path.split("/")[-1]

        return file_name

    def get_label_text(self, tag: str) -> tuple:
        current_file = self.get_current_file()
        return self.tag_labels[current_file][tag]

    def add_spacer(self) -> None:
        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacer)

    def gps_info_open(self) -> None:
        current_file = self.get_current_file()
        open_gps_url(self.tag_labels[current_file]['GPSInfo'])

    @staticmethod
    def open_tg() -> None:
        open_url('https://t.me/mrlinux0')

    @staticmethod
    def open_channels() -> None:
        open_url('https://t.me/Indigo_channels')

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    @staticmethod
    def clear_layout(layout) -> None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()

            if widget is not None:
                widget.deleteLater()
            elif item.spacerItem() is not None:
                del item

def start_app():
    logging.info("Запуск приложения")
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()