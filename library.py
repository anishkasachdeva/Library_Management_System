import subprocess as sp
import pymysql
import pymysql.cursors
from tabulate import tabulate


#add books me print statement ke database updated

def view_table(rows):

    a = []
    try:
        a.append(list(rows[0].keys()))
    except:
        print("\n-----------------\nEMPTY TABLE\n-----------------\n")   
        return
    for row in rows:
        b = []
        for k in row.keys():
            b.append(row[k])
        a.append(b)
    print(tabulate(a, tablefmt="psql", headers="firstrow"))
    print()
    return






def show_tables():
    print("Choose a VIEW option\n\n")
    print("1.  STUDENT_INFORMATION")
    print("2.  BRANCH_INFORMATION")
    print("3.  EMPLOYEE_INFORMATION")
    print("4.  MAINTAINER_INFORMATION")
    print("5.  BOOK_INFORMATION")
    print("6.  CONTACT_INFORMATION")
    print("7.  AUTHORIZATION_SYSTEM")
    print("8.  PARENT_INFORMATION")
    print("9.  COPIES_IN")
    print("10. ISSUE")
    print("11. RETURN")
    print("12. Return from function")
    print("\n\n")
    n = input()

    if n == '1':
        query = "SELECT * FROM STUDENT_INFORMATION;"
    elif n == '2':
        query = "SELECT * FROM BRANCH_INFORMATION;"
    elif n == '3':
        query = "SELECT * FROM EMPLOYEE_INFORMATION;"
    elif n == '4':
        query = "SELECT * FROM MAINTAINER_INFORMATION;"
    elif n == '5':
        query = "SELECT * FROM BOOK_INFORMATION;"
    elif n == '6':
        query = "SELECT * FROM CONTACT_INFORMATION;"
    elif n == '7':
        query = "SELECT * FROM AUTHORIZATION_SYSTEM;"
    elif n == '8':
        query = "SELECT * FROM PARENT_INFORMATION;"
    elif n == '9':
        query = "SELECT * FROM COPIES_IN;"
    elif n == '10':
        query = "SELECT * FROM ISSUE;"
    elif n == '11':
        query = "SELECT * FROM LIBRARY.RETURN;"
    elif n == '12':
        return

    try:
        # print("try hua\n")
        cur.execute(query)
    except Exception as e:
        # print("excepts hua\n")
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return

    rows = cur.fetchall()
    view_table(rows)
    con.commit()





