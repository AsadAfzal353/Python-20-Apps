from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton, QComboBox

import sys


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        # Create widgets
        dist_label = QLabel("Distance:")
        self.dist_line_edit = QLineEdit()

        time_label = QLabel("Time (hours):")
        self.time_line_edit = QLineEdit()

        self.units_label = QComboBox()
        self.units_label.addItems(['Metric (km)', 'Imperial (mi)'])

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")

        # Add widgets to grid
        grid.addWidget(dist_label, 0, 0)
        grid.addWidget(self.dist_line_edit, 0, 1)
        grid.addWidget(self.units_label, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 2)
        
        self.setLayout(grid) # Inherited from QWidget

    def calculate_speed(self):
        speed = float(self.dist_line_edit.text())/float(self.time_line_edit.text())

        if self.units_label.currentText() == 'Metric (km)':
            units = "km/h"
        elif self.units_label.currentText() == 'Imperial (mi)':
            speed /= 1.609
            units = "mph"

        self.output_label.setText(f"Average Speed: {round(speed, 2)} {units}")


app = QApplication(sys.argv) # list of paths
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())