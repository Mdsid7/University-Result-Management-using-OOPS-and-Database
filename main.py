import database
import math
class Student:
    def _init_(self):
        self.Name= ""
        self.USN=""
        self.Class=""
        self.Section=""
        self.DBMS=0
        self.ADA= 0 
        self.OOP=0
        self.DSA=0  
        self.OS=0 
        self.SE=0
        self.Average=0 
        self.Grade=0
        self.SGPA=0

    def students(self):
        self.USN=(input("Enter your USN:"))
        USN2=self.USN
        USN3=self.USN
        database.results(self.USN,USN2,USN3)
class teacher1(Student):
    def Teacher1(self):
        a = input("Enter your Password:\n")
        if(a!=123):
            print("Password matched successfully")
            while True:
                ch=int(input("Enter your choice\n 1-Class Advisor \n 2-DBMS \n 3-ADA\n 9-back\n 0-exit \n"))
                if(ch==1):
                    self.Class_advisor1()
                elif(ch==2):
                    self.Dbms()
                elif(ch==3):
                    self.Ada()
                elif(ch==9):
                   break
                elif(ch==0):
                    exit(0)
                else:
                    print("Please enter correct choice")
        else:
            print("incorrect Password")
    
    def Class_advisor1(self):
        while True:
            s=int(input("Enter your choice\n 1-View\n 2-Perform Operations\n 3-statistics\n 9-back\n 0-exit\n"))
            if(s==1):
                database.A_view()
            elif(s==2):
                while True:
                    ch=int(input("Enter your choice \n 1-Insert new entry \n 2-Delete an entry \n 3-Update existing data \n 9-back \n 0-exit \n"))
                    if(ch==1):
                        self.Name=input("Enter the name of Student\n")
                        self.USN=input("Enter USN\n")
                        self.Class=input("Enter the class\n")
                        self.Section=input("Enter the section\n")
                        self.DBMS=input("Enter DBMS marks\n")
                        self.ADA=input("Enter ADA marks\n")
                        self.OOP=input("Enter OOP marks\n")
                        self.DSA=input("Enter DSA marks\n")
                        self.OS=input("Enter OS marks\n") 
                        self.SE=input("Enter SE marks\n")
                        
                        numbers= [self.DBMS,self.ADA, self.OOP ,self.DSA , self.OS , self.SE]
                        y=[ int(x) for x in numbers ]
                        self.Average=int(sum(y)/6)
                        if(self.Average>=90 and self.Average<=100):
                            self.Grade="O"
                        elif(self.Average>=80 and self.Average<90):
                            self.Grade="A+"
                        elif(self.Average>=70 and self.Average<80):
                            self.Grade="A"
                        elif(self.Average>=60 and self.Average<70):
                            self.Grade="B+"  
                        elif(self.Average>=55 and self.Average<60):
                            self.Grade="B"
                        elif(self.Average>=50 and self.Average<55):
                            self.Grade="C"
                        elif(self.Average>=45 and self.Average<50):
                            self.Grade="P"
                        elif(self.Average>=40 and self.Average<45):
                            self.Grade="E"
                        elif(self.Average<40):
                            self.Grade="F"
                        self.SGPA=input("Enter the SGPA\n")
                        database.insert_A_sec(self.Name,self.USN,self.Class,self.Section,self.DBMS,self.ADA,self.OOP,self.DSA,self.OS,self.SE,self.Average,self.Grade,self.SGPA)
                    elif(ch==2):
                        self.USN=input("Enter the USN of the record you want to delete:\n")
                        database.delete_A_sec(self.USN)
                    elif(ch==3):
                        while True:
                            ch=int(input("Enter the column you want to update :\n 1-Name \n 2-USN \n 3-Class \n 4-Section \n 5-DBMS \n 6-ADA \n 7-OOPS \n 8-DSA \n 9-OS \n 10-SE \n 11-Average \n 12-SGPA \n 0-back \n"))
                            if(ch==1):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Name=input("Enter the Updated Name of student \n")
                                database.update_A_sectionName(self.Name,self.USN)
                            elif(ch==2):
                                self.Name=input("Enter the Name of student you want to update: \n")
                                self.USN=input("enter the usn of student:\n")
                                database.update_A_sectionUSN(self.USN,self.Name)
                            elif(ch==3):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Class=input("Enter the Class of student: \n")
                                database.update_A_sectionClass(self.Class,self.USN)
                            elif(ch==4):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Section=input("Enter the section of student: \n")
                                database.update_A_sectionSection(self.Section,self.USN)
                            elif(ch==5):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.DBMS=input("Enter the updated marks of DBMS of student: \n")
                                database.update_A_sectionDBMS(self.DBMS,self.USN)
                                
                            elif(ch==6):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.ADA=input("Enter the updated marks of ADA of student: \n")
                                database.update_A_sectionADA(self.ADA,self.USN)
                                
                            elif(ch==7):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.OOPS=input("Enter the updated marks of OOPS of student: \n")
                                database.update_A_sectionOOPS(self.OOPS,self.USN)

                            elif(ch==8):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.DSA=input("Enter the updated marks of DSA of student: \n")
                                database.update_A_sectionDSA(self.DSA,self.USN)
                            elif(ch==9):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.OS=input("Enter the updated marks of OS of student: \n")
                                database.update_A_sectionOS(self.OS,self.USN)

                            elif(ch==10):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.SE=input("Enter the updated marks of SE of student: \n")
                                database.update_A_sectionSE(self.SE,self.USN)

                            elif(ch==11):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Average=int(input("Enter Average of student:\n"))
                                database.update_Average_A(self.Average,self.USN)
                                
                                if(self.Average>=90 and self.Average<=100):
                                    self.Grade="O"
                                elif(self.Average>=80 and self.Average<90):
                                    self.Grade="A+"
                                elif(self.Average>=70 and self.Average<80):
                                    self.Grade="A"
                                elif(self.Average>=60 and self.Average<70):
                                    self.Grade="B+"  
                                elif(self.Average>=55 and self.Average<60):
                                    self.Grade="B"
                                elif(self.Average>=50 and self.Average<55):
                                    self.Grade="C"
                                elif(self.Average>=45 and self.Average<50):
                                    self.Grade="P"
                                elif(self.Average>=40 and self.Average<45):
                                    self.Grade="E"
                                elif(self.Average<40):
                                    self.Grade="F"
                                database.update_Grade_A(self.Grade,self.USN)
                            elif(ch==12):
                                self.USN=input("enter the usn of student for which you want to update:\n ")
                                self.SGPA=input("Enter the SGPA\n")
                                database.update_A_sectionSGPA(self.SGPA,self.USN)
                            elif(ch==0):
                                break
                    elif(ch==9):
                        break   
                    elif(ch==0):
                        exit(0)
                    else:
                        print("Error,Enter correct option")  
             
            elif(s==3):
                while True:
                    c = int(input("\n 1-Display Average \n 2-Display Topper \n 9-back \n 0-exit \n "))
                    if(c==1):
                        database.A_avg()
                    elif(c==2):
                        database.A_top()
                    elif(c==9):
                        break
                    elif(c==0):
                        exit(0)
            elif(s==9):
                break
            elif(s==0):
                exit(0)
            else:
                print("Error,Enter correct option")  
    
    def Dbms(self):
        while True:
            a=int(input("\n 1-View\n 2-Update \n 3-Display Average \n 4-Display Topper \n 9-back \n 0-exit \n"))
            if(a==1):
                database.dbms_view()
            elif(a==2):
                while True:
                    a=int(input("Enter the section of student you want to update\n 1-CSE A \n 2-CSE B \n 3-CSE C \n 9-back \n 0-exit\n"))
                    if(a==1):
                        while True:
                            ch=int(input("Enter the column you want to update \n 1-Name \n 2-Class \n 3-Section \n 4-DBMS_Marks \n 9-back \n 0-exit \n"))        
                            if(ch==1):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Name=input("Enter the Updated Name of student: \n")
                                database.update_A_sectionName(self.Name,self.USN)
                            elif(ch==2):
                                self.Name=input("Enter the Name of student you want to update: \n")
                                self.USN=input("enter the usn of student:\n")
                                database.update_A_sectionUSN(self.USN,self.Name)
                            elif(ch==3):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Class=input("Enter the Class of student: \n")
                                database.update_A_sectionClass(self.Class,self.USN)
                            elif(ch==4):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Section=input("Enter the section of student: \n")
                                database.update_A_sectionSection(self.Section,self.USN)
                            elif(ch==5):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.DBMS=input("Enter the updated marks of DBMS of student: \n")
                                database.update_A_sectionDBMS(self.DBMS,self.USN)
                            elif(ch==9):
                                break
                            elif(ch==0):
                                exit(0)
                    elif(a==2):
                        while True:
                            ch=int(input("Enter the column you want to update \n 1-Name \n 2-Class \n 3-Section \n 4-DBMS_Marks \n 9-back \n 0-exit \n"))      
                            if(ch==1):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Name=input("Enter the Name of student you want to update: \n")
                                database.update_B_sectionName(self.Name,self.USN)
                            elif(ch==2):
                                self.Name=input("Enter the Updated Name of student: \n")
                                self.USN=input("enter the usn of student:\n")
                                database.update_B_sectionUSN(self.USN,self.Name)
                            elif(ch==3):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Class=input("Enter the Class of student: \n")
                                database.update_B_sectionClass(self.Class,self.USN)
                            elif(ch==4):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Section=input("Enter the section of student: \n")
                                database.update_B_sectionSection(self.Section,self.USN)
                            elif(ch==5):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.DBMS=input("Enter the updated marks of DBMS of student: \n")
                                database.update_B_sectionDBMS(self.DBMS,self.USN)
                            elif(ch==9):
                                break
                            elif(ch==0):
                                exit(0)
                    elif(a==3):
                        while True:
                            ch=int(input("Enter the column you want to update \n 1-Name \n 2-Class \n 3-Section \n 4-DBMS_Marks \n 9-back \n 0-exit \n"))           
                            if(ch==1):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Name=input("Enter the Updated Name of student: \n")
                                database.update_C_sectionName(self.Name,self.USN)
                            elif(ch==2):
                                self.Name=input("Enter the Name of student you want to update: \n")
                                self.USN=input("enter the usn of student:\n")
                                database.update_C_sectionUSN(self.USN,self.Name)
                            elif(ch==3):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Class=input("Enter the Class of student: \n")
                                database.update_C_sectionClass(self.Class,self.USN)
                            elif(ch==4):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Section=input("Enter the section of student: \n")
                                database.update_C_sectionSection(self.Section,self.USN)
                            elif(ch==5):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.DBMS=input("Enter the updated marks of DBMS of student: \n")
                                database.update_C_sectionDBMS(self.DBMS,self.USN)
                            elif(ch==9):
                                break
                            elif(ch==0):
                                exit(0)
                    elif(a==9):
                        break
                    elif(a==0):
                        exit(0)

            elif(a==3):
                database.dbms_avg()
            elif(a==4):
                database.dbms_top()
            elif(a==9):
                break
            elif(a==0):
                exit(0)

    def Ada(self):
        while True:
            ch=int(input(" 1-View\n 2-Update \n 3-Display Average \n 4-Display Topper \n 9-back \n 0-exit \n"))
            if(ch==1):
                database.ada_view()
            elif(ch==2):
                while True:
                    a=int(input("Enter the section of student you want to update\n 1-CSE A \n 2-CSE B \n 3-CSE C \n 9-back \n 0-exit\n"))
                    if(a==1):
                        while True:
                            ch=int(input("Enter the column you want to update \n 1-Name \n 2-Class \n 3-Section \n 4-ADA_Marks \n 9-back \n 0-exit \n"))          
                            if(ch==1):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Name=input("Enter the Updated Name of student: \n")
                                database.update_A_sectionName(self.Name,self.USN)
                            elif(ch==2):
                                self.Name=input("Enter the Name of student you want to update: \n")
                                self.USN=input("enter the usn of student:\n")
                                database.update_A_sectionUSN(self.USN,self.Name)
                            elif(ch==3):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Class=input("Enter the Class of student: \n")
                                database.update_A_sectionClass(self.Class,self.USN)
                            elif(ch==4):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Section=input("Enter the section of student: \n")
                                database.update_A_sectionSection(self.Section,self.USN)
                            elif(ch==5):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.ADA=input("Enter the updated marks of ADA of student: \n")
                                database.update_A_sectionADA(self.ADA,self.USN)
                            elif(ch==9):
                                break
                            elif(ch==0):
                                exit(0)
                    elif(a==2):
                        while True:
                            ch=int(input("Enter the column you want to update \n 1-Name \n 2-Class \n 3-Section \n 4-ADA_Marks \n 9-back \n 0-exit \n"))           
                            if(ch==1):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Name=input("Enter the Updated Name of student: \n")
                                database.update_B_sectionName(self.Name,self.USN)
                            elif(ch==2):
                                self.Name=input("Enter the Name of student you want to update: \n")
                                self.USN=input("enter the usn of student:\n")
                                database.update_B_sectionUSN(self.USN,self.Name)
                            elif(ch==3):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Class=input("Enter the Class of student: \n")
                                database.update_B_sectionClass(self.Class,self.USN)
                            elif(ch==4):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Section=input("Enter the section of student: \n")
                                database.update_B_sectionSection(self.Section,self.USN)
                            elif(ch==5):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.ADA=input("Enter the updated marks of ADA of student: \n")
                                database.update_B_sectionADA(self.ADA,self.USN)
                            elif(ch==9):
                                break
                            elif(ch==0):
                                exit(0)
                    elif(a==3):
                        while True:
                            ch=int(input("Enter the column you want to update \n 1-Name \n 2-Class \n 3-Section \n 4-ADA_Marks \n 9-back \n 0-exit \n"))           
                            if(ch==1):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Name=input("Enter the Updated Name of student: \n")
                                database.update_C_sectionName(self.Name,self.USN)
                            elif(ch==2):
                                self.Name=input("Enter the Name of student you want to update: \n")
                                self.USN=input("enter the usn of student:\n")
                                database.update_C_sectionUSN(self.USN,self.Name)
                            elif(ch==3):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Class=input("Enter the Class of student: \n")
                                database.update_C_sectionClass(self.Class,self.USN)
                            elif(ch==4):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Section=input("Enter the section of student: \n")
                                database.update_C_sectionSection(self.Section,self.USN)
                            elif(ch==5):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.ADA=input("Enter the updated marks of ADA of student: \n")
                                database.update_C_sectionADA(self.ADA,self.USN)
                            elif(ch==9):
                                break
                            elif(ch==0):
                                exit(0)
                    elif(a==9):
                        break
                    elif(a==0):
                        exit(0)
                
            elif(ch==3):
                database.ada_avg()
            elif(ch==4):
                database.ada_top()
            elif(ch==9):
                break
            elif(ch==0):
                exit(0)