def addBook(): #leave for now
    try:
        row = {}
        print("Enter new book's details: ")
        row["BookTitle"] = input("Book Title ")
        row["BookID"] = input("Book ID ")
        row["Author"] = input("Author ")
        
        flag = 1
        query = "SELECT * FROM BOOK_INFORMATION WHERE BookTitle = '%s' AND BookID = '%s' AND Author = '%s'" % (row["BookTitle"], row["BookID"],row["Author"])
        cur.execute(query)
        x1 = cur.fetchone()
        con.commit()

        if x1 == None:
            query = "SELECT * FROM BOOK_INFORMATION WHERE BookID = '%s'" % (row["BookID"])
            cur.execute(query)
            x2 = cur.fetchone()
            con.commit()

            if x2 == None:

                query = "INSERT INTO BOOK_INFORMATION(BookID, BookTitle, Author) VALUES('%s', '%s', '%s')" % (row["BookID"], row["BookTitle"], row["Author"])
                cur.execute(query)
                con.commit()
                row["BranchID"] = input("Branch ID ")
                No_of_copies = int(input("No_of_copies "))
                while(No_of_copies <= 0):
                    print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
                    No_of_copies = int(input("No_of_copies "))
                
                query = "INSERT INTO COPIES_IN(BookID, BranchID, TotalCopies, AvailableCopies) VALUES('%s', '%s', '%d', '%d')" % (row["BookID"], row["BranchID"],No_of_copies,No_of_copies)
                cur.execute(query)
                con.commit()

            else:
                print("\n\nIncorrect Data: PLEASE TRY AGAIN WITH CORRECT DATA!\n")
                flag = 0

        else:
            row["BranchID"] = input("Branch ID ")
            No_of_copies = int(input("No_of_copies "))
            while(No_of_copies <= 0):
                print("\n\nError: PLEASE enter a positive no\n")
                No_of_copies = int(input("No_of_copies "))
            query = "SELECT * FROM COPIES_IN WHERE BookID = '%s' AND BranchID = '%s'" % (row["BookID"], row["BranchID"])
            cur.execute(query)
            x3 = cur.fetchone()
            con.commit()
            if x3 == None:
                query = "INSERT INTO COPIES_IN(BookID, BranchID, TotalCopies, AvailableCopies) VALUES('%s', '%s', '%d', '%d')" % (row["BookID"], row["BranchID"],No_of_copies,No_of_copies)
                cur.execute(query)
                con.commit()
                

            else:
                query = "UPDATE COPIES_IN SET AvailableCopies = AvailableCopies + %d,TotalCopies = TotalCopies +  %d WHERE BookID='%s' AND BranchID='%s'" % ( No_of_copies,No_of_copies,row["BookID"],row["BranchID"])
                cur.execute(query)
                con.commit()   

        # #row_count = cur.rowcount
        # if row_count == 0:
        #     query = "INSERT INTO BOOK_INFORMATION(BookID, BookTitle, Author) VALUES('%s', '%s', '%s')" %(row["BookID"], row["BookTitle"], row["Author"])
        #     print(query)
        #     cur.execute(query)
        #     con.commit()
        #     print("Inserted Into Database")
        # else:
        #     print("Book with the given Book ID already exists")
        # query = "SELECT COUNT(*) FROM COPIES_IN WHERE Book ID = %s and BranchID = %s"
        # cur.execute(query, (row["BookID"], row["BranchID"], ))
        # row_count = cur.row_count
        # if row_count == 0:
        #     query = "INSERT INTO COPIES_IN(BookID, BranchID, TotalCopies, AvailableCopies) VALUES('%s', '%s', 1, 1)" %(row["BookID"], row["BranchID"])
        #     print(query)
        #     cur.execute(query)
        #     con.commit()
        #     print("Inserted Into Database")
        # else:

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)

    return



def Issue():
    try:
        row = {}
        print("Enter book's details for issuing: ")
        row["BookID"] = input("Book ID ")
        row["RollNumber"] = input("Student RollNumber ")
        row["BranchID"] = input("Branch ID ")
        row["StaffID"] = input("Staff ID ")
        row["IssueTime"] = input("Issue Time ")


        query = "SELECT * FROM ISSUE WHERE BookID='%s' AND RollNumber='%s' AND BranchID='%s' AND StaffID='%s' AND IssueTime='%s'" % ( row["BookID"],row["RollNumber"],row["BranchID"],row["StaffID"], row["IssueTime"])
        cur.execute(query)
        x = cur.fetchone()
        con.commit()

        print(1)
        if x and x["BookID"] == row["BookID"] and x["RollNumber"] == row["RollNumber"] and x["BranchID"] == row["BranchID"] and x["StaffID"] == row["StaffID"] and x["IssueTime"] == row["IssueTime"]:
            print("\n\nDuplicate data\n")
        else:
            query = "SELECT BranchID,StaffID FROM EMPLOYEE_INFORMATION WHERE BranchID = '%s' AND StaffID = '%s'" % (row["BranchID"], row["StaffID"])
            cur.execute(query)
            x1 = cur.fetchone()
            con.commit() 

            print(2)

            if x1 == None:
                print("\n\nIncorrect Data: PLEASE TRY AGAIN WITH CORRECT DATA!\n")
            else:
                query = "SELECT BranchID,BookID FROM COPIES_IN WHERE BranchID = '%s' AND BookID = '%s'" % (row["BranchID"], row["BookID"])
                cur.execute(query)
                x2 = cur.fetchone()
                con.commit()

                print(3)

                if x2 == None:
                    print("\n\nIncorrect Data: PLEASE TRY AGAIN WITH CORRECT DATA!\n")
                else:
                    query = "SELECT AvailableCopies FROM COPIES_IN WHERE BranchID = '%s' AND BookID = '%s'" % (row["BranchID"], row["BookID"])
                    cur.execute(query)
                    x3 = cur.fetchone()
                    con.commit()

                    print(4, x3)
                    if x3["AvailableCopies"] == 0:
                        print("\n\nBOOK NOT AVAILABLE\n")
                    else:
                        query = "UPDATE COPIES_IN SET AvailableCopies=AvailableCopies-1 WHERE BookID='%s' AND BranchID='%s'" % (row["BookID"],row["BranchID"])
                        cur.execute(query)
                        con.commit()

                        print(row)
                        query = "INSERT INTO ISSUE(RollNumber, StaffID, BranchID, BookID, IssueTime) VALUES('%s', '%s', '%s', '%s', '%s')" %(row["RollNumber"], row["StaffID"], row["BranchID"], row["BookID"], str(row["IssueTime"]))
                        print(query)
                        cur.execute(query)

    
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)

    return

