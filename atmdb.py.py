#ATM
import time
import sqlite3
db=sqlite3.connect('database.db')
cs=db.cursor()
##table=''' create table KTM(
##'c_name' varchar(20) not null,
##'acc_num' int primary key,
##'pin' int not null);'''
##cs.execute(table)
class ATM():
    name = 'KTM_bank'
    address='chennai'
    ATM_amt=100000
    def __init__(self,name,acc_no,pin):
        self.name=name
        self.acc_no=acc_no
        self.pin=pin
        self.balance=0
        self.hist ={'time':[],'type':[],'amt':[]}
    print("****__Welcome_To_KTM_BANK__****",sep='\t')
    print('---------------------------------')
    print()
    
    def deposit(self):
        pin=int(input('Enter PIN :'))
        if pin==self.pin:
            amt=int(input('Enter amount to deposite :$'))
            if amt>0:
                self.balance+=amt
                self.hist['time'].append(time.ctime())
                self.hist['type'].append('deposit')
                self.hist['amt'].append(amt)
                print()
                print(f'*** Successfully deposited {amt} in your account ***')
                print('------------------------------------------------------')

            else:
                print()
                print('Enter valid amount')
        else:
            print()
            print('--- Wrong pin ---')   
    def withdraw(self):
        print()
        pin=int(input('Enter PIN :'))
        if pin==self.pin:
            amt=int(input('Enter amount to withdraw :$'))
            if amt<self.balance:
                self.balance-=amt
                self.hist['time'].append(time.ctime())
                self.hist['type'].append('Withdra')
                self.hist['amt'].append(amt)
                
                print()
                print('*** Collect cash ***')
                print('--------------------------------------------')
            else:
                print()
                print('--- Insufficient amount ---')
        else:
            print()
            print('--- Wrong PIN ---')
       
            
    def bank_balance(self):
        print()
        pin=int(input('Enter PIN :'))
        if pin==self.pin:
            print(f'Your bank balance is :${self.balance}')
        else:
            print('--- Wrong PIN ---')
            
    def change_pin(self):
        print()
        pin=int(input('Enter old PIN :'))
        if pin==self.pin:
            print()
            newpin=int(input('Enter New PIN :'))
            repin=int(input('Re-Enter New PIN :'))
            if 999<newpin and newpin==repin:
                self.pin=newpin
                update=f'''update KTM set pin={newpin} where acc_num={self.acc_no};'''
                cs.execute(update)
                print()
                print('*** Your PIN has been successfully changed ***')
                print('----------------------------------------------')
            else:
                print()
                print('--- Your PIN is invalid or less the 4 digit ---')
        else:
            print()
            print('--- Wrong PIN ---')
            
    def history(self):
        print()
        pin=int(input('Enter PIN :'))
        if pin==self.pin:
            print()
            print('S.NO','\tDay','\t\tDeposit/Withdraw','Amount\t\t\t\t',sep='\t\t')
            print('----''\t\t-------------------------','-----------------','------\t\t\t\t',sep='\t\t')
            for i in range(len(self.hist['time'])):
                for j in self.hist:
                    if j!='amt':
                        print(1+i,self.hist[j][i],sep='\t\t',end='')
                    else:
                        print('\t\t\t\t',f'${self.hist[j][i]}',)
        else:
            print()
            print('--- Wrong PIN ---')   
        print()
        
    def main(self):
        while True:
            print()
            print('Enter --> 1 ---->  To Deposit')
            print('Enter --> 2 ---->  To Cash withdraw')
            print('Enter --> 3 ---->  To Check bank balance')
            print('Enter --> 4 ---->  To ChangePIN')
            print('Enter --> 5 ---->  To Transaction history')
            print('Enter --> 6 ---->  To Exit')
            print('============================================')
            print()
            option=int(input('Choose a required number: '))
            print()
            print('============================================')

            if option==1:
                  self.deposit()
            elif option==2:
                self.withdraw()
            elif option==3:
                self.bank_balance()
            elif option==4:
                self.change_pin()
            elif option==5:
                self.history()
            elif option==6:
                print()
                print('*** Thanks for visiting KTM_bank ***')
                return
            else:
                print('--- option does not match,Try again ---')
                 
    def activate(self):
        print()
        print('OTP number is :',len(self.name)*self.pin)
        otp=int(input('Enter OTP number:'))
        if len(self.name)*self.pin==otp:
            print()
            print(f'*** Account number :{self.acc_no},successfully Activated ***')
            print('-------------------------------------------------------------')
            print()
            c1.main()
        else:
            print('Wrong OTP')

name=str(input('Enter Your Name:'))
acc=int(input('Enter Your Account_Number To Activate:'))
pin=int(input('Enter pin 4 digit number to activate:'))

while len(str(pin)) != 4:
    if len(str(pin))==4:
        pass
    else:
        print()
        print('Pin Must Be In 4 Digit')
        pin=int(input('Enter pin 4 digit number to activate:'))
    

values=f'''insert into KTM values('{name}',{acc},{pin});''' 
cs.execute(values)
        
c1=ATM(name,acc,pin)
c1.activate()
db.commit()



                                                            

    