class teacher2(teacher1):
    def Teacher2(self):
        a = input("Enter your Password:\n")
        if(a!=456):
            print("Password matched successfully")
            while True:
                ch=int(input("Enter your choice\n 1-Class Advisor \n 2-OOP \n 3-DSA\n 9-back\n 0-exit \n"))
                if(ch==1):
                    self.Class_advisor2()
                elif(ch==2):
                    self.Oop()
                elif(ch==3):
                    self.Dsa()
                elif(ch==9):
                   break
                elif(ch==0):
                    exit(0)
                else:
                    print("Please enter correct choice")
        else:
            print("incorrect Password")
    
    def Class_advisor2(self):
        while True:
            ch=int(input("Enter your choice\n 1-View\n 2-Perform Operations\n 3-statistics\n 9-back\n 0-exit\n"))
            if (ch==1):
                database.B_view()
            elif(ch==2):
                while True:
                    ch=int(input("Enter your choice \n 1-Insert new entry \n 2-Delete an entry \n 3-Update existing data \n 9-back \n 0-exit \n"))
                    if(ch==1):
                        self.Name=input("Enter the name of Student\n")
                        self.USN=input("Enter USN\n")
                        self.Class=input("Enter the class\n")
                        self.Section=input("Enter the section\n")
                        self.DBMS=input("Enter DBMS marks\n")
                        self.ADA=input("Enter ADA marks\n")
                        self.OOP=input("Enter OOP marks\n")
                        self.DSA=input("Enter DSA marks\n")
                        self.OS=input("Enter OS marks\n") 
                        self.SE=input("Enter SE marks\n")
                        
                        numbers= [self.DBMS,self.ADA, self.OOP ,self.DSA , self.OS , self.SE]
                        y=[ int(x) for x in numbers ]
                        self.Average=sum(y)/6
                        if(self.Average>=90 and self.Average<=100):
                            self.Grade="O"
                        elif(self.Average>=80 and self.Average<90):
                            self.Grade="A+"
                        elif(self.Average>=70 and self.Average<80):
                            self.Grade="A"
                        elif(self.Average>=60 and self.Average<70):
                            self.Grade="B+"  
                        elif(self.Average>=55 and self.Average<60):
                            self.Grade="B"
                        elif(self.Average>=50 and self.Average<55):
                            self.Grade="C"
                        elif(self.Average>=45 and self.Average<50):
                            self.Grade="P"
                        elif(self.Average>=40 and self.Average<45):
                            self.Grade="E"
                        elif(self.Average<40):
                            self.Grade="F"
                        self.SGPA=input("Enter the SGPA\n")
                        database.insert_B_sec(self.Name,self.USN,self.Class,self.Section,self.DBMS,self.ADA,self.OOP,self.DSA,self.OS,self.SE,self.Average,self.Grade,self.SGPA)
                    elif(ch==2):
                        self.USN=input("Enter the USN of the record you want to delete:\n")
                        database.delete_B_sec(self.USN)
                    elif(ch==3):
                       while True:
                            ch=int(input("Enter the column you want to update :\n 1-Name \n 2-USN \n 3-Class \n 4-Section \n 5-DBMS \n 6-ADA \n 7-OOPS \n 8-DSA \n 9-OS \n 10-SE \n 11-Average \n 12-SGPA \n 0-back \n"))
                            if(ch==1):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Name=input("Enter the Updated Name of student: \n")
                                database.update_B_sectionName(self.Name,self.USN)
                            elif(ch==2):
                                self.Name=input("Enter the Name of student you want to update: \n")
                                self.USN=input("enter the usn of student:\n")
                                database.update_B_sectionUSN(self.USN,self.Name)
                            elif(ch==3):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Class=input("Enter the Class of student: \n")
                                database.update_B_sectionClass(self.Class,self.USN)
                            elif(ch==4):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Section=input("Enter the section of student: \n")
                                database.update_B_sectionSection(self.Section,self.USN)
                            elif(ch==5):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.DBMS=input("Enter the updated marks of DBMS of student: \n")
                                database.update_B_sectionDBMS(self.DBMS,self.USN)
                                
                            elif(ch==6):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.ADA=input("Enter the updated marks of ADA of student: \n")
                                database.update_B_sectionADA(self.ADA,self.USN)
                                
                            elif(ch==7):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.OOPS=input("Enter the updated marks of OOPS of student: \n")
                                database.update_B_sectionOOPS(self.OOPS,self.USN)

                            elif(ch==8):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.DSA=input("Enter the updated marks of DSA of student: \n")
                                database.update_B_sectionDSA(self.DSA,self.USN)
                            elif(ch==9):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.OS=input("Enter the updated marks of OS of student: \n")
                                database.update_B_sectionOS(self.OS,self.USN)

                            elif(ch==10):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.SE=input("Enter the updated marks of SE of student: \n")
                                database.update_B_sectionSE(self.SE,self.USN)

                            elif(ch==11):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Average=int(input("Enter Average of student:\n"))
                                database.update_Average_B(self.Average,self.USN)
                                
                                if(self.Average>=90 and self.Average<=100):
                                    self.Grade="O"
                                elif(self.Average>=80 and self.Average<90):
                                    self.Grade="A+"
                                elif(self.Average>=70 and self.Average<80):
                                    self.Grade="A"
                                elif(self.Average>=60 and self.Average<70):
                                    self.Grade="B+"  
                                elif(self.Average>=55 and self.Average<60):
                                    self.Grade="B"
                                elif(self.Average>=50 and self.Average<55):
                                    self.Grade="C"
                                elif(self.Average>=45 and self.Average<50):
                                    self.Grade="P"
                                elif(self.Average>=40 and self.Average<45):
                                    self.Grade="E"
                                elif(self.Average<40):
                                    self.Grade="F"
                                database.update_Grade_B(self.Grade,self.USN)
                            elif(ch==12):
                                self.USN=input("enter the usn of student for which you want to update:\n ")
                                self.SGPA=input("Enter the SGPA\n")
                                database.update_B_sectionSGPA(self.SGPA,self.USN)
                            elif(ch==0):
                                break
                    elif(ch==9):
                        break   
                    elif(ch==0):
                        exit(0)
                    else:
                        print("Error,Enter correct option")
                    
            elif(ch==3):
                while True:
                    c = int(input("\n 1-Display Average \n 2-Display Topper \n 9-back \n 0-exit \n "))
                    if(c==1):
                        database.B_avg()
                    elif(c==2):
                        database.B_top()
                    elif(c==9):
                        break
                    elif(c==0):
                        exit(0)
            elif(ch==9):
                break
            elif(ch==0):
                exit(0)
            else:
                print("Error,Enter correct option")
    def Oop(self):
        while True:
            a=int(input("\n 1-View\n 2-Update \n 3-Display Average \n 4-Display Topper \n 9-back \n 0-exit \n"))
            if(a==1):
                database.oop_view()
            elif(a==2):
                while True:
                    a=int(input("Enter the section of student you want to update\n 1-CSE A \n 2-CSE B \n 3-CSE C \n 9-back \n 0-exit\n"))
                    if(a==1):
                        while True:
                            ch=int(input("Enter the column you want to update \n 1-Name \n 2-Class \n 3-Section \n 4-OOP_Marks \n 9-back \n 0-exit \n"))           
                            if(ch==1):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Name=input("Enter the Updated Name of student: \n")
                                database.update_A_sectionName(self.Name,self.USN)
                            elif(ch==2):
                                self.Name=input("Enter the Name of student you want to update: \n")
                                self.USN=input("enter the usn of student:\n")
                                database.update_A_sectionUSN(self.USN,self.Name)
                            elif(ch==3):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Class=input("Enter the Class of student: \n")
                                database.update_A_sectionClass(self.Class,self.USN)
                            elif(ch==4):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Section=input("Enter the section of student: \n")
                                database.update_A_sectionSection(self.Section,self.USN)
                            elif(ch==5):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.DBMS=input("Enter the updated marks of DBMS of student: \n")
                                database.update_A_sectionDBMS(self.DBMS,self.USN)
                            elif(ch==9):
                                break
                            elif(ch==0):
                                exit(0)
                    elif(a==2):
                        while True:
                            ch=int(input("Enter the column you want to update \n 1-Name \n 2-Class \n 3-Section \n 4-OOP_Marks \n 9-back \n 0-exit \n"))           
                            if(ch==1):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Name=input("Enter the Updated Name of student: \n")
                                database.update_B_sectionName(self.Name,self.USN)
                            elif(ch==2):
                                self.Name=input("Enter the Name of student you want to update: \n")
                                self.USN=input("enter the usn of student:\n")
                                database.update_B_sectionUSN(self.USN,self.Name)
                            elif(ch==3):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Class=input("Enter the Class of student: \n")
                                database.update_B_sectionClass(self.Class,self.USN)
                            elif(ch==4):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Section=input("Enter the section of student: \n")
                                database.update_B_sectionSection(self.Section,self.USN)
                            elif(ch==5):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.OOP=input("Enter the updated marks of OOP of student: \n")
                                database.update_B_sectionOOPS(self.OOP,self.USN)
                            elif(ch==9):
                                break
                            elif(ch==0):
                                exit(0)
                    elif(a==3):
                        while True:
                            ch=int(input("Enter the column you want to update \n 1-Name \n 2-Class \n 3-Section \n 4-OOP_Marks \n 9-back \n 0-exit \n"))           
                            if(ch==1):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Name=input("Enter the Updated Name of student: \n")
                                database.update_C_sectionName(self.Name,self.USN)
                            elif(ch==2):
                                self.Name=input("Enter the Name of student you want to update: \n")
                                self.USN=input("enter the usn of student:\n")
                                database.update_C_sectionUSN(self.USN,self.Name)
                            elif(ch==3):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Class=input("Enter the Class of student: \n")
                                database.update_C_sectionClass(self.Class,self.USN)
                            elif(ch==4):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Section=input("Enter the section of student: \n")
                                database.update_C_sectionSection(self.Section,self.USN)
                            elif(ch==5):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.OOP=input("Enter the updated marks of OOP of student: \n")
                                database.update_C_sectionOOPS(self.OOP,self.USN)
                            elif(ch==9):
                                break
                            elif(ch==0):
                                exit(0)
                    elif(a==9):
                        break
                    elif(a==0):
                        exit(0)
                
            elif(a==3):
                database.oop_avg()
            elif(a==4):
                database.oop_top()
            elif(a==9):
                break
            elif(a==0):
                exit(0)

    def Dsa(self):
        while True:
            ch=int(input(" 1-View\n 2-Update \n 3-Display Average \n 4-Display Topper \n 9-back \n 0-exit \n"))
            if(ch==1):
                database.dsa_view()
            elif(ch==2):
                 while True:
                    a=int(input("Enter the section of student you want to update\n 1-CSE A \n 2-CSE B \n 3-CSE C \n 9-back \n 0-exit\n"))
                    if(a==1):
                        while True:
                            ch=int(input("Enter the column you want to update \n 1-Name \n 2-Class \n 3-Section \n 4-DSA_Marks \n 9-back \n 0-exit \n"))           
                            if(ch==1):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Name=input("Enter the Updated Name of student: \n")
                                database.update_A_sectionName(self.Name,self.USN)
                            elif(ch==2):
                                self.Name=input("Enter the Name of student you want to update: \n")
                                self.USN=input("enter the usn of student:\n")
                                database.update_A_sectionUSN(self.USN,self.Name)
                            elif(ch==3):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Class=input("Enter the Class of student: \n")
                                database.update_A_sectionClass(self.Class,self.USN)
                            elif(ch==4):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Section=input("Enter the section of student: \n")
                                database.update_A_sectionSection(self.Section,self.USN)
                            elif(ch==5):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.DSA=input("Enter the updated marks of DSA of student: \n")
                                database.update_A_sectionDSA(self.DSA,self.USN)
                            elif(ch==9):
                                break
                            elif(ch==0):
                                exit(0)
                    elif(a==2):
                        while True:
                            ch=int(input("Enter the column you want to update \n 1-Name \n 2-Class \n 3-Section \n 4-DSA_Marks \n 9-back \n 0-exit \n"))           
                            if(ch==1):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Name=input("Enter the Updated Name of student: \n")
                                database.update_B_sectionName(self.Name,self.USN)
                            elif(ch==2):
                                self.Name=input("Enter the Name of student you want to update: \n")
                                self.USN=input("enter the usn of student:\n")
                                database.update_B_sectionUSN(self.USN,self.Name)
                            elif(ch==3):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Class=input("Enter the Class of student: \n")
                                database.update_B_sectionClass(self.Class,self.USN)
                            elif(ch==4):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Section=input("Enter the section of student: \n")
                                database.update_B_sectionSection(self.Section,self.USN)
                            elif(ch==5):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.DSA=input("Enter the updated marks of DSA of student: \n")
                                database.update_B_sectionDSA(self.DSA,self.USN)
                            elif(ch==9):
                                break
                            elif(ch==0):
                                exit(0)
                    elif(a==3):
                        while True:
                            ch=int(input("Enter the column you want to update \n 1-Name \n 2-Class \n 3-Section \n 4-DSA_Marks \n 9-back \n 0-exit \n"))           
                            if(ch==1):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Name=input("Enter the Updated Name of student: \n")
                                database.update_C_sectionName(self.Name,self.USN)
                            elif(ch==2):
                                self.Name=input("Enter the Name of student you want to update: \n")
                                self.USN=input("enter the usn of student:\n")
                                database.update_C_sectionUSN(self.USN,self.Name)
                            elif(ch==3):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Class=input("Enter the Class of student: \n")
                                database.update_C_sectionClass(self.Class,self.USN)
                            elif(ch==4):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Section=input("Enter the section of student: \n")
                                database.update_C_sectionSection(self.Section,self.USN)
                            elif(ch==5):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.DSA=input("Enter the updated marks of DSA of student: \n")
                                database.update_C_sectionDSA(self.DSA,self.USN)
                            elif(ch==9):
                                break
                            elif(ch==0):
                                exit(0)
                    elif(a==9):
                        break
                    elif(a==0):
                        exit(0)
                
            elif(ch==3):
                database.dsa_avg()
            elif(ch==4):
                database.dsa_top()
            elif(ch==9):
                break
            elif(ch==0):
                exit(0)
