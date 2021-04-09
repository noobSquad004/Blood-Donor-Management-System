from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox
from PyQt5 import uic
import sys
import mysql.connector
from copy import deepcopy
from datetime import date

#global variables
key = -1
pid = -1
group = ''
area = ''


def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

class ui(QMainWindow):
    def __init__(self):
        self.con = mysql.connector.connect(
            host =  'localhost',
            user = 'root',
            passwd = '',
            database = 'blood'
        )

        super(ui, self).__init__()
        uic.loadUi('home.ui', self)
        self.reg_home.clicked.connect(self.register)
        self.manage.clicked.connect(self.managee)
        self.search.clicked.connect(self.search_)
        self.record.clicked.connect(self.records)
        self.show()

    def search_(self):
        global area, group
        group = str(self.group.currentText())
        area = str(self.area.text())

        if area == '':
            msg = QMessageBox()
            msg.setWindowTitle('Error!')
            msg.setText('You must have to select an area! Try Again.')
            msg.setIcon(QMessageBox.Critical)
            msg.setDetailedText('You might input a wrong Database name.\nMake sure you entered a valid DB name.')

            msg.exec_()

        else:
            self.close()
            self.run = searchh()

    def register(self):
        self.close()
        self.run = reg()

    def managee(self):
        self.close()
        self.run = mng()

    def records(self):
        self.close()
        self.run = record_()

class record_(QMainWindow):
    def __init__(self):
        self.con = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='blood'
        )

        super(record_, self).__init__()
        uic.loadUi('record.ui', self)
        self.loaddata()
        self.setTable()
        self.home.clicked.connect(self.homee)

        self.show()

    def setTable(self):
        self.table.setColumnWidth(0, 140)
        self.table.setColumnWidth(1, 50)
        self.table.setColumnWidth(2, 90)
        self.table.setColumnWidth(3, 120)
        self.table.setColumnWidth(4, 100)
        self.table.setColumnWidth(5, 97)
        self.table.setColumnWidth(6, 140)
        self.table.setColumnWidth(7, 97)
        self.table.setColumnWidth(8, 50)

    def loaddata(self):
        try:
            cursor = self.con.cursor()
            cursor.execute(f"SELECT * FROM requester join donor JOIN record HAVING record.rid = requester.rid AND record.did = donor.did")

            numberOfRow = 0

            for row in cursor:
                numberOfRow += 1

            rowNum = 0

            cursor.execute(f"SELECT * FROM requester join donor JOIN record HAVING record.rid = requester.rid AND record.did = donor.did")

            self.table.setRowCount(numberOfRow)
            for row in cursor:
                self.table.setItem(rowNum, 0, QTableWidgetItem(str(row[1])))
                self.table.setItem(rowNum, 1, QTableWidgetItem(str(row[2])))
                self.table.setItem(rowNum, 2, QTableWidgetItem(str(row[5])))
                self.table.setItem(rowNum, 3, QTableWidgetItem(str(row[6])))

                self.table.setItem(rowNum, 4, QTableWidgetItem(str(row[4])))
                self.table.setItem(rowNum, 5, QTableWidgetItem(str(row[3])))

                self.table.setItem(rowNum, 6, QTableWidgetItem(str(row[8])))
                self.table.setItem(rowNum, 7, QTableWidgetItem(str(row[12])))
                age = calculateAge(row[11])
                self.table.setItem(rowNum, 8, QTableWidgetItem(str(age)))
                rowNum += 1

        except:
            msg = QMessageBox()
            msg.setWindowTitle('Error!')
            msg.setText('An Unexpected Error Occurred! Try Again.')
            msg.setIcon(QMessageBox.Critical)
            msg.setDetailedText('You might input a wrong Database name.\nMake sure you entered a valid DB name.')

            msg.exec_()

    def homee(self):
        self.close()
        self.run = ui()

