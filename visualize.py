from PyQt5 import QtWidgets
from window import Window
from fourier_series import FourierSeries

class FourierSeriesApp(FourierSeries, Window, QtWidgets.QMainWindow):
    """
    Main class for the Fourier Series Visualization application.
    """

    def __init__(self, safe_dict):
        # Call the __init__ method of the superclasses in the correct order
        QtWidgets.QMainWindow.__init__(self)
        Window.__init__(self)
        FourierSeries.__init__(self, safe_dict)

        # Setup GUI
        self.setup_ui(self)

        # Connect buttons to functions
        self.button_plot.clicked.connect(self.update_graph)
        self.button_exit.clicked.connect(self.close_window)

    def get_input(self):
        """
        Get user input from the GUI elements.
        """
        self.limit_n = int(self.edit_n.text())
        self.time_interval = np.arange(float(self.edit_xstart.text()), float(self.edit_xend.text()), 0.01)
        data = np.zeros((2, self.time_interval.shape[0]))
        data[1, :] = self.time_interval
        self.data = data
        self.an_expression = self.text_an.toPlainText().splitlines()
        self.bn_expression = self.text_bn.toPlainText().splitlines()
        self.a0 = float(self.edit_a0.text())
        self.mod_num = int(self.edit_mod.text())
        self.period = float(self.edit_period.text())
        self.magnitude = np.zeros((2, self.limit_n))
        self.magnitude[1, :] = np.arange(1, self.limit_n + 1, 1)
        self.theta = np.zeros((2, self.limit_n))
        self.theta[1, :] = np.arange(1, self.limit_n + 1, 1)

    def update_graph(self):
        """
        Update the GUI with the Fourier series visualization.
        """
        self.get_input()
        self.data = self.find_values()
        self.plot_graph(self.data, "Fourier Series Visualization", self.mpl_function)
        self.plot_stem(self.magnitude, "Magnitude", self.mpl_magnitude)
        self.plot_stem(self.theta, "Phase", self.mpl_phase)

    def plot_graph(self, data, name, mpl_widget):
        """
        Plot a line graph using Matplotlib on the specified MplWidget.
        """
        mpl_widget.canvas.axes.clear()
        mpl_widget.canvas.axes.plot(data[1, :], data[0, :])
        mpl_widget.canvas.axes.set_title(name)
        mpl_widget.canvas.draw()

    def plot_stem(self, data, name, mpl_widget):
        """
        Plot a stem graph using Matplotlib on the specified MplWidget.
        """
        mpl_widget.canvas.axes.clear()
        mpl_widget.canvas.axes.stem(data[1, :], data[0, :], use_line_collection=True)
        mpl_widget.canvas.axes.set_title(name)
        mpl_widget.canvas.draw()

    def run(self):
        """
        Run the application.
        """
        self.show()
