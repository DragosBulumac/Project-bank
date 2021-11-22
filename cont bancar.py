import sys


print("Bine ai venit la banca DRAGOS")
sold = 1576.324
restart = "d"
incercari = 0
count = 3
pinul = 1236


while True:
    pin = int(input("Introduceti pinul corect : "))
    if pin != pinul :
        print("Wrong")
        incercari += 1
        if incercari == count :
            print("Blocare card")
            sys.exit()
        else:
            continue


    else:
        print("Ai introdus pinul corect")
        break



while restart not in ("n" , "No" , "N" ) :
        print(" Te rog apasa 1 pentru sold \n")
        print(" Te rog apasa 2 pentru a extrage \n")
        print(" Te rog apasa 3 pentru a depune \n")
        print(" Te rog apasa 4 pentru a ridica carudl  \n")
        optiune = int(input("Introduceti obtiunea dorita : "))
        if optiune == 1 :
            print("Soldul dumneavoastra este : " , sold , "RON")
            restart = input("Va rog introduceti d daca doriti sa va intoarceti : ")
            if restart in ("n" , "No" , "N" ):
                print("Thank you")
                break
        if optiune == 2 :


            extragere = float(input("Ce suma doriti sa extrageti : "))
            sold = sold - extragere
            print(sold)
            if sold < 0:
                print("Vedeti ca o sa faceti o descoperire pe card")
            else:
                print("Va multumim pentru extragere")


        if optiune ==3 :
            depunere = float(input("Ce suma doresti sa depui : "))
            sold = sold + depunere
            print(sold)


        if optiune == 4:
            print("Puteti ridica cardul")
            break
