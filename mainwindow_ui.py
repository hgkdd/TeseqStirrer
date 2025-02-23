# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(429, 490)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAbout.setMenuRole(QAction.MenuRole.AboutRole)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionQuit.setMenuRole(QAction.MenuRole.QuitRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.stirrer_mode_tab = QWidget()
        self.stirrer_mode_tab.setObjectName(u"stirrer_mode_tab")
        self.gridLayout_10 = QGridLayout(self.stirrer_mode_tab)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.stirmode_start_pushButton = QPushButton(self.stirrer_mode_tab)
        self.stirmode_start_pushButton.setObjectName(u"stirmode_start_pushButton")

        self.gridLayout_10.addWidget(self.stirmode_start_pushButton, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.stirrer_mode_tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_8 = QGridLayout(self.groupBox_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stirrmode_cw_radioButton = QRadioButton(self.groupBox_3)
        self.stirrmode_cw_radioButton.setObjectName(u"stirrmode_cw_radioButton")
        self.stirrmode_cw_radioButton.setChecked(True)

        self.verticalLayout_4.addWidget(self.stirrmode_cw_radioButton)

        self.stirrmode_ccw_radioButton = QRadioButton(self.groupBox_3)
        self.stirrmode_ccw_radioButton.setObjectName(u"stirrmode_ccw_radioButton")

        self.verticalLayout_4.addWidget(self.stirrmode_ccw_radioButton)


        self.gridLayout_8.addLayout(self.verticalLayout_4, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.tabWidget.addTab(self.stirrer_mode_tab, "")
        self.tuner_mode_tab = QWidget()
        self.tuner_mode_tab.setObjectName(u"tuner_mode_tab")
        self.gridLayout_6 = QGridLayout(self.tuner_mode_tab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBox_4 = QGroupBox(self.tuner_mode_tab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_12 = QGridLayout(self.groupBox_4)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tunmode_cw_radioButton = QRadioButton(self.groupBox_4)
        self.tunmode_cw_radioButton.setObjectName(u"tunmode_cw_radioButton")
        self.tunmode_cw_radioButton.setChecked(True)

        self.verticalLayout_5.addWidget(self.tunmode_cw_radioButton)

        self.tunmode_ccw_radioButton = QRadioButton(self.groupBox_4)
        self.tunmode_ccw_radioButton.setObjectName(u"tunmode_ccw_radioButton")

        self.verticalLayout_5.addWidget(self.tunmode_ccw_radioButton)


        self.gridLayout_12.addLayout(self.verticalLayout_5, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_4, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.groupBox_5 = QGroupBox(self.tuner_mode_tab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.formLayout_2 = QFormLayout(self.groupBox_5)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.tun_mode_abs_go_pushButton = QPushButton(self.groupBox_5)
        self.tun_mode_abs_go_pushButton.setObjectName(u"tun_mode_abs_go_pushButton")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.tun_mode_abs_go_pushButton)

        self.label_3 = QLabel(self.groupBox_5)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.tunmode_abs_pos_doubleSpinBox = QDoubleSpinBox(self.groupBox_5)
        self.tunmode_abs_pos_doubleSpinBox.setObjectName(u"tunmode_abs_pos_doubleSpinBox")
        self.tunmode_abs_pos_doubleSpinBox.setDecimals(1)
        self.tunmode_abs_pos_doubleSpinBox.setMaximum(360.000000000000000)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.tunmode_abs_pos_doubleSpinBox)


        self.gridLayout_6.addWidget(self.groupBox_5, 3, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.tuner_mode_tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout = QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.step_doubleSpinBox = QDoubleSpinBox(self.groupBox_2)
        self.step_doubleSpinBox.setObjectName(u"step_doubleSpinBox")
        self.step_doubleSpinBox.setDecimals(1)
        self.step_doubleSpinBox.setMaximum(360.000000000000000)
        self.step_doubleSpinBox.setValue(5.000000000000000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.step_doubleSpinBox)

        self.tunmode_step_once_pushButton = QPushButton(self.groupBox_2)
        self.tunmode_step_once_pushButton.setObjectName(u"tunmode_step_once_pushButton")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.tunmode_step_once_pushButton)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.tun_mode_time_doubleSpinBox = QDoubleSpinBox(self.groupBox_2)
        self.tun_mode_time_doubleSpinBox.setObjectName(u"tun_mode_time_doubleSpinBox")
        self.tun_mode_time_doubleSpinBox.setDecimals(1)
        self.tun_mode_time_doubleSpinBox.setMaximum(3600.000000000000000)
        self.tun_mode_time_doubleSpinBox.setValue(1.000000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.tun_mode_time_doubleSpinBox)

        self.tunmode_step_cont_pushButton = QPushButton(self.groupBox_2)
        self.tunmode_step_cont_pushButton.setObjectName(u"tunmode_step_cont_pushButton")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.tunmode_step_cont_pushButton)


        self.gridLayout_6.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tuner_mode_tab, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.init_groupBox = QGroupBox(self.frame)
        self.init_groupBox.setObjectName(u"init_groupBox")
        self.gridLayout = QGridLayout(self.init_groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.velocity_spinBox = QSpinBox(self.init_groupBox)
        self.velocity_spinBox.setObjectName(u"velocity_spinBox")
        self.velocity_spinBox.setEnabled(False)
        self.velocity_spinBox.setMinimum(1)
        self.velocity_spinBox.setMaximum(100)
        self.velocity_spinBox.setValue(50)

        self.verticalLayout.addWidget(self.velocity_spinBox)

        self.init_pushButton = QPushButton(self.init_groupBox)
        self.init_pushButton.setObjectName(u"init_pushButton")

        self.verticalLayout.addWidget(self.init_pushButton)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.init_groupBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.groupBox_6 = QGroupBox(self.frame)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_4 = QGridLayout(self.groupBox_6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.cur_pos_label = QLabel(self.groupBox_6)
        self.cur_pos_label.setObjectName(u"cur_pos_label")
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.cur_pos_label.setFont(font)
        self.cur_pos_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_4.addWidget(self.cur_pos_label, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_2.addWidget(self.groupBox_6)

        self.stop_pushButton = QPushButton(self.frame)
        self.stop_pushButton.setObjectName(u"stop_pushButton")
        font1 = QFont()
        font1.setPointSize(40)
        self.stop_pushButton.setFont(font1)
        self.stop_pushButton.setAutoFillBackground(False)
        self.stop_pushButton.setStyleSheet(u"background-color: rgb(255, 38, 0);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.stop_pushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.quit_pushButton = QPushButton(self.frame)
        self.quit_pushButton.setObjectName(u"quit_pushButton")

        self.verticalLayout_2.addWidget(self.quit_pushButton)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 429, 22))
        self.menuStirrerRC = QMenu(self.menubar)
        self.menuStirrerRC.setObjectName(u"menuStirrerRC")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.velocity_spinBox, self.init_pushButton)
        QWidget.setTabOrder(self.init_pushButton, self.stirrmode_cw_radioButton)
        QWidget.setTabOrder(self.stirrmode_cw_radioButton, self.stirrmode_ccw_radioButton)
        QWidget.setTabOrder(self.stirrmode_ccw_radioButton, self.stirmode_start_pushButton)
        QWidget.setTabOrder(self.stirmode_start_pushButton, self.tunmode_cw_radioButton)
        QWidget.setTabOrder(self.tunmode_cw_radioButton, self.tunmode_ccw_radioButton)
        QWidget.setTabOrder(self.tunmode_ccw_radioButton, self.stop_pushButton)
        QWidget.setTabOrder(self.stop_pushButton, self.quit_pushButton)
        QWidget.setTabOrder(self.quit_pushButton, self.tabWidget)

        self.menubar.addAction(self.menuStirrerRC.menuAction())
        self.menuStirrerRC.addAction(self.actionAbout)
        self.menuStirrerRC.addSeparator()
        self.menuStirrerRC.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)
        self.stirrmode_ccw_radioButton.clicked["bool"].connect(self.tunmode_ccw_radioButton.setChecked)
        self.stirrmode_cw_radioButton.clicked["bool"].connect(self.tunmode_cw_radioButton.setChecked)
        self.tunmode_ccw_radioButton.clicked["bool"].connect(self.stirrmode_ccw_radioButton.setChecked)
        self.tunmode_cw_radioButton.clicked["bool"].connect(self.stirrmode_cw_radioButton.setChecked)
        self.quit_pushButton.clicked.connect(MainWindow.close)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"StirrerRC", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.stirmode_start_pushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Direction of Rotation", None))
        self.stirrmode_cw_radioButton.setText(QCoreApplication.translate("MainWindow", u"Clockwise", None))
        self.stirrmode_ccw_radioButton.setText(QCoreApplication.translate("MainWindow", u"Counter Clockwise", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stirrer_mode_tab), QCoreApplication.translate("MainWindow", u"Stirrer Mode", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Direction of Rotation", None))
        self.tunmode_cw_radioButton.setText(QCoreApplication.translate("MainWindow", u"Clockwise", None))
        self.tunmode_ccw_radioButton.setText(QCoreApplication.translate("MainWindow", u"Counter Clockwise", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Absolute Operation", None))
        self.tun_mode_abs_go_pushButton.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Angle:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Relative Operation", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Step:", None))
        self.step_doubleSpinBox.setSuffix(QCoreApplication.translate("MainWindow", u" deg", None))
        self.tunmode_step_once_pushButton.setText(QCoreApplication.translate("MainWindow", u"Step Once", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.tun_mode_time_doubleSpinBox.setSuffix(QCoreApplication.translate("MainWindow", u" s", None))
        self.tunmode_step_cont_pushButton.setText(QCoreApplication.translate("MainWindow", u"Step Continuously", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tuner_mode_tab), QCoreApplication.translate("MainWindow", u"Tuner Mode", None))
        self.init_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Initialization", None))
        self.velocity_spinBox.setSuffix(QCoreApplication.translate("MainWindow", u" %", None))
        self.velocity_spinBox.setPrefix(QCoreApplication.translate("MainWindow", u"Velocity: ", None))
        self.init_pushButton.setText(QCoreApplication.translate("MainWindow", u"Init", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Current Position", None))
        self.cur_pos_label.setText(QCoreApplication.translate("MainWindow", u"???", None))
        self.stop_pushButton.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.quit_pushButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.menuStirrerRC.setTitle(QCoreApplication.translate("MainWindow", u"StirrerRC", None))
    # retranslateUi

