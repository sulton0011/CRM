from PyQt5.QtCore import center
import mysql.connector
from datetime import date, datetime

########################################################################################################################################################################################
# MYSQL malumotlariga kirish uchun oqim
class M_MYSQL:
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(
            host = "localhost",
            database = 'Student',
            user = 'root'
        )
        c = self.connection.cursor()
        ################### Tichers
        try:
            query = f'SELECT * FROM Tichers;'
            c.execute(query)
            info = c.fetchall()
            if info == []:
                query = f"INSER INTO Tichers (name, Agreement) VALUES ('TEST', 50);"
                c.execute(query)
                self.connection.comment()
        
        except:
            query = f'CREATE TABLE Tichers( id INTEGER PRIMARY KEY AUTO_INCREMENT, name VARCHAR(64), Agreement INTEGER );'
            c.execute(query)
            self.connection.comment()
        
            query = f"INSER INTO Tichers (name, Agreement) VALUES ('TEST', 50);"
            c.execute(query)
            self.connection.comment()
        ################### Ticher_wallet
        try:
            query = f'SELECT * FROM Ticher_wallet;'
            c.execute(query)
            info = c.fetchall()
            if info == []:
                query = f"INSER INTO Ticher_wallet (Ticher_id, mony_size, date_mony) VALUES (1, 0, '2021-12-31');"
                c.execute(query)
                self.connection.comment()

        except:
            query = f'CREATE TABLE Ticher_wallet(Ticher_id INTEGER, mony_size INTEGER, date_mony DATE, FOREIGN KEY (Ticher_id) REFERENCES Tichers(id));'
            c.execute(query)
            self.connection.comment()

            query = f"INSER INTO Ticher_wallet (Ticher_id, mony_size, date_mony) VALUES (1, 0, '2021-12-31');"
            c.execute(query)
            self.connection.comment()   
        ###################
        
########################################################################################################################################################################################
# o'quv markaz haqidegi malumotlar va qobilyatlar
class Center(M_MYSQL):
    def tableWidget_date_moniy_commint(self):
        query = "SELECT mony_data, mony_size, commint FROM center_wallet ORDER BY mony_data DESC;"
        
        c = self.connection.cursor()
        c.execute(query)
        data = c.fetchall()     
        
        return data

    def tableWidget_lineEdit(self):
        query = "SELECT SUM(mony_size) FROM center_wallet;"

        c = self.connection.cursor()
        c.execute(query)
        data = c.fetchall()     
        
        return data[0][0]

    def Add_moniy(self, moniy, comment):
        date = datetime.now().strftime("%Y.%m.%d %H:%M")
        query = f"INSERT INTO Center_wallet(Center_id, mony_data, mony_size, commint) VALUES(1, '{date}', {moniy}, '{comment}');"

        c = self.connection.cursor()
        c.execute(query)
        self.connection.commit()

    def Reduce_moniy(self, moniy, comment):
        date = datetime.now().strftime("%Y.%m.%d %H:%M")
        query = f"INSERT INTO Center_wallet(Center_id, mony_data, mony_size, commint) VALUES(1, '{date}', -{moniy}, '{comment}');"

        c = self.connection.cursor()
        c.execute(query)
        self.connection.commit()