class searchh(QMainWindow):
    def __init__(self):
        self.con = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='blood'
        )

        super(searchh, self).__init__()
        uic.loadUi('search.ui', self)
        self.loaddata()
        self.setTable()
        self.home.clicked.connect(self.homee)
        self.confirm.clicked.connect(self.confirmed)
        self.show()

    def setTable(self):
        self.table.setColumnWidth(0, 180)
        self.table.setColumnWidth(1, 70)
        self.table.setColumnWidth(2, 80)
        self.table.setColumnWidth(3, 150)
        self.table.setColumnWidth(4, 50)
        self.table.setColumnWidth(5, 110)
        self.table.setColumnWidth(6, 70)
        self.table.setColumnWidth(7, 50)
        self.table.setColumnWidth(8, 124)

    def loaddata(self):
        try:
            global group, area
            area1 = '%'+ area + '%'
            cursor = self.con.cursor()
            cursor.execute(f"select * from donor where bg = '{group}' and area like '{area1}'")

            numberOfRow = 0

            for row in cursor:
                numberOfRow += 1

            rowNum = 0

            cursor.execute(f"select * from donor where bg = '{group}' and area like '{area1}'")

            self.table.setRowCount(numberOfRow)
            for row in cursor:
                self.table.setItem(rowNum, 0, QTableWidgetItem(str(row[1])))
                self.table.setItem(rowNum, 1, QTableWidgetItem(str(row[2])))
                self.table.setItem(rowNum, 2, QTableWidgetItem(str(row[3])))
                self.table.setItem(rowNum, 3, QTableWidgetItem(str(row[9])))
                age = calculateAge(row[4])
                self.table.setItem(rowNum, 4, QTableWidgetItem(str(age)))
                if str(row[8]) == '1900-01-01':
                    self.table.setItem(rowNum, 5, QTableWidgetItem('Never'))
                else:
                    self.table.setItem(rowNum, 5, QTableWidgetItem(str(row[8])))

                self.table.setItem(rowNum, 6, QTableWidgetItem(str(row[6])))
                self.table.setItem(rowNum, 7, QTableWidgetItem(str(row[7])))
                self.table.setItem(rowNum, 8, QTableWidgetItem(str(row[5])))
                rowNum += 1

        except:
            msg = QMessageBox()
            msg.setWindowTitle('Error!')
            msg.setText('An Unexpected Error Occurred! Try Again.')
            msg.setIcon(QMessageBox.Critical)
            msg.setDetailedText('You might input a wrong Database name.\nMake sure you entered a valid DB name.')

            msg.exec_()

    def confirmed(self):
        global key,group, area
        area1 = '%' + area + '%'
        index = self.table.selectionModel().selectedRows()

        if len(index) == 1:
            for indexs in sorted(index):
                x = indexs.row()
            cursor = self.con.cursor()
            cursor.execute(f"select * from donor where bg = '{group}' and area like '{area1}'")
            i = 0
            for row in cursor:
                if i == x:
                    selected = deepcopy(row)
                i += 1
            key = selected[0]
        if key == -1:
            msg = QMessageBox()
            msg.setWindowTitle('Error!')
            msg.setText('Select a donor and try Again...')
            msg.setIcon(QMessageBox.Critical)
            msg.setDetailedText('You might input a wrong input.\nor, make sure you entered a unique Student ID.\nor, make sure you checked courses correctly.')

            msg.exec_()
        else:
            self.close()
            self.run = recipient()

    def homee(self):
        global group, area,key
        key=-1
        area,group = '',''
        self.close()
        self.run = ui()

