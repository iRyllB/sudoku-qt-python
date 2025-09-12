# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QVBoxLayout, QPushButton
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from ui_form import Ui_MainWindow   # your main menu UI


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.startButton.clicked.connect(self.startButton_clicked)
        self.ui.settingsButton.clicked.connect(self.settingsButton_clicked)
        self.ui.exitButton.clicked.connect(self.exitButton_clicked)

    def startButton_clicked(self):
        print("Start Button was clicked!")
        # Pass self so GameWindow knows who called it
        self.game_window = GameWindow(self)
        self.game_window.show()
        self.hide()

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


class GameWindow(QMainWindow):
    def __init__(self, mainwindow):
        super().__init__()
        # Store reference to the main menu window
        self.mainwindow = mainwindow

        # Load maingame.ui dynamically
        loader = QUiLoader()
        ui_file = QFile("maingame.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)  # game UI is now inside self.ui
        ui_file.close()

        # Connect back button
        self.ui.backButton.clicked.connect(self.backButton_clicked)

    def backButton_clicked(self):
        print("Back Button was clicked")
        self.close()
        self.mainwindow.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
