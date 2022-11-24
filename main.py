import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)

        self.setFixedSize(960, 480)
        self.update_count = 0

        self.btn.clicked.connect(self.update)

    def paintEvent(self, event):
        self.update_count += 1
        if self.update_count <= 2:
            return

        painter = QPainter(self)
        painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        x, y = randint(25, self.frameGeometry().width() - 25), randint(25, self.frameGeometry().height() - 25)
        diameter = randint(25, min(self.frameGeometry().width() - x, self.frameGeometry().height() - y))
        painter.drawEllipse(x, y, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