class recipient(QMainWindow):
    def __init__(self):
        self.con = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='blood'
        )

        super(recipient, self).__init__()
        uic.loadUi('recipient.ui', self)
        self.cancel.clicked.connect(self.homee)
        self.subnit.clicked.connect(self.register)

        self.show()

    def register(self):
        global group, area, key , pid

        name = str(self.name.text())
        phone = str(self.phone.text())
        ddate = self.ddate.date().toPyDate()
        hospital = str(self.hospital.text())


        if name != '' and phone!= '' and hospital!= '':
            cursor = self.con.cursor()
            cursor.execute(f"insert into requester (pname, pbg, phone, needed_blood_date, area, hospital) values ('{name}','{group}','{phone}','{ddate}','{area}','{hospital}')")
            self.con.commit()

            cursor.execute('select * from requester')

            for row in cursor:
                if str(row[1]) == name and str(row[3]) == phone:
                    selected = deepcopy(row)
            pid = int(selected[0])

            cursor.execute(f"insert into record (rid, did) values ({pid},{key})")
            self.con.commit()

            msg = QMessageBox()
            msg.setWindowTitle('Successfully added!')
            msg.setText('You registered successfully...')

            msg.exec_()

            self.homee()

        else:
            msg = QMessageBox()
            msg.setWindowTitle('Error!')
            msg.setText('An Unexpected Error Occurred! Try Again.')
            msg.setIcon(QMessageBox.Critical)
            msg.setDetailedText('You might input a wrong input.\nor, make sure you entered a unique Student ID.\nor, make sure you checked courses correctly.')

            msg.exec_()

    def homee(self):
        global group, area, key, pid
        key = -1
        pid = -1
        area, group = '',''
        self.close()
        self.run = ui()

class reg(QMainWindow):
    def __init__(self):
        self.con = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='blood'
        )

        super(reg, self).__init__()
        uic.loadUi('reg.ui', self)
        self.cancel.clicked.connect(self.homee)
        self.subnit.clicked.connect(self.register)

        self.show()

    def register(self):
        name = str(self.name.text())
        gender = str(self.gender.currentText())
        group = str(self.group.currentText())
        dob = self.bdate.date().toPyDate()
        phone = str(self.phone.text())
        disease = str(self.disease.currentText())
        hac = str(self.hac.currentText())
        ddate = self.ddate.date().toPyDate()
        area = str(self.area.text())

        if self.never.isChecked():
            ddate = date(1900,1,1)


        if name != '' and phone!= '' and area!= '':
            cursor = self.con.cursor()
            cursor.execute(f"insert into donor (name, gender, bg, dob, phone, disease, vac, ldd, area) values ('{name}','{gender}','{group}','{dob}','{phone}','{disease}','{hac}','{ddate}','{area}')")
            self.con.commit()

            msg = QMessageBox()
            msg.setWindowTitle('Successfully added!')
            msg.setText('You registered successfully...')

            msg.exec_()

            self.homee()

        else:
            msg = QMessageBox()
            msg.setWindowTitle('Error!')
            msg.setText('An Unexpected Error Occurred! Try Again.')
            msg.setIcon(QMessageBox.Critical)
            msg.setDetailedText(
                'You might input a wrong input.\nor, make sure you entered a unique Student ID.\nor, make sure you checked courses correctly.')

            msg.exec_()

    def homee(self):
        self.close()
        self.run = ui()


