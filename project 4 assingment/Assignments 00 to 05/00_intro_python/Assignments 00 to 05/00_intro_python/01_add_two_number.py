def main():
  try:  
    num1= (input("Entre the 1st number: "))
    num1 = int(num1)
    num2 = (input("Entre the 2nd number: "))
    num2 = int(num2)
    total = num1 + num2
    print(f" {num1} + {num2} = {total}")
  except ValueError:
    print("Invalid Input! please enter only number.")
main()