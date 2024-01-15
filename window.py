from PyQt5 import QtCore, QtGui, QtWidgets
from mpl_widget import MplWidget

class Window(object):
    """
    GUI setup class using PyQt5.
    """

    def setup_ui(self, MainWindow):
        """
        Set up the main GUI layout and components.
        """
        # Create and configure the main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 840)

        # Set up central widget and layout
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")

        # Add Plot and Exit buttons
        self.button_plot = QtWidgets.QPushButton(self.central_widget)
        self.button_plot.setGeometry(QtCore.QRect(220, 720, 100, 30))
        self.button_plot.setObjectName("button_plot")

        self.button_exit = QtWidgets.QPushButton(self.central_widget)
        self.button_exit.setGeometry(QtCore.QRect(340, 720, 100, 30))
        self.button_exit.setObjectName("button_exit")

        # Create MplWidgets for plotting
        self.mpl_function = MplWidget(self.central_widget)
        self.mpl_function.setGeometry(QtCore.QRect(40, 30, 560, 220))
        self.mpl_function.setObjectName("MplWidget")

        self.mpl_magnitude = MplWidget(self.central_widget)
        self.mpl_magnitude.setGeometry(QtCore.QRect(40, 250, 270, 220))
        self.mpl_magnitude.setObjectName("MplWidget2")

        self.mpl_phase = MplWidget(self.central_widget)
        self.mpl_phase.setGeometry(QtCore.QRect(330, 250, 270, 220))
        self.mpl_phase.setObjectName("MplWidget3")

        # Add labels and text fields
        self.label_an = QtWidgets.QLabel(self.central_widget)
        self.label_an.setGeometry(QtCore.QRect(125, 480, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_an.setFont(font)
        self.label_an.setObjectName("label_an")

        # Set the main layout for the central widget
        self.set_layout(MainWindow)

    def set_layout(self, MainWindow):
        """
        Set the main layout for the central widget.
        """
        # Set up the layout for the central widget
        self.vertical_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.vertical_layout.setObjectName("vertical_layout")

        # Add widgets to the layout
        self.vertical_layout.addWidget(self.button_plot)
        self.vertical_layout.addWidget(self.button_exit)
        self.vertical_layout.addWidget(self.mpl_function)
        self.vertical_layout.addWidget(self.mpl_magnitude)
        self.vertical_layout.addWidget(self.mpl_phase)

        # Set the central widget for the main window
        MainWindow.setCentralWidget(self.central_widget)

        # Set up menu bar and status bar
        self.setup_menu_bar(MainWindow)
        self.setup_status_bar(MainWindow)

        # Set fixed size for the window
        self.set_fixed_size()

    def set_fixed_size(self):
        """
        Set a fixed size for the main window.
        """
        self.central_widget.setFixedSize(self.central_widget.size())

    def setup_menu_bar(self, MainWindow):
        """
        Set up the menu bar for the main window.
        """
        # Create and configure the menu bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

    def setup_status_bar(self, MainWindow):
        """
        Set up the status bar for the main window.
        """
        # Create and configure the status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

    def retranslate_ui(self, MainWindow):
        """
        Translate and set text for UI components.
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fourier Series Visualization"))
        self.button_plot.setText(_translate("MainWindow", "Plot"))
        self.button_exit.setText(_translate("MainWindow", "Exit"))
        self.label_an.setText(_translate("MainWindow", "an"))

    def close_window(self):
        """
        Close the application.
        """
        QtCore.QCoreApplication.instance().quit()