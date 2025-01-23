# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QVBoxLayout,
    QWidget)
from meta_app.ui.views import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QSize(800, 500))
        MainWindow.setMaximumSize(QSize(800, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(32, 32, 32);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_bar = QFrame(self.centralwidget)
        self.side_bar.setObjectName(u"side_bar")
        self.side_bar.setMinimumSize(QSize(60, 0))
        self.side_bar.setStyleSheet(u"background-color: rgb(72, 73, 73);")
        self.side_bar.setFrameShape(QFrame.Shape.NoFrame)
        self.side_bar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.side_bar)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 22, -1, -1)
        self.main_btn = QPushButton(self.side_bar)
        self.main_btn.setObjectName(u"main_btn")
        self.main_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.main_btn.setStyleSheet(u"border: none;\n"
"margin-bottom: 10px;")
        icon = QIcon()
        icon.addFile(u":/images/main-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.main_btn.setIcon(icon)
        self.main_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.main_btn)

        self.settings_btn = QPushButton(self.side_bar)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.settings_btn.setStyleSheet(u"border: none;\n"
"margin-bottom: 10px;")
        icon1 = QIcon()
        icon1.addFile(u":/images/settings_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings_btn.setIcon(icon1)
        self.settings_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.settings_btn)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addWidget(self.side_bar)

        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.verticalLayout = QVBoxLayout(self.main_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_drag_drop = QFrame(self.main_page)
        self.frame_drag_drop.setObjectName(u"frame_drag_drop")
        self.frame_drag_drop.setStyleSheet(u"border: 3px dashed rgba(191, 191, 191, 218) ;\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"border-image: repeating-linear-gradient(45deg, white 0%, white 10%, transparent 10%, transparent 20%) 1;")
        self.frame_drag_drop.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_drag_drop.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_drag_drop.setMidLineWidth(10)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_drag_drop)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(248, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label = QLabel(self.frame_drag_drop)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(u"border: none;")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(248, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_drag_drop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pages.addWidget(self.main_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.frame = QFrame(self.settings_page)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(50, 20, 455, 250))
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_4.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_4)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setFamilies([u"a_Concepto"])
        font2.setPointSize(18)
        font2.setBold(True)
        self.label_5.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_5.addWidget(self.label_6)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        font3 = QFont()
        font3.setPointSize(16)
        self.label_7.setFont(font3)

        self.verticalLayout_6.addWidget(self.label_7)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_tg_open = QPushButton(self.frame_4)
        self.btn_tg_open.setObjectName(u"btn_tg_open")
        self.btn_tg_open.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_tg_open.setStyleSheet(u"border: none;\n"
"border-radius: 3px;\n"
"background-color: rgb(13, 118, 225);\n"
"padding: 5px;")

        self.horizontalLayout_5.addWidget(self.btn_tg_open)

        self.btn_channels_open = QPushButton(self.frame_4)
        self.btn_channels_open.setObjectName(u"btn_channels_open")
        self.btn_channels_open.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_channels_open.setStyleSheet(u"border: none;\n"
"border-radius: 3px;\n"
"background-color: rgb(13, 118, 225);\n"
"padding: 5px;")

        self.horizontalLayout_5.addWidget(self.btn_channels_open)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.pages.addWidget(self.settings_page)
        self.info_page = QWidget()
        self.info_page.setObjectName(u"info_page")
        self.verticalLayout_2 = QVBoxLayout(self.info_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.files_tab = QTabWidget(self.info_page)
        self.files_tab.setObjectName(u"files_tab")
        self.test_tab = QWidget()
        self.test_tab.setObjectName(u"test_tab")
        self.verticalLayout_7 = QVBoxLayout(self.test_tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scrollArea = QScrollArea(self.test_tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scroll_file_content = QWidget()
        self.scroll_file_content.setObjectName(u"scroll_file_content")
        self.scroll_file_content.setGeometry(QRect(0, 0, 694, 439))
        self.horizontalLayout_4 = QHBoxLayout(self.scroll_file_content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.left_frame_info = QFrame(self.scroll_file_content)
        self.left_frame_info.setObjectName(u"left_frame_info")
        self.left_frame_info.setFrameShape(QFrame.Shape.NoFrame)
        self.left_frame_info.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.left_frame_info)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.left_frame_info)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(66, 66, 67);\n"
"border-radius: 3px;\n"
"padding: 5px;")

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.horizontalLayout_4.addWidget(self.left_frame_info)

        self.horizontalSpacer_3 = QSpacerItem(578, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.scrollArea.setWidget(self.scroll_file_content)

        self.verticalLayout_7.addWidget(self.scrollArea)

        self.files_tab.addTab(self.test_tab, "")

        self.verticalLayout_2.addWidget(self.files_tab)

        self.pages.addWidget(self.info_page)

        self.horizontalLayout.addWidget(self.pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(0)
        self.files_tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.main_btn.setText("")
        self.settings_btn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0442\u0430\u0449\u0438\u0442\u0435 \u0444\u0430\u0439\u043b", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u0441\u0438\u044f - 0.1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0438:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u042d\u0442\u043e \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043f\u0440\u0435\u0434\u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u043e \u0434\u043b\u044f \u0440\u0430\u0431\u043e\u0442\u044b \u0441 \u043c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u043c\u0438 \u0444\u0430\u0439\u043b\u043e\u0432\n"
"\u0412\u044b \u043c\u043e\u0436\u0435\u0442\u0435 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0435\u0433\u043e \u0431\u0435\u0441\u043f\u043b\u0430\u0442\u043d\u043e \u0432 \u0441\u0432\u043e\u0438\u0445 \u0446\u0435\u043b\u044f\u0445", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f:", None))
        self.btn_tg_open.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0433\u0440\u0430\u043c", None))
        self.btn_channels_open.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b\u044b", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c", None))
        self.files_tab.setTabText(self.files_tab.indexOf(self.test_tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
    # retranslateUi