########################################################################################################################################################################################
# student haqidegi malumotlari va unig qobilyatlari
class Students(M_MYSQL):

    # Studentlarni id, ismi, jami puli, puli nechta darsga etishini qaytaradi
    def tableWidget_id_name_moniy_lesson(self):
        query = "SELECT id, name, SUM(mony_size) FROM Students INNER JOIN Student_wallet ON Students.id = Student_wallet.Student_id GROUP BY Student.Students.id;"

        c = self.connection.cursor()
        c.execute(query)
        data = c.fetchall()     

        for i in range(len(data)):
            data[i] = list(data[i])
            data[i].append(self.tableWindget_lessons_remained(data[i][1], data[i][2]))

        return data

    # o'ziga student ismini va jami pul miqdorini oladi song unig puli nechta darsga etishini qaytaradi
    def tableWindget_lessons_remained(self, name, mony):
        c = self.connection.cursor()

        query = f"select DISTINCT Team_id from Team_S_S WHERE Student_name like '%{name}%';"
        c.execute(query)
        data = c.fetchall() 

        # print(data)
        
        query = f"SELECT Direction_id FROM Team WHERE id = {data[0][0]};"
        c.execute(query)
        data = c.fetchall() 
        
        query = f"SELECT lesson_mony,  lesson_size FROM Direction WHERE Id = {data[0][0]}"
        c.execute(query)
        data = c.fetchall() 

        return mony // (data[0][0] // data[0][1])

    # barcha oquvchilarni pul miqdorini qaytaradi
    def tableWidget_lineEdit(self):
        query = "SELECT SUM(mony_size) FROM Student_wallet;"

        c = self.connection.cursor()
        c.execute(query)
        data = c.fetchall()     
        
        return data[0][0]

    # sutdentni ismini oladi son uni hisobidegi jami pulni qaytaradi
    def tableWidget_sum(self, name):
        query = f"SELECT SUM(mony_size) FROM STUDENT_WALLET WHERE student_id = {self.Sorch_students(name)[0][0]};"

        c = self.connection.cursor()
        c.execute(query)
        info = c.fetchall()
        return info[0][0]

    # Oziga studentni idsi va pul miqdorini oladi son oquvchini cashilogidan pulni ayiradi
    def Get_money(self, Student_name, moniy):
        date = datetime.now().strftime("%Y.%m.%d %H:%M")
        query = f"INSERT INTO Student_wallet(Student_id, date_mony, mony_size) VALUES({self.Sorch_students(Student_name)[0][0]}, '{date}', -{moniy});"

        c = self.connection.cursor()
        c.execute(query)
        self.connection.commit()

    # Student idsini va pul miqdorini oziga oladi va shu pul miqdorini studentni kashilogiga qoshadi
    def Add_moniy(self, Student_id, moniy):
        date = datetime.now().strftime("%Y.%m.%d %H:%M")
        query = f"INSERT INTO Student_wallet(Student_id, date_mony, mony_size) VALUES({Student_id}, '{date}', {moniy});"

        c = self.connection.cursor()
        c.execute(query)
        self.connection.commit()

    # oziga student idisini oladi va studentni pul aynalmalarini qaytaradi
    def Histre(self, Student_id):
        query = f"SELECT date_mony, mony_size FROM Student_wallet WHERE Student_id = {Student_id} ORDER BY date_mony DESC;"

        c = self.connection.cursor()
        c.execute(query)
        info = c.fetchall()

        return info

    # oziga guruh idsini va oquvchi ismini oladi va yangi oquvchi yaratadi
    def Add_Students(self, Team_id, Student_name):
        query = f"INSERT INTO Students (name) VALUES ('{Student_name}');"

        c = self.connection.cursor()
        c.execute(query)
        self.connection.commit()

        Teams().Add_student(Team_id, Student_name)
        self.Add_moniy(self.Sorch_students(Student_name)[0][0], 0)

    # o'ziga students ismini oladi va studentni idsi va toli ismini qaytaradi
    def Sorch_students(self, Students_name):
        query = f"SELECT * FROM  students WHERE name like '%{Students_name}%';"

        c = self.connection.cursor()
        c.execute(query)
        info = c.fetchall()

        return info

    # Student imini kiritiladi son barcha table uni ochib tashedi 
    def Delete_students(self, Students_name):
        c = self.connection.cursor()
        
        query = f"DELETE FROM Team_S_S WHERE Student_name LIKE '%{Students_name}%';"
        c.execute(query)
        self.connection.commit()
        
        query = f"DELETE FROM Student_wallet WHERE Student_id = {self.Sorch_students(Students_name)[0][0]};"
        c.execute(query)
        self.connection.commit()
        
        query = f"DELETE FROM Students WHERE id = {self.Sorch_students(Students_name)[0][0]};"
        c.execute(query)
        self.connection.commit()

