import subprocess

from PySide6.QtCore import QObject, Signal, QThread, QProcess
from PySide6.QtWidgets import QMainWindow

from ui.transcode import Ui_MainWindow


class TranscodeWindow(QMainWindow):
    # Window Setup
    def __init__(self, movies):
        super(TranscodeWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Setup threads
        self.thread = QThread()
        self.encode_worker = EncodeWorker(movies)
        self.encode_worker.moveToThread(self.thread)
        self.thread.started.connect(self.encode_worker.run)
        self.encode_worker.progress.connect(self.record_progress)
        self.encode_worker.finished.connect(lambda: self.ui.encode_progress.setValue(self.ui.encode_progress.value() + 1))
        self.thread.start()

        # Handle Progress bar
        self.ui.encode_progress.setMaximum(len(movies))

    def record_progress(self, n):
        self.ui.encode_list.addItem(n)
        self.ui.encode_list.scrollToBottom()

class EncodeWorker(QObject):
    progress = Signal(str)
    finished = Signal()

    def __init__(self, movies):
        super(EncodeWorker, self).__init__()
        self.movies = movies
        self.runner = QProcess(self)

    def run(self):
        for movie in self.movies:
            self.runner.setWorkingDirectory(movie.directory)
            self.runner.start("HandBrakeCLI.exe", ["--preset-import-gui",
                                                   "--encoder",
                                                   "nvenc_h264",
                                                   "-i", movie.file,
                                                   "-o", movie.file + "_transcode.m4v"])
            self.runner.readyReadStandardOutput.connect(self.get_output)
            self.runner.waitForFinished()
            self.finished.emit()

    def get_output(self):
        process_output = bytes(self.runner.readAllStandardOutput()).decode("utf8")
        self.progress.emit(process_output)