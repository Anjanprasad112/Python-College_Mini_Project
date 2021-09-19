import re
from random import randint
capcha=''
for i in range(randint(5,6)):
    random=chr(randint(33,126))
    capcha+=capcha+random

def kcet_fees():
    print("\n**********KCET FEE STRUCTURE**********\n")
    print("Name : "+mode_name)
    print("Kcet rank : "+rank)
    print("Kcet Registration no. : "+mode_regs)
    print("Kcet application no. : "+mode_applyno)
    print("""Kcet govt fee : ₹62,500
college fee : ₹30,000
TOTAL FEES : ₹92,500""")
def comedk_fees():
    print("\n**********COMEDK FEE STRUCTURE**********\n")
    print("Name : "+mode_name)
    print("Comedk rank : "+rank)
    print("Comedk TAT no. : "+mode_regs)
    print("Comedk application no. : "+mode_applyno)
    print("""Comedk govt fee : ₹1,43,500
college fee : ₹30,000
TOTAL FEES : ₹173500""")
def documents():
    print("\n********List Of Documents**********\n")
    print("""\nKCET/COMEDK 2021 application form printout

Proof of application fee payment

KCET/COMEDK 2021 admit card

Photo copy of Score card of SSLC/10th Standard

Photo copy Score card of 2nd PUC/12th Standard

Two recent passport size photographs

Study Certificate Counter signed by the concerned BEO/DDPI\n""")
def slot_bookingforkcet():
    print("\n****Slot Booked For Kcet Admission**********\n")
    print("Name : "+mode_name)
    print("Kcet rank : "+rank)
    print("Kcet registration no. : "+mode_regs)
    print("Kcet application no. : "+mode_applyno)
    print("Date : 21-09-2021")
    print("Time : Between 9am to 3pm\n")
    print("For futher information contact GAT,Bengaluru phno.:95915-10211")
    print("Thank You Have A Nice Day!!!")
def slot_bookingforcomedk():
    print("\n****Slot Booked For Comedk Admission**********\n")
    print("Name : "+mode_name)
    print("Comedk rank : "+rank)
    print("Comedk TAT no. : "+mode_regs)
    print("Comedk application no. : "+mode_applyno)
    print("Date : 25-09-2021")
    print("Time : Between 9am to 4pm\n")
    print("For futher information contact GAT,Bengaluru phno : 95915-10211")
    print("\nThank Your Have A Nice Day!!!")
    