from datetime import datetime

def getDuration(then, now = datetime.now(), interval = "default"):

    # Returns a duration as specified by variable interval
    # Functions, except totalDuration, returns [quotient, remainder]

    duration = now - then # For build-in functions
    duration_in_s = duration.total_seconds()

    def years():
        return divmod(duration_in_s, 31556926) # Seconds in a year=31556926.

    def days(seconds = None):
        return divmod(seconds or duration_in_s, 86400) # Seconds in a day = 86400

    def hours(seconds = None):
        return divmod(seconds or duration_in_s, 3600) # Seconds in an hour = 3600

    def minutes(seconds = None):
        return divmod(seconds or duration_in_s, 60) # Seconds in a minute = 60

    def seconds(seconds = None):
        if seconds:
            return divmod(seconds, 1)
        return duration_in_s

    def totalDuration():
        y = years()
        d = days(y[1]) # Use remainder to calculate next variable
        h = hours(d[1])
        m = minutes(h[1])
        s = seconds(m[1])

        return "Time between dates: {} years, {} days, {} hours, {} minutes and {} seconds".format(int(y[0]), int(d[0]), int(h[0]), int(m[0]), int(s[0]))

    return int(days()[0])

def getFine(returnt, issue):
    # then = datetime.strptime(issue, "%Y-%m-%d %H:%M:%S")
    then = issue
    now = datetime.strptime(returnt, "%Y-%m-%d %H:%M:%S")

    fineperday = 2
    return max(getDuration(then, now, "days") - 10, 0) * fineperday


