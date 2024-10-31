import sys
from cgitb import small

import self
from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.ui.clickButton.clicked.connect(self.Opcje)
        self.input = ''
        self.result = ''
        self.show()


    def Opcje(self):
        self.input = self.ui.inputLine.text()
        if self.ui.bigButton.isChecked():
            self.result = self.input.upper()
        elif self.ui.smallButton.isChecked():
            self.result = self.input.lower()
        elif self.ui.convertButton.isChecked():
            self.result = self.input.swapcase()

        self.ui.resultLine.setText(self.result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyForm()
    sys.exit(app.exec())