########################################################################################################################################################################################
# o'qtuvchi haqidagi malumotlar va unig qobilyatlari
class Tichers(M_MYSQL):

    # o'qtuvchini ismi, jami pul miqdori va nechta guruhi mavjutligini qaytaradi
    def tableWidget_id_name_moniy_team(self):
        query = "SELECT id, name, SUM(mony_size) FROM Tichers INNER JOIN Ticher_wallet ON Tichers.id = Ticher_wallet.Ticher_id GROUP BY Tichers.id;"

        c = self.connection.cursor()
        c.execute(query)
        data = c.fetchall()     

        for i in range(len(data)):
            data[i] = list(data[i])
            data[i].append(self.tableWidget_number_of_team(data[i][0]))

        return data

    # o'ziga oqtuvchni idisini oladi va o'qtuvchini nechta guruhi mavjutligini qaytaradi
    def tableWidget_number_of_team(self, Ticher_id):
        query = f"SELECT * FROM Team WHERE Ticher_id = {Ticher_id};"

        c = self.connection.cursor()
        c.execute(query)
        data = c.fetchall()

        return len(data)

    # Barcha oqtuvchilarni jami pul miqdorini qaytaradi
    def tableWidget_lineEdit(self):
        query = "SELECT SUM(mony_size) FROM Ticher_wallet;"

        c = self.connection.cursor()
        c.execute(query)
        data = c.fetchall()     
        
        return data[0][0]

    # O'ziga oqtuvchini idsini oladi va shu oqtuvchidagi pul aynalmalarni qaytaradi
    def Histre(self, Ticher_id):
        query = f"SELECT date_mony, mony_size FROM Ticher_wallet WHERE Ticher_id = {Ticher_id} ORDER BY date_mony DESC;"

        c = self.connection.cursor()
        c.execute(query)
        info = c.fetchall()

        return info
    
    # O'qtuvchi idsi va pul miqdorini kiritiladi son oqtuvchini hisobidan shu pul miqdorichalik pul ayriladi
    def Get_money(self, Ticher_id, money):
        date = datetime.now().strftime("%Y.%m.%d %H:%M")
        query = f"INSERT INTO Ticher_wallet (Ticher_id, mony_size, date_mony) VALUES ({Ticher_id}, -{money}, '{date}');"

        c = self.connection.cursor()
        c.execute(query)
        self.connection.commit()

    # O'ziga oqtuvchini ismini va o'quvchidan necha foyz olishini kelishilgan holatta qabul qiladi va yangi oqtuvchi yaratadi
    def Add_Tichers(self, Ticher_name, Agreement):
        c = self.connection.cursor()

        query = f"INSERT INTO Tichers(name, Agreement) VALUES ('{Ticher_name}', {Agreement});"
        c.execute(query)
        self.connection.commit()

        date = datetime.now().strftime("%Y.%m.%d %H:%M")
        query = f"INSERT INTO Ticher_wallet (Ticher_id, mony_size, date_mony) VALUES ({self.Sorch_ticher(Ticher_name)[0][0]}, 0, '{date}');"
        c.execute(query)
        self.connection.commit()

    # O'ziga o'qtuvchini ismini oladi vani barch malumotlarini qaytaradi
    def Sorch_ticher(self, Ticher_name):
        query = f"SELECT * FROM Tichers WHERE name LIKE '%{Ticher_name}%';"

        c = self.connection.cursor()
        c.execute(query)
        info = c.fetchall()

        return info

    # O'ziga o'qtuvchini ismini oladi son uni toliq ochirip tashledi barcha tabledan
    def Delete_Ticher(self, Ticher_name):
        c = self.connection.cursor()

        query = f"DELETE FROM Ticher_wallet WHERE Ticher_id = {self.Sorch_ticher(Ticher_name)[0][0]};"
        c.execute(query)
        self.connection.commit()



        query = f" SELECT * FROM Team WHERE Ticher_id = {self.Sorch_ticher(Ticher_name)[0][0]};"
        c.execute(query)
        info = c.fetchall()
        # print(info)
        if info != []:
            Teams().Delete_team(info[0][0])


        query = f"DELETE FROM Tichers WHERE name LIKE '%{Ticher_name}%';"
        c.execute(query)
        self.connection.commit()

    # O'ziga oqtuvchini id sini oladi va uqtuvchihaqidagi malumotlarni qaytaradi
    def Sorch_Ticher_id(self, Ticher_id):
        query = f"SELECT * FROM Tichers WHERE id = {Ticher_id};"

        c = self.connection.cursor()
        c.execute(query)
        info = c.fetchall()

        return info

    # oziga O'qtuvchini idsini va pul miqdorini oladi son pulni oqtuvchini cashilogiga qoshadi
    def Add_money(self, Ticher_id, money):
        date = datetime.now().strftime("%Y.%m.%d %H:%M")
        query = f"INSERT INTO Ticher_wallet (Ticher_id, mony_size, date_mony) VALUES ({Ticher_id}, {money}, '{date}');"

        c = self.connection.cursor()
        c.execute(query)
        self.connection.commit()

    def tableWidget_line_edit_ticher(self, name):
        query = f"SELECT SUM(mony_size) FROM Ticher_wallet WHERE Ticher_id = {self.Sorch_ticher(name)[0][0]};"

        c = self.connection.cursor()
        c.execute(query)
        info = c.fetchall()

        return info[0][0]

