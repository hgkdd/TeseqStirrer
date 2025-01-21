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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(428, 469)
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
        self.pushButton_4 = QPushButton(self.stirrer_mode_tab)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_10.addWidget(self.pushButton_4, 1, 0, 1, 1)

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

        self.groupBox_2 = QGroupBox(self.tuner_mode_tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.step_spinBox = QSpinBox(self.groupBox_2)
        self.step_spinBox.setObjectName(u"step_spinBox")
        self.step_spinBox.setMinimum(1)
        self.step_spinBox.setMaximum(360)
        self.step_spinBox.setValue(5)

        self.verticalLayout_3.addWidget(self.step_spinBox)

        self.pushButton_5 = QPushButton(self.groupBox_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_3.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.groupBox_2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_3.addWidget(self.pushButton_6)


        self.gridLayout_6.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.tuner_mode_tab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.spinBox = QSpinBox(self.groupBox_5)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(359)

        self.verticalLayout_6.addWidget(self.spinBox)

        self.pushButton_7 = QPushButton(self.groupBox_5)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_6.addWidget(self.pushButton_7)


        self.gridLayout_6.addWidget(self.groupBox_5, 2, 0, 1, 1)

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
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.velocity_spinBox = QSpinBox(self.groupBox)
        self.velocity_spinBox.setObjectName(u"velocity_spinBox")
        self.velocity_spinBox.setMinimum(1)
        self.velocity_spinBox.setMaximum(100)
        self.velocity_spinBox.setValue(50)

        self.verticalLayout.addWidget(self.velocity_spinBox)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.groupBox_6 = QGroupBox(self.frame)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_4 = QGridLayout(self.groupBox_6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label = QLabel(self.groupBox_6)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_2.addWidget(self.groupBox_6)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        font1 = QFont()
        font1.setPointSize(40)
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(255, 38, 0);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 428, 37))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stirrmode_ccw_radioButton.clicked["bool"].connect(self.tunmode_ccw_radioButton.setChecked)
        self.stirrmode_cw_radioButton.clicked["bool"].connect(self.tunmode_cw_radioButton.setChecked)
        self.tunmode_ccw_radioButton.clicked["bool"].connect(self.stirrmode_ccw_radioButton.setChecked)
        self.tunmode_cw_radioButton.clicked["bool"].connect(self.stirrmode_cw_radioButton.setChecked)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Direction of Rotation", None))
        self.stirrmode_cw_radioButton.setText(QCoreApplication.translate("MainWindow", u"Clockwise", None))
        self.stirrmode_ccw_radioButton.setText(QCoreApplication.translate("MainWindow", u"Counter Clockwise", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stirrer_mode_tab), QCoreApplication.translate("MainWindow", u"Stirrer Mode", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Direction of Rotation", None))
        self.tunmode_cw_radioButton.setText(QCoreApplication.translate("MainWindow", u"Clockwise", None))
        self.tunmode_ccw_radioButton.setText(QCoreApplication.translate("MainWindow", u"Counter Clockwise", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Relative Operation", None))
        self.step_spinBox.setSuffix(QCoreApplication.translate("MainWindow", u" deg", None))
        self.step_spinBox.setPrefix(QCoreApplication.translate("MainWindow", u"Step: ", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Step Once", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Step Continiusly", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Absolute Operation", None))
        self.spinBox.setSuffix(QCoreApplication.translate("MainWindow", u" deg", None))
        self.spinBox.setPrefix(QCoreApplication.translate("MainWindow", u"Position: ", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tuner_mode_tab), QCoreApplication.translate("MainWindow", u"Tuner Mode", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Initialization", None))
        self.velocity_spinBox.setSuffix(QCoreApplication.translate("MainWindow", u" %", None))
        self.velocity_spinBox.setPrefix(QCoreApplication.translate("MainWindow", u"Velocity: ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Init", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Current Position", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"???", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
    # retranslateUi

