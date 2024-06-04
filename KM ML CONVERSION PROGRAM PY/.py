def km_to_miles(kilometers):
    return kilometers * 0.621371

def miles_to_km(mile):
    return mile * 1.60934

def main():
    print("K/M Conversion Program")
    print("1. Kilometer to Mile")
    print("2. Mile to Kilometer")

    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        kilometers = float(input("Enter the Kilometer: "))
        miles = km_to_miles(kilometers)
        print(kilometers, "Kilometer is equal to", miles, "Mile.")
    elif choice == 2:
        miles = float(input("Enter the Miles: "))
        kilometers = miles_to_km(miles)
        print(miles, "Mile is equal to", kilometers, "Kilometer.")
    else:
        print("Invalid choice!")

main()
