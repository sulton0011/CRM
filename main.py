from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QTableWidgetItem,
    QLabel, QApplication, QTreeWidget, QDialog, QPlainTextEdit, QTableWidget
)
import sys
from PyQt5 import QtCore, QtWidgets
from DB import Center, Students, Teams, Tichers, Directions, Teams
# from Students import Ticher

##########################################################################################################################################
# Asosiy oyna bu erda marcaz haqida malumotlar mavjut
class Main(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.window1 = Student()
        self.window1.hide()
        self.window2 = Ticher()
        self.window2.hide()
        self.window3 = Direction()
        self.window3.hide()
        self.window4 = Team()
        self.window4.hide()
        self.list = QTreeWidget()
        self.Sum = QLabel('Centre', self)
        self.Sum.setText('0')
        self.Sum.setAlignment(QtCore.Qt.AlignCenter)
        self.Add_money = QPushButton('Add money')
        self.Get_money = QPushButton('Get money')
        self.students = QPushButton('Students')
        self.tichers = QPushButton('Tichers')
        self.direction = QPushButton('Direction')
        self.team = QPushButton('Team')
        self.V_box = QVBoxLayout()
        self.H_box = QHBoxLayout()
        self.H_box2 = QHBoxLayout()
        self.H_box3 = QHBoxLayout()

        self.retranslateUi()

        self.setLayout(self.V_box)
        self.show()

        self.Add_money.clicked.connect(self.ADD_money)
        self.Get_money.clicked.connect(self.GET_money)
        self.students.clicked.connect(
            lambda checked: self.Stu(self.window1)
            )
        self.tichers.clicked.connect(
            lambda checked: self.Stu(self.window2)
            )
        self.direction.clicked.connect(
            lambda checked: self.Stu(self.window3)
            )
        self.team.clicked.connect(
            lambda checked: self.Stu(self.window4)
            )

    # Kinopka jadval va boshqa narsalarni enkarga joylash
    def retranslateUi(self):
        self.V_box.addWidget(self.list)
        self.H_box.addWidget(self.Get_money)
        self.H_box.addWidget(self.Sum)
        self.H_box.addWidget(self.Add_money)
        self.V_box.addLayout(self.H_box)
        self.H_box2.addWidget(self.students)
        self.H_box2.addWidget(self.tichers)
        self.V_box.addLayout(self.H_box2)
        self.H_box3.addWidget(self.team)
        self.H_box3.addWidget(self.direction)
        self.V_box.addLayout(self.H_box3)
        self.list.headerItem().setText(0, "Date")
        self.list.headerItem().setText(1, "Money")
        self.list.headerItem().setText(2, "Comments")
        self.List()

    # Ekrandegi markaz malumotlarini jadvalga yolash
    def List(self):
        Tree = Center().tableWidget_date_moniy_commint()

        self.list.clear()
        for i in range(len(Tree)):
            QtWidgets.QTreeWidgetItem(self.list)
        
        count = 0
        for item in Tree:
            self.list.topLevelItem(count).setText(0, f"{item[0]}")
            self.list.topLevelItem(count).setText(1, f"{item[1]}")
            self.list.topLevelItem(count).setText(2, f"{item[2]}")
            count += 1
        
        self.Sum.setText(f"{Center().tableWidget_lineEdit()}")

    #########################################################################################################################################
    # student classni ishga tushiradi
    def Stu(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()
            self.hide()

    #########################################################################################################################################

    # O'quv markazga pul qoshish uchun yangi oyna
    def ADD_money(self):
        self.close()
        self.add_money = QDialog()
        self.money = QLineEdit()
        self.money.setPlaceholderText('Enter money')
        self.comment = QPlainTextEdit()
        self.comment.setPlaceholderText("Enter comment")
        self.btn_back = QPushButton("Break")
        self.btn_ok = QPushButton('Ok')
        self.h_box = QHBoxLayout()
        self.v_box = QVBoxLayout()
        
        self.v_box.addWidget(self.money)
        self.v_box.addWidget(self.comment)
        self.h_box.addWidget(self.btn_back)
        self.h_box.addWidget(self.btn_ok)
        self.v_box.addLayout(self.h_box)

        self.add_money.setLayout(self.v_box)
        self.add_money.show()

        self.btn_back.clicked.connect(self.open)
        self.btn_ok.clicked.connect(self.Add_ok)
 
    # Asosi oynani ishga tushirish uchun 
    def open(self):
        self.add_money.close()
        self.List()
        self.show()
 
    # Asosi oynani ishga tushurushtan oldin pulni otqizish uchun
    def Add_ok(self):
        try:
            money = int(self.money.text())
            comment = self.comment.toPlainText()


            if comment != "":
                Center().Add_moniy(money, comment)
            else:
                Center().Add_moniy(money, '-')
            

            self.add_money.close()
            self.List()
            self.show()
        except:
            self.money.clear()
            self.money.setPlaceholderText("Just enter the amount of money!")

    ##########################################################################################################################################  
    # O'quv markazga pul olish uchun yangi oyna
    def GET_money(self):
        self.close()
        self.Get_money = QDialog()
        self.money = QLineEdit()
        self.money.setPlaceholderText('Enter money')
        self.comment = QPlainTextEdit()
        self.comment.setPlaceholderText("Enter comment")
        self.btn_back = QPushButton("Break")
        self.btn_ok = QPushButton('Ok')
        self.h_box = QHBoxLayout()
        self.v_box = QVBoxLayout()
        
        self.v_box.addWidget(self.money)
        self.v_box.addWidget(self.comment)
        self.h_box.addWidget(self.btn_back)
        self.h_box.addWidget(self.btn_ok)
        self.v_box.addLayout(self.h_box)

        self.Get_money.setLayout(self.v_box)
        self.Get_money.show()

        self.btn_back.clicked.connect(self.exec)
        self.btn_ok.clicked.connect(self.GET_Ok)

    # Asosi oynani ishga tushurushtan oldin pulni ayiradi uchun
    def GET_Ok(self):
        try:
            money = int(self.money.text())
            comment = self.comment.toPlainText()

            if comment != "":
                Center().Reduce_moniy(money, comment)
            else:
                Center().Reduce_moniy(money, '-')

            self.Get_money.close()
            self.List()
            self.show()
        except:
            self.money.clear()
            self.money.setPlaceholderText("Just enter the amount of money!")

    # Asosi oynani ishga tushirish uchun 
    def exec(self):
        self.Get_money.close()
        self.List()
        self.show()
 
##########################################################################################################################################

class Student(QWidget):
 
    def __init__(self) -> None:
        super().__init__()
        self.list = QTreeWidget()
        self.Sum = QLabel('Centre', self)
        self.Sum.setText('0')
        self.Sum.setAlignment(QtCore.Qt.AlignCenter)
        self.Add_money = QPushButton('Add money')
        self.sorch_name = QLineEdit()
        self.delete_students = QPushButton('Delete students')
        self.history = QPushButton('History')
        self.add_student = QPushButton('Add student')
        self.breack = QPushButton('Break')
        self.V_box = QVBoxLayout()
        self.H_box = QHBoxLayout()
        self.H_box2 = QHBoxLayout()
        self.H_box3 = QHBoxLayout()

        self.retranslateUi1()

        self.setLayout(self.V_box)
        self.show()

        self.breack.clicked.connect(self.Btn_break)
        self.Add_money.clicked.connect(self.Add_Money)
        self.delete_students.clicked.connect(self.delete)
        self.history.clicked.connect(self.Histry)
        self.add_student.clicked.connect(self.Add_Student)

    def Histry(self):
        if Students().Sorch_students(self.sorch_name.text()) != ([]) and self.sorch_name.text() != '':
            self.window1 = Histry(f'{Students().Sorch_students(self.sorch_name.text())[0][1]}')
            self.window1.show()
            self.hide()
        else:
            self.sorch_name.clear()
            self.sorch_name.setPlaceholderText("Please enter the name tagir!")
   
    def Add_Student(self):
        self.window1 = Add_Student()
        self.window1.show()
        self.hide()

    # elementlarni sahifa ustida joylashishi
    def retranslateUi1(self):
        self.V_box.addWidget(self.list)
        self.H_box.addWidget(self.sorch_name)
        self.H_box.addWidget(self.Sum)
        self.H_box.addWidget(self.Add_money)
        self.H_box2.addWidget(self.delete_students)
        self.H_box2.addWidget(self.history)
        self.H_box3.addWidget(self.breack)
        self.H_box3.addWidget(self.add_student)
        self.V_box.addLayout(self.H_box)
        self.V_box.addLayout(self.H_box2)
        self.V_box.addLayout(self.H_box3)
        self.list.headerItem().setText(0, "Name")
        self.list.headerItem().setText(1, "Money")
        self.list.headerItem().setText(2, "Lessons remined")
        self.sorch_name.setPlaceholderText("Enter name")
        self.List()

    # sahifani yopilishi
    def Btn_break(self):
        window1 = Main()
        window1.show()
        self.hide()

    # Ekrandegi markaz malumotlarini jadvalga yolash
    def List(self):
        Tree = Students().tableWidget_id_name_moniy_lesson()

        self.list.clear()
        for i in range(len(Tree)):
            QtWidgets.QTreeWidgetItem(self.list)
        
        count = 0
        for item in Tree:
            self.list.topLevelItem(count).setText(0, f"{item[1]}")
            self.list.topLevelItem(count).setText(1, f"{item[2]}")
            self.list.topLevelItem(count).setText(2, f"{item[3]}")
            count += 1
        
        self.Sum.setText(f"{Students().tableWidget_lineEdit()}")

    ##########################################################################################################################################   
    # O'quv markazga pul qoshish uchun yangi oyna
    def Add_Money(self):
        if Students().Sorch_students(self.sorch_name.text()) != ([]) and self.sorch_name.text() != '':
            self.close()
            self.add_money = QDialog()
            self.money = QLineEdit()
            self.money.setPlaceholderText('Enter money')
            self.comment = QPlainTextEdit()
            self.comment.setPlaceholderText("Enter comment")
            self.btn_back = QPushButton("Break")
            self.btn_ok = QPushButton('Ok')
            self.Qlable = QLabel()
            self.Qlable.setAlignment(QtCore.Qt.AlignCenter)
            self.h_box = QHBoxLayout()
            self.v_box = QVBoxLayout()
            
            self.v_box.addWidget(self.Qlable)
            self.v_box.addWidget(self.money)
            self.v_box.addWidget(self.comment)
            self.h_box.addWidget(self.btn_back)
            self.h_box.addWidget(self.btn_ok)
            self.v_box.addLayout(self.h_box)
            self.Qlable.setText(f'{Students().Sorch_students(self.sorch_name.text())[0][1]}')

            self.add_money.setLayout(self.v_box)
            self.add_money.show()

            self.btn_back.clicked.connect(lambda checked: self.open(self.add_money))
            self.btn_ok.clicked.connect(self.Add_ok)
        else:
            self.sorch_name.clear()
            self.sorch_name.setPlaceholderText("Please enter the name tagir!")
 
    # Asosi oynani ishga tushirish uchun 
    def open(self, widget):
        widget.close()
        self.List()
        self.sorch_name.clear()
        self.show()
 
    # Asosi oynani ishga tushurushtan oldin pulni otqizish uchun
    def Add_ok(self):
        try:
            money = int(self.money.text())

            Students().Add_moniy(Students().Sorch_students(self.sorch_name.text())[0][0], money)

            self.add_money.close()
            self.List()
            self.sorch_name.clear()
            self.show()
        except:
            self.money.clear()
            self.money.setPlaceholderText("Just enter the amount of money!")

    ##########################################################################################################################################   
    # studentni ochirish uchun yangi oyna ochadi
    def delete(self):
        if Students().Sorch_students(self.sorch_name.text()) != ([]) and self.sorch_name.text() != '':
            self.close()
            self.delet = QDialog()
            self.lable = QLabel()
            self.btn_back = QPushButton('Break')
            self.btn_ok = QPushButton('Ok')
            self.v_box = QVBoxLayout()
            self.h_box = QHBoxLayout()
            self.v_box.addWidget(self.lable)
            self.h_box.addWidget(self.btn_back)
            self.h_box.addWidget(self.btn_ok)
            self.v_box.addLayout(self.h_box)
            
            self.lable.setText(f'Do you want to delete {Students().Sorch_students(self.sorch_name.text())[0][1]} completely?')

            self.delet.setLayout(self.v_box)
            self.delet.show()

            self.btn_back.clicked.connect(lambda checked: self.open(self.delet))
            self.btn_ok.clicked.connect(self.del_ok)
        else:
            self.sorch_name.clear()
            self.sorch_name.setPlaceholderText("Please enter the name tagir!")
 
    # studentni ochirish tastiqlangandan keyn ochiradi
    def del_ok(self):
        Students().Delete_students(Students().Sorch_students(self.sorch_name.text())[0][1])
        self.open(self.delet)

    ##########################################################################################################################################

class Histry(QWidget):
    def __init__(self, name) -> None:
        super().__init__()
        self.window1 = Student()
        self.window1.hide()
        self.name = name
        self.TreeWidget = QTreeWidget()
        self.Qlabel = QLabel()
        self.Qlabel.setText('0')
        self.Qlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_break = QPushButton("Break")
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.retranslateUi()

        self.setLayout(self.v_box)
        self.show()

        self.btn_break.clicked.connect(lambda checked: self.Break(self.window1))

    # sahifadegi narsalarni joylashtiradi
    def retranslateUi(self):
        self.h_box.addWidget(self.Qlabel)
        self.h_box.addWidget(self.btn_break)
        self.v_box.addWidget(self.TreeWidget)
        self.v_box.addLayout(self.h_box)
        self.TreeWidget.headerItem().setText(0, "Date")
        self.TreeWidget.headerItem().setText(1, "Money")
        self.list()

    # sahifadegi royhatni toldiradi
    def list(self):
            Tree = Students().Histre(Students().Sorch_students(self.name)[0][0])
            self.TreeWidget.clear()
            for i in range(len(Tree)):
                QtWidgets.QTreeWidgetItem(self.TreeWidget)
            
            count = 0
            for item in Tree:
                self.TreeWidget.topLevelItem(count).setText(0, f"{item[0]}")
                self.TreeWidget.topLevelItem(count).setText(1, f"{item[1]}")
                count += 1
            
            self.Qlabel.setText(f"{Students().tableWidget_sum(self.name)}")       

    # sahifani yopish
    def Break(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()
            self.hide()

     # O'quv markazga pul qoshish uchun yangi oyna

    ##########################################################################################################################################

class Add_Student(QWidget):
    def __init__(self) -> None:
        super().__init__()
        # self.window1 = Student()
        # self.window1.hide()
        self.lable = QLabel()
        self.QlineEdid = QLineEdit()
        self.Combo_Box = QComboBox()
        self.btn_break = QPushButton("Break")
        self.btn_ok = QPushButton('Ok')
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.retranslateUi()

        self.setLayout(self.v_box)
        self.show()

        self.btn_break.clicked.connect(lambda checked: self.Break(Student()))
        self.btn_ok.clicked.connect(self.Add_Student_Ok)


    # sahifadegi narsalarni joylashtiradi
    def retranslateUi(self):
        self.h_box.addWidget(self.btn_break)
        self.h_box.addWidget(self.btn_ok)
        self.v_box.addWidget(self.lable)
        self.v_box.addWidget(self.Combo_Box)
        self.v_box.addWidget(self.QlineEdid)
        self.v_box.addLayout(self.h_box)
        self.QlineEdid.setPlaceholderText('Enter your full name!')
        self.list()

    # sahifadegi royhatni toldiradi
    def list(self):
        self.Combo_Box.clear()
        self.Combo_Box.addItem("")
        self.Combo_Box.setItemText(0, "Team")

        caunt = 1
        for i in Teams().tableWidget_direction_name_ticher_student():
            self.Combo_Box.addItem("")
            self.Combo_Box.setItemText(caunt, f"{i[2]}")
            caunt += 1


    # sahifani yopish
    def Break(self, window):
        self.window1 = Student()
        self.window1.show()
        self.hide()

     # O'quv markazga pul qoshish uchun yangi oyna

    def Add_Student_Ok(self):
        combobox = self.Combo_Box.currentText()
        name = self.QlineEdid.text()

        if name != '' and combobox != 'Team':
            Students().Add_Students(Teams().Sorch_team_name(f'{combobox}')[0][0], name)
            self.window1 = Student()
            self.window1.show()
            self.hide()

        else:
            self.lable.setText('Uni to\'liq va to\'g\'ri kiritganingizga ishonch hosil qiling')

##########################################################################################################################################

class Ticher(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.list = QTreeWidget()
        self.Sum = QLabel('Centre', self)
        self.Sum.setText('0')
        self.Sum.setAlignment(QtCore.Qt.AlignCenter)
        self.Add_money = QPushButton('Get money')
        self.sorch_name = QComboBox()
        self.delete_students = QPushButton('Delete Ticher')
        self.history = QPushButton('History')
        self.add_student = QPushButton('Add Ticher')
        self.breack = QPushButton('Break')
        self.V_box = QVBoxLayout()
        self.H_box = QHBoxLayout()
        self.H_box2 = QHBoxLayout()
        self.H_box3 = QHBoxLayout()

        self.retranslateUi2()

        self.setLayout(self.V_box)
        self.show()

        self.breack.clicked.connect(self.Btn_break_Ticher)
        self.Add_money.clicked.connect(self.Get_Money_Ticher)
        self.delete_students.clicked.connect(self.Ticher_delete)
        self.history.clicked.connect(self.Ticher_Histry)
        self.add_student.clicked.connect(self.Add_Ticher)

    def Ticher_Histry(self):
        if self.sorch_name.currentText() != 'Enter Name' and self.sorch_name.currentText() != "Please enter the name tagir!":
            self.window1 = Ticher_Histry(self.sorch_name.currentText())
            self.window1.show()
            self.hide()
        else:
            self.sorch_name.setItemText(0, "Please enter the name tagir!")
   
    def Add_Ticher(self):
        self.window1 = Add_Ticher()
        self.window1.show()
        self.hide()

    # elementlarni sahifa ustida joylashishi
    def retranslateUi2(self):
        self.V_box.addWidget(self.list)
        self.H_box.addWidget(self.sorch_name)
        self.H_box.addWidget(self.Sum)
        self.H_box.addWidget(self.Add_money)
        self.H_box2.addWidget(self.delete_students)
        self.H_box2.addWidget(self.history)
        self.H_box3.addWidget(self.breack)
        self.H_box3.addWidget(self.add_student)
        self.V_box.addLayout(self.H_box)
        self.V_box.addLayout(self.H_box2)
        self.V_box.addLayout(self.H_box3)
        self.list.headerItem().setText(0, "Name")
        self.list.headerItem().setText(1, "Money")
        self.list.headerItem().setText(2, "Number of Team")
        # self.sorch_name.setPlaceholderText("Enter name")
        self.List1()

    # sahifani yopilishi
    def Btn_break_Ticher(self):
        window1 = Main()
        window1.show()
        self.hide()

    # Ekrandegi markaz malumotlarini jadvalga yolash
    def List1(self):
        Tree = Tichers().tableWidget_id_name_moniy_team()

        self.list.clear()
        for i in range(len(Tree)):
            QtWidgets.QTreeWidgetItem(self.list)
        
        count = 0
        for item in Tree:
            self.list.topLevelItem(count).setText(0, f"{item[1]}")
            self.list.topLevelItem(count).setText(1, f"{item[2]}")
            self.list.topLevelItem(count).setText(2, f"{item[3]}")
            count += 1
        
        self.Sum.setText(f"{Tichers().tableWidget_lineEdit()}")

        self.sorch_name.clear()
        self.sorch_name.addItem("")
        self.sorch_name.setItemText(0, "Enter Name")

        caunt = 1
        for i in Tree:
            self.sorch_name.addItem("")
            self.sorch_name.setItemText(caunt, f"{i[1]}")
            caunt += 1


    ##########################################################################################################################################   
    # O'quv markazga pul qoshish uchun yangi oyna
    def Get_Money_Ticher(self):
        if self.sorch_name.currentText() != 'Enter Name' and self.sorch_name.currentText() != "Please enter the name tagir!":
            self.close()
            self.Get_money = QDialog()
            self.money = QLineEdit()
            self.money.setPlaceholderText('Enter money')
            self.comment = QPlainTextEdit()
            self.comment.setPlaceholderText("Enter comment")
            self.btn_back = QPushButton("Break")
            self.btn_ok = QPushButton('Ok')
            self.h_box = QHBoxLayout()
            self.v_box = QVBoxLayout()
            
            self.v_box.addWidget(self.money)
            self.v_box.addWidget(self.comment)
            self.h_box.addWidget(self.btn_back)
            self.h_box.addWidget(self.btn_ok)
            self.v_box.addLayout(self.h_box)

            self.Get_money.setLayout(self.v_box)
            self.Get_money.show()

            self.btn_back.clicked.connect(lambda checked: self.open(self.Get_money))
            self.btn_ok.clicked.connect(self.Ticher_Get_ok)
        else:
            self.sorch_name.setItemText(0, "Please enter the name tagir!")

    # Asosi oynani ishga tushirish uchun 
    def open(self, widget):
        widget.close()
        self.List1()
        self.show()
 
    # Asosi oynani ishga tushurushtan oldin pulni otqizish uchun
    def Ticher_Get_ok(self):
        try:
            money = int(self.money.text())
            name = self.sorch_name.currentText()
            id = Tichers().Sorch_ticher(name)[0][0]

            Tichers().Get_money(id, money)

            self.Get_money.close()
            self.List1()
            self.show()
        except:
            self.money.clear()
            self.money.setPlaceholderText("Just enter the amount of money!")

    ##########################################################################################################################################   
    # studentni ochirish uchun yangi oyna ochadi
    def Ticher_delete(self):
        if self.sorch_name.currentText() != 'Enter Name' and self.sorch_name.currentText() != "Please enter the name tagir!":
            self.close()
            self.delet = QDialog()
            self.lable = QLabel()
            self.btn_back = QPushButton('Break')
            self.btn_ok = QPushButton('Ok')
            self.v_box = QVBoxLayout()
            self.h_box = QHBoxLayout()
            name = self.sorch_name.currentText()
            self.v_box.addWidget(self.lable)
            self.h_box.addWidget(self.btn_back)
            self.h_box.addWidget(self.btn_ok)
            self.v_box.addLayout(self.h_box)
            
            self.lable.setText(f'Do you want to delete {name} completely?')

            self.delet.setLayout(self.v_box)
            self.delet.show()

            self.btn_back.clicked.connect(lambda checked: self.open(self.delet))
            self.btn_ok.clicked.connect(self.Ticher_del_ok)
        else:
            self.sorch_name.setItemText(0, "Please enter the name tagir!")
 
    # studentni ochirish tastiqlangandan keyn ochiradi
    def Ticher_del_ok(self):
        Tichers().Delete_Ticher(self.sorch_name.currentText())
        self.open(self.delet)

class Ticher_Histry(QWidget):
    def __init__(self, name) -> None:
        super().__init__()
        self.window1 = Ticher()
        self.window1.hide()
        self.name = name
        self.TreeWidget = QTreeWidget()
        self.Qlabel = QLabel()
        self.Qlabel.setText('0')
        self.Qlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_break = QPushButton("Break")
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.retranslateUi()

        self.setLayout(self.v_box)
        self.show()

        self.btn_break.clicked.connect(lambda checked: self.Break(self.window1))


    # sahifadegi narsalarni joylashtiradi
    def retranslateUi(self):
        self.h_box.addWidget(self.Qlabel)
        self.h_box.addWidget(self.btn_break)
        self.v_box.addWidget(self.TreeWidget)
        self.v_box.addLayout(self.h_box)
        self.TreeWidget.headerItem().setText(0, "Date")
        self.TreeWidget.headerItem().setText(1, "Money")
        self.list()

    # sahifadegi royhatni toldiradi
    def list(self):
            id = Tichers().Sorch_ticher(self.name)[0][0]
            Tree = Tichers().Histre(id)
            self.TreeWidget.clear()
            for i in range(len(Tree)):
                QtWidgets.QTreeWidgetItem(self.TreeWidget)
            
            count = 0
            for item in Tree:
                self.TreeWidget.topLevelItem(count).setText(0, f"{item[0]}")
                self.TreeWidget.topLevelItem(count).setText(1, f"{item[1]}")
                count += 1
            
            self.Qlabel.setText(f"{Tichers().tableWidget_line_edit_ticher(self.name)}")       

    # sahifani yopish
    def Break(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()
            self.hide()

     # O'quv markazga pul qoshish uchun yangi oyna

class Add_Ticher(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.lable = QLabel()
        self.QlineEdid = QLineEdit()
        self.QlineEdid2 = QLineEdit()
        self.btn_break = QPushButton("Break")
        self.btn_ok = QPushButton('Ok')
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.retranslateUi()

        self.setLayout(self.v_box)
        self.show()

        self.btn_break.clicked.connect(lambda checked: self.Break(Ticher()))
        self.btn_ok.clicked.connect(self.Add_Ticher_Ok)


    # sahifadegi narsalarni joylashtiradi
    def retranslateUi(self):
        self.h_box.addWidget(self.btn_break)
        self.h_box.addWidget(self.btn_ok)
        self.v_box.addWidget(self.lable)
        self.v_box.addWidget(self.QlineEdid2)
        self.v_box.addWidget(self.QlineEdid)
        self.v_box.addLayout(self.h_box)
        self.QlineEdid.setPlaceholderText('Enter your full name!')
        self.QlineEdid2.setPlaceholderText('Enter Agreement!')

    # sahifani yopish
    def Break(self, window):
        self.window1 = Ticher()
        self.window1.show()
        self.hide()

     # O'quv markazga pul qoshish uchun yangi oyna

    def Add_Ticher_Ok(self):
        try:
            Agreement = int(self.QlineEdid2.text())
            name = self.QlineEdid.text()

            if name != '' and Agreement < 100:

                Tichers().Add_Tichers(name, Agreement)
           
                self.window1 = Ticher()
                self.window1.show()
                self.hide()

            else:
                self.QlineEdid.clear()
                self.QlineEdid2.clear()
                self.lable.setText('Uni to\'liq va to\'g\'ri kiritganingizga ishonch hosil qiling')
        except:
            self.QlineEdid.clear()
            self.QlineEdid2.clear()
            self.lable.setText('Uni to\'liq va to\'g\'ri kiritganingizga ishonch hosil qiling')

##########################################################################################################################################

class Direction(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.list = QTreeWidget()
        self.Sum = QLabel('Centre', self)
        self.Sum.setText('0')
        self.Sum.setAlignment(QtCore.Qt.AlignCenter)
        self.sorch_name = QComboBox()
        self.delete_students = QPushButton('Delete direction')
        self.history = QPushButton('Change direction')
        self.add_student = QPushButton('Add direction')
        self.breack = QPushButton('Break')
        self.V_box = QVBoxLayout()
        self.H_box = QHBoxLayout()
        self.H_box2 = QHBoxLayout()
        self.H_box3 = QHBoxLayout()

        self.retranslateUi2()

        self.setLayout(self.V_box)
        self.show()

        self.breack.clicked.connect(self.Btn_break_Direction)
        self.delete_students.clicked.connect(self.Ticher_delete)
        self.history.clicked.connect(self.Change_Direction)
        self.add_student.clicked.connect(self.Add_Direction)

    # Directionni dars soni va narxini ozgartirish uchun yangi class ni ishga tushuradi
    def Change_Direction(self):
        if self.sorch_name.currentText() != 'Enter direction' and self.sorch_name.currentText() != "Please enter the name tagir!":
            self.window1 = Change_Direction(self.sorch_name.currentText())
            self.window1.show()
            self.hide()
        else:
            self.sorch_name.setItemText(0, "Please enter the name tagir!")

    # Yangi Directin qoshish uchun yangi class ni ishga tushiradi 
    def Add_Direction(self):
        self.window1 = Add_Direction()
        self.window1.show()
        self.hide()

    # elementlarni sahifa ustida joylashishi
    def retranslateUi2(self):
        self.V_box.addWidget(self.list)
        self.H_box.addWidget(self.sorch_name)
        self.H_box.addWidget(self.Sum)
        self.H_box2.addWidget(self.delete_students)
        self.H_box2.addWidget(self.history)
        self.H_box3.addWidget(self.breack)
        self.H_box3.addWidget(self.add_student)
        self.V_box.addLayout(self.H_box)
        self.V_box.addLayout(self.H_box2)
        self.V_box.addLayout(self.H_box3)
        self.list.headerItem().setText(0, "Name")
        self.list.headerItem().setText(1, "Lesson money")
        self.list.headerItem().setText(2, "Lesson size")
        self.List2()

    # sahifani yopilishi
    def Btn_break_Direction(self):
        window1 = Main()
        window1.show()
        self.hide()

    # Ekrandegi markaz malumotlarini jadvalga yolash
    def List2(self):
        Tree = Directions().tableWidget_name_mony_lesson()

        self.list.clear()
        for i in range(len(Tree)):
            QtWidgets.QTreeWidgetItem(self.list)
        
        count = 0
        for item in Tree:
            self.list.topLevelItem(count).setText(0, f"{item[1]}")
            self.list.topLevelItem(count).setText(1, f"{item[2]}")
            self.list.topLevelItem(count).setText(2, f"{item[3]}")
            count += 1
        
        self.Sum.setText(f"{Directions().tableWodget_lineEdit()}")

        self.sorch_name.clear()
        self.sorch_name.addItem("")
        self.sorch_name.setItemText(0, "Enter direction")

        caunt = 1
        for i in Tree:
            self.sorch_name.addItem("")
            self.sorch_name.setItemText(caunt, f"{i[1]}")
            caunt += 1


    ##########################################################################################################################################   
    # Asosi oynani ishga tushirish uchun 
    def open(self, widget):
        widget.close()
        self.List2()
        self.show()
 
    # studentni ochirish uchun yangi oyna ochadi
    def Ticher_delete(self):
        if self.sorch_name.currentText() != 'Enter direction' and self.sorch_name.currentText() != "Please enter the name tagir!":
            self.close()
            self.delet = QDialog()
            self.lable = QLabel()
            self.btn_back = QPushButton('Break')
            self.btn_ok = QPushButton('Ok')
            self.v_box = QVBoxLayout()
            self.h_box = QHBoxLayout()
            name = self.sorch_name.currentText()
            self.v_box.addWidget(self.lable)
            self.h_box.addWidget(self.btn_back)
            self.h_box.addWidget(self.btn_ok)
            self.v_box.addLayout(self.h_box)
            
            self.lable.setText(f'Do you want to delete {name} completely?')

            self.delet.setLayout(self.v_box)
            self.delet.show()

            self.btn_back.clicked.connect(lambda checked: self.open(self.delet))
            self.btn_ok.clicked.connect(self.Ticher_del_ok)
        else:
            self.sorch_name.setItemText(0, "Please enter the name tagir!")
 
    # studentni ochirish tastiqlangandan keyn ochiradi
    def Ticher_del_ok(self):
        name = self.sorch_name.currentText()
        Directions().Delete_direction(name)
        self.open(self.delet)

class Change_Direction(QWidget):
    def __init__(self, name) -> None:
        super().__init__()
        self.window1 = Direction()
        self.window1.hide()
        self.name = name
        self.Qlabel = QLabel()
        self.size1 = QLineEdit()
        self.money1 = QLineEdit()
        self.Qlabel.setText('0')
        self.Qlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_break = QPushButton("Break")
        self.btn_ok = QPushButton("Ok")
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.retranslateUi()

        self.setLayout(self.v_box)
        self.show()

        self.btn_break.clicked.connect(lambda checked: self.Break(self.window1))
        self.btn_ok.clicked.connect(self.Btn_ok)

    # sahifadegi narsalarni joylashtiradi
    def retranslateUi(self):
        self.h_box.addWidget(self.btn_break)
        self.h_box.addWidget(self.btn_ok)
        self.v_box.addWidget(self.Qlabel)
        self.v_box.addWidget(self.size1)
        self.v_box.addWidget(self.money1)
        self.v_box.addLayout(self.h_box)
        self.Qlabel.setText(f'{self.name}')
        self.size1.setPlaceholderText("Enter size")
        self.money1.setPlaceholderText("Enter money")

    # sahifadegi royhatni toldiradi
    def Btn_ok(self):
        try:
            money = int(self.money1.text())
            size = int(self.size1.text())
            name = self.name


            Directions().Chenge(name, size, money)
           
            self.window1 = Direction()
            self.window1.show()
            self.hide()

        except:
            self.size1.clear()
            self.money1.clear()
            self.Qlabel.setText(f'{self.name} Make sure you enter it completely and correctly!')
 
    # sahifani yopish
    def Break(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()
            self.hide()

     # O'quv markazga pul qoshish uchun yangi oyna

class Add_Direction(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.lable = QLabel()
        self.QlineEdid = QLineEdit()
        self.QlineEdid2 = QLineEdit()
        self.QlineEdid3 = QLineEdit()
        self.btn_break = QPushButton("Break")
        self.btn_ok = QPushButton('Ok')
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.retranslateUi()

        self.setLayout(self.v_box)
        self.show()

        self.btn_break.clicked.connect(lambda checked: self.Break(Direction()))
        self.btn_ok.clicked.connect(self.Add_Direction_Ok)

    # sahifadegi narsalarni joylashtiradi
    def retranslateUi(self):
        self.h_box.addWidget(self.btn_break)
        self.h_box.addWidget(self.btn_ok)
        self.v_box.addWidget(self.lable)
        self.v_box.addWidget(self.QlineEdid)
        self.v_box.addWidget(self.QlineEdid2)
        self.v_box.addWidget(self.QlineEdid3)
        self.v_box.addLayout(self.h_box)
        self.QlineEdid.setPlaceholderText('Enter your full name!')
        self.QlineEdid2.setPlaceholderText('Enter the number of lessons per month!')
        self.QlineEdid3.setPlaceholderText('Enter the monthly price!')

    # sahifani yopish
    def Break(self, window):
        self.window1 = Direction()
        self.window1.show()
        self.hide()

     # O'quv markazga pul qoshish uchun yangi oyna

    # Direction qoshish tastiqlangandan son qoshadi
    def Add_Direction_Ok(self):
        try:
            money = int(self.QlineEdid3.text())
            size = int(self.QlineEdid2.text())
            name = self.QlineEdid.text()

            if name != '' and self.QlineEdid2.text() != '' and self.QlineEdid3.text() != '':

                Directions().Add_direction(name, size, money)
           
                self.window1 = Direction()
                self.window1.show()
                self.hide()

            else:
                self.QlineEdid.clear()
                self.QlineEdid2.clear()
                self.lable.setText('Make sure you enter it completely and correctly!')
        except:
            self.QlineEdid.clear()
            self.QlineEdid2.clear()
            self.lable.setText('Make sure you enter it completely and correctly!')

##########################################################################################################################################

class Team(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.list = QTreeWidget()
        self.Sum = QPushButton('List of students')
        self.sorch_name = QComboBox()
        self.crm = QPushButton('C.R.M')
        self.delete_students = QPushButton('Delete direction')
        self.history = QPushButton('Add students')
        self.add_student = QPushButton('Add team')
        self.breack = QPushButton('Break')
        self.V_box = QVBoxLayout()
        self.H_box = QHBoxLayout()
        self.H_box2 = QHBoxLayout()
        self.H_box3 = QHBoxLayout()

        self.retranslateUi2()

        self.setLayout(self.V_box)
        self.show()

        self.breack.clicked.connect(self.Btn_break_Team)
        self.delete_students.clicked.connect(self.Team_delete)
        self.Sum.clicked.connect(self.list_of_students)
        self.add_student.clicked.connect(self.Add_Team)
        self.crm.clicked.connect(self.CRM)
        self.history.clicked.connect(self.Add_student_team)

    def list_of_students(self):
        if self.sorch_name.currentText() != 'Enter Team' and self.sorch_name.currentText() != 'Please enter the name tagir!':
            self.window1 = List_of_Students(self.sorch_name.currentText())
            self.window1.show()
            self.hide()
        else:
            self.sorch_name.setItemText(0, "Please enter the name tagir!")
   
    def Add_Team(self):
        self.window1 = Add_Team()
        self.window1.show()
        self.hide()

    def Add_student_team(self):
        self.window1 = Add_Team_students()
        self.window1.show()
        self.hide()

    def CRM(self):
        if self.sorch_name.currentText() != 'Enter Team' and self.sorch_name.currentText() != 'Please enter the name tagir!':
            self.window1 = CRM(self.sorch_name.currentText())
            self.window1.show()
            self.hide()
        else:
            self.sorch_name.setItemText(0, "Please enter the name tagir!")

    # elementlarni sahifa ustida joylashishi
    def retranslateUi2(self):
        self.V_box.addWidget(self.list)
        self.V_box.addWidget(self.crm)
        self.H_box.addWidget(self.sorch_name)
        self.H_box.addWidget(self.Sum)
        self.H_box2.addWidget(self.delete_students)
        self.H_box2.addWidget(self.history)
        self.H_box3.addWidget(self.breack)
        self.H_box3.addWidget(self.add_student)
        self.V_box.addLayout(self.H_box)
        self.V_box.addLayout(self.H_box2)
        self.V_box.addLayout(self.H_box3)
        self.list.headerItem().setText(0, "Route name")
        self.list.headerItem().setText(1, "Name")
        self.list.headerItem().setText(2, "Teacher's name")
        self.list.headerItem().setText(3, "Number of students")
        self.List2()

    # sahifani yopilishi
    def Btn_break_Team(self):
        window1 = Main()
        window1.show()
        self.hide()

    # Ekrandegi markaz malumotlarini jadvalga yolash
    def List2(self):
        Tree = Teams().tableWidget_direction_name_ticher_student()

        self.list.clear()
        for i in range(len(Tree)):
            QtWidgets.QTreeWidgetItem(self.list)
        
        count = 0
        for item in Tree:
            self.list.topLevelItem(count).setText(0, f"{item[2]}")
            self.list.topLevelItem(count).setText(1, f"{item[1]}")
            self.list.topLevelItem(count).setText(2, f"{item[3]}")
            self.list.topLevelItem(count).setText(3, f"{item[4]}")
            count += 1

        self.sorch_name.clear()
        self.sorch_name.addItem("")
        self.sorch_name.setItemText(0, "Enter Team")

        caunt = 1
        for i in Tree:
            self.sorch_name.addItem("")
            self.sorch_name.setItemText(caunt, f"{i[2]}")
            caunt += 1


    ##########################################################################################################################################   
    # Asosi oynani ishga tushirish uchun 
    def open(self, widget):
        widget.close()
        self.List2()
        self.show()
 
    # studentni ochirish uchun yangi oyna ochadi
    def Team_delete(self):
        if self.sorch_name.currentText() != 'Enter Team' and self.sorch_name.currentText() != 'Please enter the name tagir!':
            self.close()
            self.delet = QDialog()
            self.lable = QLabel()
            self.btn_back = QPushButton('Break')
            self.btn_ok = QPushButton('Ok')
            self.v_box = QVBoxLayout()
            self.h_box = QHBoxLayout()
            name = self.sorch_name.currentText()
            self.v_box.addWidget(self.lable)
            self.h_box.addWidget(self.btn_back)

            if Teams().Sorch_team_S_S_name(Teams().Sorch_team_name(name)[0][0]) == []:
                self.lable.setText(f'Do you want to delete {name} completely?')
                self.h_box.addWidget(self.btn_ok)
            else:
                self.lable.setText(f'It is not possible to delete because there are students in group {name}!')
            self.v_box.addLayout(self.h_box)


            self.delet.setLayout(self.v_box)
            self.delet.show()

            self.btn_back.clicked.connect(lambda checked: self.open(self.delet))
            self.btn_ok.clicked.connect(self.Team_del_ok)
        else:
            self.sorch_name.setItemText(0, "Please enter the name tagir!")
 
    # studentni ochirish tastiqlangandan keyn ochiradi
    def Team_del_ok(self):
        id = Teams().Sorch_team_name(self.sorch_name.currentText())[0][0]
        Teams().Delete_team(id)
        self.open(self.delet)

    ##########################################################################################################################################

class List_of_Students(QWidget):
    def __init__(self, name) -> None:
        super().__init__()
        self.window1 = Team()
        self.window1.hide()
        self.name = name
        self.TreeWidget = QTreeWidget()
        self.Qlabel = QLabel()
        self.Qlabel.setText('0')
        self.Qlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_break = QPushButton("Break")
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.retranslateUi()

        self.setLayout(self.v_box)
        self.show()

        self.btn_break.clicked.connect(lambda checked: self.Break(self.window1))


    # sahifadegi narsalarni joylashtiradi
    def retranslateUi(self):
        self.h_box.addWidget(self.btn_break)
        self.h_box.addWidget(self.Qlabel)
        self.v_box.addWidget(self.TreeWidget)
        self.v_box.addLayout(self.h_box)
        self.TreeWidget.headerItem().setText(0, "Students name")
        self.TreeWidget.headerItem().setText(1, "Total money")
        self.list()

    # sahifadegi royhatni toldiradi
    def list(self):
            id = Teams().Sorch_team_name(self.name)[0][0]
            Tree = Teams().List_if_student(id)
            self.TreeWidget.clear()

            for i in range(len(Tree)):
                QtWidgets.QTreeWidgetItem(self.TreeWidget)
            
            count = 0
            for item in Tree:
                self.TreeWidget.topLevelItem(count).setText(0, f"{item[0]}")
                self.TreeWidget.topLevelItem(count).setText(1, f"{item[1]}")
                count += 1
            
            self.Qlabel.setText(f"{len(Tree)}")       

    # sahifani yopish
    def Break(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()
            self.hide()

     # O'quv markazga pul qoshish uchun yangi oyna

class Add_Team(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.lable = QLabel()
        self.lable.setAlignment(QtCore.Qt.AlignCenter)
        self.QlineEdid = QLineEdit()
        self.QCombobox = QComboBox()
        self.QCombobox2 = QComboBox()
        self.btn_break = QPushButton("Break")
        self.btn_ok = QPushButton('Ok')
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.retranslateUi()

        self.setLayout(self.v_box)
        self.show()

        self.btn_break.clicked.connect(lambda checked: self.Break(Team()))
        self.btn_ok.clicked.connect(self.Add_Ticher_Ok)

    # sahifadegi narsalarni joylashtiradi
    def retranslateUi(self):
        self.h_box.addWidget(self.btn_break)
        self.h_box.addWidget(self.btn_ok)
        self.v_box.addWidget(self.lable)
        self.v_box.addWidget(self.QlineEdid)
        self.v_box.addWidget(self.QCombobox)
        self.v_box.addWidget(self.QCombobox2)
        self.v_box.addLayout(self.h_box)
        self.QlineEdid.setPlaceholderText('Enter your full name!')
        self.lable.setText('Add Team')


        Tree = Directions().tableWidget_name_mony_lesson()
        self.QCombobox.clear()
        self.QCombobox.addItem("")
        self.QCombobox.setItemText(0, "Enter Direction")

        caunt = 1
        for i in Tree:
            self.QCombobox.addItem("")
            self.QCombobox.setItemText(caunt, f"{i[1]}")
            caunt += 1


        Tree = Tichers().tableWidget_id_name_moniy_team()
        self.QCombobox2.clear()
        self.QCombobox2.addItem("")
        self.QCombobox2.setItemText(0, "Enter Tichers")

        caunt = 1
        for i in Tree:
            self.QCombobox2.addItem("")
            self.QCombobox2.setItemText(caunt, f"{i[1]}")
            caunt += 1


    # sahifani yopish
    def Break(self, window):
        self.window1 = Team()
        self.window1.show()
        self.hide()

     # O'quv markazga pul qoshish uchun yangi oyna

    def Add_Ticher_Ok(self):
        derection = Directions().Sorch_Direction_name(self.QCombobox.currentText())[0][0]
        ticher = Tichers().Sorch_ticher(self.QCombobox2.currentText())[0][0]
        name = self.QlineEdid.text()

        if name != '' and derection != 'Enter Direction' and ticher != 'Enter Tichers':
            Teams().Add_Team(derection, name, ticher)
            # print(name, derection, ticher)
        
            self.window1 = Team()
            self.window1.show()
            self.hide()
        else:
            self.lable.setText('Make sure you enter it completely and correctly!')

class Add_Team_students(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.lable = QLabel()
        self.lable.setAlignment(QtCore.Qt.AlignCenter)
        self.QlineEdid = QLineEdit()
        self.QCombobox = QComboBox()
        self.QCombobox2 = QComboBox()
        self.btn_break = QPushButton("Break")
        self.btn_ok = QPushButton('Ok')
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.retranslateUi()

        self.setLayout(self.v_box)
        self.show()

        self.btn_break.clicked.connect(lambda checked: self.Break(Team()))
        self.btn_ok.clicked.connect(self.Add_Ticher_Ok)

    # sahifadegi narsalarni joylashtiradi
    def retranslateUi(self):
        self.h_box.addWidget(self.btn_break)
        self.h_box.addWidget(self.btn_ok)
        self.v_box.addWidget(self.lable)
        self.v_box.addWidget(self.QlineEdid)
        self.v_box.addWidget(self.QCombobox)
        self.v_box.addLayout(self.h_box)
        self.QlineEdid.setPlaceholderText('enter the full name of the student!')
        self.lable.setText('Add community students')


        Tree = Teams().tableWidget_direction_name_ticher_student()
        self.QCombobox.clear()
        self.QCombobox.addItem("")
        self.QCombobox.setItemText(0, "Enter Team")

        caunt = 1
        for i in Tree:
            self.QCombobox.addItem("")
            self.QCombobox.setItemText(caunt, f"{i[2]}")
            caunt += 1


    # sahifani yopish
    def Break(self, window):
        self.window1 = Team()
        self.window1.show()
        self.hide()

     # O'quv markazga pul qoshish uchun yangi oyna

    def Add_Ticher_Ok(self):
        team = self.QCombobox.currentText()
        name = self.QlineEdid.text()

        if name != '' and team != 'Enter Team':
            if Students().Sorch_students(name) != []:
                name = Students().Sorch_students(name)[0][1]
                team = Teams().Sorch_team_name(team)

                try:
                    print(Teams().List_if_student(team[0][0])[0][0], Teams().Sorch_team_Students(name)[0][1])
                    if Teams().List_if_student(team[0][0])[0][0] != Teams().Sorch_team_Students(name)[0][1]:
                        Teams().Add_student(team[0][0], name)
            
                        self.window1 = Team()
                        self.window1.show()
                        self.hide()
                    else:
                        self.lable.setText(f'{name} is present in group {team[0][2]}!')
                except:
                    print(team[0][0], name)
                    Teams().Add_student(team[0][0], name)
                
                    self.window1 = Team()
                    self.window1.show()
                    self.hide()

            else:
                self.lable.setText(f'There is no student named {name}!')
        else:
            self.lable.setText('Make sure you enter it completely and correctly!')

class CRM(QWidget):
    def __init__(self, Team_name) -> None:
        super().__init__()
        self.window1 = Team()
        self.window1.hide()
        self.name = Team_name
        self.TableWidget = QTableWidget()
        self.Qlabel = QLabel()
        self.Qlabel.setText('0')
        self.Qlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_break = QPushButton("Break")
        self.btn_Ok = QPushButton("Ok")
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.retranslateUi()

        self.setLayout(self.v_box)
        self.show()

        self.btn_break.clicked.connect(lambda checked: self.Break(self.window1))
        self.btn_Ok.clicked.connect(lambda checked: self.Ok(self.window1))


    # sahifadegi narsalarni joylashtiradi
    def retranslateUi(self):
        self.h_box.addWidget(self.btn_break)
        self.h_box.addWidget(self.Qlabel)
        self.h_box.addWidget(self.btn_Ok)
        self.v_box.addWidget(self.TableWidget)
        self.v_box.addLayout(self.h_box)
        self.TableWidget.setColumnCount(2)
        self.TableWidget.setColumnWidth(0, 150)
        self.TableWidget.setHorizontalHeaderLabels(['Name', 'ATTENDACE'])

        self.list()

    # sahifadegi royhatni toldiradi
    def list(self):
            id = Teams().Sorch_team_name(self.name)[0][0]
            Tree = Teams().List_if_student(id)
            self.TableWidget.setRowCount(len(Tree))

            count = 0
            for item in Tree:
                self.TableWidget.setItem(count,0,QTableWidgetItem(f'{item[0]}'))

                chkBoxItem = QTableWidgetItem()
                chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                chkBoxItem.setCheckState(QtCore.Qt.Unchecked)       
                self.TableWidget.setItem(count,1,chkBoxItem)
                count += 1

            self.Qlabel.setText(f"{len(Tree)}")       

    # sahifani yopish
    def Break(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()
            self.hide()

     # O'quv markazga pul qoshish uchun yangi oyna

    def Ok(self, window):
        checked_list = []
        for i in range(self.TableWidget.rowCount()):
            if self.TableWidget.item(i, 1).checkState() == 2:
                checked_list.append(self.TableWidget.item(i,0).text())
        
        if checked_list != []:
            Teams().CRM(checked_list, self.name)

        self.Break(window)

##########################################################################################################################################

if __name__ == '__main__':
    app = QApplication([])
    win = Main()
    sys.exit(app.exec_())