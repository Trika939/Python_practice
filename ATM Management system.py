"""
ATM MANAGEMENT SYSTEM
   
    1.Create Account
    2.view all account
    3. Login
    4. Deposit
    5. Withdraw
    6.Change PIN
    7. Balance Enquiry
    8.Delete Account
     0.Exit
   

"""
#IMPORT PICKLE
import pickle

# A METHOD TO GET ACCOUNT INFORMETION
def getaccount():
    file=open('account.bin','rb')
    AC=dict()
    try:
        while True:
            AC.update( pickle.load(file) )
    except:
        pass
    return AC


# A METHOD TO UPDATE ACCOUNT INFOF METION
def updateaccount(AC):
    file=open('account.bin','wb')
    for CAC,info in AC.items():
        pickle.dump({CAC:info},file)
    file.close()    


# A METHOD TO CREATE ACCOUNT INFORMETION
def CreateAccount():
    CAC=input("\n\tEnter New Account Number  :  ")
    AC=getaccount()
    if AC.get(CAC,False):
        print("\n\tCustomer already Exist On This AC ")
    else:    
        CNAME=input("\tEnter Cutomer Name    :   ")
        CMOB=input("\tEnter Customer Mobile    :    ")
        CPIN=input("\tEnter Cutomer PIN      :    ")
        COPB=input("\tEnter Your Opening Balance  :  ")
        AC.update({CAC:[CNAME,CMOB,CPIN,COPB]})
        updateaccount(AC)
        print("\n\tYour Account Create Succeccfully ! ")
    
# A METHOD TO VIEW ALL ACCOUNT INFORMETION
def Viewallaccount():
    AC=getaccount()
    for CAC,info in AC.items():
        print("\n\tAccount Number  :",CAC)
        print("\tCustomer Name  :",info[0])
        print("\tCustomer Mobile    :",info[1])
        print("\tCustomer ATM PIN     :",info[2])
        print("\tCuctomer Opening Balance :",info[3])
        print("\t----------------------------------------------------------------------------------------------")


# A METHOD TO LOGIN ACCOUNT NUMBER
def DeleteAccount():
    CAC=input("\n\tEnter Customer Account Nunber To Delete  : ")
    AC=getaccount()
    A=AC.get(CAC,False)
    if A:
        print("\n\tCustomer Name:",A[0])
        print("\tCustomer Mobile :",A[1])
        print("\tCustomer ATM PIN :",A[2])
        print("\tCustomer Opening Balance :",A[3])
        choice=input("\n\tDo You Want To Delete This Account Number (Y/n)  :  ")
        if choice in 'Yy':
            AC.pop(CAC)
            updateaccount(AC)
            print("\n\tAccount Deleted Successfully ! ")
    else:
        print("\n\tAccount Not Found On This CAC ! ")


# A METHOD TO LOGIN ACCOUNT
def LoginAccount():
    CAC=input("\n\tEnter Account Number  : ")
    CPIN=input("\tEnter PIN : ")
    AC=getaccount()
    if AC.get(CAC,False):
        if AC[CAC][2]==CPIN:
            print("\n\t******ACCOUNT DETAILS*******")
            print("\tAccount Number :",CAC)
            print("\tCustomer Name  :",AC[CAC][0])
            print("\tCustomer Mobile :",AC[CAC][1])
            print("\tCurrent Balance :",AC[CAC][3])
            print("\t------------------------------------------------------------")
            print("\tLogin Successfully ! ")
        else:
            print("\n\tWrong PIN ")
    else:
        print("\n\tAccount Not Found ! ")

# A METHOD TO DEPOSIT AMOUNT INFORMETION
def Deposit():
    CAC = input("\n\tEnter Account Number : ")
    CPIN = input("\tEnter PIN : ")
    AC=getaccount()
    if AC.get (CAC,False):
        if AC[CAC][2]==CPIN:
            Amount=int(input("\n\tEnter Deposit Amount : "))
            Balance=int(AC[CAC][3])
            Balance=Balance+Amount
            AC[CAC][3]=str(Balance)
            updateaccount(AC)
            print("\n\tEnter Deposited Successfully ")
            print("\tCurrent Balance :",Balance)
        else:
            print("\n\tWrong PIN ")
    else:
       print("\n\tAccount Not Found ")


 # A METHOD TO WITHDRAW THIS AMOUNT
def Withdraw():
    CAC=input("\n\tEnter Account Number :  ")
    CPIN=input("\tEnter PIN  :  ")
    AC=getaccount()
    if AC.get(CAC,False):
        if AC[CAC][2]==CPIN:
            Amount=int(input("\n\tEnter Withdraw Amount  :  "))
            Balance=int(AC[CAC][3])
            if Balance>=Amount:
                Balance=Balance-Amount
                AC[CAC][3]=str(Balance)
                updateaccount(AC)
                print("\n\tSuccessfully Withdraw .......")
            else:
                print("\n\tInsufficient Balance ")
        else:
            print("\n\tWrong PIN ")
    else:
        print("\n\tAccount Not Found ")


# A MENTHOD TO CHANGE ACCOUNT PIN
def ChangePIN():
    CAC=input("\n\tEnter Account Number  :  ")
    OPIN=input("\tEnter Old PIN     :  ")
    AC=getaccount()
    if AC.get(CAC,False):
        if AC[CAC][2]==OPIN:
            NPIN=input("\n\tEnter New PIN  : ")
            AC[CAC][2]=NPIN
            updateaccount(AC)
            print("\n\tChanged Successfully ")
        else:
            print("\n\tWrong Old PIN ")
    else:
        print("\n\tAccount Not Found ")


# A MENTHOD TO CHECK BALANCE ENQUIRY INFORMETION
def BalanceEnquiry():
    CAC=input("\n\tEnter Account Number  : ")
    CPIN=input("\tEnter PIN   : ")
    AC=getaccount()
    if AC.get(CAC,False):
        if AC[CAC][2]==CPIN:
            print("\n\tAccount Number  :",CAC)
            print("\tCustomer Name :",AC[CAC][0])
            print("\tCurrent Balance :",AC[CAC][3])
        else:
            print("\n\tWrong PIN ")
    else:
        print("\n\tAccount Not Found ")
        
        
#=======================================================================================
while True:
    print("\n\tATM MANAGEMENTN SYSTEM")
    print('''
    1.Create Account
    2.view all account
    3. Login
    4. Deposit
    5. Withdraw
    6.Change PIN
    7. Balance Enquiry
    8.Delete Account
     0.Exit
    ''')
    ch=int(input("\n\tEnter your choice   :  "))
    if ch==1:
        CreateAccount()
    elif ch==2:
        Viewallaccount()
    elif ch==3:
        LoginAccount()
    elif ch==4:
        Deposit()
    elif ch==5:
        Withdraw()
    elif ch==6:
        ChangePIN()
    elif ch==7:
        BalanceEnquiry()    
    elif ch==8:
        DeleteAccount()
    elif ch==0:
        print("\n\tExist.....")
        break
