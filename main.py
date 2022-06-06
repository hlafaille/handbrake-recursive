import sys

from PySide6.QtWidgets import QApplication, QStackedWidget

from ui_classes.main import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    stacked = QStackedWidget()
    window = MainWindow(stacked)
    stacked.addWidget(window)
    stacked.show()

    sys.exit(app.exec())