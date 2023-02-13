# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication
from ui_main_window import UIMainWindow

#Точка входа в приложение
class mainWindow(UIMainWindow):
    #Инициализация главного окна приложения
    def __init__(self):
        super().__init__()
            
if __name__=="__main__":
    app=QApplication(sys.argv)
    mainwindow=UIMainWindow()
    sys.exit(app.exec_())