class mng(QMainWindow):
    def __init__(self):
        self.con = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='blood'
        )

        super(mng, self).__init__()
        uic.loadUi('manage.ui', self)
        self.setTable()
        self.load_data()

        self.home.clicked.connect(self.homee)
        self.delete_2.clicked.connect(self.deletee)
        self.update.clicked.connect(self.updatee)
        self.search.clicked.connect(self.search_)
        self.refresh.clicked.connect(self.fresh)

        self.show()

    def search_(self):
        name = str(self.name.text())
        area = str(self.area.text())
        group = str(self.group.currentText())

        name = '%'+name +'%'
        area = '%'+area+'%'

        sql = f"select * from donor where name like '{name}' and area like '{area}'"
        if group != 'All':
            sql += f"and bg = '{group}'"

        cursor = self.con.cursor()
        cursor.execute(sql)

        numberOfRow = 0

        for row in cursor:
            numberOfRow += 1

        rowNum = 0

        cursor.execute(sql)

        self.table.setRowCount(numberOfRow)
        for row in cursor:
            self.table.setItem(rowNum, 0, QTableWidgetItem(str(row[1])))
            self.table.setItem(rowNum, 1, QTableWidgetItem(str(row[2])))
            self.table.setItem(rowNum, 2, QTableWidgetItem(str(row[3])))
            self.table.setItem(rowNum, 3, QTableWidgetItem(str(row[9])))
            age = calculateAge(row[4])
            self.table.setItem(rowNum, 4, QTableWidgetItem(str(age)))
            if str(row[8]) == '1900-01-01':
                self.table.setItem(rowNum, 5, QTableWidgetItem('Never'))
            else:
                self.table.setItem(rowNum, 5, QTableWidgetItem(str(row[8])))

            self.table.setItem(rowNum, 6, QTableWidgetItem(str(row[6])))
            self.table.setItem(rowNum, 7, QTableWidgetItem(str(row[7])))
            self.table.setItem(rowNum, 8, QTableWidgetItem(str(row[5])))
            rowNum += 1

    def setTable(self):
        self.table.setColumnWidth(0, 180)
        self.table.setColumnWidth(1, 70)
        self.table.setColumnWidth(2, 80)
        self.table.setColumnWidth(3, 150)
        self.table.setColumnWidth(4, 50)
        self.table.setColumnWidth(5, 110)
        self.table.setColumnWidth(6, 70)
        self.table.setColumnWidth(7, 50)
        self.table.setColumnWidth(8, 124)
    def load_data(self):
        try:
            cursor = self.con.cursor()
            cursor.execute('select * from donor')

            numberOfRow = 0

            for row in cursor:
                numberOfRow += 1

            rowNum = 0

            cursor.execute('select * from donor')

            self.table.setRowCount(numberOfRow)
            for row in cursor:
                self.table.setItem(rowNum, 0, QTableWidgetItem(str(row[1])))
                self.table.setItem(rowNum, 1, QTableWidgetItem(str(row[2])))
                self.table.setItem(rowNum, 2, QTableWidgetItem(str(row[3])))
                self.table.setItem(rowNum, 3, QTableWidgetItem(str(row[9])))
                age = calculateAge(row[4])
                self.table.setItem(rowNum, 4, QTableWidgetItem(str(age)))
                if str(row[8]) == '1900-01-01':
                    self.table.setItem(rowNum, 5, QTableWidgetItem('Never'))
                else: self.table.setItem(rowNum, 5, QTableWidgetItem(str(row[8])))

                self.table.setItem(rowNum, 6, QTableWidgetItem(str(row[6])))
                self.table.setItem(rowNum, 7, QTableWidgetItem(str(row[7])))
                self.table.setItem(rowNum, 8, QTableWidgetItem(str(row[5])))
                rowNum += 1

        except:
            msg = QMessageBox()
            msg.setWindowTitle('Error!')
            msg.setText('An Unexpected Error Occurred! Try Again.')
            msg.setIcon(QMessageBox.Critical)
            msg.setDetailedText('You might input a wrong Database name.\nMake sure you entered a valid DB name.')

            msg.exec_()


    def deletee(self):
        global key
        index = self.table.selectionModel().selectedRows()
        global key

        if len(index) == 1:
            for indexs in sorted(index):
                x = indexs.row()
            cursor = self.con.cursor()
            cursor.execute('select * from donor')
            i = 0
            for row in cursor:
                if i == x:
                    selected = deepcopy(row)
                i += 1

            key = selected[0]

        if key != -1:
            cursor = self.con.cursor()
            cursor.execute(f"delete from record where did = {int(key)};")
            self.con.commit()

            cursor = self.con.cursor()
            cursor.execute(f"delete from donor where did = {int(key)};")
            self.con.commit()

            key = -1

            self.close()
            self.run = mng()

        else:
            msg = QMessageBox()
            msg.setWindowTitle('Error!')
            msg.setText('An Unexpected Error Occurred! Try Again.')
            msg.setIcon(QMessageBox.Critical)

            msg.exec_()

    def fresh(self):
        self.load_data()
        self.name.setText('')
        self.area.setText('')
        self.group.setCurrentIndex(0)

    def homee(self):
        self.close()
        self.run = ui()

    def updatee(self):
        global key
        index = self.table.selectionModel().selectedRows()

        if len(index) == 1:
            for indexs in sorted(index):
                x = indexs.row()
            cursor = self.con.cursor()
            cursor.execute('select * from donor')
            i = 0
            for row in cursor:
                if i == x:
                    selected = deepcopy(row)
                i += 1
            key = selected[0]
        if key==-1:
            msg = QMessageBox()
            msg.setWindowTitle('Error!')
            msg.setText('Select a donor and try Again...')
            msg.setIcon(QMessageBox.Critical)
            msg.setDetailedText('You might input a wrong input.\nor, make sure you entered a unique Student ID.\nor, make sure you checked courses correctly.')

            msg.exec_()
        else:
            self.close()
            self.run = update_()
