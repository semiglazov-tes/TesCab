# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from menu import Menu
from splash import Splash

#Создание главного окна
class UIMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800,600)
        self.setWindowTitle("Личный кабинет проектировщика")
        self.setWindowIcon(QIcon("img\\Icon.jpg"))
        self.splash=Splash(self)
        self.menu=Menu(self)
        self.show()
 
