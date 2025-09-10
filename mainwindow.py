# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QPushButton

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.startButton.clicked.connect(self.startButton_clicked)
        self.ui.settingsButton.clicked.connect(self.settingsButton_clicked)
        self.ui.exitButton.clicked.connect(self.exitButton_clicked)

    def startButton_clicked(self):
        print("Start Button was clicked!")
        # do something here

    def settingsButton_clicked(self):
        print("Settings Button was clicked!")
        self.settings_window = SettingsWindow()
        self.settings_window.exec()

    def exitButton_clicked(self):
        print("Exit Button was clicked!")
        self.close()

class SettingsWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.setFixedSize(300, 200)  # small window size

        layout = QVBoxLayout()

        label = QLabel("Settings go here!")
        layout.addWidget(label)

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.setLayout(layout)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
