from PyQt5.QtWidgets import QApplication
from visualize import FourierSeriesApp
from safe_dict import create_safe_dict

if __name__ == "__main__":
    app = QApplication([])
    safe_dict = create_safe_dict()
    fourier_series_app = FourierSeriesApp(safe_dict)
    fourier_series_app.run()
    app.exec_()
    