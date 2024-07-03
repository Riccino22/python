from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton
import sys

class AppStudens(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Students Management")
        grid = QGridLayout()
                
        self.setLayout(grid)
        


app = QApplication(sys.argv)
app_calculator = AppStudens()
app_calculator.show()
sys.exit(app.exec())