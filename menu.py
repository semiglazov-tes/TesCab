# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QAction
from PyQt5 import QtSql,QtCore,QtWidgets
class Menu():
        #Создание меню главного окна
    def createMenu(self):
        fileMenuTrigered=QAction("Инфо",self)
        fileMenuTrigered.triggered.connect(self.showfileMenu)
        menubar=self.menuBar()
        fileMenu=menubar.addMenu("Файл")
        fileMenu.addAction(fileMenuTrigered)

        #Обработчик события нажатия на "Инфо"
    def showfileMenu(self):
        self.datawindow=QtWidgets.QTableView(self)
        con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        con.setDatabaseName("db\\testdb.db3")
        con.open()
        sqm = QtSql.QSqlQueryModel(self)
        sqm.setQuery('select * from test')
        sqm.setHeaderData(1, QtCore.Qt.Horizontal, 'Имя')
        sqm.setHeaderData(2, QtCore.Qt.Horizontal, 'Игровой номер')
        self.datawindow.setModel(sqm)
        self.datawindow.hideColumn(0)
        self.datawindow.setColumnWidth(1, 150)
        self.datawindow.setColumnWidth(2,150)
        self.datawindow.resize(600,400)
        self.datawindow.show()