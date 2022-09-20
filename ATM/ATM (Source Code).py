import os
import mysql.connector

# DataBase Connection

mydb = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "",
    database = "atm"
)

# ************************************************************************************************************* #

# ATM Login & Registration Function

def AtmLoginRegister():

    print("\t\t\t\t\t\tWELCOME TO MK BANK")
    print("\t\t\t\t\t\t******************\n\n")

    print ("ENTER YOUR CHOICE")
    print ("*****************\n\n")

    print ("\nEnter 1 for Login...!")
    print ("Enter 2 for Create New Account...!\n")

    login_value = input("Enter your Choice : ")

    if(login_value == "1"):
        
        os.system('CLS')
        AtmLogin()

    elif (login_value == "2"):

        os.system('CLS')
        CreateNewAccount()

    else:

        os.system('CLS')
        print("Please Enter the Correct Choice...!\n\n\n")
        AtmLoginRegister()

# ************************************************************************************************************* #

# ATM Login Function

def AtmLogin():

    print ("\t\t\t\tWelcome to MK Bank ATM")
    print ("\t\t\t\t**********************\n\n\n")

    account_no = input("Enter Your Account Number: ")
    account_pin = input("Enter Your PIN: ")

    mycursor = mydb.cursor(buffered = True)

    sql_query = "select account_holder_name, account_pin from account_users where account_no = %s"
    mycursor.execute(sql_query, (account_no,))
    rowcount = mycursor.rowcount

    if (rowcount == 0):
        os.system('CLS')
        print("Account Not Founded. Please Create New Account...!\n\n")
        AtmLoginRegister()

    else:
        os.system('CLS')
        result = mycursor.fetchall()

        for i in result:
            
            account_holder_name = i[0]
            db_pin = i[1]

        if(account_pin == db_pin):

            os.system('CLS')
            AccountDashboard(account_no, account_holder_name)

        else:
            os.system('CLS')
            print("Invalid Account Number or PIN Number...!\n\n")
            AtmLogin()

# ************************************************************************************************************* #

# Amount Deposit Choose Check Function

def ChooseCheck(account_no, account_holder_name):
    
    print ("\n\nENTER YOUR CHOICE")
    print ("*****************\n\n")

    print("1 For BACK...!")
    print("2 For LOGOUT...!\n\n")

    choose = input("Enter Your Choice: ")

    if(choose == "1"):

        os.system('CLS')
        AccountDashboard(account_no, account_holder_name)
    
    elif(choose == "2"):

        os.system('CLS')
        Logout()

    else:

        os.system('CLS')
        print("Please Enter the Correct Choice...!\n\n")
        ChooseCheck(account_no, account_holder_name)

# ************************************************************************************************************* #

# Deposit Your Amount Function

def AmountDeposit(account_no, account_holder_name):

    print("\t\t\t\tDEPOSIT YOUR AMOUNT")
    print("\t\t\t\t*******************\n")
    
    mycursor = mydb.cursor(buffered = True)

    sql_query = "select account_balance from account_transactions where account_no = %s"
    mycursor.execute(sql_query, (account_no,))
    result = mycursor.fetchall()

    for i in result:
        for j in i:
            balance = j

    try:

        amount = float(input("Enter the Amount: "))

    except:

        os.system('CLS')
        print("Please Enter Correct Amount...!\n\n")
        AmountDeposit(account_no, account_holder_name)

    else:
        
        account_balance = balance + amount

        sql_query = "update account_transactions set account_balance = %s where account_no = %s"
        value = (account_balance, account_no)
        mycursor.execute(sql_query, value)

        mydb.commit()

        os.system('CLS')

        print("\t\t\t\tDEPOSIT YOUR AMOUNT")
        print("\t\t\t\t*******************\n")

        print("\nAmount Deposited Successfully...!\n\n")

        mycursor = mydb.cursor(buffered = True)

        sql_query = "select account_balance from account_transactions where account_no = %s"
        mycursor.execute(sql_query, (account_no,))
        result = mycursor.fetchall()

        for i in result:
            for j in i:
                print("\nACCOUNT BALANCE")
                print("***************\n")

                print("Your Account Balance: ",j)

        ChooseCheck(account_no, account_holder_name)

# ************************************************************************************************************* #

# Withdraw Your Amount Function

def AmountWithdraw(account_no, account_holder_name):

    print("\t\t\t\tWITHDRAW YOUR AMOUNT")
    print("\t\t\t\t********************\n")
    
    mycursor = mydb.cursor(buffered = True)

    sql_query = "select account_balance from account_transactions where account_no = %s"
    mycursor.execute(sql_query, (account_no,))
    result = mycursor.fetchall()

    for i in result:
        for j in i:
            balance = j

    try:

        amount = float(input("Enter the Amount: "))

    except:

        os.system('CLS')
        print("Please Enter Correct Amount...!\n\n")
        AmountWithdraw(account_no, account_holder_name)

    else:
        
        account_balance = balance - amount

        sql_query = "update account_transactions set account_balance = %s where account_no = %s"
        value = (account_balance, account_no)
        mycursor.execute(sql_query, value)

        mydb.commit()

        os.system('CLS')

        print("\t\t\t\tWITHDRAW YOUR AMOUNT")
        print("\t\t\t\t********************\n")

        print("\nAmount Withdraw Successfully...!\n\n")

        mycursor = mydb.cursor(buffered = True)

        sql_query = "select account_balance from account_transactions where account_no = %s"
        mycursor.execute(sql_query, (account_no,))
        result = mycursor.fetchall()

        for i in result:
            for j in i:
                print("\nACCOUNT BALANCE")
                print("***************\n")

                print("Your Account Balance: ",j)

        ChooseCheck(account_no, account_holder_name)

