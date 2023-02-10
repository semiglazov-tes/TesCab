# -*- coding: utf-8 -*-
import time
from PyQt5.QtWidgets import QSplashScreen
from PyQt5.QtGui import QPixmap
class Splash():
       #Заставка перед запуском приложения
    def splash_loading(self):
        splash=QSplashScreen(QPixmap("img\SplashScreen.jpg"))
        splash.show()
        time.sleep(3)
        splash.finish(self)