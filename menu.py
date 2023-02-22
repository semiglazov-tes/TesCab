# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from eatReportWindow import EatReportWindow
class Menu(QtWidgets.QWidget):
        #Создание меню главного окна
    def __init__(self,mainWindow):
        super().__init__()
        self.parentWindow=mainWindow
        self.subMenu=mainWindow.menuBar().addMenu("Отчеты")
        #Создание подменю "Отчет о питании"
        self.eatMenuTrigered=QtWidgets.QAction("Отчет о питании",self)
        self.eatMenuTrigered.triggered.connect(self.eatMenuClicked)
        self.subMenu.addAction(self.eatMenuTrigered)
        #Создание подменю "Рабочий отчет"
        self.workMenuTrigered=QtWidgets.QAction("Рабочий отчет",self)
        self.workMenuTrigered.triggered.connect(self.workMenuClicked)
        self.subMenu.addAction(self.workMenuTrigered)
        #Обработчик события нажатия на "Отчет о питании"
    def eatMenuClicked(self):
        self.eatReportWindow=EatReportWindow(self.parentWindow)
        #Обработчик события нажатия на "Рабочий отчет"
    def workMenuClicked(self):
        self.window=QtWidgets.QWidget()
        self.window.resize(100,100)
        self.window.show()

        