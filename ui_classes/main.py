import os
from dataclasses import dataclass

from PySide6.QtCore import QObject, Signal, QThread
from PySide6.QtWidgets import QMainWindow, QFileDialog

from ui.main import Ui_MainWindow
from ui_classes.transcode import TranscodeWindow


class MainWindow(QMainWindow):
    # Window Setup
    def __init__(self, stacked):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Recursive Handbrake - Configuration")
        self.ui.tabWidget.setCurrentIndex(0)

        # Variables
        self.stacked = stacked
        self.file_extensions = ["txt", "srt", "jpg", "png"]
        self.movies = []

        # Connections
        self.ui.browse_directories_button.clicked.connect(self.select_directory)
        self.ui.add_file_extension.clicked.connect(self.add_extension)
        self.ui.begin_encoding_button.clicked.connect(self.begin_encoding)

        # Setup threads
        self.thread = QThread()
        self.discovery_worker = DiscoveryWorker()
        self.discovery_worker.moveToThread(self.thread)
        self.thread.started.connect(self.discovery_worker.run)
        self.discovery_worker.add_movie.connect(self.load_discovered_movie)
        self.discovery_worker.finished.connect(self.finished_discovering_movies)

    def begin_encoding(self):
        window = TranscodeWindow(self.movies)
        self.stacked.addWidget(window)
        self.stacked.setCurrentIndex(self.stacked.currentIndex() + 1)

    # Select Directory
    def select_directory(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.ui.movies_list.clear()
        self.discovery_worker.path = file
        self.ui.directory_path.setText(file)
        self.thread.start()
        self.ui.browse_directories_button.setEnabled(False)

    # Called when DiscoveryWorker has finished walking the specified directory
    def finished_discovering_movies(self):
        self.ui.progress.setValue(0)

    # Called when the add extension button is clicked
    def add_extension(self):
        self.file_extensions.append(self.ui.file_extension.text())
        self.ui.file_extensions_table.addItem(self.ui.file_extension.text())

    # Save all discovered movies into memory, display them in a list for the user
    def load_discovered_movie(self, n):
        # get the file extension
        extension = list(reversed(n.file.split(".")))[0]

        # check if its in the blacklist/whitelist
        if extension not in self.file_extensions:
            self.ui.movies_list.addItem(n.file)
            self.movies.append(n)

        if self.ui.progress.value() == self.ui.progress.maximum() - 10:
            self.ui.progress.setMaximum(self.ui.progress.maximum() + 50)
        self.ui.progress.setValue(self.ui.progress.value() + 1)

        self.ui.movies_list.scrollToBottom()


@dataclass
class Movie:
    file: str
    path: str
    directory: str


class DiscoveryWorker(QObject):
    add_movie = Signal(Movie)
    finished = Signal()
    walk_length = Signal(int)
    path = ""

    def run(self):
        # walk over the directory specified in config path
        walk = os.walk(self.path)
        for root, dirs, files in walk:
            for name in files:
                self.add_movie.emit(Movie(file=name, path=root + name, directory=root))
        self.finished.emit()