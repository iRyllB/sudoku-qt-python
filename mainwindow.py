# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QLabel,
    QVBoxLayout, QPushButton, QLineEdit, QGridLayout
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt
from PySide6.QtGui import QIntValidator
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
        # Open Game Window
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

        self.setCentralWidget(self.ui)

        # Connect back button
        self.ui.backButton.clicked.connect(self.backButton_clicked)
        self.build_sudoku_board()

    def build_sudoku_board(self):
        """Create a 9x9 Sudoku board inside boardContainer."""
        # Ensure boardContainer has a layout
        if isinstance(self.ui.boardcontainer.layout(), QGridLayout):
            grid = self.ui.boardContainer.layout()
        else:
            grid = QGridLayout()
            self.ui.boardcontainer.setLayout(grid)

        grid.setSpacing(0)  # no spacing between cells
        self.cells = []

        for row in range(9):
            row_cells = []
            for col in range(9):
                cell = QLineEdit()
                cell.setMaxLength(1)  # one digit only
                cell.setFixedSize(40, 40)
                cell.setAlignment(Qt.AlignCenter)

                # Font and center
                cell.setStyleSheet("font-size: 18px; border: 1px solid black;")

                # Restrict input to numbers 1–9
                cell.setValidator(QIntValidator(1, 9, cell))

                # Add bold borders every 3 rows/cols
                top = 2 if row % 3 == 0 else 1
                left = 2 if col % 3 == 0 else 1
                right = 2 if col == 8 else 1
                bottom = 2 if row == 8 else 1

                cell.setStyleSheet(
                    f"font-size: 18px; border-top: {top}px solid black; "
                    f"border-left: {left}px solid black; "
                    f"border-right: {right}px solid black; "
                    f"border-bottom: {bottom}px solid black;"
                )

                grid.addWidget(cell, row, col)
                row_cells.append(cell)
            self.cells.append(row_cells)

    def backButton_clicked(self):
        print("Back Button was clicked")
        self.close()
        self.mainwindow.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
