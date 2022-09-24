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

# Create New Account

def CreateNewAccount():

    print("\t\t\t\tWELCOME TO MK BANK")
    print("\t\t\t\t******************\n\n")

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

        mydb.commit()

        os.system('CLS')

        print("\nAccount Created Successfully...!\n")

        Index()

    else:
           
        os.system('CLS')
        print("Phone Number is Already Taken...!\n")
        
        CreateNewAccount()

# ************************************************************************************************************* #

# Login

def Login():

    print ("\t\t\t\tWelcome to MK Bank ATM")
    print ("\t\t\t\t**********************\n")

    print("LOGIN TO YOUR ACCOUNT")
    print("*********************\n")

    account_no = input("Enter Your Account Number: ")
    account_pin = input("Enter Your PIN: ")

    mycursor = mydb.cursor(buffered = True)

    sql_query = "select account_holder_name, account_pin from account_users where account_no = %s"
    mycursor.execute(sql_query, (account_no,))
    rowcount = mycursor.rowcount

    if (rowcount == 0):
        os.system('CLS')
        print("Account Not Founded. Please Create New Account...!\n\n")
        Index()

    else:
        os.system('CLS')
        result = mycursor.fetchall()

        for i in result:
            
            account_holder_name = i[0]
            db_pin = i[1]

        if(account_pin == db_pin):

            os.system('CLS')
            Dashboard(account_no, account_holder_name)

        else:
            os.system('CLS')
            print("Invalid Account Number or PIN Number...!\n\n")
            Login()

# ************************************************************************************************************* #

# Deposit

def Deposit(account_no, account_holder_name):

    print("\t\t\t\tWELCOME TO MK BANK")
    print("\t\t\t\t******************\n\n")

    print("DEPOSIT YOUR AMOUNT")
    print("*******************\n\n")

    try:

        amount = float(input("Enter the Amount: "))

    except:

        os.system('CLS')
        print("Please Enter Correct Amount...!\n\n")
        Deposit(account_no, account_holder_name)

    else:

        import datetime
        datetime = datetime.datetime.now()
        date_time = datetime.strftime("%d-%m-%Y %I:%M:%S %p")

        transactions_type = "Deposit"
        
        mycursor = mydb.cursor(buffered = True)
        sql_query = "insert into account_transactions_history (account_no, transactions_date_time, transactions_type, transactions_amount) values (%s, %s, %s, %s)"
        value = (account_no, date_time, transactions_type, amount)
        mycursor.execute(sql_query, value)

        mydb.commit()

        os.system('CLS')

        print("\nAmount Deposited Successfully...!\n\n")

        Dashboard(account_no, account_holder_name)

# ************************************************************************************************************* #

# Withdrawal

def Withdrawal(account_no, account_holder_name):

    print("\t\t\t\tWELCOME TO MK BANK")
    print("\t\t\t\t******************\n\n")

    print("WITHDRAWAL YOUR AMOUNT")
    print("**********************\n\n")

    try:

        amount = float(input("Enter the Amount: "))

    except:

        os.system('CLS')
        print("Please Enter Correct Amount...!\n\n")
        Deposit(account_no, account_holder_name)

    else:

        mycursor = mydb.cursor(buffered = True)

        sql_query = "select transactions_type, transactions_amount from account_transactions_history where account_no = %s"
        value = (account_no,)
        mycursor.execute(sql_query, value)
        result = mycursor.fetchall()

        d_count = 0
        w_count = 0

        for i in result:
            
            transaction_type = i[0]

            if(transaction_type == "Deposit"):

                deposit_amount = i[1]
                d_count = d_count + deposit_amount

            else:
                
                withdrawal_amount = i[1]
                w_count = w_count + withdrawal_amount

        balance_amount = d_count - w_count
        
        if(amount <= balance_amount):

            import datetime
            datetime = datetime.datetime.now()
            date_time = datetime.strftime("%d-%m-%Y %I:%M:%S %p")

            transactions_type = "Withdrawal"
        
            sql_query = "insert into account_transactions_history (account_no, transactions_date_time, transactions_type, transactions_amount) values (%s, %s, %s, %s)"
            value = (account_no, date_time, transactions_type, amount)
            mycursor.execute(sql_query, value)

            mydb.commit()

            os.system('CLS')

            print("\nAmount Withdrawn Successfully...!\n\n")

            Dashboard(account_no, account_holder_name)

        else:

            os.system('CLS')
            print("Do not have a Sufficient Account Balance to Withdrawal...!\n\n")
            
            Dashboard(account_no, account_holder_name)

# ************************************************************************************************************* #

# Statements