def Return():
    try:
        print("Enter book's details for returning: ")
        row = {}
        row["BookID"] = input("Book ID ")
        row["RollNumber"] = input("Student RollNumber ")
        row["BranchID"] = input("Branch ID ")
        row["StaffID"] = input("Staff ID ")
        row["ReturnTime"] = input("Return Time ")
        
        query = "SELECT * FROM LIBRARY.RETURN WHERE BookID='%s' AND RollNumber='%s' AND BranchID='%s' AND StaffID='%s' AND ReturnTime='%s'" % ( row["BookID"],row["RollNumber"],row["BranchID"],row["StaffID"], row["ReturnTime"])
        cur.execute(query)
        x = cur.fetchone()
        con.commit()

        if x and x["BookID"] == row["BookID"] and x["RollNumber"] == row["RollNumber"] and x["BranchID"] == row["BranchID"] and x["StaffID"] == row["StaffID"] and x["IssueTime"] == row["ReturnTime"]:
            print("\n\nDuplicate data\n")
        else:
            query = "SELECT BranchID,StaffID FROM EMPLOYEE_INFORMATION WHERE BranchID = '%s' AND StaffID = '%s'" % (row["BranchID"], row["StaffID"])
            cur.execute(query)
            x1 = cur.fetchone()
            con.commit() 

            if x1 == None:
                print("\n\nIncorrect Data(emloyee not in that branch): PLEASE TRY AGAIN WITH CORRECT DATA!\n")
            else:
                query = "SELECT BranchID,BookID FROM COPIES_IN WHERE BranchID = '%s' AND BookID = '%s'" % (row["BranchID"], row["BookID"])
                cur.execute(query)
                x2 = cur.fetchone()
                con.commit()

                if x2 == None:
                    print("\n\nIncorrect Data(book not in branch): PLEASE TRY AGAIN WITH CORRECT DATA!\n")
                else:
                    query = "SELECT COUNT(*) as c2 FROM ISSUE WHERE BookID='%s' AND RollNumber='%s' AND BranchID='%s'" %  (row["BookID"],row["RollNumber"],row["BranchID"])
                    cur.execute(query)
                    x3 = cur.fetchone()
                    con.commit()
                    query = "SELECT COUNT(*) as c1 FROM LIBRARY.RETURN WHERE BookID='%s' AND RollNumber='%s' AND BranchID='%s'" %  (row["BookID"],row["RollNumber"],row["BranchID"])
                    cur.execute(query)
                    x4 = cur.fetchone()
                    con.commit()
                    query = "SELECT AvailableCopies FROM COPIES_IN WHERE BranchID = '%s' AND BookID = '%s'" % (row["BranchID"], row["BookID"])
                    cur.execute(query)
                    x5 = cur.fetchone()
                    con.commit()

                    query = "SELECT IssueTime FROM ISSUE WHERE BranchID = '" + row["BranchID"] + "' AND BookID = '" + row["BookID"] + "' AND RollNumber = '" + row["RollNumber"] + "' ORDER BY IssueTime DESC LIMIT 1;"
                    
                    print(x3, x4)
                    if(x3["c2"]>x4["c1"]):
                        cur.execute(query)
                        x6 = cur.fetchone()
                        issuetime = x6["IssueTime"]

                        print(x6, row)
                        fine = getFine(row["ReturnTime"], issuetime)

                        query = "UPDATE COPIES_IN SET AvailableCopies=AvailableCopies+1 WHERE BookID='%s' AND BranchID='%s'" % (row["BookID"],row["BranchID"])
                        print(query)
                        cur.execute(query)
                        con.commit()

                        query = "INSERT INTO LIBRARY.RETURN(RollNumber, StaffID, BranchID, BookID, ReturnTime) VALUES('%s', '%s', '%s', '%s', '%s')" %(row["RollNumber"], row["StaffID"], row["BranchID"], row["BookID"], row["ReturnTime"])
                        cur.execute(query)
                        con.commit()

                        print("Your fine is ", fine)
                    else:
                        print("\n\ninvalid return request\n")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)

    return





def addEmployee(): #StaffID should not be equal to StaffID of maintainer
    try:
        row = {}
        print("Enter new employee's details: ")
        row["Name"] = input("Name ")
        row["StaffID"] = input("StaffID ")
        row["BranchID"] = input("BranchID ")
        row["Username"] = input("Username ")
        row["Password"] = input("Password ")

        query = "SELECT StaffID FROM MAINTAINER_INFORMATION WHERE StaffID='%s'" % (row["StaffID"])
        cur.execute(query)
        x = cur.fetchone()
        con.commit()
        if x==None:
            query = "INSERT INTO EMPLOYEE_INFORMATION(Name, StaffID, BranchID) VALUES('%s', '%s', '%s')" %(row["Name"], row["StaffID"], row["BranchID"])

            cur.execute(query)
            con.commit()

            query = "INSERT INTO AUTHORIZATION_SYSTEM(EmployeeID, Username, Password) VALUES('%s', '%s', '%s')" %(row["StaffID"], row["Username"], row["Password"])
            cur.execute(query)
            con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)

    return


def addStudent():
    try:
        row = {}
        print("Enter new student's details: ")
        row["FirstName"] = input("First Name ")
        row["LastName"] = input("Last Name ")
        row["EmailID"] = input("EmailID ")
        row["RollNumber"] = input("Roll Number ")

        query = "INSERT INTO STUDENT_INFORMATION(FirstName, LastName, EmailID, RollNumber) VALUES('%s', '%s', '%s', '%s')" %(row["FirstName"], row["LastName"], row["EmailID"], row["RollNumber"])

        # print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)

    return

def addBranch():
    try:
        row = {}
        print("Enter branch's details: ")
        row["BranchID"] = input("BranchID ")
        row["Address"] = input("Address ")

        query = "INSERT INTO BRANCH_INFORMATION(BranchID, Address) VALUES('%s', '%s')" %(row["BranchID"], row["Address"])

        # print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)

    return

