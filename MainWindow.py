from PyQt6.QtWidgets import QMainWindow
from ChartView import ChartView


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setCentralWidget(ChartView(self))

        self.setMinimumWidth(894)
        self.setMinimumHeight(602)

        self.setWindowTitle("SA_ÜBUNG")