########################################################################################################################################################################################
# guruhlar haqida malumotlar va qobilyatlari 
class Teams(M_MYSQL):
    
    # guruhlarni guruh yonalishi, nomi, oqtuvchisi va o'quvchi sonini korsatadi
    def tableWidget_direction_name_ticher_student(self):
        query = "SELECT * FROM Team ORDER BY name;"

        c = self.connection.cursor()
        c.execute(query)
        info = c.fetchall()

        for i in range(len(info)):
            info[i] = list(info[i])
            info[i][1] = self.tableWidget_direction_name(info[i][1])
            info[i][3] = self.tableWidget_ticher_name(info[i][3])
            info[i].append(self.tableWidget_student_size(info[i][0]))

        return info
    
    # guruh id sini jonatiladi va guruhta nechta oquvchi oqishini qaytaradi
    def tableWidget_student_size(self, Team_id):
        query = f"SELECT * FROM Team_S_S WHERE Team_id = {Team_id};"

        c = self.connection.cursor()
        c.execute(query)
        info = c.fetchall()

        return len(info)
    
    # Oqtuvchini id sini jonatilsa oqtuvchini ism familyasini qaytaradi
    def tableWidget_ticher_name(self, Ticher_id):
        query = f"SELECT * FROM Tichers WHERE id = {Ticher_id};"

        c = self.connection.cursor()
        c.execute(query)
        info = c.fetchall()

        return info[0][1]
    
    # curs id sini jonatilsa uni nimi, narxi, dars soni qaytaradi 
    def tableWidget_direction_name(self, Direction_id):
        query = f"SELECT * FROM Direction WHERE id = {Direction_id};"

        c = self.connection.cursor()
        c.execute(query)
        info = c.fetchall()

        return info[0][1]
    
    # oziga Curs idsini va guruh nomini, o'qtuvchini idsini olib yangi guruh yaratadi
    def Add_Team(self, direction_id, name, Ticher_id):
        query = f"INSERT INTO Team (Direction_id, name, Ticher_id) VALUES ({direction_id}, '{name}', {Ticher_id});"

        c = self.connection.cursor()
        c.execute(query)
        self.connection.commit()
    
    # Oziga Guruh idsini va student ismini oladi va guruhga osha studentni qoship qoyadi
    def Add_student(self, Team_id, Student_name):
        query = f"INSERT INTO Team_S_S (Team_id, Student_name) VALUES({Team_id}, '{Student_name}');"

        c = self.connection.cursor()
        c.execute(query)
        self.connection.commit()
    
    # Gruh idsini jonatilsa u guruhdegi oquvchilarni royhatini qaytaradi
    def List_if_student(self, Team_id):
        query = f"""SELECT Students.name, SUM(Student_wallet.mony_size) FROM Students INNER JOIN Team_S_S ON 
        Students.name = Team_S_S.Student_name LEFT JOIN Student_wallet ON Students.id = Student_wallet.Student_id 
        WHERE Team_id = {Team_id} GROUP BY Students.name ORDER BY Student_name ;"""

        c = self.connection.cursor()
        c.execute(query)
        info = c.fetchall()

        return info
    
    # Guruh idsini beliadi va u guruhni butkul ochirip tashledi
    def Delete_team(self, Team_id):
        c = self.connection.cursor()
 
        query = f"DELETE FROM Team_S_S WHERE Team_id = {Team_id};"
        c.execute(query)
        self.connection.commit()
        
        query = f"DELETE FROM Team WHERE id = {Team_id};"
        c.execute(query)
        self.connection.commit()

    # Oquvchini ismini kiritilsa u qaysi gurhta ekanligini qaytaradi
    def Sorch_team_Students(self, Student_name):
        query = f"SELECT * FROM Team_S_S WHERE Student_name LIKE '%{Student_name}%';"

        c = self.connection.cursor()
        c.execute(query)
        info = c.fetchall()

        return info

    # oziga oquvchilarni ismi tushurilgan royhatni oladi son uni bir kunlik dars narxi boyicha oqtuvchi va marcaz hisobiga otkazadi
    def CRM(self, lst_name, Team_name ):
        lessin_size = int()
        lessin_money = int()
        agreement = int()
        ticher = 0
        centers = 0
        team_id = Teams().Sorch_team_name(Team_name)
        for i in lst_name:

            lessin_size = Directions().Sorch_Direction(team_id[0][1])[0][2]
            lessin_money = Directions().Sorch_Direction(team_id[0][1])[0][3]
            agreement = Tichers().Sorch_Ticher_id(team_id[0][3])[0][2]

            amount = lessin_money / lessin_size
            ticher += (amount / 100) * agreement
            centers +=  (amount / 100) * (100 - agreement)

            print(amount, ticher, centers)

            Students().Get_money(i, amount)
            a = i
        Tichers().Add_money(self.Sorch_team(self.Sorch_team_Students(a)[0][0])[0][3], ticher)
        Center().Add_moniy(centers, f"{self.Sorch_team(self.Sorch_team_Students(a)[0][0])[0][2]}")

    # Guruh idsini berilsa u guruh haqidagi malumotlarni qaytaradi 
    def Sorch_team(self, Team_id):
        query = f"SELECT * FROM Team WHERE id = {Team_id};"

        c = self.connection.cursor()
        c.execute(query)
        info = c.fetchall()

        return info
 
    # Guruh idsini berilsa u guruh haqidagi malumotlarni qaytaradi 
    def Sorch_team_name(self, Team_name):
        query = f"SELECT * FROM Team WHERE name = '{Team_name}';"

        c = self.connection.cursor()
        c.execute(query)
        info = c.fetchall()

        return info
 
    def Sorch_team_S_S_name(self, Team_id):
        query = f"SELECT * FROM Team_S_S WHERE Team_id = '{Team_id}';"

        c = self.connection.cursor()
        c.execute(query)
        info = c.fetchall()

        return info

