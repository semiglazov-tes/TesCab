# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QAction
from PyQt5 import QtSql,QtCore,QtWidgets
class Menu():
        #Р РЋР С•Р В·Р Т‘Р В°Р Р…Р С‘Р Вµ Р С�Р ВµР Р…РЎР‹ Р С–Р В»Р В°Р Р†Р Р…Р С•Р С–Р С• Р С•Р С”Р Р…Р В°
    def createMenu(self):
        fileMenuTrigered=QAction("Р СћР В°Р В±Р В»Р С‘РЎвЂ Р В°",self)
        fileMenuTrigered.triggered.connect(self.showfileMenu)
        menubar=self.menuBar()
        fileMenu=menubar.addMenu("Р В¤Р В°Р в„–Р В»")
        fileMenu.addAction(fileMenuTrigered)

        #Р С›Р В±РЎР‚Р В°Р В±Р С•РЎвЂљРЎвЂЎР С‘Р С” Р Р…Р В°Р В¶Р В°РЎвЂљР С‘РЎРЏ Р Р…Р В° Р С—Р С•Р Т‘Р С�Р ВµР Р…РЎР‹ РЎвЂћР В°Р в„–Р В»
    def showfileMenu(self):
        self.datawindow=QtWidgets.QTableView(self)
        con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        con.setDatabaseName("db\\testdb.db3")
        con.open()
        sqm = QtSql.QSqlQueryModel(self)
        sqm.setQuery('select * from test')
        sqm.setHeaderData(1, QtCore.Qt.Horizontal, 'Р пїЅР С�РЎРЏ')
        sqm.setHeaderData(2, QtCore.Qt.Horizontal, 'Р пїЅР С–РЎР‚Р С•Р Р†Р С•Р в„– Р Р…Р С•Р С�Р ВµРЎР‚')
        self.datawindow.setModel(sqm)
        self.datawindow.hideColumn(0)
        self.datawindow.setColumnWidth(1, 150)
        self.datawindow.setColumnWidth(2, 60)
        self.datawindow.resize(600,400)
        self.datawindow.show()