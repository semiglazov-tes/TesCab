# -*- coding: utf-8 -*-
import time
from PyQt5.QtWidgets import QSplashScreen
from PyQt5.QtGui import QPixmap
class Splash():
    #Заставка перед запуском приложения
    def __init__(self,mainwindow):
        self.splash=QSplashScreen(QPixmap("img\SplashScreen.jpg"))
        self.splash.show()
        time.sleep(3)
        self.splash.finish(mainwindow)