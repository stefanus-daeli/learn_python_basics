
weight = float(input("Weigth : "))
unit = input("K())g Or (L)bs : ")

if unit.upper() == "K":
    converted = weight / 0.45
    print("Weigth in kg " + str(converted))
elif unit.upper() == "L":
    converted = weight * 0.45
    print("Weigth in lbs " + str(converted))
else:
    print("Not Count")