def addMaintainer():
    try:
        row = {}
        print("Enter maintainer's details: ")
        row["Name"] = input("Name ")
        row["StaffID"] = input("Staff ID ")
        query = "SELECT StaffID FROM EMPLOYEE_INFORMATION WHERE StaffID='%s'" % (row["StaffID"])
        cur.execute(query)
        x = cur.fetchone()
        con.commit()
        if x==None:
            query = "INSERT INTO MAINTAINER_INFORMATION(Name, StaffID) VALUES('%s', '%s')" %(row["Name"], row["StaffID"])
            cur.execute(query)
            con.commit()
            print("Inserted Into Database")
        else:
            print("\n\nInvalid staff ID\n");

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)

    return

def addContact():
    try:
        row = {}
        print("Enter contact details: ")
        row["RollNumber"] = input("Roll Number ")
        row["ContactNumber"] = input("Contact Number ")

        query = "INSERT INTO CONTACT_INFORMATION(RollNumber, ContactNumber) VALUES('%s', '%s')" %(row["RollNumber"], row["ContactNumber"])

        # print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)

    return

def addParent():
    try:
        row = {}
        print("Enter parent's details: ")
        row["SRollNumber"] = input("Roll Number ")
        row["ContactNumber"] = input("Contact Number ")
        row["Name"] = input("Name ")
        row["Gender"] = input("Gender ")
        if row["Gender"]=='M' or row["Gender"]=='F':
            query = "INSERT INTO PARENT_INFORMATION(SRollNumber, ContactNumber, Name, Gender) VALUES('%s', '%s', '%s', '%s')" %(row["SRollNumber"], row["ContactNumber"], row["Name"], row["Gender"])

        # print(query)
            cur.execute(query)
            con.commit()
            print("Inserted Into Database")
        else:
            print("wrong gender")

       

        

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)

    return

# def removeBook(BookID):
#
#     query = "DELETE FROM BOOK_INFORMATION WHERE BookID = %s"# + BookID
#
#     try:
#         cur.execute(query, (BookID, ))
#         con.commit()
#
#     except Error as error:
#         print(error)

# def removeStudent():

#     RollNumber = input("Roll Number ")
#     query = "DELETE FROM STUDENT_INFORMATION WHERE RollNumber = %s"

#     try:
#         cur.execute(query, (RollNumber, ))
#         con.commit()

#     except Error as error:
#         print(error)

# def removeEmployee():

#     EmployeeID = input("Employee ID ")
#     query = "DELETE FROM EMPLOYEE_INFORMATION WHERE EmployeeID = %s" %

#     try:
#         cur.execute(query, (EmployeeID, ))
#         con.commit()

#     except Error as error:
#         print(error)

def removeMaintainer():

    StaffID = input("Staff ID ")
    query = "DELETE FROM MAINTAINER_INFORMATION WHERE StaffID = %s"

    try:
        cur.execute(query, (StaffID, ))
        con.commit()

    except Exception as error:
        print(error)

# def removeBranch():

#     BranchID = input("Branch ID ")
#     query = "DELETE FROM BRANCH_INFORMATION WHERE BranchID = %s"

#     try:
#         cur.execute(query, (BranchID, ))
#         con.commit()

#     except Error as error:
#         print(error)

def removeBranch():
    tables = ["COPIES_IN", "EMPLOYEE_INFORMATION","MAINTAINER_INFORMATION", "ISSUE", "RETURN", "BRANCH_INFORMATION"]
    branchID = input("BranchID ")

    for table in tables:
        query = "DELETE FROM " + table + " WHERE BranchID = '" + branchID + "'"
        try:
            cur.execute(query)
            con.commit()
        except Exception as e:
            con.rollback()
            print(e)
    
    print("Branch removed succesfully")

def functionone():
    bid = input("Book ID to search for")
    query = "SELECT COUNT(*) as cnt FROM ISSUE WHERE BookID = '" + bid + "'"
    
    try:
        cur.execute(query)
        res = cur.fetchall()
        con.commit()
    except Exception as e:
        print(e)

    view_table(res)

