import random

def tarik_kartu():
    return random.randint(1, 10)

def blackjack():
    print ("Welcome to Blackjack!")
    
    pemain = tarik_kartu()
    dealer = tarik_kartu()

    print (f"Kartu anda sekarang adalah : {pemain}")

    while pemain <= 21:
        ambil_kartu = input("Apakah masih akan mengambil kartu? (y/n) : ")

        if ambil_kartu.lower() == "y":
            pemain = pemain + tarik_kartu()
            print (f"Kartu anda sekarang adalah : {pemain}")
        elif ambil_kartu.lower() == "n":
            break
        else:
            if ambil_kartu.lower() != "y" and "n":
                print("Input tidak valid")
                exit()

        if pemain > 21:
            print(f"Anda kalah! Kartu anda melebihi 21, kartu dealer adalah {dealer}")
            return

    if pemain <= 21:
        print (f"Kartu dealer adalah : {dealer}") 

        while dealer <= 17:
            dealer = dealer + tarik_kartu()
            print (f"Kartu dealer sekarang adalah : {dealer}") 

        if dealer > 21:
            print ("Anda Menang! Dealer melebihi 21")
            return
    
    if pemain < dealer:
        print ("Anda Kalah!")
    elif pemain == dealer:
        print ("Permainan Seri!")
    else:
        print ("Dealer Menang!")
        
blackjack()