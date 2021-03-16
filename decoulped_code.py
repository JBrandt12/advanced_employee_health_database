from employee_health import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sqlite3
from pprint import pprint 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *




def show_fit_testing():
    ui.Fit_testing_date.show()
    ui.label_2.show()

def show_ppe_audit():
    ui.label_8.show()
    ui.PPE_audit_date.show()

def save_user_input(list):
    conn = sqlite3.connect("employee_health.db")
    cursor = conn.cursor()
    first = ui.First_Name_input.text()
    first_name = first.lower()
    last_name = ui.Last_name_input.text()
    last_name.lower()
    full_name = first_name.lower() + " " + last_name.lower()
    dept = ui.Department_combo.currentText()
    date_started = ui.Start_Date.text()
    annual = ui.Annual_complete_date.text()
    fit_t = ui.Fit_testing_date.text()
    ppe = ui.PPE_audit_date.text()
    row = (full_name, first_name, last_name, dept, date_started, annual, fit_t, ppe)
    command = '''INSERT INTO employee1 VALUES ?, ?, ?, ?, ?, ?, ?, ? '''
    # cursor.execute(command, row)
    cursor.execute('''INSERT INTO employee1 (full_name, firstname, lastname, department, start_date, annual_complete, fit_testing, ppe_audit) VALUES(?,?,?,?,?,?,?,?)''', (row))
    conn.commit()
    conn.close()

    
    
def test_table():
    db = sqlite3.connect("employee_health.db")
    cursor=db.cursor()
    command = ''' SELECT * from employee1'''
    result = cursor.execute(command)
    for row_number, row_data in enumerate(result):
        ui.tableWidget.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            ui.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    all_rows = cursor.fetchall()

def Search_field(first_name):
    
    user_input = ui.Search_input.text()
    my_data = (user_input)
    conn = sqlite3.connect("employee_health.db")
    c = conn.cursor()
    c.execute (" SELECT * FROM employee1 WHERE firstname = (?) ", (my_data,))
    items = c.fetchall()
    for row_number, row_data in enumerate(items):
        ui.tableWidget.removeRow(0)
        ui.tableWidget.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            ui.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    all_rows = c.fetchall()



# def delete_function():
    # db = sqlite3.connect("employee_health.db")
    # cursor = db.cursor()
    # d = self.id.text()
    
    # command = "DELETE FROM employee_health WHERE rowid =(?)", id)
    # cursor.execute(command, d)
    # db.commit()
    # if rowCount() > 0:
    #     removeRow(rowCount() -1)
    # QTableWidget.selectedItems()
    
def on_selection():
    conn = sqlite3.connect("employee_health.db")
    c = conn.cursor()
    c.execute (''' SELECT * FROM employee1 WHERE ''', (full_name,))
    items = c.fetchall()
    

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)


    # Call functions 
    # create table
    conn = sqlite3.connect('employee_health.db')
    c = conn.cursor()
    # c.execute(""" CREATE TABLE employee1 (
    #     full_name text,
    #     firstname text,
    #     lastname text,
    #     department text, 
    #     start_date text,
    #     annual_complete text,
    #     fit_testing text, 
    #     ppe_audit text )
        
    #     """)
    conn.commit()
 

    # c.execute("INSERT INTO employee VALUES ('TIM Wake', 'Primary Care', '2.1.2021', '2.1.2021', 'yes', 'no' )")
    conn.commit()
    # Functions pressed
    ui.load_btn.clicked.connect(test_table)
    ui.Save_btn.clicked.connect(save_user_input)
    ui.Fit_testing_checkbox.clicked.connect(show_fit_testing)
    ui.PPE_Audit_checkbox.clicked.connect(show_ppe_audit)
    ui.Search_btn.clicked.connect(Search_field)
    

    # tableWidget.selectedItems().connect(on_selection)
    
    # ui.delete_btn.clicked.connect(delete_function)
    # hide
    ui.Fit_testing_date.hide()
    ui.PPE_audit_date.hide()
    ui.label_2.hide()
    ui.label_8.hide()
    # Header resize
    header = ui.tableWidget.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeToContents)

    conn.close()
    MainWindow.show()
    sys.exit(app.exec_())
# from PyQt5.QtWidgets import QMainWindow
# from PyQt5.QtWidgets import QApplication
# from PyQt5 import QtCore
# import sys
# from os import path
# from PyQt5.uic import loadUiType
# import pandas as pd
# from PyQt5.QtWidgets import QTableView
# from PyQt5.QtCore import QAbstractTableModel, Qt, QDate
# from PyQt5 import QtSql
# from PyQt5.QtGui import *
# from PyQt5 import QtWidgets