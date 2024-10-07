# CS 303E Quiz 2C
# do NOT rename this file, otherwise Gradescope will not accept your submission


# Problem 1: Tech Gadget Purchases
def techGadgetPurchases():
    
    item1 = input("Soldout item 1: ")
    item2 = input("Soldout item 2: ")

    watch = 59.99
    ear = 39.50
    charger = 24.75
    usbC = 12.49
    mouse = 18.99
    total = watch + ear + charger + usbC + mouse

    if (item1) == "Smart Watch":
        total -= watch
    if (item1) == "Bluetooth Earbuds":
        total -= ear
    if (item1) == "Portable Charger":
        total -= charger
    if (item1) == "USB-C Cable":
        total -= usbC
    if (item1) == "Wireless Mouse":
        total -= mouse

    if (item2) == "Smart Watch":
        total -= watch
    if (item2) == "Bluetooth Earbuds":
        total -= ear
    if (item2) == "Portable Charger":
        total -= charger
    if (item2) == "USB-C Cable":
        total -= usbC
    if (item2) == "Wireless Mouse":
        total -= mouse

    print("$",format(total, "0.2f"), sep="")






# Problem 2: First Term Greater than m
def firstTermGreaterThanM():
    m = float(input("input m: "))
    b = 0
    n = 0
    
    while (b < m):
        n += 1
        b = 1.5 * (n**2) + 0.8 * (n) + 3.2
        
    print(format(b, "0.2f"))


if __name__=="__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.

    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """
    # techGadgetPurchases()
    
    firstTermGreaterThanM()

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT