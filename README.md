# fourier-series-visualization

This project is aimed at creating an interactive program for visualizing the Fourier series of a given function with GUI. Fourier series decomposition allows representing periodic functions as a sum of sinusoidal components, making it valuable in signal processing, image compression, and various scientific applications.

![fourier_series](https://latex.codecogs.com/svg.image?f(x)=a_0&plus;\sum_{n=1}^{\infty}a_n\cos\left(\frac{n\pi&space;x}{L}\right)&plus;\sum_{n=1}^{\infty}b_n\sin\left(\frac{n\pi&space;x}{L}\right))



## Project Structure

- `main.py`: Main entry point for the application. Launches the QApplication and runs the FourierSeriesApp.

- `safe_dict.py`: Contains the function to create a dictionary with safe math functions for expression evaluation.

- `mpl_widget.py`: Custom QWidget for embedding Matplotlib figures in PyQt5 applications.

- `fourier_series.py`: Handles Fourier series visualization, including the evaluation of Fourier series components.

- `visualize.py`: Implements the FourierSeriesApp class, responsible for handling the GUI and launching the application.

- `window.py`: Defines the Window class, which sets up the main GUI layout using PyQt5.



## Usage

1. Run `main.py` to launch the Fourier Series Visualization application.

2. Input the required parameters in the GUI, such as expressions for a0, an, and bn, modulation, time interval, etc.

3. Click the "Plot" button to visualize the Fourier series based on the provided parameters.

4. Exit the application using the "Exit" button.



## Dependencies

The project relies on the following libraries:

- PyQt5: A set of Python bindings for Qt libraries, used for creating the graphical user interface.

- Matplotlib: A plotting library for the Python programming language, used to visualize the Fourier series.

- NumPy: A powerful library for numerical operations, providing support for array manipulations in this project.



## Additional Comments

- The code is modularized for better organization and readability.

- Docstrings and comments have been added to explain the purpose of classes, methods, and code blocks.

- The README file serves as comprehensive documentation, providing an overview of the project, its structure, functionality, and usage instructions.



## Author

👤 **Aras Güngöre**

- LinkedIn: [@arasgungore](https://www.linkedin.com/in/arasgungore)
- GitHub: [@arasgungore](https://github.com/arasgungore)
