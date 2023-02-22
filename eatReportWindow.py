from PyQt5 import QtWidgets,QtCore,QtSql      
class EatReportWindow(QtWidgets.QWidget):
        #Создание окна отчетов по питанию
    def __init__(self,mainWindow):
        super().__init__()
        #Создание основного контейнера
        self.container=QtWidgets.QWidget()
        self.container.setParent(mainWindow)

        #Создание календаря
        self.eatCalendar=QtWidgets.QCalendarWidget()
        self.eatCalendar.setFixedSize(400,400)
       
        #Создание таблицы дата/сумма
        self.eatTable=QtWidgets.QTableView(self)
        self.eatTable.setFixedSize(177,400)
        #Создание подключения к базе данных
        con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        con.setDatabaseName("db\\testdb.db3")
        con.open()
        sqm = QtSql.QSqlQueryModel(self)
        sqm.setQuery('select * from test')
        sqm.setHeaderData(1, QtCore.Qt.Horizontal, 'Дата')
        sqm.setHeaderData(2, QtCore.Qt.Horizontal, 'Сумма')
        self.eatTable.setModel(sqm)
        self.eatTable.hideColumn(0)
        self.eatTable.setColumnWidth(1,80)
        self.eatTable.setColumnWidth(2,80)
        self.eatTable.show()
        #Создание контейнера для выравнивания виджетов по горизонтали
        self.hbox =QtWidgets.QHBoxLayout()
        self.hbox.addWidget(self.eatTable)
        self.hbox.addWidget(self.eatCalendar)
        #добавление в основной контейнер 
        self.container.setLayout(self.hbox)
        
        #расположение окна отчетов по питанию по центру главного окна
        x=(mainWindow.width()-self.container.width())//2
        y=(mainWindow.height()-self.container.height())//2
        self.container.move(x,y)
        self.container.show()

        #привязка события двойного щелчка ЛКМ на дату
        self.eatCalendar.activated.connect(self.showTwoDate) 

        #Обработчик события двойного нажатия левой кнопкой мыши на дату QCalendarWidget
    def showTwoDate(self):
        print(self.eatCalendar.selectedDate())
        selectedDateStr=self.eatCalendar.selectedDate().toString("yyyy.MM.dd")
        print(selectedDateStr)