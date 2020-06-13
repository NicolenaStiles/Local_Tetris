# Test file for graphics in python

from PyQt5.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication([])
    label = QLabel('Hello Nocco.')
    label.show()
    app.exec_()
