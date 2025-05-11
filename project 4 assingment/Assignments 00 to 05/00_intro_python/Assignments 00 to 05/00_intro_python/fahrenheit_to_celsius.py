def main():
    fahrenheit = int(input("Enter temprature in Fahrenheit "))
    celslus = (fahrenheit - 32) * 5 // 9
    print(f"Temperature {fahrenheit}F = {celslus}c")

main()    