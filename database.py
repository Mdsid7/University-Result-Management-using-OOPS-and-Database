import mysql.connector
import string
mydb = mysql.connector.connect (
  host="localhost",
  user="root",
  password="myfamily",
  database="result"
)
mycursor=mydb.cursor()
def A_view():
  mycursor.execute("SELECT * FROM A_section")
  field_names = [i[0] for i in mycursor.description]
  print(field_names)
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)


def B_view():
  mycursor.execute("SELECT * FROM B_section")
  field_names = [i[0] for i in mycursor.description]
  print(field_names)
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)

def C_view():
  mycursor.execute("SELECT * FROM C_section")
  field_names = [i[0] for i in mycursor.description]
  print(field_names)
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)
  
def results(USN,USN2,USN3):
  sql = "SELECT * FROM A_section where USN=%s UNION SELECT * FROM B_section where USN=%s UNION SELECT * FROM C_section WHERE USN=%s"
  adr =(USN,USN2,USN3,)
  mycursor.execute(sql,adr,)
  field_names = [i[0] for i in mycursor.description]
  print(field_names)
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)

def insert_A_sec(Name,USN,Class,Section,DBMS,ADA,OOP,DSA,OS,SE,Average,Grade,SGPA):
  sql = "insert into A_section(Name,USN,Class,Section,DBMS,ADA,OOP,DSA,OS,SE,Average,Grade,SGPA) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
  val = (Name,USN,Class,Section,DBMS,ADA,OOP,DSA,OS,SE,Average,Grade,SGPA,)
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "record inserted Successfully.")

def insert_B_sec(Name,USN,Class,Section,DBMS,ADA,OOP,DSA,OS,SE,Average,Grade,SGPA):
  sql = "insert into B_section(Name,USN,Class,Section,DBMS,ADA,OOP,DSA,OS,SE,Average,Grade,SGPA) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
  val = (Name,USN,Class,Section,DBMS,ADA,OOP,DSA,OS,SE,Average,Grade,SGPA,)
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "record inserted Successfully.")

def insert_C_sec(Name,USN,Class,Section,DBMS,ADA,OOP,DSA,OS,SE,Average,Grade,SGPA):
  sql = "insert into C_section(Name,USN,Class,Section,DBMS,ADA,OOP,DSA,OS,SE,Average,Grade,SGPA) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
  val = (Name,USN,Class,Section,DBMS,ADA,OOP,DSA,OS,SE,Average,Grade,SGPA,)
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "record inserted Successfully.")

def delete_A_sec(USN):
  sql = "DELETE FROM A_section WHERE USN = %s"
  adr = (USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) deleted")

def delete_B_sec(USN):
  sql = "DELETE FROM B_section WHERE USN = %s"
  adr = (USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) deleted")

def delete_C_sec(USN):
  sql = "DELETE FROM C_section WHERE USN = %s"
  adr = (USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) deleted")

def A_avg():
  mycursor.execute("Select AVG(Average) FROM A_section")
  a = mycursor.fetchone()
  res=float('.'.join(str(ele)for ele in a))
  print("\nThe average percentage of A_section students is: "+ str(res))

def B_avg():
  mycursor.execute("Select AVG(Average) FROM B_section")
  a = mycursor.fetchone()
  res=float('.'.join(str(ele)for ele in a))
  print("\nThe average percentage of B_section students is: "+ str(res))

def C_avg():
  mycursor.execute("Select AVG(Average) FROM C_section")
  a = mycursor.fetchone()
  res=float('.'.join(str(ele)for ele in a))
  print("\nThe average percentage of C_section students is: "+ str(res))

def A_top():
  mycursor.execute("Select * FROM A_section WHERE SGPA = (SELECT MAX(SGPA) FROM A_section)")
  print("\n The Topper Of the Class is :\n")
  field_names = [i[0] for i in mycursor.description]
  print(field_names)
  a=mycursor.fetchall()
  for x in a:
    print(x)

def B_top():
  mycursor.execute("Select * FROM B_section WHERE SGPA = (SELECT MAX(SGPA) FROM B_section)")
  print("\n The Topper Of the Class is :\n")
  field_names = [i[0] for i in mycursor.description]
  print(field_names)
  a=mycursor.fetchall()
  for x in a:
    print(x)

def C_top():
  mycursor.execute("Select * FROM C_section WHERE SGPA = (SELECT MAX(SGPA) FROM C_section)")
  print("\n The Topper Of the Class is :\n")
  field_names = [i[0] for i in mycursor.description]
  print(field_names)
  a=mycursor.fetchall()
  for x in a:
    print(x)

def dbms_view():
  mycursor.execute("SELECT Name,USN,Class,Section,DBMS FROM A_section UNION SELECT Name,USN,Class,Section,DBMS FROM B_section UNION SELECT Name,USN,Class,Section,DBMS FROM C_section")
  field_names = [i[0] for i in mycursor.description]
  print(field_names)
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)

