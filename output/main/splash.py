# -*- coding: utf-8 -*-
import time
from PyQt5.QtWidgets import QSplashScreen
from PyQt5.QtGui import QPixmap
class Splash():
       #Р вЂ”Р В°Р С–РЎР‚РЎС“Р В·Р С”Р В° Р В·Р В°РЎРѓРЎвЂљР В°Р Р†Р С”Р С‘
    def splash_loading(self):
        splash=QSplashScreen(QPixmap("img\SplashScreen.jpg"))
        splash.show()
        time.sleep(3)
        splash.finish(self)