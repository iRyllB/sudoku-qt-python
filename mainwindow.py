# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QLabel,
    QVBoxLayout, QPushButton, QLineEdit, QGridLayout, QWidget
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt
from PySide6.QtGui import QIntValidator, QPainter, QPen
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


class SudokuBoard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.grid = QGridLayout(self)
        self.grid.setSpacing(0)
        self.cells = []

        cell_size = 50  # size of each Sudoku cell
        for row in range(9):
            row_cells = []
            for col in range(9):
                cell = QLineEdit()
                cell.setMaxLength(1)
                cell.setFixedSize(cell_size, cell_size)
                cell.setAlignment(Qt.AlignCenter)

                # Make cells invisible (only text shows)
                cell.setStyleSheet("""
                    border: none;
                    background: transparent;
                    font-size: 20px;
                """)

                # Only allow digits 1–9
                cell.setValidator(QIntValidator(1, 9, cell))

                self.grid.addWidget(cell, row, col)
                row_cells.append(cell)
            self.cells.append(row_cells)

    def paintEvent(self, event):
        """Draw Sudoku grid lines (thin + thick every 3 cells)."""
        painter = QPainter(self)
        rect = self.rect()
        size = rect.width() / 9

        # Thin lines
        pen = QPen(Qt.black, 1)
        painter.setPen(pen)
        for i in range(10):
            painter.drawLine(i * size, 0, i * size, rect.height())
            painter.drawLine(0, i * size, rect.width(), i * size)

        # Thick lines every 3 cells
        pen = QPen(Qt.black, 3)
        painter.setPen(pen)
        for i in range(0, 10, 3):
            painter.drawLine(i * size, 0, i * size, rect.height())
            painter.drawLine(0, i * size, rect.width(), i * size)


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

        # Insert Sudoku board into boardContainer
        self.build_sudoku_board()

    def build_sudoku_board(self):
        self.board = SudokuBoard(self.ui.boardcontainer)
        layout = QVBoxLayout(self.ui.boardcontainer)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.board)

    def backButton_clicked(self):
        print("Back Button was clicked")
        self.close()
        self.mainwindow.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
