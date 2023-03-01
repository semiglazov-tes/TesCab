from PyQt5 import QtWidgets,QtCore,QtSql
      
class EatReportWindow(QtWidgets.QWidget):
        #Создание окна отчетов по питанию
    def __init__(self,mainWindow):
        super().__init__()
        #Создание основного контейнера
        self.container=QtWidgets.QWidget()
        self.container.setParent(mainWindow)
        #Создание календаря
        self.eatCalendar=EatCalendar()
        #Создание таблицы дата/сумма
        self.eatTable=EatTabletView()
        self.eatTable.initializationEatTableView()
        #Создание контейнера для выравнивания виджетов по горизонтали
        self.hbox =QtWidgets.QHBoxLayout()
        self.hbox.addWidget(self.eatTable)
        self.hbox.addWidget(self.eatCalendar)
        #добавление в основной контейнер 
        self.container.setLayout(self.hbox)
        #расположение окна отчетов по питанию по центру главного окна и его отображение
        x=(mainWindow.width()-self.container.width())//2
        y=(mainWindow.height()-self.container.height())//2
        self.container.move(x,y)
        self.container.show()

class EatTabletView(QtWidgets.QTableView):
    def __init__(self):
        super().__init__()
        self.sizePolicy=QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        self.setSizePolicy(self.sizePolicy)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setSectionResizeMode(1)
    """def resizeEvent(self, event):   self.resize(event.size())"""
    
    #Первичное отображение таблицы дата-сумма при превом открытии вкладки "Отчет о питании"
    def initializationEatTableView(self):
        #Создание подключения к базе данных для первичного отображения таблицы-оточета по питанию
        con = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName("db\\tesCabDb.db3")
        con.open()
        #Если в таблице нет записей окно EatTabletView не отображается, при наличии записей они отображаюстя в EatTabletView
        query=QtSql.QSqlQuery()
        query.exec("select * from tesEatReport")
        numberOfRows=self.getNumberOfRows(query) 
        if numberOfRows==19:
            self.hide()
            print("1")
        else:     
            sqm = QtSql.QSqlQueryModel()
            sqm.setQuery('select * from tesEatReport')
            sqm.setHeaderData(1, QtCore.Qt.Horizontal, 'Дата')
            sqm.setHeaderData(2, QtCore.Qt.Horizontal, 'Сумма')
            self.setModel(sqm)
            self.hideColumn(0)
            print("2")
        con.close()
    #Получение количество записей в таблице   
    def getNumberOfRows(self,query):
        numberOfRows=0
        if(query.last()):
            numberOfRows =query.at() + 1;
            query.first()
        return numberOfRows

class EatCalendar(QtWidgets.QCalendarWidget):
    def __init__(self):
        super().__init__()
        #привязка события двойного щелчка ЛКМ на дату
        self.activated.connect(self.twoClickOnDate)
         
        #Обработчик события двойного нажатия левой кнопкой мыши на дату QCalendarWidget
    def twoClickOnDate(self):
        selectedDateStr=self.selectedDate().toString("yyyy.MM.dd")
        con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        con.setDatabaseName("db\\tesCabDb.db3")
        con.open()
        sqm = QtSql.QSqlQueryModel()
        sqm.setQuery('insert into tesEatReport values () ')
        print(selectedDateStr)
        