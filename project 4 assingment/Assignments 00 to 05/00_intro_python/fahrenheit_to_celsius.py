def main():
    fahrenheit = int(input("Enter temprature in Fahrenheit "))
    celslus = (fahrenheit - 32) * 5.0 / 9.0 
    print(f"Temperature {fahrenheit}F = {celslus}c")

main()    