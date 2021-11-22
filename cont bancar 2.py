print("WELCOME TO BANK DRAGOS")
restart = 'y'
ceances = 3
balance = 65.23
while ceances >= 3:
     pin = int(input("Please enter the 4 digit PIN : "))
     print("\n You enter the PIN corectly\n")
     while restart not in ('n' , 'No' , 'no' , 'N'):
          print(" Please press 1 for your balance \n")
          print(" Please press 2 for your withdraw \n")
          print(" Please press 3 to pay in \n")
          print(" Please press 4 to return CARD \n")
          option = int(input('What wold you like to choose ? '))
          if option == 1:
               print('Your balance is DOLAR$' , balance , '\n')
               restart = input("Would you like to go back ? ")
               if restart in ('n' , 'No' , 'no' , 'N') :
                    print("Thank you ")
                    break
          elif option == 2:
               option2 = ('y')
               withdraw = float(input('Hw Much Would you like to withdraw? \nDOLAR$10/DOLAR$20/DOLAR$40/DOLAR$60/DOLAR$80/DOLAR$100'))
               elif withdraw != [10 , 20 , 40 ,60 ,80 ,100 ]:
                         print("Invalid amount please retry \n")
                    restart = ("y")
               elif withdraw == 1 :
                   withdraw = float(input("Please enter the amount"))

          elif option == 3 :

