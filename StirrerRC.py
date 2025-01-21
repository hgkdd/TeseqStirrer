import sys

from PySide6 import QtCore
from PySide6.QtCore import (Qt, QLocale, QSettings)
from PySide6.QtGui import (QStandardItemModel, QStandardItem)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox,
                               QFileDialog, QTableWidgetItem, QVBoxLayout, QWidget)

from stirrer import Stirrer

# Important:
# You need to run the following command to generate the mainwindow.py file
#     pyside6-uic mainwindow.ui -o mainwindow.py
from mainwindow_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, settings, parent=None):
        super(MainWindow, self).__init__(parent)
        self.settings = settings
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # register message box for quit action
        self.ui.actionQuit.triggered.connect(MainWindow.close)

        self.ui.init_pushButton.clicked.connect(self.init_clicked)
        self.ui.velocity_spinBox.valueChanged.connect(self.velocity_changed)
        self.ui.stop_pushButton.clicked.connect(self.stopp_clicked)
        self.ui.stirmode_start_pushButton.clicked.connect(self.stirrmode_start_clicked)

        self.stirrer = Stirrer()
        self.velocity = 50 # in percent
        self.is_initialized = False

        curpos_timer = QtCore.QTimer()
        curpos_timer.setInterval(500)
        curpos_timer.timeout.connect(self._update_position)
        curpos_timer.start()

    def init_clicked(self):
        self.stirrer.initialize_drive()
        self.is_initialized = self.stirrer.drive_initialized
        self._update_position()

    def velocity_changed(self):
        self.velocity = self.ui.velocity_spinBox.value()

    def stopp_clicked(self):
        self.stirrer.stop_motor()
        self._update_position()

    def _update_position(self):
        if self.is_initialized:
            pos = self.stirrer.current_angle
            self.ui.cur_pos_label.setText(str(pos))

    def stirrmode_start_clicked(self):
        if self.is_initialized:
            vel = self.ui.velocity_spinBox.value()   # currently ignored
            if self.ui.stirrmode_cw_radioButton.isChecked():
                self.stirrer.run_clockwise()
            else:
                self.stirrer.run_anti_clockwise()

    def closeEvent(self, event):
        # fire confirmation box
        ret = QMessageBox.question(self, "StirrerRC",
                                       "Do you want to exit the application?",
                                           QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No)
        if ret == QMessageBox.StandardButton.Yes:
            # self._save_setup()
            self.stirrer.stop_motor()
            event.accept()
        else:
            event.ignore()



if __name__ == "__main__":
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    app.setOrganizationName("TUD-TETEMV")
    app.setOrganizationDomain("tu-dresden.de/et/tet")
    app.setApplicationName("StirrerRC")
    settings = QSettings()

    QLocale.setDefault(QLocale.Language.English)

    widget = MainWindow(settings)
    widget.show()
    sys.exit(app.exec())