def ada_view():
  mycursor.execute("SELECT Name,USN,Class,Section,ADA FROM A_section UNION SELECT Name,USN,Class,Section,ADA FROM B_section UNION SELECT Name,USN,Class,Section,ADA FROM C_section")
  field_names = [i[0] for i in mycursor.description]
  print(field_names)
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)

def oop_view():
  mycursor.execute("SELECT Name,USN,Class,Section,OOP FROM A_section UNION SELECT Name,USN,Class,Section,OOP FROM B_section UNION SELECT Name,USN,Class,Section,OOP FROM C_section")
  field_names = [i[0] for i in mycursor.description]
  print(field_names)
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)

def dsa_view():
  mycursor.execute("SELECT Name,USN,Class,Section,DSA FROM A_section UNION SELECT Name,USN,Class,Section,DSA FROM B_section UNION SELECT Name,USN,Class,Section,DSA FROM C_section")
  field_names = [i[0] for i in mycursor.description]
  print(field_names)
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)

def os_view():
  mycursor.execute("SELECT Name,USN,Class,Section,OS FROM A_section UNION SELECT Name,USN,Class,Section,OS FROM B_section UNION SELECT Name,USN,Class,Section,OS FROM C_section")
  field_names = [i[0] for i in mycursor.description]
  print(field_names)
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)

def se_view():
  mycursor.execute("SELECT Name,USN,Class,Section,SE FROM A_section UNION SELECT Name,USN,Class,Section,SE FROM B_section UNION SELECT Name,USN,Class,Section,SE FROM C_section")
  field_names = [i[0] for i in mycursor.description]
  print(field_names)
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)

def dbms_avg():
  mycursor.execute("Select AVG(DBMS) FROM ( Select DBMS FROM A_section UNION ALL Select DBMS FROM B_section UNION ALL Select DBMS FROM C_section) s ")
  a = mycursor.fetchone()
  res=float('.'.join(str(ele)for ele in a))
  print("\nThe average percentage in DBMS is: "+ str(res))

def ada_avg():
  mycursor.execute("Select AVG(ADA) FROM ( Select ADA FROM A_section UNION ALL Select ADA FROM B_section UNION ALL Select ADA FROM C_section) s ")
  a = mycursor.fetchone()
  res=float('.'.join(str(ele)for ele in a))
  print("\nThe average percentage in ADA is: "+ str(res))

def oop_avg():
  mycursor.execute("Select AVG(OOP) FROM ( Select OOP FROM A_section UNION ALL Select OOP FROM B_section UNION ALL Select OOP FROM C_section) s ")
  a = mycursor.fetchone()
  res=float('.'.join(str(ele)for ele in a))
  print("\nThe average percentage in OOP is: "+ str(res))  

def dsa_avg():
  mycursor.execute("Select AVG(DSA) FROM ( Select DSA FROM A_section UNION ALL Select DSA FROM B_section UNION ALL Select DSA FROM C_section) s ")
  a = mycursor.fetchone()
  res=float('.'.join(str(ele)for ele in a))
  print("\nThe average percentage in DSA is: "+ str(res))

def os_avg():
  mycursor.execute("Select AVG(OS) FROM ( Select OS FROM A_section UNION ALL Select OS FROM B_section UNION ALL Select OS FROM C_section) s ")
  a = mycursor.fetchone()
  res=float('.'.join(str(ele)for ele in a))
  print("\nThe average percentage in OS is: "+ str(res))

def se_avg():
  mycursor.execute("Select AVG(SE) FROM ( Select SE FROM A_section UNION ALL Select SE FROM B_section UNION ALL Select SE FROM C_section) s ")
  a = mycursor.fetchone()
  res=float('.'.join(str(ele)for ele in a))
  print("\nThe average percentage in SE is: "+ str(res))  

def dbms_top():
  mycursor.execute("Select Name,USN,Class,Section,DBMS FROM (SELECT Name,USN,Class,Section,DBMS FROM A_section WHERE DBMS = (SELECT MAX(DBMS) FROM A_section) UNION SELECT Name,USN,Class,Section,DBMS FROM B_section WHERE DBMS = (SELECT MAX(DBMS) FROM B_section) UNION SELECT Name,USN,Class,Section,DBMS FROM C_section WHERE DBMS = (SELECT MAX(DBMS) FROM C_section))s ORDER BY DBMS DESC LIMIT 1 ")
  print("\n The Topper Of the DBMS is :\n")
  field_names = [i[0] for i in mycursor.description]
  print(field_names)
  a = mycursor.fetchall()
  for x in a:
    print(x)

