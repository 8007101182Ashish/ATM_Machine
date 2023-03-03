amount=10000
ch=1
count=0
print("*--------------------------------------------------------------------------*")
print("*                                                                          *")
print("*             ****____<<<< WELCOME TO CHAVAN ATM >>>>____****              *")
print("*                                                                          *")
print("*--------------------------------------------------------------------------*")
while(ch==1):
    print("*--------------------------------------------------------------------------*")
    print("*                            ****_MENU_****                                *")
    print("*                                                                          *")
    print("*                            1.Deposit Money                               *")
    print("*                                                                          *")
    print("*                            2.Withdraw Money                              *")
    print("*                                                                          *")
    print("*                            3.Check Balance                               *")
    print("*                                                                          *")
    print("*--------------------------------------------------------------------------*")
    ch1=int(input("Enter Your Choice:"))
    if(ch1==1):
        deposit=int(input("Enter Your Deposit Money:"))
        amount+=deposit
        print("Deposit Amount:",amount)
        print("                                    ")
        print("Your Amount Will be Deposited Successfully")

        print("     ******AMOUNT DETAILS******     ")
        print("Deposited Amount =",deposit)
        print("Current Amount =",amount)
        print("                                    ")
        print("_______***** THANK YOU *****________")
    if(ch1==2):
        account_no=int(input("Enter Account Number:"))
        no=8007101182
        if(account_no==no):
            password=int(input("Enter Your Password:"))
            no1=1234
            if(password==no1):
                withdraw=int(input("Enter Your Withdraw Money:"))
                if(withdraw>=100):
                    if(amount>=withdraw):
                        amount-=withdraw
                        print("Withdraw amount is:",withdraw)
                        print("Amount Is Successfully Withdraw")
                        print("                               ") 
                        if(withdraw>=2500):
                            while(withdraw>2000):
                                withdraw-=2000
                                count+=1
                            print("2000 Note =",count)
                            count=0
                            while(withdraw>500):
                                withdraw-=500
                                count+=1
                            print("500 Note =",count)
                            count=0
                            while(withdraw>200):
                                withdraw-=200
                                count+=1
                            print("200 Note =",count)
                            count=0
                            while(withdraw>=100):
                                withdraw-=100
                                count+=1
                            print("100 Note =",count)
                            count=0
                            print("                               ")
                            print("*--------------------------------------------------------------------------*")
                            print("*                                                                          *")
                            print("*                   Current Amount =                                 ",amount,"*")
                            print("*                                                                          *")
                            print("*--------------------------------------------------------------------------*")
                            print("*                                                                          *")
                            print("*--------------------------------------------------------------------------*")
                            print("*                                                                          *")
                            print("*                      *** THANK YOU ***                                   *")
                            print("*                                                                          *")
                            print("*--------------------------------------------------------------------------*")
                    else:
                        print("                               ")
                        print("Oops!")
                        print("Insfficient Balance!")
                        print("                               ")
                else:
                    print("                               ")
                    print("Oops!")
                    print("Available Notes above 100.\nEnter amount multiples of 100.")
                    print("                                ")
            else:
                print("                               ")
                print("You Entered Wrong Password !")
                print("                               ")
        else:
            print("                               ")
            print("You Entered Wrong Account Number !")
            print("                               ")
    if(ch1==3):
        print("*--------------------------------------------------------------------------*")
        print("*                                                                          *")
        print("*           Available Balance is    =                               ",amount,"*")
        print("*                                                                          *")
        print("*--------------------------------------------------------------------------*")
    ch=int(input("Do You Want To Continue With Main Menu \n Press 1 \n For Exit Press 2 "))
    if(ch==2):
        print("*-------------------------------------------------------------------------------------*")
        print("|                                                                                     |")
        print("|___________----------**********THANK YOU FOR VISITING**********----------____________|")
        print("|                                                                                     |")
        print("*-------------------------------------------------------------------------------------*")
