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
        #Создание таблицы дата/сумма
        self.eatTable=EatTabletView()
        self.eatTable.initializationEatTableView()
        self.eatTable
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
        self.eatCalendar.activated.connect(self.twoClickOnDate) 

        #Обработчик события двойного нажатия левой кнопкой мыши на дату QCalendarWidget
    def twoClickOnDate(self):
        selectedDateStr=self.eatCalendar.selectedDate().toString("yyyy.MM.dd")
        print(selectedDateStr)

class EatTabletView(QtWidgets.QTableView):
    def __init__(self):
        super().__init__()
        self.sizePolicy=QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding);
        self.setSizePolicy(self.sizePolicy)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setSectionResizeMode(1)
    """def resizeEvent(self, event):   self.resize(event.size())"""

    def initializationEatTableView(self):
        #Создание подключения к базе данных для первичного отображения таблицы-оточета по питанию
        con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        con.setDatabaseName("db\\tesCabDb.db3")
        con.open()
        sqm = QtSql.QSqlQueryModel()
        sqm.setQuery('select * from tesEatReport')
        sqm.setHeaderData(1, QtCore.Qt.Horizontal, 'Дата')
        sqm.setHeaderData(2, QtCore.Qt.Horizontal, 'Сумма')
        self.setModel(sqm)
        self.hideColumn(0)
        self.show()
        con.close()
    
        