class update_(QMainWindow):
    def __init__(self):
        self.con = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='blood'
        )

        super(update_, self).__init__()
        uic.loadUi('update.ui', self)

        self.load()
        self.cancel.clicked.connect(self.homee)
        self.subnit.clicked.connect(self.updatee)

        self.show()
    def load(self):
        global key
        cursor = self.con.cursor()
        cursor.execute(f'select * from donor where did = {key}')
        for row in cursor:
            selected = deepcopy(row)
        self.name.setText(selected[1])
        if selected[2]=='Male':
            self.gender.setCurrentIndex(0)
        elif selected[2]=='Female':
            self.gender.setCurrentIndex(1)
        else: self.gender.setCurrentIndex(2)

        if selected[3]=='A+':
            self.group.setCurrentIndex(0)
        elif selected[3] == 'A-':
            self.group.setCurrentIndex(1)
        elif selected[3] == 'AB+':
            self.group.setCurrentIndex(2)
        elif selected[3] == 'AB-':
            self.group.setCurrentIndex(3)
        elif selected[3] == 'B+':
            self.group.setCurrentIndex(4)
        elif selected[3] == 'B-':
            self.group.setCurrentIndex(5)
        elif selected[3] == 'O+':
            self.group.setCurrentIndex(6)
        elif selected[3] == 'O-':
            self.group.setCurrentIndex(7)

        self.bdate.setDate(selected[4])
        self.phone.setText(selected[5])

        if selected[6] == 'No':
            self.disease.setCurrentIndex(0)
        elif selected[6] == 'Yes':
            self.disease.setCurrentIndex(1)

        if selected[7] == 'No':
            self.hac.setCurrentIndex(0)
        elif selected[7] == 'Yes':
            self.hac.setCurrentIndex(1)

        self.ddate.setDate(selected[8])

        if str(selected[8]) == '1900-01-01':
            self.never.setChecked(True)
        else: self.never.setChecked(False)
        self.area.setText(selected[9])

    def updatee(self):
        name = str(self.name.text())
        gender = str(self.gender.currentText())
        group = str(self.group.currentText())
        dob = self.bdate.date().toPyDate()
        phone = str(self.phone.text())
        disease = str(self.disease.currentText())
        hac = str(self.hac.currentText())
        ddate = self.ddate.date().toPyDate()
        area = str(self.area.text())

        if self.never.isChecked():
            ddate = date(1900,1,1)


        if name != '' and phone!= '' and area!= '':
            cursor = self.con.cursor()
            cursor.execute(f"update donor set name = '{name}', gender = '{gender}', bg = '{group}', dob = '{dob}', phone = '{phone}', disease = '{disease}', vac = '{hac}', ldd = '{ddate}', area = '{area}' where did = {key}")
            self.con.commit()

            msg = QMessageBox()
            msg.setWindowTitle('Successfully Updated!')
            msg.setText('Profile updated successfully...')

            msg.exec_()

            self.homee()

        else:
            msg = QMessageBox()
            msg.setWindowTitle('Error!')
            msg.setText('An Unexpected Error Occurred! Try Again.')
            msg.setIcon(QMessageBox.Critical)
            msg.setDetailedText('You might input a wrong input.\nor, make sure you entered a unique Student ID.\nor, make sure you checked courses correctly.')

            msg.exec_()

    def homee(self):
        global key
        key = -1
        self.close()
        self.run = mng()


app = QApplication(sys.argv)
win = ui()
app.exec_()