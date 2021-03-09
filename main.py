# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 607)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 30, 131, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 130, 801, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(420, 10, 60, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(30, 95, 111, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(390, 30, 131, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(560, 30, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(260, 10, 60, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 90, 401, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 90, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(90, 10, 60, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(50, 30, 131, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.urunkodu = QtWidgets.QLineEdit(self.tab_2)
        self.urunkodu.setGeometry(QtCore.QRect(20, 70, 101, 31))
        self.urunkodu.setObjectName("urunkodu")
        self.tipi = QtWidgets.QLineEdit(self.tab_2)
        self.tipi.setGeometry(QtCore.QRect(140, 70, 91, 31))
        self.tipi.setObjectName("tipi")
        self.voltu = QtWidgets.QLineEdit(self.tab_2)
        self.voltu.setGeometry(QtCore.QRect(250, 70, 51, 31))
        self.voltu.setObjectName("voltu")
        self.boyu = QtWidgets.QLineEdit(self.tab_2)
        self.boyu.setGeometry(QtCore.QRect(330, 70, 61, 31))
        self.boyu.setObjectName("boyu")
        self.kullailanaraclari = QtWidgets.QLineEdit(self.tab_2)
        self.kullailanaraclari.setGeometry(QtCore.QRect(580, 70, 151, 31))
        self.kullailanaraclari.setObjectName("kullailanaraclari")
        self.capi = QtWidgets.QLineEdit(self.tab_2)
        self.capi.setGeometry(QtCore.QRect(410, 70, 61, 31))
        self.capi.setObjectName("capi")
        self.disi = QtWidgets.QLineEdit(self.tab_2)
        self.disi.setGeometry(QtCore.QRect(490, 70, 61, 31))
        self.disi.setObjectName("disi")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(29, 50, 91, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(160, 50, 60, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(260, 50, 60, 16))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(340, 50, 60, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(420, 50, 60, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(500, 50, 60, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(590, 50, 131, 21))
        self.label_12.setObjectName("label_12")
        self.urunkaydet = QtWidgets.QPushButton(self.tab_2)
        self.urunkaydet.setGeometry(QtCore.QRect(200, 120, 341, 41))
        self.urunkaydet.setObjectName("urunkaydet")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
# KÜÇÜK BÜYÜK DUYARSIZ

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Kafa Çapı"))
        self.label_4.setText(_translate("MainWindow", "Hızlı Sorgu"))
        self.pushButton.setText(_translate("MainWindow", "Sorgula"))
        self.label_2.setText(_translate("MainWindow", "Boy"))
        self.pushButton_2.setText(_translate("MainWindow", "Hızlı Sorgula"))
        self.label.setText(_translate("MainWindow", "Diş"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Ürün Sorgula"))
        self.label_5.setText(_translate("MainWindow", "Ürün Kodu"))
        self.label_6.setText(_translate("MainWindow", "Tipi"))
        self.label_7.setText(_translate("MainWindow", "Volt"))
        self.label_9.setText(_translate("MainWindow", "Boy"))
        self.label_10.setText(_translate("MainWindow", "Kafa Çapı"))
        self.label_11.setText(_translate("MainWindow", "Diş"))
        self.label_12.setText(_translate("MainWindow", "Kullanılan Araçlar"))
        self.urunkaydet.setText(_translate("MainWindow", "Veri Kaydet"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Ürün Girişi"))
        self.pushButton_2.clicked.connect(self.hizlisorgula)
        self.pushButton.clicked.connect(self.sorgula)
        self.urunkaydet.clicked.connect(self.verigir)
    def hizlisorgula(self):
        self.veriler=[]
        self.hizliveri=self.lineEdit_4.text()
        self.hizliverial()
        self.tabloya_yaz()



    def sorgula(self):
        self.veriler=[]
        self.dis=self.lineEdit.text()
        self.boy=self.lineEdit_2.text()
        self.cap=self.lineEdit_3.text()
        self.verial()
        self.tabloya_yaz()
    def tabloya_yaz(self):
        self.tableWidget.setRowCount(len(self.veriler)+1)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setItem(0,0,QtWidgets.QTableWidgetItem("Ürün Kodu"))
        self.tableWidget.setItem(0,1,QtWidgets.QTableWidgetItem("Tipi"))
        self.tableWidget.setItem(0,2,QtWidgets.QTableWidgetItem("Volt"))
        self.tableWidget.setItem(0,3,QtWidgets.QTableWidgetItem("Boy"))
        self.tableWidget.setItem(0,4,QtWidgets.QTableWidgetItem("Çap"))
        self.tableWidget.setItem(0,5,QtWidgets.QTableWidgetItem("Diş"))
        self.tableWidget.setItem(0,6,QtWidgets.QTableWidgetItem("K.Araçlar"))
        satir=0
        sutun=0
        for i in self.veriler:
            print(satir)
            satir+=1
            sutun=0
            for j in i:
                print(j)
                self.tableWidget.setItem(satir,sutun,QtWidgets.QTableWidgetItem(str(j)))
                sutun+=1
        
        self.tableWidget.setColumnCount(sutun)
        
    def verial(self):
        if self.cap=="":
            try:
                sqliteConnection = sqlite3.connect('urun.db')
                cursor = sqliteConnection.cursor()
                print("Connected to SQLite")
                records=[]
                sql_select_query = """select * from uruntablo where Diş = ? AND Boy = ?"""
    
                for i in range(1,15):
                    cursor.execute(sql_select_query, (self.dis,str(float(self.boy)+i/10),))
                    records += cursor.fetchall()
                    cursor.execute(sql_select_query, (self.dis,str(float(self.boy)-i/10),))
                    records += cursor.fetchall()
                    cursor.execute(sql_select_query, (self.dis,self.boy,))
                    records += cursor.fetchall()
                records = list(dict.fromkeys(records))

                for row in records:
                    print("Ürün Kodu = ", row[0])
                    print("Tipi  = ", row[1])
                    print("Volt  = ", row[2])
                    print("Boy  = ", row[3])
                    print("Çap  = ", row[4])
                    print("Diş  = ", row[5])
                    print("Araçlar  = ", row[6])
                    self.veriler.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6]])
                cursor.close()
                return self.veriler
            except sqlite3.Error as error:
                print("Veriler Okunurken Hatayla karşılaşıldı", error)
            finally:
                if (sqliteConnection):
                    sqliteConnection.close()
                    print("Veritabanı Bağlantısı kapatıldı")
        elif self.boy=="":
            try:
                sqliteConnection = sqlite3.connect('urun.db')
                cursor = sqliteConnection.cursor()
                print("Connected to SQLite")
                records=[]
                sql_select_query = """select * from uruntablo where Diş = ? AND Çap = ?"""
    
                for i in range(1,15):
                    cursor.execute(sql_select_query, (self.dis,self.cap,))
                    records += cursor.fetchall()
                    cursor.execute(sql_select_query, (self.dis,str(float(self.cap)+i/10),))
                    records += cursor.fetchall()
                    cursor.execute(sql_select_query, (self.dis,str(float(self.cap)+i/10),))
                    records += cursor.fetchall()
                records = list(dict.fromkeys(records))

                for row in records:
                    print("Ürün Kodu = ", row[0])
                    print("Tipi  = ", row[1])
                    print("Volt  = ", row[2])
                    print("Boy  = ", row[3])
                    print("Çap  = ", row[4])
                    print("Diş  = ", row[5])
                    print("Araçlar  = ", row[6])
                    self.veriler.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6]])
                cursor.close()
                return self.veriler
            except sqlite3.Error as error:
                print("Veriler Okunurken Hatayla karşılaşıldı", error)
            finally:
                if (sqliteConnection):
                    sqliteConnection.close()
                    print("Veritabanı Bağlantısı kapatıldı") 
        elif self.dis=="":
            try:
                sqliteConnection = sqlite3.connect('urun.db')
                cursor = sqliteConnection.cursor()
                print("Connected to SQLite")
                records=[]
                sql_select_query = """select * from uruntablo where Çap = ? AND Boy = ?"""
    
                for i in range(1,15):
                    cursor.execute(sql_select_query, (str(float(self.boy)+i/10),self.cap,))
                    records += cursor.fetchall()
                    cursor.execute(sql_select_query, (str(float(self.boy)-i/10),self.cap,))
                    records += cursor.fetchall()
                    cursor.execute(sql_select_query, (self.boy,str(float(self.cap)+i/10),))
                    records += cursor.fetchall()
                    cursor.execute(sql_select_query, (self.boy,str(float(self.cap)+i/10),))
                    records += cursor.fetchall()
                    cursor.execute(sql_select_query, (str(float(self.boy)-i/10),str(float(self.cap)+i/10),))
                    records += cursor.fetchall()
                    cursor.execute(sql_select_query, (str(float(self.boy)-i/10),str(float(self.cap)+i/10),))
                    records += cursor.fetchall()
                cursor.execute(sql_select_query, (self.boy,self.cap,))
                records += cursor.fetchall()
                records = list(dict.fromkeys(records))
                for row in records:
                    print("Ürün Kodu = ", row[0])
                    print("Tipi  = ", row[1])
                    print("Volt  = ", row[2])
                    print("Boy  = ", row[3])
                    print("Çap  = ", row[4])
                    print("Diş  = ", row[5])
                    print("Araçlar  = ", row[6])
                    self.veriler.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6]])
                cursor.close()
                return self.veriler
            except sqlite3.Error as error:
                print("Veriler Okunurken Hatayla karşılaşıldı", error)
            finally:
                if (sqliteConnection):
                    sqliteConnection.close()
                    print("Veritabanı Bağlantısı kapatıldı")
        else:
            try:
                sqliteConnection = sqlite3.connect('urun.db')
                cursor = sqliteConnection.cursor()
                print("Connected to SQLite")
                records=[]
                sql_select_query = """select * from uruntablo where Diş = ? AND Boy = ? AND Çap = ?"""
    
                for i in range(1,15):
                    cursor.execute(sql_select_query, (self.dis,str(float(self.boy)+i/10),self.cap,))
                    records += cursor.fetchall()
                    cursor.execute(sql_select_query, (self.dis,str(float(self.boy)-i/10),self.cap,))
                    records += cursor.fetchall()
                    cursor.execute(sql_select_query, (self.dis,self.boy,str(float(self.cap)+i/10),))
                    records += cursor.fetchall()
                    cursor.execute(sql_select_query, (self.dis,self.boy,str(float(self.cap)+i/10),))
                    records += cursor.fetchall()
                    cursor.execute(sql_select_query, (self.dis,str(float(self.boy)-i/10),str(float(self.cap)+i/10),))
                    records += cursor.fetchall()
                    cursor.execute(sql_select_query, (self.dis,str(float(self.boy)-i/10),str(float(self.cap)+i/10),))
                    records += cursor.fetchall()
                cursor.execute(sql_select_query, (self.dis,self.boy,self.cap,))
                records += cursor.fetchall()
                records = list(dict.fromkeys(records))
                for row in records:
                    print("Ürün Kodu = ", row[0])
                    print("Tipi  = ", row[1])
                    print("Volt  = ", row[2])
                    print("Boy  = ", row[3])
                    print("Çap  = ", row[4])
                    print("Diş  = ", row[5])
                    print("Araçlar  = ", row[6])
                    self.veriler.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6]])
                cursor.close()
                return self.veriler
            except sqlite3.Error as error:
                print("Veriler Okunurken Hatayla karşılaşıldı", error)
            finally:
                if (sqliteConnection):
                    sqliteConnection.close()
                    print("Veritabanı Bağlantısı kapatıldı")

    def hizliverial(self):
        try:
            sqliteConnection = sqlite3.connect('urun.db')
            cursor = sqliteConnection.cursor()

            sql_select_query = """select * from uruntablo where Tipi = ? OR Araçlar = ? """
            cursor.execute(sql_select_query, (self.hizliveri,self.hizliveri,))
            records = cursor.fetchall()
            

            for row in records:
                print("Ürün Kodu = ", row[0])
                print("Tipi  = ", row[1])
                print("Volt  = ", row[2])
                print("Boy  = ", row[3])
                print("Çap  = ", row[4])
                print("Diş  = ", row[5])
                print("Araçlar  = ", row[6])
                self.veriler.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6]])
            cursor.close()
            return self.veriler
        except sqlite3.Error as error:
            print("Veriler Okunurken Hatayla karşılaşıldı", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("Veritabanı Bağlantısı kapatıldı")


    def veriyaz(self):

        try:
            girdi= ("'"+str(self.kod)+"'"+""",'"""+str(self.tip)+"""','"""+str(self.volt)+"""','"""+str(self.boy)+"""','"""+str(self.cap)+"""','"""+str(self.dis)+"""','"""+str(self.kullailanaraclar+"'"))
            print(girdi)
            sqliteConnection = sqlite3.connect('urun.db')
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")

            sqlite_insert_query = """INSERT INTO uruntablo
                                (Kodu, Tipi,Volt , Boy, Çap, Diş, Araçlar) 
                                VALUES 
                                ("""+str(girdi)+""")"""

            count = cursor.execute(sqlite_insert_query)
            sqliteConnection.commit()
            print("Record inserted successfully into urun table ", cursor.rowcount)
            
            msg.setWindowTitle("Başarılı")
            msg.setText("Ürün Girişi Başarılı!")
            x = msg.exec_()
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)
            
            
            msg.setWindowTitle("Hata")
            msg.setText("Ürün girişi yarpılırken hata ile karşılaşıldı!")
            x = msg.exec_()
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The SQLite connection is closed")

    
    def verigir(self):
        self.kod=self.urunkodu.text()
        self.tip=self.tipi.text()
        self.volt=self.voltu.text()
        self.boy=self.boyu.text()
        self.cap=self.capi.text()
        self.dis=self.disi.text()
        self.kullailanaraclar=self.kullailanaraclari.text()
        self.veriyaz()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    msg = QMessageBox()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
