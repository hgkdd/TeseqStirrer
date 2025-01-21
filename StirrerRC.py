import sys

from PySide6.QtCore import (Qt, QLocale, QSettings)
from PySide6.QtGui import (QStandardItemModel, QStandardItem)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox,
                               QFileDialog, QTableWidgetItem, QVBoxLayout, QWidget)


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

    def closeEvent(self, event):
        # fire confirmation box
        ret = QMessageBox.question(self, "StirrerRC",
                                       "Do you want to exit the application?",
                                           QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No)
        if ret == QMessageBox.StandardButton.Yes:
            # self._save_setup()
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
