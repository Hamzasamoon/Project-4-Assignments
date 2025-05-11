import math 
def main():
    ab:float = float  (input("Enter the length of AB: "))
    ac:float = float( input("Enter the length of AC: "))
    alam: float = ab**2 + ac**2
    print(alam)
    bc:float = math.sqrt(alam)
    print("The length of BC (the hypotenuse) is: " + str(bc))

main()