class teacher3(teacher2):
    def Teacher3(self):
        a = input("Enter your Password:\n")
        if(a!=789):
            print("Password matched successfully")
            while True:
                ch=int(input("Enter your choice\n 1-Class Advisor \n 2-OS \n 3-SE\n 9-back\n 0-exit \n"))
                if(ch==1):
                    self.Class_advisor3()
                elif(ch==2):
                    self.Os()
                elif(ch==3):
                    self.Se()
                elif(ch==9):
                   break
                elif(ch==0):
                    exit(0)
                else:
                    print("Please enter correct choice")
        else:
            print("incorrect Password")
    
    def Class_advisor3(self):
        while True:
            ch=int(input("Enter your choice\n 1-View\n 2-Perform Operations\n 3-statistics\n 9-back\n 0-exit\n"))
            if(ch==1):
                database.C_view()
            elif(ch==2):
                while True:
                    ch=int(input("Enter your choice \n 1-Insert new entry \n 2-Delete an entry \n 3-Update existing data \n 9-back \n 0-exit \n"))
                    if(ch==1):
                        self.Name=input("Enter the name of Student\n")
                        self.USN=input("Enter USN\n")
                        self.Class=input("Enter the class\n")
                        self.Section=input("Enter the section\n")
                        self.DBMS=input("Enter DBMS marks\n")
                        self.ADA=input("Enter ADA marks\n")
                        self.OOP=input("Enter OOP marks\n")
                        self.DSA=input("Enter DSA marks\n")
                        self.OS=input("Enter OS marks\n") 
                        self.SE=input("Enter SE marks\n")
                        
                        numbers= [self.DBMS,self.ADA, self.OOP ,self.DSA , self.OS , self.SE]
                        y=[ int(x) for x in numbers ]
                        self.Average=sum(y)/6
                        if(self.Average>=90 and self.Average<=100):
                            self.Grade="O"
                        elif(self.Average>=80 and self.Average<90):
                            self.Grade="A+"
                        elif(self.Average>=70 and self.Average<80):
                            self.Grade="A"
                        elif(self.Average>=60 and self.Average<70):
                            self.Grade="B+"  
                        elif(self.Average>=55 and self.Average<60):
                            self.Grade="B"
                        elif(self.Average>=50 and self.Average<55):
                            self.Grade="C"
                        elif(self.Average>=45 and self.Average<50):
                            self.Grade="P"
                        elif(self.Average>=40 and self.Average<45):
                            self.Grade="E"
                        elif(self.Average<40):
                            self.Grade="F"
                        self.SGPA=input("Enter the SGPA\n")
                        database.insert_C_sec(self.Name,self.USN,self.Class,self.Section,self.DBMS,self.ADA,self.OOP,self.DSA,self.OS,self.SE,self.Average,self.Grade,self.SGPA)
                    elif(ch==2):
                        self.USN=input("Enter the USN of the record you want to delete:\n")
                        database.delete_C_sec(self.USN)
                    elif(ch==3):
                        while True:
                            ch=int(input("Enter the column you want to update :\n 1-Name \n 2-USN \n 3-Class \n 4-Section \n 5-DBMS \n 6-ADA \n 7-OOPS \n 8-DSA \n 9-OS \n 10-SE \n 11-Average \n 12-SGPA \n 0-back \n"))
                            if(ch==1):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Name=input("Enter the Updated Name of student: \n")
                                database.update_C_sectionName(self.Name,self.USN)
                            elif(ch==2):
                                self.Name=input("Enter the Name of student you want to update: \n")
                                self.USN=input("enter the usn of student:\n")
                                database.update_C_sectionUSN(self.USN,self.Name)
                            elif(ch==3):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Class=input("Enter the Class of student: \n")
                                database.update_C_sectionClass(self.Class,self.USN)
                            elif(ch==4):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Section=input("Enter the section of student: \n")
                                database.update_C_sectionSection(self.Section,self.USN)
                            elif(ch==5):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.DBMS=input("Enter the updated marks of DBMS of student: \n")
                                database.update_C_sectionDBMS(self.DBMS,self.USN)
                                
                            elif(ch==6):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.ADA=input("Enter the updated marks of ADA of student: \n")
                                database.update_C_sectionADA(self.ADA,self.USN)
                                
                            elif(ch==7):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.OOPS=input("Enter the updated marks of OOPS of student: \n")
                                database.update_C_sectionOOPS(self.OOPS,self.USN)

                            elif(ch==8):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.DSA=input("Enter the updated marks of DSA of student: \n")
                                database.update_C_sectionDSA(self.DSA,self.USN)
                            elif(ch==9):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.OS=input("Enter the updated marks of OS of student: \n")
                                database.update_C_sectionOS(self.OS,self.USN)

                            elif(ch==10):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.SE=input("Enter the updated marks of SE of student: \n")
                                database.update_C_sectionSE(self.SE,self.USN)

                            elif(ch==11):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Average=int(input("Enter Average of student:\n"))
                                database.update_Average_C(self.Average,self.USN)
                                
                                if(self.Average>=90 and self.Average<=100):
                                    self.Grade="O"
                                elif(self.Average>=80 and self.Average<90):
                                    self.Grade="A+"
                                elif(self.Average>=70 and self.Average<80):
                                    self.Grade="A"
                                elif(self.Average>=60 and self.Average<70):
                                    self.Grade="B+"  
                                elif(self.Average>=55 and self.Average<60):
                                    self.Grade="B"
                                elif(self.Average>=50 and self.Average<55):
                                    self.Grade="C"
                                elif(self.Average>=45 and self.Average<50):
                                    self.Grade="P"
                                elif(self.Average>=40 and self.Average<45):
                                    self.Grade="E"
                                elif(self.Average<40):
                                    self.Grade="F"
                                database.update_Grade_C(self.Grade,self.USN)
                            elif(ch==12):
                                self.USN=input("enter the usn of student for which you want to update:\n ")
                                self.SGPA=input("Enter the SGPA\n")
                                database.update_C_sectionSGPA(self.SGPA,self.USN)
                            elif(ch==0):
                                break
                    elif(ch==9):
                        break   
                    elif(ch==0):
                        exit(0)
                    else:
                        print("Error,Enter correct option") 
            elif(ch==3):
                while True:
                    c = int(input("\n 1-Display Average \n 2-Display Topper \n 9-back \n 0-exit \n "))
                    if(c==1):
                        database.C_avg()
                    elif(c==2):
                        database.C_top()
                    elif(c==9):
                        break
                    elif(c==0):
                        exit(0)
            elif(ch==9):
                break
            elif(ch==0):
                exit(0)
            else:
                print("Error,Enter correct option")  
    
    def Os(self):
        while True:
            a=int(input("\n 1-View\n 2-Update \n 3-Display Average \n 4-Display Topper \n 9-back \n 0-exit \n"))
            if(a==1):
                database.os_view()
            elif(a==2):
               while True:
                    a=int(input("Enter the section of student you want to update\n 1-CSE A \n 2-CSE B \n 3-CSE C \n 9-back \n 0-exit\n"))
                    if(a==1):
                        while True:
                            ch=int(input("Enter the column you want to update \n 1-Name \n 2-Class \n 3-Section \n 4-OS_Marks \n 9-back \n 0-exit \n"))           
                            if(ch==1):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Name=input("Enter the Updated Name of student: \n")
                                database.update_A_sectionName(self.Name,self.USN)
                            elif(ch==2):
                                self.Name=input("Enter the Name of student you want to update: \n")
                                self.USN=input("enter the usn of student:\n")
                                database.update_A_sectionUSN(self.USN,self.Name)
                            elif(ch==3):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Class=input("Enter the Class of student: \n")
                                database.update_A_sectionClass(self.Class,self.USN)
                            elif(ch==4):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Section=input("Enter the section of student: \n")
                                database.update_A_sectionSection(self.Section,self.USN)
                            elif(ch==5):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.OS=input("Enter the updated marks of OS of student: \n")
                                database.update_A_sectionOS(self.OS,self.USN)
                            elif(ch==9):
                                break
                            elif(ch==0):
                                exit(0)
                    elif(a==2):
                        while True:
                            ch=int(input("Enter the column you want to update \n 1-Name \n 2-Class \n 3-Section \n 4-OS_Marks \n 9-back \n 0-exit \n"))           
                            if(ch==1):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Name=input("Enter the Updated Name of student: \n")
                                database.update_B_sectionName(self.Name,self.USN)
                            elif(ch==2):
                                self.Name=input("Enter the Name of student you want to update: \n")
                                self.USN=input("enter the usn of student:\n")
                                database.update_B_sectionUSN(self.USN,self.Name)
                            elif(ch==3):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Class=input("Enter the Class of student: \n")
                                database.update_B_sectionClass(self.Class,self.USN)
                            elif(ch==4):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Section=input("Enter the section of student: \n")
                                database.update_B_sectionSection(self.Section,self.USN)
                            elif(ch==5):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.OS=input("Enter the updated marks of OS of student: \n")
                                database.update_B_sectionOS(self.OS,self.USN)
                            elif(ch==9):
                                break
                            elif(ch==0):
                                exit(0)
                    elif(a==3):
                        while True:
                            ch=int(input("Enter the column you want to update \n 1-Name \n 2-Class \n 3-Section \n 4-OS_Marks \n 9-back \n 0-exit \n"))           
                            if(ch==1):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Name=input("Enter the Updated Name of student: \n")
                                database.update_C_sectionName(self.Name,self.USN)
                            elif(ch==2):
                                self.Name=input("Enter the Name of student you want to update: \n")
                                self.USN=input("enter the usn of student:\n")
                                database.update_C_sectionUSN(self.USN,self.Name)
                            elif(ch==3):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Class=input("Enter the Class of student: \n")
                                database.update_C_sectionClass(self.Class,self.USN)
                            elif(ch==4):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Section=input("Enter the section of student: \n")
                                database.update_C_sectionSection(self.Section,self.USN)
                            elif(ch==5):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.OS=input("Enter the updated marks of OS of student: \n")
                                database.update_C_sectionOS(self.OS,self.USN)
                            elif(ch==9):
                                break
                            elif(ch==0):
                                exit(0)
                    elif(a==9):
                        break
                    elif(a==0):
                        exit(0)
            elif(a==3):
                database.os_avg()
            elif(a==4):
                database.os_top()
            elif(a==9):
                break
            elif(a==0):
                exit(0)

    def Se(self):
        while True:
            ch=int(input(" 1-View\n 2-Update \n 3-Display Average \n 4-Display Topper \n 9-back \n 0-exit \n"))
            if(ch==1):
                database.se_view()
            elif(ch==2):
                while True:
                    a=int(input("Enter the section of student you want to update\n 1-CSE A \n 2-CSE B \n 3-CSE C \n 9-back \n 0-exit\n"))
                    if(a==1):
                        while True:
                            ch=int(input("Enter the column you want to update \n 1-Name \n 2-Class \n 3-Section \n 4-SE_Marks \n 9-back \n 0-exit \n"))           
                            if(ch==1):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Name=input("Enter the Updated Name of student: \n")
                                database.update_A_sectionName(self.Name,self.USN)
                            elif(ch==2):
                                self.Name=input("Enter the Name of student you want to update: \n")
                                self.USN=input("enter the usn of student:\n")
                                database.update_A_sectionUSN(self.USN,self.Name)
                            elif(ch==3):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Class=input("Enter the Class of student: \n")
                                database.update_A_sectionClass(self.Class,self.USN)
                            elif(ch==4):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Section=input("Enter the section of student: \n")
                                database.update_A_sectionSection(self.Section,self.USN)
                            elif(ch==5):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.SE=input("Enter the updated marks of SE of student: \n")
                                database.update_A_sectionSE(self.SE,self.USN)
                            elif(ch==9):
                                break
                            elif(ch==0):
                                exit(0)
                    elif(a==2):
                        while True:
                            ch=int(input("Enter the column you want to update \n 1-Name \n 2-Class \n 3-Section \n 4-SE_Marks \n 9-back \n 0-exit \n"))           
                            if(ch==1):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Name=input("Enter the Updated Name of student: \n")
                                database.update_B_sectionName(self.Name,self.USN)
                            elif(ch==2):
                                self.Name=input("Enter the Name of student you want to update: \n")
                                self.USN=input("enter the usn of student:\n")
                                database.update_B_sectionUSN(self.USN,self.Name)
                            elif(ch==3):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Class=input("Enter the Class of student: \n")
                                database.update_B_sectionClass(self.Class,self.USN)
                            elif(ch==4):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Section=input("Enter the section of student: \n")
                                database.update_B_sectionSection(self.Section,self.USN)
                            elif(ch==5):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.SE=input("Enter the updated marks of SE of student: \n")
                                database.update_B_sectionSE(self.SE,self.USN)
                            elif(ch==9):
                                break
                            elif(ch==0):
                                exit(0)
                    elif(a==3):
                        while True:
                            ch=int(input("Enter the column you want to update \n 1-Name \n 2-Class \n 3-Section \n 4-SE_Marks \n 9-back \n 0-exit \n"))           
                            if(ch==1):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Name=input("Enter the Updated Name of student: \n")
                                database.update_C_sectionName(self.Name,self.USN)
                            elif(ch==2):
                                self.Name=input("Enter the Name of student you want to update: \n")
                                self.USN=input("enter the usn of student:\n")
                                database.update_C_sectionUSN(self.USN,self.Name)
                            elif(ch==3):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Class=input("Enter the Class of student: \n")
                                database.update_C_sectionClass(self.Class,self.USN)
                            elif(ch==4):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.Section=input("Enter the section of student: \n")
                                database.update_C_sectionSection(self.Section,self.USN)
                            elif(ch==5):
                                self.USN=input("enter the usn of student for which you want to update:\n")
                                self.SE=input("Enter the updated marks of SE of student: \n")
                                database.update_C_sectionSE(self.SE,self.USN)
                            elif(ch==9):
                                break
                            elif(ch==0):
                                exit(0)
                    elif(a==9):
                        break
                    elif(a==0):
                        exit(0)
            elif(ch==3):
                database.se_avg()
            elif(ch==4):
                database.se_top()
            elif(ch==9):
                break
            elif(ch==0):
                exit(0)
            
def main():
    s=Student()
    s=teacher1()
    s=teacher2()
    s=teacher3()
    while True:
        ch=int(input("Enter\n 1-Student:\n 2-faculty:\n 0-exit\n"))
        if (ch==1):
            s.students()
        elif (ch==2):
            while True:
                ch=int(input("Enter your choice\n 1-Teacher1 \n 2-Teacher2 \n 3-Teacher3 \n 0-exit\n"))
                if (ch==1):
                    s.Teacher1()
                elif(ch==2):
                    s.Teacher2()
                elif(ch==3):
                    s.Teacher3()
                elif(ch==0):
                    break
                else:
                    print("Error,Enter correct choice")
        else:
            print("Wrong choice")

if __name__ == "__main__":
    main()