def Statements(account_no, account_holder_name):

    print("\t\t\t\t\tWELCOME TO MK BANK")
    print("\t\t\t\t\t******************\n\n")

    print("STATEMENTS OF TRANSACTIONS")
    print("**************************\n")

    mycursor = mydb.cursor(buffered = True)
    
    sql_query = "select transactions_date_time, transactions_type, transactions_amount from account_transactions_history where account_no = %s order by id"
    value = (account_no,)
    mycursor.execute(sql_query, value)
    result = mycursor.fetchall()

    print("""
        ********************************************************************************************
                   DATE                 DEPOSIT                WITHDRAWAL               BALANCE   
        ********************************************************************************************
    """)

    d_count = 0
    w_count = 0

    for i in result:

        transaction_type = i[1]

        if(transaction_type == "Deposit"):

            deposit_amount = i[2]
            d_count = d_count + deposit_amount

        else:
            deposit_amount = "--"

        if(transaction_type == "Withdrawal"):

            withdrawal_amount = i[2]
            w_count = w_count + withdrawal_amount

        else:
            withdrawal_amount = "--"

        balance_amount = d_count - w_count

        print("""\t  """,i[0],"""      """,deposit_amount,"""                   """,withdrawal_amount ,"""                  """,balance_amount,""" """)

    print("""
        ********************************************************************************************
    """)

    print ("ENTER YOUR CHOICE")
    print ("*****************\n")

    print("""
        ******************
        *                *
        *  1 --> Back    *
        *  2 --> Logout  *
        *                *
        ******************
    """)

    choice = input("Enter Your Choice: ")

    if(choice == "1"):
        
        os.system('CLS')
        Dashboard(account_no, account_holder_name)

    elif(choice == "2"):
        
        os.system('CLS')
        Index()

    else:

        print("Please Enter the Correct Choice...!\n\n")
        Statements(account_no, account_holder_name)

# ************************************************************************************************************* #

def Balance(account_no, account_holder_name):

    print("\t\t\t\tWELCOME TO MK BANK")
    print("\t\t\t\t******************\n\n")

    print ("ACCOUNT BALANCE")
    print ("***************\n")

    mycursor = mydb.cursor(buffered = True)

    sql_query = "select transactions_type, transactions_amount from account_transactions_history where account_no = %s"
    value = (account_no,)
    mycursor.execute(sql_query, value)
    result = mycursor.fetchall()

    d_count, w_count = 0, 0

    for i in result:
            
        # transaction_type = i[0]

        if(i[0] == "Deposit"):

            d_count = d_count + i[1]

        else:
                
            # withdrawal_amount = i[1]
            w_count = w_count + i[1]

    balance_amount = d_count - w_count

    print("Account Balance: ", balance_amount)

    print ("\n\nENTER YOUR CHOICE")
    print ("*****************\n")

    print("""
        ******************
        *                *
        *  1 --> Back    *
        *  2 --> Logout  *
        *                *
        ******************
    """)

    choice = input("Enter Your Choice: ")

    if(choice == "1"):
        
        os.system('CLS')
        Dashboard(account_no, account_holder_name)

    elif(choice == "2"):
        
        os.system('CLS')
        Index()

    else:

        print("Please Enter the Correct Choice...!\n\n")
        Balance(account_no, account_holder_name)

# ************************************************************************************************************* #

# Change Pin

def ChangePin(account_no, account_holder_name):

    print("\t\t\t\t\tWELCOME TO MK BANK")
    print("\t\t\t\t\t******************\n\n") 

    print("\t\t\t\tCHANGE ACCOUNT PIN")
    print("\t\t\t\t******************\n")

    new_pin = input("Enter Your New PIN: ")

    mycursor = mydb.cursor(buffered = True)

    sql_query = "update account_users set account_pin = %s where account_no = %s"
    value = (new_pin, account_no)
    mycursor.execute(sql_query, value)

    mydb.commit()

    os.system('CLS')

    print("\nAccount PIN Reseted Successfully...!\n\n")

    Dashboard(account_no, account_holder_name)
    
# ************************************************************************************************************* #

# Dashboard

def Dashboard(account_no, account_holder_name):
    
    print("\t\t\t\tWELCOME TO MK BANK")
    print("\t\t\t\t******************\n\n")

    print("Welcome ", account_holder_name, "\n\n")

    print ("ENTER YOUR CHOICE")
    print ("*****************\n")

    print("""
        **********************************
        *                                *
        *  1 --> Deposit Your Amount     *           
        *  2 --> Withdrawal Your Amount  *
        *  3 --> Account Statements      *
        *  4 --> Account Balance         *
        *  5 --> Change PIN              *
        *  6 --> Logout                  *
        *                                *
        **********************************
    """)

    choice = input("Enter Your Choice: ")

    if(choice == "1"):
        
        os.system('CLS')
        Deposit(account_no, account_holder_name)

    elif(choice == "2"):
        
        os.system('CLS')
        Withdrawal(account_no, account_holder_name)

    elif(choice == "3"):
        
        os.system('CLS')
        Statements(account_no, account_holder_name)

    elif(choice == "4"):
        
        os.system('CLS')
        Balance(account_no, account_holder_name)
    
    elif(choice == "5"):
        
        os.system('CLS')
        ChangePin(account_no, account_holder_name)

    elif(choice == "6"):
        
        os.system('CLS')
        Index()

    else:

        os.system('CLS')
        print("Please Enter the Correct Choice...!\n\n")
        Dashboard(account_no, account_holder_name)

# ************************************************************************************************************* #

# Index Function 

def Index():

    print("\t\t\t\tWELCOME TO MK BANK")
    print("\t\t\t\t******************\n\n")

    print ("ENTER YOUR CHOICE")
    print ("*****************\n")

    print("""
        ***************************
        *                         *
        * 1--> Login              *
        * 2--> Create New Account *
        *                         *
        ***************************\n
    """)

    choice = input("Enter Your Choice: ")

    if(choice == "1"):
        os.system("CLS")
        Login()

    elif(choice == "2"):
        os.system("CLS")
        CreateNewAccount()

    else:

        os.system("CLS")
        print("Invalid Choice. Please try Again...!\n\n")
        Index()

# ************************************************************************************************************* #

os.system("CLS")

Index()