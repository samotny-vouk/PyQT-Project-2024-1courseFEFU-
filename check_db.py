from PyQt5 import QtCore, QtGui, QtWidgets
from db_handler1 import *


class CheckThread(QtCore.QThread):
    my_signal = QtCore.pyqtSignal(str)
    Boolean_signal = QtCore.pyqtSignal(bool)

    def thr_login(self, name, passw):
        login(name, passw, self.my_signal, self.Boolean_signal)

    def thr_register(self, name, mail, passw):
        register(name, mail, passw, self.my_signal, self.Boolean_signal)

