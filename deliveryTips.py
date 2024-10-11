def deliveryTips (numDeliveries):
    tipTotal = 0
    for i in range (1, numDeliveries + 1):
        tip = float(input("Enter tip amount: "))
        if tip < 1:
            tipTotal += 1
        if 1 <= tip <= 5:
            tipTotal += tip
        if tip > 5:
            tipTotal += 5

    print("$", format(tipTotal, "0.2f"), sep="")



def extraLives():
    lives = 0
    coins = 0
    while True:
        event = input("Event or End: ")
        if event == "end":
            break
        if event not in {"goomba", "large box", "small box"}:
            print ("Invalid input")
            continue
        if event == "goomba":
            coins = 0
        if event == "small box":
            coins += 20
        if event == "large box":
            coins += 50
        if coins >= 100:
            lives += 1
            coins -= 100
    print ("Extra Lives: ", lives)
    print ("Coins: ", coins)
     