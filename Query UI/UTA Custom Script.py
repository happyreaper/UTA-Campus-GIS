import sys 
sys.path.insert(0,r'C:\PythonGui')
from PyQt4.QtGui import QApplication, QDialog
from UTA_GUI import Ui_MapQueryDialog
from PyQt4.QtSql import *
import processing

uri = QgsDataSourceURI()
uri.setConnection("localhost", "5432", "uta_map_sdb", "postgres", "password")
#uri.setDataSource("public", "uta_buildings", "geom")
db = QSqlDatabase.addDatabase("QPSQL");
db.setDatabaseName(uri.database())
db.setPort(int(uri.port()))
db.setUserName(uri.username())
db.setPassword(uri.password())
db.open()
window = QDialog()
ui = Ui_MapQueryDialog()
ui.setupUi(window)
window.show()
def pushButton_1_click():
   firstQuery()
def pushButton_2_click():
  secondQuery()
def pushButton_3_click():
    thirdQuery() 
def pushButton_4_click():
   fourthQuery()
    
def firstQuery():
    ui.queryResults.clear()
    if(ui.withinCombo.currentIndex()==0):
       query = db.exec_("""select n.name from uta_buildings as n, uta_buildings as s where  n.description='{}' and s.name ='{}' and ST_DWithin(n.geom,s.geom,{},true)""".format(ui.buildDescription.text(),ui.BuildName.text(),int(ui.buildRadius.text())))
       while(query.next()):
           ui.queryResults.append(query.value(0))
    if(ui.withinCombo.currentIndex()==1):
        query = db.exec_("""select n.id from uta_buildings as n, uta_buildings as s where  n.description='{}' and s.name ='{}' and ST_DWithin(n.geom,s.geom,{},true)""".format(ui.buildDescription.text(),ui.BuildName.text(),int(ui.buildRadius.text())))
        names=[];
        while(query.next()):
            names.append(query.value(0))
        layer=processing.getObject('uta_buildings')
        layer.setSelectedFeatures(names)
        ui.queryResults.setText("See on UTA Map")
    
def secondQuery():  
    ui.queryResults.clear()
    if(ui.typeCombo.currentIndex()==0):
       query = db.exec_("""select name from uta_buildings where  description='{}' """.format(ui.buildType.text()))
       while(query.next()):
           ui.queryResults.append(query.value(0))
    if(ui.typeCombo.currentIndex()==1):
        query = db.exec_("""select id from uta_buildings where  description='{}' """.format(ui.buildType.text()))
        names=[];
        while(query.next()):
            names.append(query.value(0))
        print names
        layer=processing.getObject('uta_buildings')
        layer.setSelectedFeatures(names)
        ui.queryResults.setText("See on UTA Map")
        
    
def thirdQuery():
    query = db.exec_("""select ST_Distance(s.geom,n.geom,true) from uta_buildings as s, uta_buildings as n where s.name='{}' and n.name='{}' """.format(ui.buildingOne.text(),ui.buidlingTwo.text()))
    while(query.next()):
         ui.queryResults.setText(str(round(query.value(0),2))+" (meters)")
def fourthQuery():  
     ui.queryResults.clear()
     if(ui.nearCombo.currentIndex()==0):
         query = db.exec_("""select n.name, ST_Distance(n.geom,s.geom,true) as distance from uta_buildings as n, uta_buildings as s where ST_Distance(n.geom,s.geom,true)>0 and n.description='{}' and s.name ='{}' order by distance asc LIMIT 1""".format(ui.buildNearType.text(),ui.buildNearName.text()))
         while(query.next()):
             ui.queryResults.append(query.value(0)+" : "+str(round(query.value(1),2))+"(meters)")
     if(ui.nearCombo.currentIndex()==1):
         query = db.exec_("""select n.id,ST_Distance(n.geom,s.geom,true) as distance  from uta_buildings as n, uta_buildings as s where ST_Distance(n.geom,s.geom,true)>0 and n.description='{}' and s.name ='{}' order by distance asc LIMIT 1""".format(ui.buildNearType.text(),ui.buildNearName.text()))
         names=[];
         while(query.next()):
             names.append(query.value(0))
         layer=processing.getObject('uta_buildings')
         layer.setSelectedFeatures(names)
         ui.queryResults.setText("See on UTA Map")
    
ui.pushButton_1.clicked.connect(pushButton_1_click)
ui.pushButton_2.clicked.connect(pushButton_2_click)
ui.pushButton_3.clicked.connect(pushButton_3_click)
ui.pushButton_4 .clicked.connect(pushButton_4_click)