# ************************************************************************************************************* #

# Check Account Balance Function

def CheckAccountBalance(account_no, account_holder_name):

    print("\t\t\t\tCHECK ACCOUNT BALANCE")
    print("\t\t\t\t*********************\n")
    
    mycursor = mydb.cursor(buffered = True)

    sql_query = "select account_balance from account_transactions where account_no = %s"
    mycursor.execute(sql_query, (account_no,))
    result = mycursor.fetchall()

    for i in result:
        for j in i:
            print("\n\nYour Account Balance: ",j)

    
    print ("\n\nENTER YOUR CHOICE")
    print ("*****************\n\n")

    print("1 For BACK...!")
    print("2 For LOGOUT...!\n\n")

    choose = input("Enter Your Choice: ")

    if(choose == "1"):

        os.system('CLS')
        AccountDashboard(account_no, account_holder_name)
    
    elif(choose == "2"):

        os.system('CLS')
        Logout()

    else:

        os.system('CLS')
        print("Please Enter the Correct Choice...!\n\n")
        CheckAccountBalance(account_no, account_holder_name)

# ************************************************************************************************************* #

# Change Pin

def ChangeAccountPin(account_no, account_holder_name):

    print("\t\t\t\tCHANGE ACCOUNT PIN")
    print("\t\t\t\t******************\n")

    new_pin = input("Enter Your New PIN: ")

    mycursor = mydb.cursor(buffered = True)

    sql_query = "update account_users set account_pin = %s where account_no = %s"
    value = (new_pin, account_no)
    mycursor.execute(sql_query, value)

    mydb.commit()

    os.system('CLS')

    print("\t\t\t\tCHANGE ACCOUNT PIN")
    print("\t\t\t\t******************\n")

    print("\nAccount PIN Reseted Successfully...!\n\n")

    ChooseCheck(account_no, account_holder_name)

# ************************************************************************************************************* #

# Logout Function

def Logout():

    os.system('CLS')
    AtmLoginRegister()

# ************************************************************************************************************* #

# Account Dashboard Function

def AccountDashboard(acc_no, account_holder_name):
    
    account_no = acc_no

    print("\t\t\t\t\t\tWELCOME TO MK BANK")
    print("\t\t\t\t\t\t******************\n\n")

    print("Welcome ", account_holder_name, "\n\n")

    print ("ENTER YOUR CHOICE")
    print ("*****************\n\n")

    print("1 For Deposit Your Amount...!")
    print("2 For Withdraw Your Amount...!")
    print("3 For Check Account Balance...!")
    print("4 For Change Your Account PIN...!")
    print("5 For Logout...!\n\n")

    choose_value = input("Enter Your Choice: ")

    if(choose_value == "1"):
        
        os.system('CLS')
        AmountDeposit(account_no, account_holder_name)

    elif(choose_value == "2"):
        
        os.system('CLS')
        AmountWithdraw(account_no, account_holder_name)

    elif(choose_value == "3"):
        
        os.system('CLS')
        CheckAccountBalance(account_no, account_holder_name)

    elif(choose_value == "4"):
        
        os.system('CLS')
        ChangeAccountPin(account_no, account_holder_name)
    
    elif(choose_value == "5"):
        
        Logout()

    else:

        os.system('CLS')
        print("Please Enter the Correct Choice...!\n\n")
        AccountDashboard(account_no, account_holder_name)

# ************************************************************************************************************* #

# Create New Account Function

def CreateNewAccount():


    print("\t\t\t\t\t\tWELCOME TO MK BANK")
    print("\t\t\t\t\t\t******************\n\n")

    print("CREATE NEW ACCOUNT")
    print("******************\n")

    print("Note: Your Phone Number is Your Account Number...!\n\n")

    account_no = input("Enter Your Phone Number: ")
    account_holder_name = input("Enter Your Name : ")
    account_pin = input("Enter Your Account PIN Number: ")

    mycursor = mydb.cursor(buffered = True)

    sql_query = "select * from account_users where account_no = %s"
    mycursor.execute(sql_query, (account_no,))
    rowcount = mycursor.rowcount
        
    if (rowcount == 0):

        sql_query = "insert into account_users (account_no, account_holder_name, account_pin) values (%s, %s, %s)"
        value = (account_no, account_holder_name, account_pin)
        mycursor.execute(sql_query, value)

        sql_query = "insert into account_transactions (account_no) values (%s)"
        value = (account_no,)
        mycursor.execute(sql_query, value)

        mydb.commit()

        os.system('CLS')

        print("\nAccount Created Successfully...!\n")

        AtmLoginRegister()

    else:
           
        os.system('CLS')
        print("Phone Number is Already Taken...!\n")
        
        CreateNewAccount()

# ************************************************************************************************************* #

os.system('CLS')

AtmLoginRegister()