print("\n******Welcome to GAT Admission App*****\n")
print("""1.Login
2.Create New Account!
3.Forgot Password?""")
e=0#This is for login purpose
while(e<100):
 login=input("Select your choice [sl.no.] : ")
 if(login=='1'):
    e=100
    y=0
    while(y<100):#In this we can give 99 invalid data
        Email1=input("Enter your email : ")
        b = Email1.endswith("@gmail.com")
        if(b==True):
            break
        else:
            y=y+1
            print("Invalid data! check your email address once again!")
    
    f=False
    while(f==False):
        password1=input("Enter password : ")
        unique_password1=re.search("\d",password1)
        if unique_password1:f=True
        else:print("password have atleast 4 characters with one digit!!!")
    l=False
    while(l==False):
        if(len(password1)>=4):l=True
        else:
            print("password requries atleast 4 characters")
            password1=input("Enter password : ")               
    print("Your successfully done with your login!!")
            
 elif(login=='2'):#This is for Create new account
    e=100
    user_name=input("Enter your name : ")
    print("Hi "+user_name+" Welcome to Global Academy Of Technology")
    input("Enter the PU College studied in : ")
    input("Enter your City/District : ")
    i=0
    while(i<100):#In this we can give 99 invalid data
        email2=input("Enter the email : ")
        x = email2.endswith("@gmail.com")
        if(x==True):
            print("Create your own unique password!")
            break
        else:
            i=i+1
            print("Ivalid input check your email address once again!")
    g=False
    while(g==False):
        password2=input("Enter an unique password : ")
        unique_password2=re.search("\d",password2)
        if unique_password2:g=True
        else:
            print("password should contain at least one digit character!!!")
    k=False
    while(k==False):
        if(len(password2)>=4):k=True
        else:
            print("password requries atleast 4 characters")
            password2=input("Enter an unique password : ")               
    j=False
    while(j==False):
        confirm_password=(input("Confirm password : "))
        if(confirm_password==password2):
            j=True
            break
        else:
            print("Please check your password again!!!")
    print("Your Response has been Stored!!!")
    print("Go to login for futher process!!!")
    exit()
 elif(login=='3'):#This is for forgot password
    e=100
    c=0
    while(c<100):#In this we can give 99 invalid data
        email3=input("Enter the email : ")
        z= email3.endswith("@gmail.com")
        if(z==True):
            print("We have sent you a email check!!")
            break
        else:
            c=c+1
            print("Invalid data! check your email-id!!")
    exit()
 else:
    # print("invalid data!!!!")
    e=e+1
    print("""Invalid data!
check your input again!!""")
    print("""1.Login
2.Create New Account!
3.Forgot Password?""")
print("""1.Kcet
2.Comedk""")
a1=True
while a1==True:
    mode=input("Select your mode of joining [slno.]: ")
    if(mode=='1'):#this for kcet.
        mode_name=input("\nEnter your name : ")
        q=False
        while(q==False):
            mode_regs=input("Enter your Kcet registration no.[for ex : xx012] : ")
            if(mode_regs[:2].isalpha() and mode_regs[2:6].isdigit() and len(mode_regs)==5):
                q=True
            else:
                print("check your input again!!")
                q=False
        mode_applyno=(input("Enter your Kcet application no.[for ex : 012345] : "))
        m=0
        while(m<100):
            if(mode_applyno.isdigit()):
             if(len(mode_applyno)!=6):
                print("Check your application no.!!!!!")
                print("application no. must be equals to 6 digits only!")
                mode_applyno=input("Enter your Kcet application no.[for ex : 012345] : ")
                m=m+1
             else:
                m=100
            else:
                print("application no. must be equals to 6 digits only!")
                mode_applyno=input("Enter your Kcet application no.[for ex : 012345] : ")
                m=0
        n=0
        while(n<100):
            rank=input("Enter your Rank : ")
            if(rank[:].isdigit() and len(rank)<=6):
                n=100
            else:
                print("Invalid Input!!!!")
                n=n+1
        a1=False
        kcet_fees()
    elif(mode=='2'):#this is for comedk..
        mode_name=input("Enter your name : ")
        q=False
        while(q==False):
            mode_regs=input("Enter your Comedk TAT no. [for ex : xx012345678] : ")
            if(mode_regs[:2].isalpha() and mode_regs[2:12].isdigit() and len(mode_regs)==11):
                q=True
            else:
                print("check your input again!!")
                q=False
        m=0
        while(m<100):
            mode_applyno=(input("Enter your Comedk application no.[for ex : xxx012345] : "))
            if(mode_applyno[:3].isalpha() and mode_applyno[3:10].isdigit() and len(mode_applyno)==9):
                m=101
            else:
                print("check your input again!!!!")
                m=m+1
        n=0
        while(n<100):
            rank=input("Enter your Rank : ")
            if(rank[:].isdigit() and len(rank)<=5):
                n=100
            else:
                print("Invalid Input!!!!!")
                n=n+1 
        comedk_fees()
        a1=False
    else:
        print("Invalid Input!!!!!")  
        a1=True
    
documents()#list of documents is here..
def code_capcha():
 print("Given Capcha : "+capcha[2:7])
 a3=False
 while a3==False:
    your_capcha=input("Your Capcha : ")
    if(your_capcha==capcha[2:7]):
        a3=True
        print("\nYour Slot has been Booked!!\n")
    else:
        print("check your data !!!!")
        a3=False
a2=False
while(a2==False):
    print("""1.SUBMIT
2.EXIT""")
    last=input("Select your input for conformation [sl no.] : ")
    if(last=='1'):
        code_capcha()
        if(mode=='1'):
            slot_bookingforkcet()
        else:
            slot_bookingforcomedk()
        a2=True
    elif(last=='2'):
        print("You are exited from program!!")
        exit()
    else:
        print("check your input again!!!!")
        a2=False
print("\n\nBy the time of admission take this printout and come to college.")