def functiontwo():
    bidq =  "select max(cnt) as c from (select COUNT(BookID) as cnt from ISSUE group by BookID) as x"
    cur.execute(bidq)
    bid = cur.fetchone()["c"]
    print(bid)
    # select bookid form issue where count(bookid) = (select max(count(*)) from issue group by bookid)
    query = "SELECT BookID FROM ISSUE group by BookID HAVING count(BookID) = '" + str(bid) + "'"

    try:
        cur.execute(query)
        res = cur.fetchone()
        bid = res["BookID"]
        q2 = "SELECT BookTitle from BOOK_INFORMATION WHERE BookID = '" + bid + "'"
        cur.execute(q2)
        res = cur.fetchone()
        print("Most issued book is " + res["BookTitle"])
        con.commit()
    except Exception as e:
        print(e)

def functionthird():
    bidq =  "select max(cnt) as c from (select COUNT(RollNumber) as cnt from ISSUE group by RollNumber) as x"
    cur.execute(bidq)
    bid = cur.fetchone()["c"]
    print(bid)

    query = "SELECT RollNumber FROM ISSUE group by RollNumber having count(RollNumber) = '" + str(bid) + "'"
    
    try:
        cur.execute(query)
        res = cur.fetchone()["RollNumber"]
        print(res)
        bid = res
        q2 = "SELECT CONCAT(FirstName, ' ', LastName) as x from STUDENT_INFORMATION WHERE RollNumber = '" + bid + "'"
        cur.execute(q2)
        res = cur.fetchone()
        print("Most active student is " + res["x"])
        con.commit()
    except Exception as e:
        print(e)


def functionfour():
    rn = input("Enter rollnumber")
    query = "SELECT COUNT(*) as cnt FROM ISSUE WHERE RollNumber = '" + rn + "'"

    try:
        cur.execute(query)
        res = cur.fetchone()
        bid = res["cnt"]
        print("Books issues by this student is " + str(bid))
        con.commit()
    except Exception as e:
        print(e)

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch==1):
        show_tables()
    elif(ch == 2):
       addBook()
    elif(ch == 3):
        removeBranch()
    elif(ch == 4):
        addStudent()
    elif(ch==5):
        Issue()
    elif(ch==6):
        Return()
    elif(ch==7):
        functionone()
    elif(ch==8):
        functiontwo()
    elif(ch==9):
        functionthird()
    elif(ch==10):
        functionfour()
    elif(ch==11):
        addEmployee()
    elif(ch==12):
        addMaintainer()
    elif(ch==13):
        addBranch()
    elif(ch==14):
        addParent()
    elif(ch==15):
        addContact()
    # elif(ch == 4):
    #     RollNumber = input("Roll Number ")
    #     removeStudent(RollNumber)
    # elif(ch == 5):
    #     addEmployee()
    # elif(ch == 6):
    #     EmployeeID = input("Employee ID")
    #     removeEmployee(EmployeeID)
    else:
        print("Error: Invalid Option")

# Global
while(1):
    tmp = sp.call('clear',shell=True)
    username = "mysql" # input("Username: ")
    password = "mysql" # input("Password: ")

    try:
        con = pymysql.connect(host='localhost',
                user=username,
                password=password,
                db='LIBRARY',
                cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear',shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")
        tmp = input("Enter any key to CONTINUE>")
    
    except Exception as e:
        print(e)
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
        continue

    with con:
        flag=0
        cur = con.cursor()
        while(1):
            tmp = sp.call('clear',shell=True)
            print("0. Logout")
            print("1. Show Tables")
            print("2. Add book")
            print("3. Remove branch")
            print("4. Add student")
            print("5. Issue a Book")
            print("6. Return a Book")
            print("7. Select count of issues for given book")
            print("8. Select book which was issued the max times")
            print("9. Select student which issued the max books")
            print("10. Return number of books issued by given student")
            print("11. Add employee")
            print("12. Add maintainer")
            print("13. Add branch")
            print("14. Add parent")
            print("15. Add student contact")
            
            # print("4. Remove student")
            # print("5. Add employee")
            # print("6. Remove employee")
            
            ch = int(input("Enter choice> "))
            # while ch == NULL :
            #     ch = int(input("Enter choice> "))
            tmp = sp.call('clear',shell=True)
            if ch==0:
                flag=1
                break
            else:
                dispatch(ch)
                tmp = input("Enter any key to CONTINUE>")
    if flag==1:
        break
