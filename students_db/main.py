from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QAction
import sys
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Students Management")
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        add_student_action = QAction('Add student', self)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)        
        
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Phone"))
        self.setCentralWidget(self.table)
        
    def load_data(self):
        connection = sqlite3.connect("students_db/database.db")
        result = connection.execute("SELECT * FROM students")
        print(list(result))
        for row_number, row_data in enumerate(result): 
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number)
                
            
        
app = QApplication(sys.argv)
app_calculator = MainWindow()
app_calculator.show()
app_calculator.load_data()
sys.exit(app.exec())