def ada_top():
  mycursor.execute("Select Name,USN,Class,Section,ADA FROM (SELECT Name,USN,Class,Section,ADA FROM A_section WHERE ADA = (SELECT MAX(ADA) FROM A_section) UNION SELECT Name,USN,Class,Section,ADA FROM B_section WHERE ADA = (SELECT MAX(ADA) FROM B_section) UNION SELECT Name,USN,Class,Section,ADA FROM C_section WHERE ADA = (SELECT MAX(ADA) FROM C_section))s ORDER BY ADA DESC LIMIT 1 ")
  print("\n The Topper Of the ADA is :\n")
  field_names = [i[0] for i in mycursor.description]
  print(field_names)
  a = mycursor.fetchall()
  for x in a:
    print(x)

def oop_top():
  mycursor.execute("Select Name,USN,Class,Section,OOP FROM (SELECT Name,USN,Class,Section,OOP FROM A_section WHERE OOP = (SELECT MAX(OOP) FROM A_section) UNION SELECT Name,USN,Class,Section,OOP FROM B_section WHERE OOP = (SELECT MAX(OOP) FROM B_section) UNION SELECT Name,USN,Class,Section,OOP FROM C_section WHERE OOP = (SELECT MAX(OOP) FROM C_section))s ORDER BY OOP DESC LIMIT 1 ")
  print("\n The Topper Of the ADA is :\n")
  field_names = [i[0] for i in mycursor.description]
  print(field_names)
  a = mycursor.fetchall()
  for x in a:
    print(x)

def dsa_top():
  mycursor.execute("Select Name,USN,Class,Section,DSA FROM (SELECT Name,USN,Class,Section,DSA FROM A_section WHERE DSA = (SELECT MAX(DSA) FROM A_section) UNION SELECT Name,USN,Class,Section,DSA FROM B_section WHERE DSA = (SELECT MAX(DSA) FROM B_section) UNION SELECT Name,USN,Class,Section,DSA FROM C_section WHERE DSA = (SELECT MAX(DSA) FROM C_section))s ORDER BY DSA DESC LIMIT 1 ")
  print("\n The Topper Of the DSA is :\n")
  field_names = [i[0] for i in mycursor.description]
  print(field_names)
  a = mycursor.fetchall()
  for x in a:
    print(x)

def os_top():
  mycursor.execute("Select Name,USN,Class,Section,OS FROM (SELECT Name,USN,Class,Section,OS FROM A_section WHERE OS = (SELECT MAX(OS) FROM A_section) UNION SELECT Name,USN,Class,Section,OS FROM B_section WHERE OS = (SELECT MAX(OS) FROM B_section) UNION SELECT Name,USN,Class,Section,OS FROM C_section WHERE OS = (SELECT MAX(OS) FROM C_section))s ORDER BY OS DESC LIMIT 1 ")
  print("\n The Topper Of the OS is :\n")
  field_names = [i[0] for i in mycursor.description]
  print(field_names)
  a = mycursor.fetchall()
  for x in a:
    print(x)

def se_top():
  mycursor.execute("Select Name,USN,Class,Section,SE FROM (SELECT Name,USN,Class,Section,SE FROM A_section WHERE SE = (SELECT MAX(SE) FROM A_section) UNION SELECT Name,USN,Class,Section,SE FROM B_section WHERE SE = (SELECT MAX(SE) FROM B_section) UNION SELECT Name,USN,Class,Section,SE FROM C_section WHERE SE = (SELECT MAX(SE) FROM C_section))s ORDER BY SE DESC LIMIT 1 ")
  print("\n The Topper Of the SE is :\n")
  field_names = [i[0] for i in mycursor.description]
  print(field_names)
  a = mycursor.fetchall()
  for x in a:
    print(x)    