########################################################################################################################################################################################
# curs haqidagi malumotlar va qobilyatlari
class Directions(M_MYSQL):
    
    # curslarni nomi, narxi va darslar sonini
    def tableWidget_name_mony_lesson(self):
        query = "SELECT id, name, lesson_mony, lesson_size FROM Direction;"

        c = self.connection.cursor()
        c.execute(query)
        info = c.fetchall()

        return info
    
    # curslarni jami pul miqdorini hisobledi
    def tableWodget_lineEdit(self):
        query = "SELECT SUM(lesson_mony) FROM Direction;"

        c = self.connection.cursor()
        c.execute(query)
        info = c.fetchall()

        return info[0][0]
    
    # yangi curs yaratadi
    def Add_direction(self, name, size, money):
        query = f"INSERT INTO Direction(name, lesson_size, lesson_mony) VALUES('{name}', {size}, {money});"

        c = self.connection.cursor()
        c.execute(query)
        self.connection.commit()
    
    # cursni ochirip tashledi
    def Delete_direction(self, name):
        query = f"DELETE FROM Direction WHERE name LIKE '%{name}%';"

        c = self.connection.cursor()
        c.execute(query)
        self.connection.commit()
    
    # cursni pulini va darslar miqdorini ozgartiradi
    def Chenge(self, name, size, money):
        query = f"UPDATE Direction SET lesson_size = {size}, lesson_mony = {money} WHERE name LIKE '%{name}%'"

        c = self.connection.cursor()
        c.execute(query)
        self.connection.commit()
    
    # Curs malumotlarini curs idsi orqali qidirish
    def Sorch_Direction(self, Directin_id):
        query = f"SELECT * FROM Direction WHERE id = {Directin_id};"

        c = self.connection.cursor()
        c.execute(query)
        info = c.fetchall()

        return info
    
    # Curs malumotlarini curs nomi orqali qidirish
    def Sorch_Direction_name(self, Directin_name):
        query = f"SELECT * FROM Direction WHERE name LIKE '%{Directin_name}%';"

        c = self.connection.cursor()
        c.execute(query)
        info = c.fetchall()

        return info

########################################################################################################################################################################################
if __name__ == "__main__":
    a = Teams()
    a.Delete_team(11)