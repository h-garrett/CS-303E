# CS 303E Quiz 1D
# do NOT rename this file, otherwise Gradescope will not accept your submission
import math

# Problem 1: Calculate Power
def calculatePower():
    
    m1 = float(input("m1: "))
    m2 = float(input("m2: "))
    d = float(input("d: "))

    m1_3 = m1 ** 3
    m2_2 = m2 ** 2
    d_5 = d ** 5

    mTotal = m1_3 * m2_2
    md = mTotal / d_5
    root = md + 6.674
    PDI = math.sqrt(root)
    ans = PDI * 2
    print(format(ans, "0.2f"))




# Problem 2: Cookie Baking
def muffinBaking():
    
    e = float(input("eggs: "))
    s = float(input("sugar cups: "))
    f = float(input("flour cups: "))

    batchEggs = e // 3
    batchSugar = s // 2.5
    batchFlour = f // 4.2

    batches = int(min(batchEggs, batchFlour, batchSugar))
    print(batches)




if __name__=="__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.
    
    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """
    # calculatePower()
    # muffinBaking()

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT
