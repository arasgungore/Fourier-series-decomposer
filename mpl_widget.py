from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

class MplWidget(QWidget):
    """
    Custom QWidget for embedding Matplotlib figures in PyQt5 applications.
    """

    def __init__(self, parent=None):
        super(MplWidget, self).__init__(parent)
        self.canvas = FigureCanvas(Figure())

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        # Add Matplotlib canvas to the layout
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)