def update_A_sectionName(Name,USN):
  sql = "UPDATE A_section set Name=%s WHERE USN=%s"
  adr = (Name,USN,)
  mycursor.execute(sql,adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

def update_B_sectionName(Name,USN):
  sql = "UPDATE B_section set Name=%s WHERE USN = %s"
  adr = (Name,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

def update_C_sectionName(Name,USN):
  sql ="UPDATE C_section set Name = %s where USN=%s "
  adr = (Name,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

def update_A_sectionUSN(USN,Name):
  sql = "UPDATE A_section set USN = %s where Name=%s"
  adr = (USN,Name,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

def update_B_sectionUSN(USN,Name):
  sql = "UPDATE B_section set USN = %s where Name=%s"
  adr = (USN,Name,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

def update_C_sectionUSN(USN,Name):
  sql = "UPDATE C_section set USN = %s where Name=%s"
  adr = (USN,Name,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

def update_A_sectionClass(Class,USN):
  sql = "UPDATE A_section set Class = %s  where USN=%s"
  adr = (Class,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

def update_B_sectionClass(Class,USN):
  sql = "UPDATE B_section set Class = %s where USN=%s"
  adr = (Class,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

def update_C_sectionClass(Class,USN):
  sql = "UPDATE C_section set Class = %s where USN =%s"
  adr = (Class,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

def update_A_sectionSection(Section,USN):
  sql = "UPDATE A_section set Section = %s where USN =%s"
  adr = (Section,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")
def update_B_sectionSection(Section,USN):
  sql = "UPDATE B_section set Section = %s where  USN =%s"
  adr = (Section,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

def update_C_sectionSection(Section,USN):
  sql = "UPDATE C_section SET Section = %s where USN=%s"
  adr = (Section,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

def update_A_sectionDBMS(DBMS,USN):
  sql = "UPDATE A_section SET DBMS = %s where USN=%s"
  adr = (DBMS,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

def update_B_sectionDBMS(DBMS,USN):
  sql = "UPDATE B_section SET DBMS = %s where USN=%s"
  adr = (DBMS,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

def update_C_sectionDBMS(DBMS,USN):
  sql = "UPDATE C_section set DBMS = %s where USN=%s"
  adr = (DBMS,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")


def update_A_sectionADA(ADA,USN):
  sql = "UPDATE A_section set ADA = %s where USN=%s"
  adr = (ADA,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")
def update_B_sectionADA(ADA,USN):
  sql = "UPDATE B_section set ADA = %s where USN=%s"
  adr = (ADA,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

  
def update_C_sectionADA(ADA,USN):
  sql = "UPDATE C_section set ADA = %s where USN=%s"
  adr = (ADA,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")


def update_A_sectionOOPS(OOPS,USN):
  sql = "UPDATE A_section set OOPS = %s where USN=%s"
  adr = (OOPS,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")
def update_B_sectionOOPS(OOPS,USN):
  sql = "UPDATE B_section set OOPS = %s where USN=%s"
  adr = (OOPS,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")
def update_C_sectionOOPS(OOPS,USN):
  sql = "UPDATE C_section set OOPS = %s where USN=%s"
  adr = (OOPS,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")


def update_A_sectionDSA(DSA,USN):
  sql = "UPDATE A_section set DSA = %s where USN=%s"
  adr = (DSA,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")
def update_B_sectionDSA(DSA,USN):
  sql = "UPDATE B_section set DSA = %s where USN=%s"
  adr = (DSA,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

def update_C_sectionDSA(DSA,USN):
  sql = "UPDATE C_section set DSA = %s where USN=%s"
  adr = (DSA,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

def update_A_sectionOS(OS,USN):
  sql = "UPDATE A_section set OS = %s where USN =%s"
  adr = (OS,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

def update_B_sectionOS(OS,USN):
  sql = "UPDATE B_section set OS = %s where USN =%s"
  adr = (OS,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

def update_C_sectionOS(OS,USN):
  sql = "UPDATE C_section set OS = %s where USN =%s"
  adr = (OS,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

def update_A_sectionSE(SE,USN):
  sql = "UPDATE A_section set SE = %s where USN=%s"
  adr = (SE,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

def update_B_sectionSE(SE,USN):
  sql = "UPDATE B_section set SE = %s where USN=%s"
  adr = (SE,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")


def update_C_sectionSE(SE,USN):
  sql = "UPDATE C_section set SE = %s where USN=%s"
  adr = (SE,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

def update_Average_A(Average,USN):
  sql = "UPDATE A_section set Average = %s where USN=%s"
  adr = (Average,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

def update_Average_B(Average,USN):
  sql = "UPDATE B_section set Average = %s where USN=%s"
  adr = (Average,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

def update_Average_C(Average,USN):
  sql = "UPDATE C_section set Average = %s where USN=%s"
  adr = (Average,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

def update_Grade_A(Grade,USN):
  sql = "UPDATE A_section set Grade = %s where USN=%s"
  adr = (Grade,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

def update_Grade_B(Grade,USN):
  sql = "UPDATE B_section set Grade = %s where USN=%s"
  adr = (Grade,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

def update_Grade_C(Grade,USN):
  sql = "UPDATE C_section set Grade = %s where USN=%s"
  adr = (Grade,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

def update_A_sectionSGPA(SGPA,USN):
  sql = "UPDATE A_section set SGPA=%s where USN=%s"
  adr = (SGPA,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")
  
def update_B_sectionSGPA(SGPA,USN):
  sql = "UPDATE B_section set SGPA=%s where USN=%s"
  adr = (SGPA,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")

def update_C_sectionSGPA(SGPA,USN):
  sql = "UPDATE C_section set SGPA=%s where USN=%s"
  adr = (SGPA,USN,)
  mycursor.execute(sql, adr)
  mydb.commit()
  print(mycursor.rowcount, "record(s) updated")


