#!/usr/bin/env python3
import os
import sys
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtCore import QDate

class DurationCalculator(QtWidgets.QMainWindow):

    def __init__(self):

        # init user interface:
        super(DurationCalculator, self).__init__()
        self.show()
        scriptPath = os.path.dirname(os.path.abspath(__file__))     # Fails if the script is executed by exec()
        self.ui = uic.loadUi(scriptPath + '/' + 'durationcalc.ui', self)

        # Event handlers:
        self.ui.caleldar_from.selectionChanged.connect(self.from_changed)
        self.ui.caleldar_to.selectionChanged.connect(self.to_changed)
        self.ui.spinbox_days.valueChanged.connect(self.days_changed)

        # Set start date to today
        today =  QDate.currentDate()
        self.ui.caleldar_from.setSelectedDate(today)
        self.from_changed() # signals are not emitted so we call this manually

    def from_changed(self):
        date_from = self.ui.caleldar_from.selectedDate()
        days = self.ui.spinbox_days.value()
        date_to = date_from.addDays(days - 1)
        self.ui.caleldar_to.blockSignals(True)
        self.ui.caleldar_to.setMinimumDate(date_from)
        self.ui.caleldar_to.setSelectedDate(date_to)
        self.ui.caleldar_to.blockSignals(False)
    
    def to_changed(self):
        date_to = self.ui.caleldar_to.selectedDate()
        date_from = self.ui.caleldar_from.selectedDate()
        days = date_from.daysTo(date_to)
        self.ui.spinbox_days.blockSignals(True)
        self.ui.spinbox_days.setValue(days + 1)
        self.ui.spinbox_days.blockSignals(False)
        
    def days_changed(self, days):
        date_from = self.ui.caleldar_from.selectedDate()
        date_to = date_from.addDays(days - 1)
        self.ui.caleldar_to.blockSignals(True)
        self.ui.caleldar_to.setSelectedDate(date_to)
        self.ui.caleldar_to.blockSignals(False)


def startApplication():
    app = QtWidgets.QApplication(sys.argv)
    window = DurationCalculator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    startApplication()
