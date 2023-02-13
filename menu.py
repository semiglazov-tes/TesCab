# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
class Menu():
        #Создание меню главного окна
    def createMenu(self):
        menubar=self.menuBar()
        subMenu=menubar.addMenu("Отчеты")
        #Создание подменю "Отчет о питании"
        eatMenuTrigered=QtWidgets.QAction("Отчет о питании",self)
        eatMenuTrigered.triggered.connect(self.eatMenuClicked)
        subMenu.addAction(eatMenuTrigered)
        #Создание подменю "Рабочий отчет"
        workMenuTrigered=QtWidgets.QAction("Рабочий отчет",self)
        workMenuTrigered.triggered.connect(self.workMenuClicked)
        subMenu.addAction(workMenuTrigered)

        #Обработчик события нажатия на "Отчет о питании"
    def eatMenuClicked(self):
        self.eatCalendar=QtWidgets.QCalendarWidget(parent=self)
        self.eatCalendar.resize(200,200)
        self.eatCalendar.show()
        self.eatCalendar.activated.connect(self.showTwoDate)    
        #Обработчик события двойного нажатия левой кнопкой мыши на дату QCalendarWidget
    def showTwoDate(self):
        #print(self.eatCalendar.selectedDate())
        print("showTwoDate")
    
        





        #Обработчик события нажатия на "Рабочий отчет"
    def workMenuClicked(self):
        self.window=QtWidgets.QWidget()
        self.window.resize(100,100)
        self.window.show()

        